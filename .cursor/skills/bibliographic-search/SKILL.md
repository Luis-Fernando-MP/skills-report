---
name: bibliographic-search
description: >-
  Find up to 5 open-access sources for citation gaps (e.g. TODO: citar from
  make-report), debate usefulness with critico-estricto and defensor-fundamento
  before download, save under bibliographic/search + bibliographic/docs, then
  refresh project Graphify. Use when user says bibliographic-search.
---

# bibliographic-search

Busca **hasta 5** fuentes **OA** para cerrar huecos de citación en un proyecto `docs/content/<FOLDER>/`, valida utilidad con **2 agentes** antes de descargar, escribe PDF + MD + catálogo bajo **`bibliographic/`** y refresca Graphify.

**SoT del cómo:** `common/bibliographic-search/model1.md`. Seguir ese playbook al pie.

**No confundir con `bibliography-auto`** (carpeta `bibliography/`). Aquí: `bibliographic/search/**` + `bibliographic/docs/`.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  config.json
  bibliographic/
    search/
      docs.md             # catálogo FINAL: solo lo descargado (1:1 con pdfs/)
      debate.md
      pdfs/<slug>.pdf
    docs/
      <slug>.md           # PDF → MD enrich
  index-manifest.json
  graphify-out/
```

## Invoke

```text
/bibliographic-search
/bibliographic-search DS
/bibliographic-search DS -- from draft TODOs
```

Sin `profile.md` → pedir **init-project** primero. Si viene de **make-report**, usar los `TODO: citar — …` del draft como queries.

## Lookup Graphify (obligatorio)

Antes de Grep/Read amplio:

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

Si no hay grafo → pedir **graphify-project**. Tras esta skill, el refresh deja el grafo al día (incluye `bib_search`).

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (`citation_style`).
2. Leer playbook `common/bibliographic-search/model1.md` y el playbook de citación.
3. Recoger queries (TODOs del draft o lista del usuario). Si ya hay `bibliographic/` → **preguntar** antes de sobrescribir.
4. Buscar candidatos OA. **No descargar aún.**
5. **Debate** (Task / agentes), modo `bibliographic_search_utilidad`:
   - `critico-estricto` — utilidad / ruido / fuera de alcance; WebSearch ≤3.
   - `defensor-fundamento` — evidencia o `punto_debil`; WebSearch ≤3.
6. Consolidar → `bibliographic/search/debate.md`. Solo `GO` / `GO_con_cambios` pasan.
7. Descargar ≤5 PDFs OA → `search/pdfs/`; `pdftotext` → `bibliographic/docs/<slug>.md`; enriquecer con `python scripts/graphify_bib_enrich.py …`. Verificar en disco.
8. **Al final del material:** escribir `bibliographic/search/docs.md` **solo** con fuentes que tengan PDF + MD reales.
9. Registrar `config.tools["bibliographic-search"]`.
10. Invocar **graphify-project**: `pnpm graphify:project -- <FOLDER>`.
11. Chat: aceptadas, rechazadas, `pendiente_oa` (solo chat/debate), citas listas para TODOs si aplica.

## Formato `docs.md`

- Título, Autores, Keywords, Query/TODO, Razón, Cita, DOI/URL, PDF, MD, Estado (`ok`).
- **Regla:** número de secciones `##` = número de PDFs en `search/pdfs/`.

## Forbidden

- Guardar en `bibliography/` o mezclar con bibliography-auto.
- Ignorar el playbook; PICOCT como dependencia.
- Descargar antes del debate; inventar fichas / `pendiente_oa` en el catálogo.
- Paywall bypass / Sci-Hub; más de 5 PDFs.
- graphify-root / graphify-theme; sobrescribir en silencio.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../agents/defensor-fundamento.md)

```text
modo: bibliographic_search_utilidad
FOLDER
profile_resumen + queries_o_todos + candidatos (sin PDF aún)
objetivo: GO|NO_GO por utilidad a query + profile
```
