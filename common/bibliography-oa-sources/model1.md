# Bibliography OA sources — model1

Playbook de **capacidad compartida**: búsqueda **open access multi-fuente**.

**Consumidores:** `bibliography-auto` y `bibliography-search` (obligatorio en su Paso 2).  
**No** es skill de cierre Graphify ni de descarga. **No** usar desde `bibliography-picoct` ni PRISMA (aún draft).

## Propósito

Dado un conjunto de **queries** (desde profile o desde `TODO: citar`), producir una lista corta de **candidatos OA** con metadatos verificables **sin descargar PDF**.

## Fuentes (orden de intento)

Usar **al menos 2** de las primarias por corrida (salvo que una sola ya cubra ≥8 candidatos útiles). Preferir APIs/páginas públicas.

| Prioridad | Fuente | Cuándo | OA tip |
|-----------|--------|--------|--------|
| 1 | **OpenAlex** | Default amplio (works, open access filter) | `is_oa` / `oa_url` / `best_oa_location` |
| 2 | **Semantic Scholar** | CS/SE, overlap con OpenAlex | `openAccessPdf.url` si existe |
| 3 | **arXiv** | Preprints CS/math/stat | PDF directo `arxiv.org/pdf/…` |
| 4 | **PubMed / PMC** | Salud, bio, clínico | PMC full text / enlace OA |
| 5 | **Crossref / Unpaywall** (opcional) | Resolver DOI → OA | Solo si hay DOI dudoso |
| 6 | **SciELO / publishers OA** | ES/LATAM o journal OA explícito | Landing → PDF |

**Forbidden:** Sci-Hub, Library Genesis, shadow libraries, bypass de paywall, inventar DOI/PDF.

## Entrada

```text
modo_consumidor: bibliography_auto | bibliography_search
FOLDER
queries: […]          # auto: derivadas del profile; search: TODOs / lista
profile_resumen: …    # breve
max_candidatos_crudos: 12–20   # antes del filtro OA
max_para_debate: 8–12          # lo que pasa al crítico/defensor
```

## Procedimiento

### 1. Armar queries

- **auto:** 2–5 queries EN (y 1–2 ES si el dominio es LATAM) desde tema/problema/alcance del profile. Evitar buzzwords solos (`digitalization`, `AI`).
- **search:** una query por `TODO: citar — …` (+ sinónimos cortos). No mezclar varios TODOs en una sola query opaca.

### 2. Buscar en paralelo lógico

Por cada query, consultar ≥2 fuentes de la tabla. Anotar `fuente` en cada hit.

Herramientas: WebSearch / WebFetch / APIs públicas documentadas. No scrapear agresivo.

### 3. Normalizar candidato

Campos obligatorios:

| Campo | Notas |
|-------|--------|
| titulo | |
| autores | lista corta |
| año | |
| abstract_o_snippet | ≤800 chars |
| keywords | si hay |
| doi_url | DOI o landing |
| pdf_oa_url | solo si OA explícito; si no, vacío |
| fuente | openalex \| semantic_scholar \| arxiv \| pubmed \| other |
| query_origen | qué query/TODO lo trajo |
| is_oa | true \| false \| unknown |

### 4. Dedupe

1. Mismo DOI → 1 registro (fusionar fuentes).
2. Sin DOI: título normalizado (lowercase, sin puntuación) + año.
3. Preferir el registro con `pdf_oa_url` no vacío.

### 5. Priorizar para el debate

Orden sugerido:

1. `is_oa=true` + `pdf_oa_url` presente  
2. Alineación a query/profile (título/abstract)  
3. Año reciente si el dominio lo pide  
4. Venue reconocible (no blog)

Pasar al debate **8–12** candidatos máx. (el consumidor recorta a ≤5 PDFs tras GO).

### 6. Salida hacia el consumidor

Lista JSON-like o markdown checklist **sin** archivos en disco. El consumidor corre el debate y solo entonces descarga.

```text
candidatos: [
  { titulo, autores, año, abstract_o_snippet, keywords?, doi_url, pdf_oa_url?, fuente, query_origen, is_oa }
]
fuentes_consultadas: [openalex, semantic_scholar, …]
queries_usadas: […]
```

## Forbidden

- Descargar PDF aquí.
- Inventar metadatos o URLs OA.
- Usar solo una fuente genérica de WebSearch sin pasar por OpenAlex/S2/arXiv/PubMed cuando el dominio aplica.
- Mezclar resultados en `bibliography/auto` vs `search` (eso lo hace el consumidor).
- Sci-Hub / paywall bypass.

## Relación

| Skill | Cómo usa este playbook |
|-------|-------------------------|
| **bibliography-auto** | Paso 2: queries desde profile → candidatos |
| **bibliography-search** | Paso 2: queries desde TODOs → candidatos |
| bibliography-picoct / PRISMA | **No** (siguen en draft) |
