# ITD — Proyectos académicos + Graphify

Skills de inicio:

- Explorar: `init-theme` → `init-theme-polish` → `init-project`
- Tema ya propuesto: `init-theme-audit` → `init-theme-audit-polish` → `init-project`

Graphify: `graphify-project`, `graphify-root`.

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

## Skills

| Skill | Qué hace | Salida |
|-------|----------|--------|
| `init-theme` | 3–4 tópicos → 3 alternativas + benchmarking | `theme.md` |
| `init-theme-polish` | Debate 4 agentes sobre las 3 alts | `theme-debate.md` + `theme-polish.md` |
| `init-theme-audit` | 1 tema propuesto + benchmarking | `theme-audit.md` |
| `init-theme-audit-polish` | Debate 4 agentes (modo una_alternativa) | `theme-audit-debate.md` + `theme-audit-polish.md` |
| `init-project` | Inicializa proyecto (profile + config) | `docs/content/<FOLDER>/` |
| `graphify-project` | Memoria Graphify de un proyecto | `docs/content/<FOLDER>/graphify-out/` |
| `graphify-root` | Memoria Graphify del repo | `graphify-out/` |

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
# Explorar
init-theme → init-theme-polish → init-project → …

# Tema ya propuesto (ej. Romantex)
init-theme-audit → init-theme-audit-polish → init-project → …
  → pegar/ajustar structure.md (override) o config.modelo (path)
  → apuntes en docs/content/<FOLDER>/docs/
  → init-project-mvp (rellena tools["mvp-N"])
  → graphify-project (PASS)
```

De vez en cuando **`graphify-root`** si cambias skills / README.

## Requisitos Graphify

```bash
pipx install graphifyy
pipx ensurepath && hash -r
graphify install --platform cursor
```
