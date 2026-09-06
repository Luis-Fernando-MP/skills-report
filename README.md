# ITD — Proyectos académicos + Graphify

## Skills (orden de ejecución)

Dos vías de arranque del tema; después el pipeline es el mismo.

### Vía A — Explorar tópicos

| # | Skill | Qué hace |
|---|--------|----------|
| 1 | `init-theme` | De 3–4 tópicos, propone 3 alternativas de proyecto + benchmarking |
| 2 | `init-theme-polish` | Debate 4 agentes sobre las 3 alts → veredicto y tema final |

### Vía B — Tema ya propuesto

| # | Skill | Qué hace |
|---|--------|----------|
| 1 | `init-theme-audit` | Audita un tema concreto + benchmarking |
| 2 | `init-theme-audit-polish` | Debate 4 agentes (una alternativa) → veredicto, tema final y MVP entregables |

### Proyecto e informe (después de A o B)

| # | Skill | Qué hace |
|---|--------|----------|
| 3 | `init-project` | Crea `docs/content/<FOLDER>/` con `profile.md` + `config.json` |
| 4 | `init-project-mvp` | Genera pack MVP (`mvp/mvp-N-slug/*.md`) y registra `tools["mvp-N"]` |
| 5 | `bibliography-picoct` | Marco PICO/PICOC/PICOCT, keywords EN/ES y ecuaciones Scopus |
| 6 | `make-informe` | *(pendiente)* Redacta el informe según structure + alcance + tools |
| — | `prepare-bibliography-manual` / `automatic` | *(pendiente)* CSV / búsqueda de fuentes |

### Memoria Graphify (cuando haga falta)

| Skill | Qué hace |
|--------|----------|
| `graphify-project` | Indexa un proyecto académico (`docs/content/<FOLDER>/graphify-out/`) |
| `graphify-root` | Indexa el repo (skills, README, layout) |
| `graphify-theme` | Indexa un tema RSL legado (`docs/[titulo-breve]/`) |

### RSL legado (opcional, paralelo al flujo init)

| Skill | Qué hace |
|--------|----------|
| `rsl-make-report` | Arma `informe.md` UTP + PDFs RSL |
| `rsl-polish-report` | Pule el informe con debate 4 agentes |
| `rsl-make-paper` | Arma introducción académica `paper.md` |
| `rsl-polish-paper` | Pule el paper con debate 4 agentes |

## Layout

```text
docs/topics/<FOLDER>/
  theme.md                 # 3 alternativas (init-theme)
  theme-debate.md          # acta (init-theme-polish)
  theme-polish.md          # veredicto (init-theme-polish)
  theme-audit.md           # tema único (init-theme-audit)
  theme-audit-debate.md    # acta (init-theme-audit-polish)
  theme-audit-polish.md    # veredicto (init-theme-audit-polish)

docs/content/<FOLDER>/
  config.json           # citation_style, modelo (paths), alcance, mvp, playbooks, tools
  profile.md            # tema, descripción, problema, alcance
  structure.md          # opcional — si existe, pisa config.modelo
  docs/                 # apuntes md/qmd
  mvp/                  # packs generados (init-project-mvp)
  graphify-out/         # memoria del proyecto (gitignored)
  index-manifest.json

common/citation-style/  # APA7.md, IEEE.md  ← config.citation_style
common/structure/       # model1.md, …     ← config.modelo (si no hay override)

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

## Orden sugerido

```text
# Vía A
init-theme → init-theme-polish → init-project → init-project-mvp
  → bibliography-picoct → (bib manual/auto) → make-informe

# Vía B (tema ya propuesto)
init-theme-audit → init-theme-audit-polish → init-project → init-project-mvp
  → bibliography-picoct → (bib manual/auto) → make-informe

# Memoria (cuando cambies docs / skills)
graphify-project | graphify-root
```

## Requisitos Graphify

```bash
pipx install graphifyy
pipx ensurepath && hash -r
graphify install --platform cursor
```
