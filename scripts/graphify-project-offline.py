#!/usr/bin/env python3
"""
Project Graphify pipeline (docs/content/<FOLDER>).

Corpus: profile.md, structure.md (local or common/structure/{modelo}),
docs/**/*.{md,qmd}, bibliography/auto/docs.md, bibliography/docs/**/*.md
Manifest: docs/content/<FOLDER>/index-manifest.json
Resolved copies (qmd / modelo): graphify-out/_corpus/ (gitignored with graphify-out)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MANIFEST_NAME = "index-manifest.json"
MIN_HEADINGS_NOTE = 3
MIN_PROFILE_NODES = 2
REPO_ROOT = Path(__file__).resolve().parent.parent


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def entry_key(rel: str) -> str:
    return rel.replace("\\", "/")


def count_md_headings(text: str) -> int:
    return len(re.findall(r"(?m)^#{1,3}\s+\S+", text))


def load_manifest(project: Path) -> dict:
    path = project / MANIFEST_NAME
    if not path.exists():
        return {"version": 1, "updated_at": None, "entries": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(project: Path, manifest: dict) -> None:
    manifest["updated_at"] = utc_now()
    (project / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def load_config(project: Path) -> dict:
    path = project / "config.json"
    if not path.exists():
        return {
            "citation_style": "APA7",
            "modelo": "model1",
            "alcance": [],
            "mvp": 1,
            "tools": {
                "design-thinking": "common/design-thinking/model1.md",
                "lean-canvas": "common/lean-canvas/model1.md",
                "rat": "common/rat/model1.md",
                "foda": "common/foda/model1.md",
                "as-is-to-be": "common/as-is-to-be/model1.md",
            },
        }
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_structure_source(project: Path, config: dict) -> tuple[Path | None, str]:
    """Return (path, kind) where kind is 'local' | 'modelo'."""
    local = project / "structure.md"
    if local.exists() and local.stat().st_size > 40:
        text = local.read_text(encoding="utf-8", errors="replace")
        if re.search(r"(?m)^#{1,3}\s+\S+", text):
            return local, "local"
    modelo = str(config.get("modelo") or "model1").strip()
    candidate = REPO_ROOT / "common" / "structure" / f"{modelo}.md"
    if candidate.exists():
        return candidate, "modelo"
    return None, "missing"


def strip_qmd_frontmatter(text: str) -> str:
    if text.startswith("---"):
        m = re.match(r"^---\s*\n.*?\n---\s*\n(.*)$", text, re.S)
        if m:
            return m.group(1).lstrip("\n")
    return text


def list_note_files(project: Path) -> list[Path]:
    docs = project / "docs"
    if not docs.is_dir():
        return []
    out: list[Path] = []
    for p in sorted(docs.rglob("*")):
        if not p.is_file():
            continue
        if p.name.startswith(".") or p.name == ".gitkeep":
            continue
        if p.suffix.lower() in {".md", ".qmd"}:
            out.append(p)
    return out


def list_bib_auto_files(project: Path) -> list[tuple[Path, str]]:
    """Return (path, kind) for bibliography auto corpus.

    kind: bib_auto_index | bib_auto
    """
    out: list[tuple[Path, str]] = []
    catalog = project / "bibliography" / "auto" / "docs.md"
    if catalog.is_file() and catalog.stat().st_size > 20:
        out.append((catalog, "bib_auto_index"))
    bib_docs = project / "bibliography" / "docs"
    if bib_docs.is_dir():
        for p in sorted(bib_docs.rglob("*.md")):
            if not p.is_file() or p.name.startswith(".") or p.name == ".gitkeep":
                continue
            out.append((p, "bib_auto"))
    return out


def ensure_corpus_md(project: Path, source: Path, dest_rel: str, transform=None) -> Path:
    corpus = project / "graphify-out" / "_corpus"
    dest = corpus / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    text = source.read_text(encoding="utf-8", errors="replace")
    if transform:
        text = transform(text)
    dest.write_text(text, encoding="utf-8")
    return dest


def prepare(project: Path, force: bool = False) -> dict:
    config = load_config(project)
    manifest = load_manifest(project)
    entries: dict = manifest.setdefault("entries", {})
    needs_agent: list[str] = []
    prepared: list[str] = []
    skipped: list[str] = []

    # profile.md
    profile = project / "profile.md"
    if profile.exists():
        rel = "profile.md"
        digest = sha256_file(profile)
        ent = entries.get(rel)
        if (
            not force
            and ent
            and ent.get("sha256") == digest
            and ent.get("status") in {"md_ready", "graphify_indexed"}
        ):
            skipped.append(rel)
        else:
            text = profile.read_text(encoding="utf-8", errors="replace")
            headings = count_md_headings(text)
            status = "md_ready" if headings >= 1 else "needs_agent"
            entries[rel] = {
                "sha256": digest,
                "status": status,
                "kind": "profile",
                "heading_count": headings,
                "updated_at": utc_now(),
            }
            prepared.append(rel)
            if status == "needs_agent":
                needs_agent.append(rel)

    # structure (local or modelo → corpus copy)
    struct_src, kind = resolve_structure_source(project, config)
    if struct_src is None:
        print(
            "warn: no structure.md local and modelo missing under common/structure/",
            file=sys.stderr,
        )
    else:
        if kind == "local":
            rel = "structure.md"
            digest = sha256_file(struct_src)
            index_path = struct_src
        else:
            modelo = str(config.get("modelo") or "model1")
            rel = f"modelo:{modelo}"
            digest = sha256_file(struct_src)
            index_path = ensure_corpus_md(
                project, struct_src, "structure.md",
            )
            # header note for provenance
            body = index_path.read_text(encoding="utf-8")
            if not body.startswith("<!-- modelo:"):
                index_path.write_text(
                    f"<!-- modelo: common/structure/{modelo}.md -->\n\n{body}",
                    encoding="utf-8",
                )

        ent = entries.get(rel)
        if (
            not force
            and ent
            and ent.get("sha256") == digest
            and ent.get("status") in {"md_ready", "graphify_indexed"}
        ):
            skipped.append(rel)
        else:
            text = index_path.read_text(encoding="utf-8", errors="replace")
            headings = count_md_headings(text)
            status = "md_ready" if headings >= MIN_HEADINGS_NOTE else "needs_agent"
            entries[rel] = {
                "sha256": digest,
                "status": status,
                "kind": "structure",
                "source": entry_key(str(struct_src.relative_to(REPO_ROOT)) if struct_src.is_relative_to(REPO_ROOT) else str(struct_src)),
                "index_md": entry_key(str(index_path.relative_to(project))),
                "heading_count": headings,
                "updated_at": utc_now(),
            }
            prepared.append(rel)
            if status == "needs_agent":
                needs_agent.append(rel)

    # course notes
    for note in list_note_files(project):
        rel = entry_key(str(note.relative_to(project)))
        digest = sha256_file(note)
        ent = entries.get(rel)
        if (
            not force
            and ent
            and ent.get("sha256") == digest
            and ent.get("status") in {"md_ready", "graphify_indexed"}
        ):
            skipped.append(rel)
            continue

        if note.suffix.lower() == ".qmd":
            index_path = ensure_corpus_md(
                project,
                note,
                Path("notes") / f"{note.stem}.md",
                transform=strip_qmd_frontmatter,
            )
            text = index_path.read_text(encoding="utf-8", errors="replace")
            index_rel = entry_key(str(index_path.relative_to(project)))
        else:
            index_path = note
            text = note.read_text(encoding="utf-8", errors="replace")
            index_rel = rel

        headings = count_md_headings(text)
        status = "md_ready" if headings >= MIN_HEADINGS_NOTE else "needs_agent"
        entries[rel] = {
            "sha256": digest,
            "status": status,
            "kind": "note",
            "index_md": index_rel,
            "heading_count": headings,
            "updated_at": utc_now(),
        }
        prepared.append(rel)
        if status == "needs_agent":
            needs_agent.append(rel)
            print(f"needs_agent: {rel} (headings={headings})")
        else:
            print(f"prepared: {rel} (headings={headings})")

    # bibliography auto: catalog + PDF→MD under bibliography/docs/
    for bib_path, bib_kind in list_bib_auto_files(project):
        rel = entry_key(str(bib_path.relative_to(project)))
        digest = sha256_file(bib_path)
        ent = entries.get(rel)
        needs_enrich = False
        if bib_kind == "bib_auto":
            peek = bib_path.read_text(encoding="utf-8", errors="replace")
            needs_enrich = "section-chunks + finding-hooks" not in peek
        if (
            not force
            and not needs_enrich
            and ent
            and ent.get("sha256") == digest
            and ent.get("status") in {"md_ready", "graphify_indexed"}
        ):
            skipped.append(rel)
            continue

        # bib_auto papers: enrich with finding hooks + page locators before hash/index
        if bib_kind == "bib_auto":
            try:
                # import sibling script next to this file
                sys.path.insert(0, str(Path(__file__).resolve().parent))
                from graphify_bib_enrich import enrich_bib_md

                pdf_candidate = (
                    project / "bibliography" / "auto" / "pdfs" / f"{bib_path.stem}.pdf"
                )
                enrich_bib_md(
                    bib_path,
                    pdf_candidate if pdf_candidate.is_file() else None,
                    force=force or needs_enrich,
                )
            except Exception as e:
                print(f"warn: bib enrich skipped for {rel}: {e}", file=sys.stderr)

        digest = sha256_file(bib_path)
        text = bib_path.read_text(encoding="utf-8", errors="replace")
        headings = count_md_headings(text)
        min_h = 1 if bib_kind == "bib_auto_index" else MIN_HEADINGS_NOTE
        status = "md_ready" if headings >= min_h else "needs_agent"
        entry: dict = {
            "sha256": digest,
            "status": status,
            "kind": bib_kind,
            "index_md": rel,
            "heading_count": headings,
            "updated_at": utc_now(),
        }
        if bib_kind == "bib_auto":
            pdf_candidate = (
                project / "bibliography" / "auto" / "pdfs" / f"{bib_path.stem}.pdf"
            )
            if pdf_candidate.is_file():
                entry["source_pdf"] = entry_key(
                    str(pdf_candidate.relative_to(project))
                )
            if "section-chunks + finding-hooks" in text:
                entry["technique"] = "section-chunks + finding-hooks + es-aliases"
        entries[rel] = entry
        prepared.append(rel)
        if status == "needs_agent":
            needs_agent.append(rel)
            print(f"needs_agent: {rel} (headings={headings})")
        else:
            print(f"prepared: {rel} (headings={headings})")

    save_manifest(project, manifest)
    report = {
        "stage": "A_prepare",
        "prepared": prepared,
        "skipped": skipped,
        "needs_agent": needs_agent,
        "manifest": str(project / MANIFEST_NAME),
    }
    print(json.dumps({"prepare": report}, ensure_ascii=False, indent=2))
    return report


def stamp_agent(project: Path, rel: str, notes: str = "") -> None:
    manifest = load_manifest(project)
    key = entry_key(rel)
    ent = manifest.setdefault("entries", {}).get(key)
    if not ent:
        print(f"error: no manifest entry for {key}", file=sys.stderr)
        sys.exit(1)
    index_rel = ent.get("index_md") or key
    path = project / index_rel
    if not path.exists():
        path = project / key
    if not path.exists():
        print(f"error: missing file for {key}", file=sys.stderr)
        sys.exit(1)
    text = path.read_text(encoding="utf-8", errors="replace")
    headings = count_md_headings(text)
    if headings < MIN_HEADINGS_NOTE:
        print(
            f"error: need >= {MIN_HEADINGS_NOTE} headings, found {headings}",
            file=sys.stderr,
        )
        sys.exit(1)
    ent["status"] = "md_ready"
    ent["heading_count"] = headings
    source_for_hash = project / key if (project / key).is_file() else path
    ent["sha256"] = sha256_file(source_for_hash)
    ent["agent_notes"] = notes
    ent["updated_at"] = utc_now()
    save_manifest(project, manifest)
    print(f"stamped md_ready: {key} (headings={headings})")


def stamp_graphify(project: Path, indexed_rels: list[str]) -> None:
    manifest = load_manifest(project)
    entries = manifest.setdefault("entries", {})
    now = utc_now()
    for rel in indexed_rels:
        key = entry_key(rel)
        ent = entries.get(key)
        if not ent:
            continue
        if ent.get("status") == "needs_agent":
            continue
        ent["status"] = "graphify_indexed"
        ent["graphify_indexed_at"] = now
    save_manifest(project, manifest)


def collect_md_files(project: Path) -> tuple[list[Path], list[str]]:
    manifest = load_manifest(project)
    entries = manifest.get("entries", {})
    md_files: list[Path] = []
    indexed_keys: list[str] = []

    for key, ent in sorted(entries.items()):
        if ent.get("status") == "needs_agent":
            print(f"skip (needs_agent): {key}")
            continue
        if ent.get("status") not in {"md_ready", "graphify_indexed"}:
            continue
        index_rel = ent.get("index_md") or key
        # modelo: keys use corpus path
        if key.startswith("modelo:"):
            path = project / (ent.get("index_md") or "graphify-out/_corpus/structure.md")
        elif index_rel != key and (project / index_rel).exists():
            path = project / index_rel
        else:
            path = project / key
        if not path.exists():
            print(f"warn: missing {path}", file=sys.stderr)
            continue
        if path.suffix.lower() != ".md":
            continue
        md_files.append(path)
        indexed_keys.append(key)

    # Always try profile/structure on disk if somehow missing from prepare
    for name in ("profile.md", "structure.md"):
        p = project / name
        if p.exists() and p not in md_files:
            md_files.append(p)
            indexed_keys.append(name)

    return md_files, indexed_keys


def build_graph(project: Path) -> dict:
    from graphify.analyze import god_nodes as find_gods, surprising_connections
    from graphify.build import build
    from graphify.cluster import cluster, score_all
    from graphify.export import to_json
    from graphify.extractors.markdown import extract_markdown
    from graphify.report import generate

    out = project / "graphify-out"
    out.mkdir(parents=True, exist_ok=True)

    md_files, indexed_keys = collect_md_files(project)
    extractions = []
    per_file_nodes: dict[str, int] = {}
    for f in md_files:
        result = extract_markdown(f)
        if not result:
            continue
        n = len(result.get("nodes") or [])
        try:
            label = str(f.relative_to(project))
        except ValueError:
            label = f.name
        per_file_nodes[label] = n
        extractions.append(result)
        print(f"extracted: {label} → {n} nodes")

    if not extractions or not any(e.get("nodes") for e in extractions):
        print("error: no markdown nodes extracted", file=sys.stderr)
        sys.exit(1)

    G = build(extractions, directed=False, root=str(project))
    communities = cluster(G)
    cohesion = score_all(G, communities)
    labels = {i: f"Community {i}" for i in communities}
    gods = find_gods(G)
    surprises = surprising_connections(G)

    graph_path = out / "graph.json"
    if not to_json(G, communities, str(graph_path), force=True, community_labels=labels):
        print("error: to_json refused", file=sys.stderr)
        sys.exit(1)

    detection = {
        "files_by_type": {"document": [str(p) for p in md_files]},
        "total_files": len(md_files),
        "total_words": 0,
        "languages": {},
    }
    token_cost = {"input": 0, "output": 0, "total": 0, "model": "offline-ast"}
    try:
        report = generate(
            G, communities, cohesion, labels, gods, surprises, detection, token_cost, str(project)
        )
    except Exception as e:
        report = (
            f"# Graphify project report\n\n"
            f"- Nodes: {G.number_of_nodes()}\n- Edges: {G.number_of_edges()}\n"
            f"- Fallback: {e}\n"
        )
    (out / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    try:
        from graphify.exporters.html import to_html

        to_html(G, communities, str(out / "graph.html"), community_labels=labels)
    except Exception as e:
        print(f"warn: graph.html skipped: {e}", file=sys.stderr)

    stamp_graphify(project, indexed_keys)
    meta = {
        "stage": "C_build",
        "mode": "offline-markdown",
        "project": str(project),
        "files": list(per_file_nodes.keys()),
        "nodes_per_file": per_file_nodes,
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "communities": len(communities),
        "manifest": str(project / MANIFEST_NAME),
        "graph": str(graph_path),
    }
    (out / "project-build.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps({"build": meta}, ensure_ascii=False, indent=2))
    return meta


def verify(project: Path) -> dict:
    graph_path = project / "graphify-out" / "graph.json"
    manifest = load_manifest(project)
    errors: list[str] = []
    warnings: list[str] = []

    if not graph_path.exists():
        errors.append("missing graphify-out/graph.json")
        result = {"ok": False, "errors": errors, "warnings": warnings}
        print(json.dumps({"verify": result}, indent=2))
        return result

    data = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = data.get("nodes") or []

    profile_nodes = [n for n in nodes if str(n.get("source_file", "")).endswith("profile.md")]
    if (project / "profile.md").exists() and len(profile_nodes) < MIN_PROFILE_NODES:
        errors.append(
            f"profile.md under-indexed ({len(profile_nodes)} nodes, want >= {MIN_PROFILE_NODES})"
        )

    note_files = list_note_files(project)
    if note_files:
        note_nodes = [
            n
            for n in nodes
            if (sf := str(n.get("source_file", "")).replace("\\", "/")).startswith("docs/")
            or "/_corpus/notes/" in sf
            or sf.startswith("graphify-out/_corpus/notes/")
        ]
        if len(note_nodes) < 1:
            warnings.append("docs/ notes present but no note nodes in graph")

    bib_files = list_bib_auto_files(project)
    if bib_files:
        bib_nodes = [
            n
            for n in nodes
            if (sf := str(n.get("source_file", "")).replace("\\", "/")).startswith(
                "bibliography/"
            )
        ]
        if len(bib_nodes) < 1:
            warnings.append("bibliography auto MD present but no bibliography nodes in graph")

    entries = manifest.get("entries") or {}
    for key, ent in entries.items():
        if ent.get("status") == "needs_agent":
            warnings.append(f"pending needs_agent: {key}")

    if len(nodes) < 5:
        errors.append(f"graph too small: {len(nodes)} nodes")

    # smoke queries from profile keywords
    queries = ["proyecto", "problema", "alcance"]
    profile = project / "profile.md"
    if profile.exists():
        text = profile.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\*\*Nombre del proyecto:\*\*\s*(.+)", text):
            word = re.sub(r"\W+", " ", m.group(1)).strip().split()
            if word:
                queries.insert(0, word[0])
                break

    for q in queries[:4]:
        r = subprocess.run(
            ["graphify", "query", q, "--graph", str(graph_path), "--budget", "600"],
            capture_output=True,
            text=True,
        )
        out = (r.stdout or "") + (r.stderr or "")
        m = re.search(r"(\d+) nodes found", out)
        count = int(m.group(1)) if m else 0
        if count < 1:
            warnings.append(f"query empty: {q!r}")
        else:
            print(f"query_ok: {q!r} → {count} nodes")

    result = {
        "stage": "D_verify",
        "ok": not errors,
        "nodes": len(nodes),
        "errors": errors,
        "warnings": warnings,
        "graph": str(graph_path),
        "manifest": str(project / MANIFEST_NAME),
    }
    print(json.dumps({"verify": result}, ensure_ascii=False, indent=2))
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="Project Graphify pipeline")
    ap.add_argument("project")
    ap.add_argument("--prepare-only", action="store_true")
    ap.add_argument("--build-only", action="store_true")
    ap.add_argument("--verify-only", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--stamp-agent", metavar="ENTRY_REL")
    ap.add_argument("--stamp-notes", default="")
    args = ap.parse_args()
    project = Path(args.project).resolve()
    if not project.is_dir():
        print(f"error: not a directory: {project}", file=sys.stderr)
        sys.exit(1)

    if args.stamp_agent:
        stamp_agent(project, args.stamp_agent, notes=args.stamp_notes)
        return

    if args.verify_only:
        ok = verify(project)["ok"]
        sys.exit(0 if ok else 1)

    if args.build_only:
        build_graph(project)
        ok = verify(project)["ok"]
        sys.exit(0 if ok else 1)

    prep = prepare(project, force=args.force)
    if args.prepare_only:
        sys.exit(2 if prep.get("needs_agent") else 0)

    if prep.get("needs_agent"):
        print(
            "error: unresolved needs_agent — enrich headings then --stamp-agent:\n"
            + "\n".join(f"  - {x}" for x in prep["needs_agent"]),
            file=sys.stderr,
        )
        sys.exit(2)

    build_graph(project)
    ok = verify(project)["ok"]
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
