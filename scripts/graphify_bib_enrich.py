#!/usr/bin/env python3
"""
Enrich bibliography/docs/<slug>.md for Graphify project queries.

Graphify indexes markdown headings as nodes. Plain pdftotext dumps under a few
## sections are weak for “where does the paper say X?”. This rewriter adds:

- source_pdf + page locators in labels
- finding hooks (EN sentence as ### heading = snippet in the graph)
- ES hallazgo aliases (glossary) so Spanish queries also hit
- section chunks with body text under each heading
- optional bounded page chunks from the PDF

Idempotent: skips if Technique already set (unless --force).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

TECHNIQUE = "section-chunks + finding-hooks + es-aliases"

# Lightweight EN→ES tokens for bilingual graph hooks (not a full translation).
_GLOSS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bdistributed transactions\b", re.I), "transacciones distribuidas"),
    (re.compile(r"\bdistributed transaction\b", re.I), "transacción distribuida"),
    (re.compile(r"\bmicroservices\b", re.I), "microservicios"),
    (re.compile(r"\bmicroservice\b", re.I), "microservicio"),
    (re.compile(r"\bmonolithic systems\b", re.I), "sistemas monolíticos"),
    (re.compile(r"\bmonolithic architecture\b", re.I), "arquitectura monolítica"),
    (re.compile(r"\bmonolithic\b", re.I), "monolítico"),
    (re.compile(r"\bmonolith\b", re.I), "monolito"),
    (re.compile(r"\bexperiments?\b", re.I), "experimentos"),
    (re.compile(r"\bcomparing\b", re.I), "comparan"),
    (re.compile(r"\bperformance\b", re.I), "rendimiento"),
    (re.compile(r"\blatency\b", re.I), "latencia"),
    (re.compile(r"\bconsistency\b", re.I), "consistencia"),
    (re.compile(r"\binventory\b", re.I), "inventario"),
    (re.compile(r"\border\b", re.I), "pedido"),
    (re.compile(r"\bsaga pattern\b", re.I), "patrón saga"),
    (re.compile(r"\bevent sourcing\b", re.I), "event sourcing"),
    (re.compile(r"\beventual consistency\b", re.I), "consistencia eventual"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify_anchor(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9áéíóúüñÁÉÍÓÚÜÑ]+", "-", text.lower()).strip("-")
    return s[:80] or "chunk"


def split_pdf_pages(raw_text: str) -> list[str]:
    pages = raw_text.split("\f")
    while pages and not pages[-1].strip():
        pages.pop()
    return pages or [raw_text]


def pdftotext_raw(pdf: Path) -> str:
    r = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or "pdftotext failed").strip())
    return r.stdout or ""


def find_page_for_snippet(pages: list[str], snippet: str) -> int | None:
    if not snippet or len(snippet) < 12:
        return None
    needle = re.sub(r"\s+", " ", snippet[:80]).lower()
    for i, page in enumerate(pages, start=1):
        hay = re.sub(r"\s+", " ", page).lower()
        if needle[:40] in hay:
            return i
    return None


def gloss_es(text: str) -> str:
    out = text
    for pat, repl in _GLOSS:
        out = pat.sub(repl, out)
    return out


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, m.group(2)


def split_md_sections(body: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Return (preamble, [(level, title, content), ...]) for ## / ###."""
    lines = body.splitlines()
    preamble: list[str] = []
    sections: list[tuple[str, str, str]] = []
    cur_level = ""
    cur_title = ""
    cur_buf: list[str] = []
    started = False
    for line in lines:
        hm = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
        if hm:
            if started:
                sections.append((cur_level, cur_title, "\n".join(cur_buf).strip()))
            else:
                preamble_text = "\n".join(preamble).strip()
                if preamble_text:
                    pass  # keep preamble separately
            started = True
            cur_level = hm.group(1)
            cur_title = hm.group(2).strip()
            cur_buf = []
            continue
        if not started:
            preamble.append(line)
        else:
            cur_buf.append(line)
    if started:
        sections.append((cur_level, cur_title, "\n".join(cur_buf).strip()))
    return "\n".join(preamble).strip(), sections


def section_body(sections: list[tuple[str, str, str]], *names: str) -> str:
    want = {n.lower() for n in names}
    for _lvl, title, content in sections:
        if title.lower() in want:
            return content.strip()
    return ""


