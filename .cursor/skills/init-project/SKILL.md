---
name: init-project
description: >-
  Create an academic project under docs/content/{FOLDER}: derive folder name
  from the topic, fill profile.md (mirror of theme-audit-polish), company.md
  when the subject is a real company/entity, and config.json. Use when user
  says init-project (legacy: project-init).
---

# init-project

Tercer paso de la familia **init-*** (tras `init-theme-audit-polish` / `init-theme-polish` si aplica). Inicializa un **proyecto académico** en `docs/content/<FOLDER>/`.

## CLI vs skill

| Vía | Input | Qué hace |
|-----|--------|----------|
| `pnpm project:init <FOLDER>` | **Solo** nombre de carpeta | Molde vacío + defaults |
| Esta skill | Tema + extras / polish | **Deriva** `FOLDER`, crea molde, rellena **profile**, **company.md** (si aplica) y **config** |

## Layout

```text
docs/content/<FOLDER>/
  config.json          # citation_style, modelo, alcance, mvp, playbooks, tools
  profile.md           # espejo: tema final + MVP + Marco PICOCT
  company.md           # SOLO si tipo_sujeto = empresa|entidad (omitir si dominio_sin_empresa)
  structure.md         # opcional — override del modelo común
  docs/                # apuntes md/qmd del curso
  mvp/                 # lo crea init-project-mvp

common/citation-style/*.md
common/structure/*.md
common/<tool>/model1.md
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
| `alcance` | array (vacío = todo el índice) | make-report |
| `mvp` | número activo | init-project-mvp / make-report |
| `playbooks` | tool → path common | **cómo** generar (init-project-mvp) |
| `tools` | mapa `mvp-N` + opc. `company` | **qué** usar en el informe |

Tras crear `company.md`:

```json
"tools": {
  "company": "./company.md"
}
```

(Los `mvp-N` los rellena **init-project-mvp**.)

## Resolución del índice

1. `docs/content/<FOLDER>/structure.md` con contenido útil → **override**.
2. Si no → path de `config.modelo`.
3. Si el path no existe → listar `common/structure/*.md` y pedir corrección.

**No** crear `structure.md` en el molde (sigue opcional).

## Compatibilidad (configs viejos)

Si `tools` apunta a `common/...` y no hay `playbooks`: tratar esos valores como `playbooks`, dejar `tools: {}`, avisar en chat.

## `company.md` (condicional)

**Crear** si el polish / tema tiene `tipo_sujeto: empresa|entidad` (o nombra organización real).  
**No crear** si `dominio_sin_empresa` o el usuario declara que no hay organización ancla.

Fuente: ficha del polish (`theme-audit-polish` / `theme-polish`). Si la ficha es pobre → **completar con investigación pública** (WebSearch / oficiales) **antes** de escribir; no inventar.

Plantilla mínima:

```markdown
# Empresa — <Nombre>

## Identificación
- Razón social / marca: …
- País / sede pública: …
- Sector: …
- Escala (pública): …

## Reseña histórica
*(Fundación, hitos, expansión — solo hechos con fuente pública. Sustancia: varios párrafos, no dos líneas.)*

## Misión, visión y valores
…

## Principios / identidad de gestión (si publicados)
…

## Oferta y relevancia para el proyecto
*(Líneas de negocio / productos públicos ligados al problema del profile.)*

## Fuentes
- …
```

## Procedure

1. Leer lo que aportó el usuario. **Fuente preferida:** `docs/topics/<…>/theme-audit-polish.md` (Tema final + MVP + **Marco PICOCT** + ficha empresa); si no, `theme-polish.md`; si no, input manual. No inventar hechos de empresa.
2. Determinar `tipo_sujeto` (del polish o clasificar).
3. **Derivar `FOLDER`:** código corto del usuario o slug; si ya existe, preguntar.
4. Si la carpeta no existe → `pnpm project:init <FOLDER>` desde la raíz del repo.
5. Escribir **`profile.md`** como espejo del polish:
   - Tema / Descripción / Problema / Alcance / MVP entregables / Origen.
   - Incluir `tipo_sujeto`.
   - Si el polish trae **`## Marco PICOCT`** → **copiarla completa**.
   - Si GO/GO_con_cambios y **falta** Marco PICOCT → avisar en chat.
6. Si aplica empresa/entidad → escribir **`company.md`** (plantilla arriba) + registrar `tools.company`. Si no aplica → **no** crear el archivo.
7. Escribir **`config.json`:**
   - `citation_style`: default `common/citation-style/APA7.md`.
   - `modelo`: default `common/structure/model1.md`.
   - `alcance`: array o `[]` + avisar.
   - `mvp`: arranque del polish o `1`.
   - `playbooks`: default model1.
   - `tools`: `{}` o `{ "company": "./company.md" }` si hubo ficha.
8. Chat: path, `FOLDER`, si hay `company.md`, `config.mvp`, playbooks, PICOCT, siguiente **`init-project-mvp mvp-<N>`**.

## Lookup

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

## Forbidden

- Inventar datos de empresa/tema no aportados ni hallados en fuentes públicas.
- Omitir `company.md` cuando el tema es de empresa/entidad real.
- Crear `company.md` vacío o de dos líneas cuando hay fuentes públicas abundantes.
- Acortar el polish si trae MVP entregables **o** Marco PICOCT.
- Copiar playbooks de `common/` al proyecto (solo referenciar en `playbooks`).
- Rellenar `tools` con paths `common/` (eso es `playbooks`).
- Regenerar Graphify / ejecutar **init-project-mvp** aquí.
- Tocar RSL ni borrar proyectos sin confirmación.
