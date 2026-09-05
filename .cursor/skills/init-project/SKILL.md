---
name: init-project
description: >-
  Create an academic project under docs/content/{FOLDER}: derive folder name
  from the topic, fill profile.md (mirror of theme-audit-polish) and config.json
  (citation_style, modelo, alcance, mvp). Use when user says init-project
  (legacy: project-init).
---

# init-project

Tercer paso de la familia **init-*** (tras `init-theme-audit-polish` / `init-theme-polish` si aplica). Inicializa un **proyecto académico** en `docs/content/<FOLDER>/`.

## CLI vs skill

| Vía | Input | Qué hace |
|-----|--------|----------|
| `pnpm project:init <FOLDER>` | **Solo** nombre de carpeta | Molde vacío + `APA7` + `modelo: model1` + `mvp: 1` |
| Esta skill | Tema + extras / polish | **Deriva** `FOLDER`, crea molde, rellena **profile** y **config** |

## Layout

```text
docs/content/<FOLDER>/
  config.json          # citation_style, modelo, alcance, mvp
  profile.md           # espejo del tema final + MVP entregables del polish
  structure.md         # opcional — si existe, pisa al modelo común
  docs/                # apuntes md/qmd del curso
  design-thinking/     # lo crea init-project-mvp (no esta skill)

common/citation-style/<id>.md
common/structure/<modelo>.md   # índice si no hay structure.md local
```

## Resolución del índice

1. `docs/content/<FOLDER>/structure.md` con contenido útil → usar ese.
2. Si no → `common/structure/{config.modelo}.md`.
3. Si falta el modelo → listar `common/structure/*.md` y pedir corrección.

## Procedure

1. Leer lo que aportó el usuario. **Fuente preferida:** `docs/topics/<…>/theme-audit-polish.md` (Tema final + MVP entregables); si no, `theme-polish.md`; si no, input manual. No inventar hechos de empresa.
2. **Derivar `FOLDER`:**
   - Si el usuario da un código corto (`MOST`, `PASS`) → usarlo.
   - Si no → slug corto; si `docs/content/<FOLDER>/` ya existe, preguntar o elegir variante.
3. Si la carpeta no existe → `pnpm project:init <FOLDER>` desde la raíz del repo.
4. Escribir **`profile.md`** como espejo del polish (misma información; sin inventar):

```markdown
# Perfil del proyecto

## Tema
…

## Descripción
…

## Problema identificado
…

## Alcance
…

## MVP entregables

### MVP de arranque (recomendado al equipo)
MVP N — …

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | … | … | … | se trabaja ahora |
| … | … | … | … | … |

### Fuera de secuencia / descartado
- …

## Origen
- polish: docs/topics/…/theme-audit-polish.md (o theme-polish.md / manual)
- veredicto: GO | GO_con_cambios | (n/a)
```

5. Escribir **`config.json`:**
   - `citation_style`: el del usuario si existe `common/citation-style/<id>.md`; default `APA7`.
   - `modelo`: el pedido tras verificar `common/structure/X.md`; default `model1`.
   - `alcance`: capítulos/secciones si los indica; si no → `[]` y avisar.
   - `mvp`: número del **MVP de arranque** del polish/profile; default **`1`**.
6. **Índice:** modelo común → solo `config.modelo`; índice pegado → `structure.md` local; nada → `model1` sin structure local.
7. Chat: path, `FOLDER`, `config.mvp`, índice efectivo, qué falta (`alcance`, apuntes), siguiente skill **`init-project-mvp mvp-<N>`**.

## Invoke examples

```text
Usa init-project

Carpeta: PASS
Fuente: docs/topics/ITD/theme-audit-polish.md
Modelo: model1
Citas: APA7
```

```text
Usa init-project con el tema final de docs/topics/ITD/theme-audit-polish.md
```

## Forbidden

- Inventar datos de empresa/tema no aportados.
- Acortar el polish a 4 campos planos si el polish trae MVP entregables.
- Copiar `common/structure/*.md` al proyecto solo porque se eligió un modelo.
- Regenerar Graphify (**graphify-project**).
- Ejecutar Design Thinking aquí (**init-project-mvp**).
- Tocar skills RSL ni borrar proyectos existentes sin confirmación.
