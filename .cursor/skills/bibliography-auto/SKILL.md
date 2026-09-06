---
name: bibliography-auto
description: >-
  Find up to 5 open-access sources from a project profile (no PICOCT), debate
  usefulness with critico-estricto and defensor-fundamento before download,
  save PDFs under bibliography/auto/pdfs, MD under bibliography/docs, catalog
  in auto/docs.md, then create/refresh project Graphify. Use when user says
  bibliography-auto.
---

# bibliography-auto

Busca **hasta 5** fuentes **OA públicas** para un proyecto en `docs/content/<FOLDER>/`, valida utilidad con **2 agentes** antes de descargar, escribe catálogo + PDF + MD y refresca Graphify.

**SoT del cómo:** `common/bibliography-auto/model1.md`. Seguir ese playbook al pie.

**Independiente de PICOCT** — no usar `bibliography/PICOCT|PICOC|PICO/` como input.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  config.json
  bibliography/
    auto/
      docs.md             # catálogo (ficha + cita según citation_style)
      debate.md           # acta utilidad
      pdfs/<slug>.pdf
    docs/
      <slug>.md           # PDF → MD
  index-manifest.json
  graphify-out/
```

## Invoke

```text
/bibliography-auto
/bibliography-auto DS
/bibliography-auto @docs/content/DS/config.json
```

Sin `profile.md` → pedir **init-project** primero.

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (`citation_style`).
2. Leer playbook `common/bibliography-auto/model1.md` y el playbook de citación apuntado por config.
3. Si ya hay contenido en `bibliography/auto/` o `bibliography/docs/` → **preguntar** antes de sobrescribir.
4. Buscar candidatos OA (agente elige bases/queries). **No descargar aún.**
5. **Debate** (Task / agentes), modo `bibliography_auto_utilidad`:
   - `critico-estricto` — utilidad / ruido / fuera de alcance; WebSearch ≤3.
   - `defensor-fundamento` — evidencia o `punto_debil`; WebSearch ≤3.
6. Consolidar → `bibliography/auto/debate.md`. Solo `GO` / `GO_con_cambios` pasan; ante duda → no descargar.
7. Descargar ≤5 PDFs OA → `auto/pdfs/`; `pdftotext` → `bibliography/docs/<slug>.md` (≥3 headings).
8. Escribir `bibliography/auto/docs.md` (título, autores, keywords, razón, cita según style, paths, estado).
9. Registrar `config.tools["bibliography-auto"]` (catalog, debate, pdfs, docs).
10. Invocar **graphify-project**: `pnpm graphify:project -- <FOLDER>` (create o update; manifest skip por hash).
11. Chat: aceptadas / rechazadas, `pendiente_oa`, paths, Graphify skipped vs nuevos.

## Formato `docs.md` (por fuente)

- Título, Autores, Keywords, Razón, Cita (`citation_style`), DOI/URL, PDF, MD, Estado (`ok` | `pendiente_oa`).

## Forbidden

- Ignorar el playbook.
- Usar PICOCT como dependencia.
- Descargar antes del debate.
- Paywall bypass / Sci-Hub / inventar DOI o PDF.
- Más de 5 PDFs; guardar PDF fuera de `auto/pdfs/`.
- graphify-root / graphify-theme; make-informe.
- Sobrescribir en silencio.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../agents/defensor-fundamento.md)

```text
modo: bibliography_auto_utilidad
FOLDER
profile_resumen + candidatos (sin PDF aún)
objetivo: GO|NO_GO por utilidad al profile
```