def extract_findings(abstract: str, limit: int = 10) -> list[str]:
    candidates: list[str] = []
    for sent in re.split(r"(?<=[.!?])\s+", abstract):
        sent = re.sub(r"\s+", " ", sent).strip()
        if 40 < len(sent) < 280:
            candidates.append(sent)
    # Prefer empirically / comparison / performance sentences first
    scored = []
    for s in candidates:
        score = 0
        low = s.lower()
        for tok in (
            "experiment",
            "compar",
            "performance",
            "latency",
            "impact",
            "monolith",
            "evaluat",
            "throughput",
            "consistenc",
        ):
            if tok in low:
                score += 2
        scored.append((score, s))
    scored.sort(key=lambda x: (-x[0], candidates.index(x[1])))
    ordered = [s for _, s in scored]
    # keep original order for ties already handled; ensure diversity: take top scored then fill
    out: list[str] = []
    for s in ordered:
        if s not in out:
            out.append(s)
        if len(out) >= limit:
            break
    return out


def keywords_from_pdf(pages: list[str]) -> list[str]:
    blob = "\n".join(pages[:2]) if pages else ""
    m = re.search(
        r"(?is)Key\s*words?\s*[:\n]\s*(.+?)(?:\n\s*\n|\n\s*[A-Z][a-z]+\s|\n\s*1\.\s)",
        blob,
    )
    if not m:
        m = re.search(r"(?im)^Keywords?:\s*(.+)$", blob)
    if not m:
        return []
    raw = re.sub(r"\s+", " ", m.group(1)).strip()
    out = []
    for p in re.split(r"[,;]", raw):
        p = p.strip(" .-")
        if 2 < len(p) < 80:
            out.append(p)
    return out[:16]


def keywords_from_sections(sections: list[tuple[str, str, str]]) -> list[str]:
    raw = section_body(sections, "Keywords", "Key words", "Palabras clave")
    out: list[str] = []
    if raw:
        for p in re.split(r"[\n;,]", raw):
            p = re.sub(r"^[-*]\s*", "", p).strip()
            m = re.match(r"^#{1,3}\s+\[PDF[^\]]+\]\s+Concept:\s*(.+)$", p, re.I)
            if m:
                p = m.group(1).strip()
            if p.lower().startswith("concepto:") or p.lower().startswith("locator:"):
                continue
            if 2 < len(p) < 80 and not p.startswith("#") and not p.startswith("- Locator"):
                out.append(p)
    for _lvl, title, _content in sections:
        m = re.match(r"^\[PDF[^\]]+\]\s+Concept:\s*(.+)$", title, re.I)
        if m:
            kw = m.group(1).strip()
            if kw and kw not in out:
                out.append(kw)
    return out[:16]


def already_enriched(text: str) -> bool:
    return TECHNIQUE in text or "section-chunks + finding-hooks" in text


