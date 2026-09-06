---
name: init-project
description: >-
  Create an academic project under docs/content/{FOLDER}: derive folder name
  from the topic, fill profile.md (mirror of theme-audit-polish) and config.json
  (citation_style, modelo, alcance, mvp, tools). Use when user says init-project
  (legacy: project-init).
---

# init-project

Tercer paso de la familia **init-*** (tras `init-theme-audit-polish` / `init-theme-polish` si aplica). Inicializa un **proyecto académico** en `docs/content/<FOLDER>/`.

## CLI vs skill

| Vía | Input | Qué hace |
|-----|--------|----------|
| `pnpm project:init <FOLDER>` | **Solo** nombre de carpeta | Molde vacío + defaults (`mvp: 1`, `tools` completos) |
| Esta skill | Tema + extras / polish | **Deriva** `FOLDER`, crea molde, rellena **profile** y **config** |

## Layout

```text
docs/content/<FOLDER>/
  config.json          # citation_style, modelo, alcance, mvp, tools
  profile.md           # espejo del tema final + MVP entregables del polish
  structure.md         # opcional — si existe, pisa al modelo común
  docs/                # apuntes md/qmd del curso
  mvp/                 # lo crea init-project-mvp → mvp/mvp-N-slug/*.md

common/citation-style/<id>.md
common/structure/<modelo>.md
common/design-thinking/model1.md   # playbook tool DT (no carpeta de salida)
common/lean-canvas/model1.md
common/rat/model1.md
common/foda/model1.md
common/as-is-to-be/model1.md
```

## Resolución del índice

1. `docs/content/<FOLDER>/structure.md` con contenido útil → usar ese.
2. Si no → `common/structure/{config.modelo}.md`.
3. Si falta el modelo → listar `common/structure/*.md` y pedir corrección.

## Procedure

1. Leer lo que aportó el usuario. **Fuente preferida:** `docs/topics/<…>/theme-audit-polish.md` (Tema final + MVP entregables); si no, `theme-polish.md`; si no, input manual. No inventar hechos de empresa.
2. **Derivar `FOLDER`:** código corto del usuario o slug; si ya existe, preguntar.
3. Si la carpeta no existe → `pnpm project:init <FOLDER>` desde la raíz del repo.
4. Escribir **`profile.md`** como espejo del polish (Tema / Descripción / Problema / Alcance / MVP entregables / Origen).
5. Escribir **`config.json`:**
   - `citation_style`: default `APA7` (verificar `common/citation-style/`).
   - `modelo`: default `model1` (verificar `common/structure/`).
   - `alcance`: array de capítulos o `[]` + avisar.
   - `mvp`: arranque del polish o `1`.
   - `tools`: objeto tool → path de playbook. **Default = todos los model1.** Si el usuario pide un subconjunto o `model2`, validar que el path exista bajo `common/`.

Default `tools`:

```json
"tools": {
  "design-thinking": "common/design-thinking/model1.md",
  "lean-canvas": "common/lean-canvas/model1.md",
  "rat": "common/rat/model1.md",
  "foda": "common/foda/model1.md",
  "as-is-to-be": "common/as-is-to-be/model1.md"
}
```

Ejemplo omitiendo FODA y usando otro canvas a futuro:

```json
"tools": {
  "design-thinking": "common/design-thinking/model1.md",
  "lean-canvas": "common/lean-canvas/model2.md",
  "rat": "common/rat/model1.md",
  "as-is-to-be": "common/as-is-to-be/model1.md"
}
```

6. **Índice:** como antes (`structure.md` local o `config.modelo`).
7. Chat: path, `FOLDER`, `config.mvp`, tools habilitadas, siguiente **`init-project-mvp mvp-<N>`**.

## Forbidden

- Inventar datos de empresa/tema no aportados.
- Acortar el polish si trae MVP entregables.
- Copiar playbooks de `common/` al proyecto (solo referenciar paths en `tools`).
- Regenerar Graphify / ejecutar **init-project-mvp** aquí.
- Tocar RSL ni borrar proyectos sin confirmación.
