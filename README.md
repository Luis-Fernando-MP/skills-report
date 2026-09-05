# ITD — Proyectos académicos + Graphify

Skills de inicio: `init-theme` → `init-theme-polish` → `init-project`. Graphify: `graphify-project`, `graphify-root`.

## Layout

```text
docs/topics/<FOLDER>/
  theme.md              # 3 alternativas (init-theme)
  theme-debate.md       # acta + scores (init-theme-polish)
  theme-polish.md       # veredicto + tema final (init-theme-polish)

docs/content/<FOLDER>/
  config.json           # citation_style, modelo, alcance
  profile.md            # tema, descripción, problema, alcance
  structure.md          # opcional — si existe, pisa al modelo común
  docs/                 # apuntes md/qmd
  graphify-out/         # memoria del proyecto (gitignored)
  index-manifest.json

common/citation-style/  # APA7.md, IEEE.md
common/structure/       # model1.md, … (config.modelo)

graphify-out/           # memoria del repo (skills, README…)
```

**Índice del informe:** `structure.md` local si existe; si no → `common/structure/{config.modelo}.md`.

## Skills

| Skill | Qué hace | Salida |
|-------|----------|--------|
| `init-theme` | 3–4 tópicos → 3 alternativas + benchmarking | `docs/topics/<FOLDER>/theme.md` |
| `init-theme-polish` | Debate 4 agentes; scores + veredicto | `theme-debate.md` + `theme-polish.md` |
| `init-project` | Inicializa proyecto (profile + config) | `docs/content/<FOLDER>/` |
| `graphify-project` | Memoria Graphify de un proyecto | `docs/content/<FOLDER>/graphify-out/` |
| `graphify-root` | Memoria Graphify del repo | `graphify-out/` |

## Init — tema

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

## Init — proyecto

| Vía | Input | Efecto |
|-----|--------|--------|
| `pnpm project:init <FOLDER>` | Solo nombre de carpeta | Molde vacío (`APA7`, `modelo: model1`) |
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
Modelo: model1
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
init-theme
  → init-theme-polish   # theme-debate.md + theme-polish.md (o NO_GO → otros tópicos)
  → init-project        # docs/content/<FOLDER>/
  → pegar/ajustar structure o config.modelo
  → apuntes en docs/content/<FOLDER>/docs/
  → graphify-project (PASS)
  → (generación de capítulos: siguiente fase)
```

De vez en cuando **`graphify-root`** si cambias skills / README.

## Requisitos Graphify

```bash
pipx install graphifyy
pipx ensurepath && hash -r
graphify install --platform cursor
```
