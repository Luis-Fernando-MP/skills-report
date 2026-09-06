---
name: bibliography-auto
description: >-
  Find up to 5 open-access sources from a project profile (no PICOCT), debate
  usefulness with critico-estricto and defensor-fundamento before download,
  save PDFs under bibliography/auto/pdfs, MD under bibliography/docs, catalog
  in auto/docs.md (only what was actually downloaded), then create/refresh
  project Graphify. Use when user says bibliography-auto.
---

# bibliography-auto

Busca **hasta 5** fuentes **OA públicas** para un proyecto en `docs/content/<FOLDER>/`, valida utilidad con **2 agentes** antes de descargar, escribe PDF + MD + catálogo y refresca Graphify.

**SoT del cómo:** `common/bibliography-auto/model1.md`. Seguir ese playbook al pie.

**Independiente de PICOCT** — no usar `bibliography/PICOCT|PICOC|PICO/` como input.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  config.json
  bibliography/
    auto/
      docs.md             # catálogo FINAL: solo lo descargado (1:1 con pdfs/)
      debate.md           # acta utilidad (+ pendiente_oa / rechazos)
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

## Lookup Graphify (obligatorio en el proyecto)

Antes de Grep/Read amplio de `bibliography/`, `mvp/`, `docs/` o PDFs:

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

Usar el resultado del grafo (documento, finding, `src`, página/`loc`) para orientar; no volcar MD/PDF al contexto. Si no hay `graphify-out/graph.json` → pedir **graphify-project**. Tras esta skill, el refresh (paso 10) deja el grafo al día.

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (`citation_style`).
2. Leer playbook `common/bibliography-auto/model1.md` y el playbook de citación apuntado por config.
3. Si ya hay contenido en `bibliography/auto/` o MD top-level en `bibliography/docs/*.md` (excluir `docs/search/`) → **preguntar** antes de sobrescribir.
4. Buscar candidatos OA (agente elige bases/queries). **No descargar aún.**
5. **Debate** (Task / agentes), modo `bibliography_auto_utilidad`:
   - `critico-estricto` — utilidad / ruido / fuera de alcance; WebSearch ≤3.
   - `defensor-fundamento` — evidencia o `punto_debil`; WebSearch ≤3.
6. Consolidar → `bibliography/auto/debate.md`. Solo `GO` / `GO_con_cambios` pasan; ante duda → no descargar.
7. Descargar ≤5 PDFs OA → `auto/pdfs/`; `pdftotext` → `bibliography/docs/<slug>.md`; enriquecer con `python scripts/graphify_bib_enrich.py …` (≥3 headings; findings + páginas). Verificar archivos en disco.
8. **Al final del material** (después de 7, antes de Graphify): escribir `bibliography/auto/docs.md` **solo** con fuentes que tengan PDF + MD reales. Si hay 2 PDFs → 2 secciones. No inventar `pendiente_oa` ni paths.
9. Registrar `config.tools["bibliography-auto"]` (catalog, debate, pdfs, docs).
10. Invocar **graphify-project**: `pnpm graphify:project -- <FOLDER>` (create o update; manifest skip por hash).
11. Chat: aceptadas (con path), rechazadas, `pendiente_oa` (solo chat/debate), Graphify skipped vs nuevos.

## Formato `docs.md` (por fuente real)

- Título, Autores, Keywords, Razón, Cita (`citation_style`), DOI/URL, PDF, MD, Estado (`ok`).
- **Regla:** el número de secciones `##` = número de PDFs en `auto/pdfs/`. Nada más.

## Forbidden

- Ignorar el playbook.
- Usar PICOCT como dependencia.
- Descargar antes del debate.
- Escribir `docs.md` antes de terminar descargas/MD, o con más entradas que archivos reales.
- Inventar fichas / DOI / PDF / `pendiente_oa` en el catálogo.
- Paywall bypass / Sci-Hub.
- Más de 5 PDFs; guardar PDF fuera de `auto/pdfs/`.
- graphify-root; make-informe.
- Sobrescribir en silencio.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../../agents/defensor-fundamento.md)

```text
modo: bibliography_auto_utilidad
FOLDER
profile_resumen + candidatos (sin PDF aún)
objetivo: GO|NO_GO por utilidad al profile
```