def enrich_bib_md(
    md_path: Path,
    pdf_path: Path | None = None,
    *,
    force: bool = False,
    max_page_chunks: int = 12,
) -> dict:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    if already_enriched(text) and not force:
        return {"path": str(md_path), "skipped": True, "reason": "already_enriched"}

    meta, body = parse_front_matter(text)
    _, sections = split_md_sections(body)

    # Prefer H1 title
    title = meta.get("title") or md_path.stem.replace("-", " ")
    for lvl, t, _ in sections:
        if lvl == "#":
            title = t
            break

    stem = md_path.stem
    parent = md_path.parent  # …/docs
    grand = parent.parent  # bibliography | bibliographic | …

    def project_root() -> Path:
        """Project dir = parent of bibliography/ or bibliographic/."""
        if grand.name in {"bibliography", "bibliographic"}:
            return grand.parent
        return md_path.parent.parent.parent

    if pdf_path is None:
        # bibliography/docs/<slug>.md → auto/pdfs/<slug>.pdf
        # bibliographic/docs/<slug>.md → search/pdfs/<slug>.pdf
        if grand.name == "bibliographic" and parent.name == "docs":
            cand = grand / "search" / "pdfs" / f"{stem}.pdf"
        else:
            cand = grand / "auto" / "pdfs" / f"{stem}.pdf"
        pdf_path = cand if cand.is_file() else None
        if not pdf_path and meta.get("pdf_path"):
            alt = project_root() / meta["pdf_path"]
            if alt.is_file():
                pdf_path = alt

    pages: list[str] = []
    pdf_rel = meta.get("pdf_path") or meta.get("source_pdf") or ""
    if pdf_path and pdf_path.is_file():
        try:
            pages = split_pdf_pages(pdftotext_raw(pdf_path))
            proj = project_root()
            # climb from PDF if needed
            walk = pdf_path
            for _ in range(6):
                walk = walk.parent
                if (walk / "profile.md").exists() or (walk / "config.json").exists():
                    proj = walk
                    break
            try:
                pdf_rel = str(pdf_path.resolve().relative_to(proj.resolve())).replace(
                    "\\", "/"
                )
            except ValueError:
                pdf_rel = str(pdf_path)
        except Exception as e:
            print(f"warn: pdftotext failed for {pdf_path}: {e}", file=sys.stderr)

    abstract = section_body(sections, "Abstract", "Resumen")
    if not abstract and pages:
        # fallback first long para on p.1
        paras = [p.strip() for p in re.split(r"\n\s*\n", pages[0]) if len(p.strip()) > 200]
        abstract = re.sub(r"\s+", " ", paras[0])[:2500] if paras else ""

    keywords = keywords_from_sections(sections)
    if not keywords and pages:
        keywords = keywords_from_pdf(pages)
    findings = extract_findings(abstract)
    abs_page = find_page_for_snippet(pages, abstract[:60]) if pages and abstract else 1

    doi = meta.get("doi_url") or meta.get("doi") or ""
    authors = meta.get("authors") or section_body(sections, "Autores", "Authors")
    year = meta.get("year") or section_body(sections, "Año", "Year")

    fm_lines = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
    ]
    if authors:
        fm_lines.append(f'authors: "{authors.splitlines()[0].strip()[:200]}"')
    if year:
        fm_lines.append(f"year: {year.splitlines()[0].strip()[:12]}")
    if doi:
        fm_lines.append(f'doi_url: "{doi}"')
    if pdf_rel:
        fm_lines.append(f'source_pdf: "{pdf_rel}"')
        fm_lines.append(f'pdf_path: "{pdf_rel}"')
    fm_lines.append(f"pages: {len(pages) if pages else 0}")
    fm_lines.append(f"technique: {TECHNIQUE}")
    fm_lines.append(f"enriched_at: {utc_now()}")
    fm_lines.append("---")

    parts: list[str] = [
        "\n".join(fm_lines),
        "",
        f"# {title}",
        "",
        f"> Fuente PDF: `{pdf_rel or 'unknown'}` · técnica **{TECHNIQUE}**",
        "",
        "## Metadata",
        f"- Stem: `{stem}`",
        f"- PDF: `{pdf_rel or 'unknown'}`",
        f"- DOI: `{doi or 'unknown'}`",
        f"- Pages: `{len(pages) if pages else '?'}`",
        f"- Technique: `{TECHNIQUE}`",
        "",
        "## Locator index",
        "",
        "| Kind | Label | PDF page |",
        "|------|-------|----------|",
        f"| abstract | Abstract | {abs_page or 1} |",
    ]

    for sent in findings:
        p = find_page_for_snippet(pages, sent[:50]) if pages else abs_page
        label = (sent[:90] + ("…" if len(sent) > 90 else "")).replace("|", "/")
        parts.append(f"| finding | {label} | {p or abs_page or 1} |")
        es = gloss_es(sent)
        if es != sent:
            es_label = (es[:90] + ("…" if len(es) > 90 else "")).replace("|", "/")
            parts.append(f"| hallazgo | {es_label} | {p or abs_page or 1} |")

    for kw in keywords:
        p = find_page_for_snippet(pages, kw) if pages else None
        parts.append(f"| concept | {kw.replace('|', '/')} | {p or '?'} |")

    skip_titles = {
        "metadata",
        "locator index",
        "abstract",
        "keywords",
        "findings",
        "hallazgos",
        "concept index",
        "page chunks",
        "autores",
        "authors",
        "año",
        "year",
    }

    for lvl, t, content in sections:
        if lvl == "#":
            continue
        if t.lower() in skip_titles:
            continue
        if t.lower().startswith("[pdf p."):
            continue
        p = find_page_for_snippet(pages, content[:60]) if pages and content else None
        parts.append(
            f"| section | {t.replace('|', '/')} | {p or '?'} |"
        )

    parts.extend(["", "## Abstract", ""])
    parts.append(abstract or "_(sin abstract)_")
    parts.append("")

    parts.extend(["", "## Findings", ""])
    parts.append(
        "_Cada ### es un nodo Graphify; el título es el snippet consultable (EN + alias ES)._"
    )
    parts.append("")
    for i, sent in enumerate(findings):
        p = find_page_for_snippet(pages, sent[:50]) if pages else abs_page
        pinfo = f"p.{p}" if p else f"p.{abs_page or '?'}"
        parts.append(f"### [PDF {pinfo}] Finding: {sent}")
        parts.append(f"- Locator: `{pdf_rel or stem}` · página **{p or abs_page or '?'}**")
        parts.append("")
        parts.append(sent)
        parts.append("")
        es = gloss_es(sent)
        if es != sent:
            parts.append(f"### [PDF {pinfo}] Hallazgo: {es}")
            parts.append(f"- Locator: `{pdf_rel or stem}` · página **{p or abs_page or '?'}** · alias ES")
            parts.append("")
            parts.append(es)
            parts.append("")

    parts.extend(["", "## Keywords", ""])
    if keywords:
        for kw in keywords:
            p = find_page_for_snippet(pages, kw) if pages else None
            pinfo = f"p.{p}" if p else "p.?"
            parts.append(f"### [PDF {pinfo}] Concept: {kw}")
            parts.append(f"- Locator: `{pdf_rel or stem}` · página **{p or '?'}**")
            parts.append("")
            es_kw = gloss_es(kw)
            if es_kw.lower() != kw.lower():
                parts.append(f"### [PDF {pinfo}] Concepto: {es_kw}")
                parts.append(f"- Locator: `{pdf_rel or stem}` · página **{p or '?'}** · alias ES")
                parts.append("")
    else:
        parts.append("_(sin keywords)_")
        parts.append("")

    parts.extend(["", "## Sections", ""])
    for lvl, t, content in sections:
        if lvl == "#":
            continue
        if t.lower() in skip_titles or t.lower().startswith("[pdf"):
            continue
        if t.lower() in {"abstract", "keywords", "references", "referencias"}:
            # Abstract/Keywords already handled; keep References as section
            if t.lower() in {"abstract", "keywords"}:
                continue
        p = find_page_for_snippet(pages, content[:80]) if pages and content else None
        pinfo = f"p.{p}" if p else "p.?"
        heading = "###" if lvl == "##" else "####"
        parts.append(f"{heading} [PDF {pinfo}] Section: {t}")
        parts.append(f"- Locator: `{pdf_rel or stem}` · página **{p or '?'}**")
        parts.append("")
        body_txt = content.strip()
        if len(body_txt) > 8000:
            body_txt = body_txt[:8000] + "\n\n…[truncado]…"
        parts.append(body_txt or "_(vacío)_")
        parts.append("")

    if pages and max_page_chunks > 0:
        parts.extend(["", "## Page chunks", ""])
        parts.append("_Nodos por página del PDF (acotado)._")
        parts.append("")
        limit = min(len(pages), max_page_chunks)
        for i in range(1, limit + 1):
            page = pages[i - 1]
            preview = next(
                (
                    re.sub(r"\s+", " ", ln).strip()
                    for ln in page.splitlines()
                    if 12 < len(re.sub(r"\s+", " ", ln).strip()) < 120
                ),
                f"page {i}",
            )
            body_txt = page.strip()
            if len(body_txt) > 6000:
                body_txt = body_txt[:6000] + "\n\n…[truncado]…"
            parts.append(f"### [PDF p.{i}] {preview}")
            parts.append(f"- Locator: `{pdf_rel or stem}` · página **{i}** / {len(pages)}")
            parts.append("")
            parts.append(body_txt)
            parts.append("")
        if len(pages) > limit:
            parts.append(f"_… {len(pages) - limit} páginas más en el PDF (no indexadas como chunks)._")
            parts.append("")

    out = "\n".join(parts).rstrip() + "\n"
    md_path.write_text(out, encoding="utf-8")
    return {
        "path": str(md_path),
        "skipped": False,
        "findings": len(findings),
        "keywords": len(keywords),
        "pages": len(pages),
        "source_pdf": pdf_rel,
        "headings": len(re.findall(r"(?m)^#{1,3}\s+\S+", out)),
    }


def enrich_project_bib(project: Path, *, force: bool = False) -> list[dict]:
    bib_docs = project / "bibliography" / "docs"
    if not bib_docs.is_dir():
        return []
    reports = []
    for md in sorted(bib_docs.glob("*.md")):
        if md.name.startswith("."):
            continue
        pdf = project / "bibliography" / "auto" / "pdfs" / f"{md.stem}.pdf"
        reports.append(
            enrich_bib_md(md, pdf if pdf.is_file() else None, force=force)
        )
    return reports


def main() -> None:
    ap = argparse.ArgumentParser(description="Enrich bibliography/docs MD for Graphify")
    ap.add_argument("target", help="project dir or single .md path")
    ap.add_argument("--pdf", type=Path, default=None)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--max-page-chunks", type=int, default=12)
    args = ap.parse_args()
    target = Path(args.target)
    if target.is_dir():
        for r in enrich_project_bib(target, force=args.force):
            print(r)
    elif target.is_file():
        print(
            enrich_bib_md(
                target,
                args.pdf,
                force=args.force,
                max_page_chunks=args.max_page_chunks,
            )
        )
    else:
        print(f"error: not found: {target}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
