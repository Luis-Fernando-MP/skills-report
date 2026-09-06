---
name: init-project
description: >-
  Create an academic project under docs/content/{FOLDER}: derive folder name
  from the topic, fill profile.md (mirror of theme-audit-polish) and config.json
  (citation_style, modelo, alcance, mvp, playbooks, tools). Use when user says
  init-project (legacy: project-init).
---

# init-project

Tercer paso de la familia **init-*** (tras `init-theme-audit-polish` / `init-theme-polish` si aplica). Inicializa un **proyecto académico** en `docs/content/<FOLDER>/`.

## CLI vs skill

| Vía | Input | Qué hace |
|-----|--------|----------|
| `pnpm project:init <FOLDER>` | **Solo** nombre de carpeta | Molde vacío + defaults |
| Esta skill | Tema + extras / polish | **Deriva** `FOLDER`, crea molde, rellena **profile** y **config** |

## Layout

```text
docs/content/<FOLDER>/
  config.json          # citation_style, modelo, alcance, mvp, playbooks, tools
  profile.md           # espejo: tema final + MVP + Marco PICOCT (si viene del polish)
  structure.md         # opcional — override del modelo común
  docs/                # apuntes md/qmd del curso
  mvp/                 # lo crea init-project-mvp → mvp/mvp-N-slug/*.md

common/citation-style/*.md
common/structure/*.md
common/<tool>/model1.md   # playbooks (vía config.playbooks)
```

## Schema `config.json`

```json
{
  "citation_style": "common/citation-style/APA7.md",
  "modelo": "common/structure/model1.md",
  "alcance": [],
  "mvp": 1,
  "playbooks": {
    "design-thinking": "common/design-thinking/model1.md",
    "lean-canvas": "common/lean-canvas/model1.md",
    "rat": "common/rat/model1.md",
    "foda": "common/foda/model1.md",
    "as-is-to-be": "common/as-is-to-be/model1.md"
  },
  "tools": {}
}
```

| Clave | Valor | Uso |
|-------|--------|-----|
| `citation_style` | path `common/citation-style/*.md` | estilo de cita del informe |
| `modelo` | path `common/structure/*.md` | índice default |
| `alcance` | array (vacío = todo el índice) | futuro make-informe |
| `mvp` | número activo | init-project-mvp / make-informe |
| `playbooks` | tool → path common | **cómo** generar (init-project-mvp) |
| `tools` | mapa `mvp-N` → artefactos generados | **qué** usar en el informe; vacío hasta mvp |

Tras `init-project-mvp` para N=1, ejemplo:

```json
"tools": {
  "mvp-1": {
    "design-thinking": "./mvp/mvp-1-<slug>/design-thinking.md",
    "lean-canvas": "./mvp/mvp-1-<slug>/lean-canvas.md",
    "foda": "./mvp/mvp-1-<slug>/foda.md",
    "rat": "./mvp/mvp-1-<slug>/rat.md",
    "as-is-to-be": "./mvp/mvp-1-<slug>/as-is-to-be.md"
  }
}
```

Lookup activo: `tools["mvp-" + config.mvp]`.

## Resolución del índice

1. `docs/content/<FOLDER>/structure.md` con contenido útil → **override** (pisa `modelo`).
2. Si no → leer el path de `config.modelo`.
3. Si el path no existe → listar `common/structure/*.md` y pedir corrección.

**No** crear `structure.md` en el molde (sigue opcional).

## Compatibilidad (configs viejos)

Si `tools` apunta a `common/...` y no hay `playbooks`: tratar esos valores como `playbooks`, dejar `tools: {}`, avisar en chat.

## Procedure

1. Leer lo que aportó el usuario. **Fuente preferida:** `docs/topics/<…>/theme-audit-polish.md` (Tema final + MVP entregables + **Marco PICOCT**); si no, `theme-polish.md`; si no, input manual. No inventar hechos de empresa.
2. **Derivar `FOLDER`:** código corto del usuario o slug; si ya existe, preguntar.
3. Si la carpeta no existe → `pnpm project:init <FOLDER>` desde la raíz del repo.
4. Escribir **`profile.md`** como espejo del polish:
   - Tema / Descripción / Problema / Alcance / MVP entregables / Origen.
   - Si el polish trae **`## Marco PICOCT (para bibliography)`** (o equivalente) → **copiarla completa** (no acortar).
   - Si el polish es GO/GO_con_cambios y **falta** Marco PICOCT → avisar en chat (ideal re-correr `init-theme-audit-polish` o completar a mano).
5. Escribir **`config.json`:**
   - `citation_style`: default `common/citation-style/APA7.md` (verificar que exista).
   - `modelo`: default `common/structure/model1.md` (verificar).
   - `alcance`: array o `[]` + avisar.
   - `mvp`: arranque del polish o `1`.
   - `playbooks`: default todos model1; si el usuario pide subconjunto o `model2`, validar paths bajo `common/`.
   - `tools`: `{}` (los rellena **init-project-mvp**).
6. Chat: path, `FOLDER`, `config.mvp`, playbooks, si PICOCT quedó en profile, siguiente **`init-project-mvp mvp-<N>`** (y luego **graphify-project** cuando haya corpus que indexar).

## Lookup (después de creado el proyecto)

Cuando el grafo exista, skills/agentes sobre este `FOLDER` usan:

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

## Forbidden

- Inventar datos de empresa/tema no aportados.
- Acortar el polish si trae MVP entregables **o** Marco PICOCT.
- Copiar playbooks de `common/` al proyecto (solo referenciar en `playbooks`).
- Rellenar `tools` con paths `common/` (eso es `playbooks`).
- Regenerar Graphify / ejecutar **init-project-mvp** aquí.
- Tocar RSL ni borrar proyectos sin confirmación.
