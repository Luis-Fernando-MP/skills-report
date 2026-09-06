---
name: bibliography-search
description: >-
  Find up to 5 open-access sources for citation gaps (e.g. TODO: citar from
  make-report), debate usefulness with critico-estricto and defensor-fundamento
  before download, save under bibliography/search + bibliography/docs/search,
  then refresh project Graphify. Use when user says bibliography-search.
---

# bibliography-search

Busca **hasta 5** fuentes **OA** para cerrar huecos de citación en un proyecto `docs/content/<FOLDER>/`, valida utilidad con **2 agentes** antes de descargar, escribe PDF + MD + catálogo bajo **`bibliography/search/`** y refresca Graphify.

**SoT del cómo:** `common/bibliography-search/model1.md`. Seguir ese playbook al pie.  
**Búsqueda OA (Paso 2):** `common/bibliography-oa-sources/model1.md` (obligatorio).

**No confundir con `bibliography-auto`** (`bibliography/auto/`). Aquí: `bibliography/search/**` + `bibliography/docs/search/`.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  config.json
  bibliography/
    search/
      docs.md
      debate.md
      pdfs/<slug>.pdf
    docs/
      search/<slug>.md
  index-manifest.json
  graphify-out/
```

## Invoke

```text
/bibliography-search
/bibliography-search DDS
/bibliography-search DDS -- from draft TODOs
```

Sin `profile.md` → pedir **init-project** primero. Si viene de **make-report**, usar los `TODO: citar — …` del draft como queries.

## Lookup Graphify (obligatorio)

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

Si no hay grafo → pedir **graphify-project**. Tras esta skill, el refresh deja el grafo al día (incluye `bib_search`).

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (`citation_style`).
2. Leer playbook `common/bibliography-search/model1.md`, el playbook de citación, y **`common/bibliography-oa-sources/model1.md`**.
3. Recoger queries (TODOs del draft o lista del usuario). Si ya hay `bibliography/search/` → **preguntar** antes de sobrescribir.
4. Buscar candidatos OA **según bibliography-oa-sources** (OpenAlex, S2, arXiv, PubMed, …). **No descargar aún.**
5. **Debate** (Task / agentes), modo `bibliography_search_utilidad`:
   - `critico-estricto` — utilidad / ruido / fuera de alcance; WebSearch ≤3.
   - `defensor-fundamento` — evidencia o `punto_debil`; WebSearch ≤3.
6. Consolidar → `bibliography/search/debate.md`. Solo `GO` / `GO_con_cambios` pasan.
7. Descargar ≤5 PDFs OA → `search/pdfs/`; `pdftotext` → `bibliography/docs/search/<slug>.md`; enriquecer con `python scripts/graphify_bib_enrich.py …`. Verificar en disco.
8. **Al final del material:** escribir `bibliography/search/docs.md` **solo** con fuentes que tengan PDF + MD reales.
9. Registrar `config.tools["bibliography-search"]`. Si hay `docs/reports-trace.json`, marcar TODOs `done` cuando se cierren.
10. Invocar **graphify-project**: `pnpm graphify:project -- <FOLDER>`.
11. Chat: aceptadas, rechazadas, `pendiente_oa` (solo chat/debate), citas listas para TODOs si aplica, fuentes OA usadas.

## Formato `docs.md`

- Título, Autores, Keywords, Query/TODO, Razón, Cita, DOI/URL, PDF, MD, Estado (`ok`).
- **Regla:** número de secciones `##` = número de PDFs en `search/pdfs/`.

## Forbidden

- Mezclar catálogos auto vs search.
- Ignorar el playbook search u **oa-sources**; buscar sin `common/bibliography-oa-sources/model1.md`.
- PICOCT como dependencia.
- Descargar antes del debate; inventar fichas / `pendiente_oa` en el catálogo.
- Paywall bypass / Sci-Hub; más de 5 PDFs.
- graphify-root; sobrescribir en silencio.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../../agents/defensor-fundamento.md)

```text
modo: bibliography_search_utilidad
FOLDER
profile_resumen + queries_o_todos + candidatos (sin PDF aún)
objetivo: GO|NO_GO por utilidad a query + profile
```
