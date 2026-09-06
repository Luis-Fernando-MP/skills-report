# ITD — Proyectos académicos + Graphify

## Skills (orden de ejecución)

Dos vías de arranque del tema; después el pipeline es el mismo.

### Vía A — Explorar tópicos

| # | Skill | Qué hace |
|---|--------|----------|
| 1 | `init-theme` | Tópicos → `brainstorm-theme` → ficha empresa si aplica → `benchmark-theme` → `theme-brainstorm.md` + `theme.md` |
| 2 | `init-theme-polish` | Debate 5 agentes (+ `gramatica-continuidad` en R3) → `theme-debate.md` + `theme-polish.md` (ficha si empresa\|entidad) |

### Vía B — Tema ya propuesto

| # | Skill | Qué hace |
|---|--------|----------|
| 1 | `init-theme-audit` | Tema propuesto → ficha si aplica → `brainstorm-theme` → `benchmark-theme` → `theme-audit-brainstorm.md` + `theme-audit.md` |
| 2 | `init-theme-audit-polish` | Debate 5 agentes (+ `gramatica-continuidad` en R3) → `theme-audit-debate.md` + `theme-audit-polish.md` (ficha si empresa\|entidad) |

### Proyecto e informe (después de A o B)

| # | Skill | Qué hace |
|---|--------|----------|
| 3 | `init-project` | Crea `docs/content/<FOLDER>/` con `profile.md` + `config.json` |
| 4 | `init-project-mvp` | Genera pack MVP (`mvp/mvp-N-slug/*.md`) y registra `tools["mvp-N"]` |
| 5 | `bibliography-picoct` | Marco PICO/PICOC/PICOCT, keywords EN/ES y ecuaciones Scopus |
| 6 | `bibliography-auto` | Hasta 5 fuentes OA vía **bibliography-oa-sources** (debate → PDF/MD + `auto/docs.md` + Graphify) |
| 7 | `make-report` | Draft versionado `docs/vN-tag/draft.md` + `docs/reports-trace.json` (alias `make-informe`) |
| 8 | `bibliography-search` | OA para huecos `TODO: citar` vía **bibliography-oa-sources** → `bibliography/search` + `docs/search` + Graphify |
| 9 | `make-report-polish` | Pule último draft → `reporte.md` + `reporte-debate.md` (7 agentes; no toca draft) |
| — | `bibliography-oa-sources` | Capacidad compartida OA multi-fuente (OpenAlex/S2/arXiv/PubMed); la usan auto y search |
| — | `prepare-bibliography-manual` | *(pendiente)* CSV / búsqueda manual / PRISMA |

Agentes de tema (no skills sueltas): `brainstorm-theme`, `benchmark-theme` — los lanzan init-theme / init-theme-audit.

### Memoria Graphify (cuando haga falta)

| Skill | Qué hace |
|--------|----------|
| `graphify-project` | Indexa un proyecto académico (`docs/content/<FOLDER>/graphify-out/`) |
| `graphify-root` | Indexa el repo (skills, README, layout) |

## Layout

```text
docs/topics/<FOLDER>/
  theme-brainstorm.md      # acta lluvia (init-theme)
  theme.md                 # 3 alternativas (init-theme)
  theme-debate.md          # acta (init-theme-polish)
  theme-polish.md          # veredicto (init-theme-polish)
  theme-audit-brainstorm.md # acta lluvia (init-theme-audit)
  theme-audit.md           # tema único (init-theme-audit)
  theme-audit-debate.md    # acta (init-theme-audit-polish)
  theme-audit-polish.md    # veredicto (init-theme-audit-polish)

docs/content/<FOLDER>/
  config.json           # citation_style, modelo (paths), alcance, mvp, playbooks, tools
  profile.md            # tema, descripción, problema, alcance
  structure.md          # opcional — si existe, pisa config.modelo
  docs/                 # apuntes + drafts vN-tag/draft.md + reports-trace.json + reporte.md
  mvp/                  # packs generados (init-project-mvp)
  bibliography/         # auto/ + search/ + docs/ (+ docs/search/)
  graphify-out/         # memoria del proyecto (gitignored)
  index-manifest.json

common/citation-style/  # APA7.md, IEEE.md  ← config.citation_style
common/structure/       # model1.md, …     ← config.modelo (si no hay override)
common/make-report/
common/make-report-polish/
common/bibliography-auto/
common/bibliography-search/
common/bibliography-oa-sources/  # capacidad OA multi-fuente (auto + search)
common/bibliography-picoct/
common/design-thinking/ # + lean-canvas, foda, rat, as-is-to-be (MVP)

graphify-out/           # memoria del repo (skills, README…)
```

**Índice del informe:** `structure.md` local si existe con contenido útil; si no → path en `config.modelo` (p. ej. `common/structure/model1.md`).

**Config (resumen):** `playbooks` = cómo generar (`common/…`); `tools` = mapa `mvp-N` → artefactos en `./mvp/mvp-N-slug/*.md`.

## Init — explorar tópicos

```text
Usa init-theme
Carpeta: ITD
Tópicos:
1. …
2. …
3. …
```

```text
Usa init-theme-polish sobre ITD
```

## Init — auditar un tema ya propuesto

```text
Usa init-theme-audit
Carpeta: ITD
Tema: Digitalización del inventario y estandarización de tallaje en Calzados Romantex S.A.C
Descripción: …
Problema: …
Alcance: …
```

```text
Usa init-theme-audit-polish sobre ITD
```

## Init — proyecto

| Vía | Input | Efecto |
|-----|--------|--------|
| `pnpm project:init <FOLDER>` | Solo nombre de carpeta | Molde vacío (paths APA7 + model1, playbooks, `tools: {}`) |
| Skill `init-project` | Tema + extras (o `theme-polish.md`) | Deriva carpeta; rellena **profile** y **config** |

```bash
pnpm project:init MOST
```

```text
Usa init-project
Carpeta: MOST
Tema: …
Descripción: …
Problema: …
Alcance: …
Modelo: common/structure/model1.md
```

## Graphify — proyecto

```text
Usa graphify-project sobre FIS
```

```bash
pnpm graphify:project -- FIS
pnpm graphify:project -- FIS --prepare-only
```

Consulta:

```bash
graphify query "Lean Canvas" --graph docs/content/FIS/graphify-out/graph.json
```

## Graphify — root

```text
Usa graphify-root
```

```bash
pnpm graphify:refresh
```

## Chequeo local

```bash
pnpm run check:pipeline
```

Valida skills/playbooks, links a agentes, paths bib auto vs search, y `reports-trace` de DDS.

## Orden sugerido

```text
# Vía A
init-theme → init-theme-polish → init-project → init-project-mvp
  → bibliography-picoct → bibliography-auto → make-report → bibliography-search → make-report-polish

# Vía B (tema ya propuesto)
init-theme-audit → init-theme-audit-polish → init-project → init-project-mvp
  → bibliography-picoct → bibliography-auto → make-report → bibliography-search → make-report-polish

# Memoria (cuando cambies docs / skills)
graphify-project | graphify-root
# bibliography-auto / bibliography-search / make-report / make-report-polish invocan graphify-project al cerrar
```

## Requisitos Graphify

```bash
pipx install graphifyy
pipx ensurepath && hash -r
graphify install --platform cursor
```
