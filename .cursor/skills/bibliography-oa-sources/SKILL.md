---
name: bibliography-oa-sources
description: >-
  Shared open-access multi-source search playbook (OpenAlex, Semantic Scholar,
  arXiv, PubMed). Not run alone — consumed by bibliography-auto and
  bibliography-search Paso 2. Use when wiring or updating OA candidate search.
---

# bibliography-oa-sources

Capacidad compartida de **candidatos OA multi-fuente**. No descarga PDFs ni escribe catálogos.

**SoT:** `common/bibliography-oa-sources/model1.md`.

## Consumidores

- **`bibliography-auto`** — Paso 2 (queries desde profile)
- **`bibliography-search`** — Paso 2 (queries desde `TODO: citar` / lista)

## Invoke

No se invoca sola en el pipeline de curso. Las skills consumidoras **deben** leer el playbook antes de buscar candidatos.

Si el usuario pide solo “cómo buscar OA”: resumir el playbook; no crear `bibliography/auto` ni `search`.

## Forbidden

- Sustituir a auto/search.
- PRISMA / picoct (draft).
- Sci-Hub / paywall bypass.
- graphify-root / graphify-project desde aquí.
