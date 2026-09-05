---
name: init-project
description: >-
  Create an academic project under docs/content/{FOLDER}: derive folder name
  from the topic, fill profile.md and config.json (citation_style, modelo,
  alcance). Use when user says init-project (legacy: project-init).
---

# init-project

Tercer paso de la familia **init-*** (tras `init-theme` / `init-theme-polish` si aplica). Inicializa un **proyecto académico** en `docs/content/<FOLDER>/`.

## CLI vs skill

| Vía | Input | Qué hace |
|-----|--------|----------|
| `pnpm project:init <FOLDER>` | **Solo** nombre de carpeta | Molde vacío + `APA7` + `modelo: model1` |
| Esta skill | Tema + extras del usuario | **Deriva** `FOLDER`, crea molde, rellena **profile** y **config** |

## Layout

```text
docs/content/<FOLDER>/
  config.json     # citation_style, modelo, alcance
  profile.md      # nombre, descripción, problema, alcance de propuesta
  structure.md    # opcional — si existe, pisa al modelo común
  docs/           # apuntes md/qmd del curso

common/citation-style/<id>.md
common/structure/<modelo>.md   # índice si no hay structure.md local
```

## Resolución del índice

1. `docs/content/<FOLDER>/structure.md` con contenido útil → usar ese.
2. Si no → `common/structure/{config.modelo}.md`.
3. Si falta el modelo → listar `common/structure/*.md` y pedir corrección.

## Procedure

1. Leer lo que aportó el usuario (tema, descripción, problema, alcance, estilo de cita, modelo, capítulos, carpeta explícita). Si viene de `theme-polish.md`, preferir el tema final de ahí.
2. **Derivar `FOLDER`:**
   - Si el usuario da un código corto (`MOST`, `FIS`) → usarlo.
   - Si no → slug corto (mayúsculas o kebab seguro) a partir del curso/tema; si `docs/content/<FOLDER>/` ya existe, preguntar o elegir variante.
3. Si la carpeta no existe → `pnpm project:init <FOLDER>` desde la raíz del repo.
4. Escribir **`profile.md`** solo con datos dados (no inventar hechos de empresa):

```markdown
# Perfil del proyecto

**Nombre del proyecto:** …
**Descripción:** …
**Problema identificado:** …
**Alcance de la propuesta:** …
```

5. Escribir **`config.json`:**
   - `citation_style`: el que diga el usuario si existe `common/citation-style/<id>.md`; default `APA7`.
   - `modelo`: si dice “usa el modelo X” → `X` tras verificar `common/structure/X.md`; default `model1`.
   - `alcance`: si indica capítulos/secciones (o `*`) → array tipo `[{ "capitulo": "1", "secciones": "*" }]`; si no → `[]` y avisar.
6. **Índice:**
   - Modelo común pedido → solo `config.modelo` (no copiar el md al proyecto).
   - Índice pegado por el usuario → crear `structure.md` local (gana sobre `modelo`).
   - Nada → dejar `modelo: "model1"` sin `structure.md`.
7. Chat: path, `FOLDER`, qué quedó en profile/config, índice efectivo, y qué falta (`alcance`, apuntes en `docs/`, etc.).

## Invoke examples

```text
Usa init-project

Carpeta: MOST
Tema: Informe digitalización inventario PyME calzado
Descripción: …
Problema: …
Alcance: MVP inventario + fichas técnicas
Modelo: model1
Citas: APA7
Alcance capítulos: capítulo 1 todas las secciones
```

```text
Usa init-project con el tema final de docs/topics/ITD/theme-polish.md
```

## Forbidden

- Inventar datos de empresa/tema no aportados.
- Copiar `common/structure/*.md` al proyecto solo porque se eligió un modelo (usar `config.modelo`).
- Regenerar Graphify (eso es **graphify-project**).
- Tocar skills RSL ni borrar proyectos existentes sin confirmación.
