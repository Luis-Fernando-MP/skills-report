# Make report — model1

Playbook para la skill **`make-report`** (alias **`make-informe`**). Redacta un **draft versionado, profesional y sustancial** del informe académico según `config.modelo` + `config.alcance`, usa **`company.md`** cuando hay organización ancla, Graphify durante la redacción, y cierra huecos de citación con **bibliographic-search**.

**No es `rsl-make-report`**. Aquí: `docs/content/<FOLDER>/`.

## Propósito

Producir:

```text
docs/content/<FOLDER>/docs/v<N>-<tag>/draft.md
```

Esta skill deja la **base completa** del informe (detalle, prosa académica, secciones llenas). Una skill de polish posterior limpiará estilo/citas; **aquí no se entrega un “casi informe”**.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  company.md           # si tipo_sujeto = empresa|entidad (requerido para cap. 1.1)
  config.json
  structure.md         # opcional
  docs/vN-tag/draft.md
  mvp/…
  bibliographic/…
  graphify-out/
```

## Schema `config.alcance`

| Valor | Significado |
|-------|-------------|
| `[]`, `"*"`, `["*"]` | Toda la estructura del modelo |
| `[{ "capitulo": 1, "secciones": ["*"] }]` | Solo ese capítulo |
| `[{ "capitulo": 1, "secciones": ["1.1", "1.2"] }]` | Prefijo inclusivo |
| Varios objetos | Unión |

**Referencias:** siempre al final del `draft.md`.

## Tag de versión

| Alcance efectivo | `<tag>` |
|------------------|---------|
| Todo el modelo | `completo` |
| Solo capítulo 1 | `capitulo-1` |
| Capítulos 1 y 2 | `capitulo-1-2` |
| Otro recorte | `capitulo-<lista>` |

`<N>` = siguiente entero libre bajo `docs/v*-*/` (nunca sobrescribir).

## Estándar de calidad (obligatorio)

### Qué sí

- Prosa **académico-profesional**, párrafos desarrollados, secciones con sustancia.
- Cap. presentación de empresa: **reseña histórica real** (fundación, hitos, expansión) desde `company.md` + fuentes públicas; misión/visión/valores con sustancia.
- Diagnóstico y Lean Canvas: integrar MVP de forma narrativa **cerrada** (hechos del proyecto como decisiones/criterios del PoC, no como dudas abiertas al lector).
- Separar en frases distintas lo **documentado con fuente** de lo que es **diseño del PoC** — sin etiquetas internas.
- Citas donde aportan (teoría, dato corporativo); no repetir la misma cita en cada frase.
- Portada/metadato **alineados** con lo que el draft realmente cubre.

### Qué no (prohibido en el cuerpo del draft)

| Prohibido | Por qué |
|-----------|---------|
| `pendiente_campo`, `hipótesis`, `evidencia` como labels de pipeline | Son meta del proceso init/MVP, no del informe |
| “no se afirma como auditoría certificada”, “valídalo con sponsor”, “propuesta de trabajo no hallazgos” | Descarga la responsabilidad al lector |
| Reseña histórica de 2 líneas + salvedad metodológica | Confunde falta de AS-IS interno con falta de historia pública |
| Inventar hechos internos de la empresa | Solo fuentes públicas / `company.md` |
| “Casi reporte”, disclaimers de calidad | El polish limpia; esta base debe ser sólida |

**Único placeholder permitido en el draft:** `TODO: citar — <afirmación>` cuando falta fuente verificable.

## Pipeline

```mermaid
flowchart TD
  company[company_md] --> validate[Validacion_pre]
  profile[profile_md] --> validate
  validate --> outline[Outline_por_alcance]
  outline --> draftWrite[Redactar_draft_profesional]
  mvp[tools_mvp_N] --> draftWrite
  graphNow[graphify_query] --> draftWrite
  cite[citation_style] --> draftWrite
  draftWrite --> out["docs/vN-tag/draft.md"]
  out --> gp1[pnpm_graphify_project]
  draftWrite --> todos[TODO_citar]
  gp1 --> todos
  todos -->|hay_pendientes| search[bibliographic_search]
  search --> replace[Reemplazar_TODOs]
  replace --> gp3[graphify_project]
  todos -->|sin_pendientes| done[Listo]
  gp3 --> done
```

### Paso 1 — Resolver proyecto

1. `FOLDER` + leer `profile.md` y `config.json`.
2. Si `tipo_sujeto` / tema implica empresa o entidad:
   - Exigir `company.md` (o `config.tools.company`). Si falta o está vacío → **detener** y pedir `init-project` / completar ficha.
   - Si existe pero es pobre (p. ej. <1 página útil) → **ampliar con investigación pública** antes de redactar 1.1; actualizar `company.md`.
3. Si `dominio_sin_empresa` → no exigir `company.md`; omitir o adaptar secciones de empresa del modelo con justificación **sustantiva** en el draft (contexto del dominio), sin disclaimers de pipeline.
4. Resolver índice: `structure.md` local útil → override; si no → `config.modelo`.
5. Leer playbook de `citation_style`.
6. Sin `profile.md` → pedir **init-project**.

### Paso 2 — Outline por alcance

1. Parsear el índice del modelo.
2. Filtrar según `config.alcance`. `[]` = completo.
3. Construir outline de headings (`##`, `###`).
4. Decidir `<tag>` y `<N>`.

### Paso 3 — Validación pre-redacción

Antes de escribir el draft:

1. Contrastar profile ↔ company ↔ MVP ↔ bib (Graphify + lectura dirigida).
2. Si hay contradicciones, huecos graves o riesgo de meta-prosa → lanzar subagente **`critico-estricto`** en modo `validacion_informe` con el outline y hallazgos.
3. Resolver: completar `company.md`, acotar afirmaciones a fuentes, o ampliar investigación. **No** copiar objeciones del crítico al draft como disclaimers.

### Paso 4 — Lookup Graphify (durante redacción)

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

Consultas típicas: empresa (`company.md`), tema, papers, conceptos del capítulo, MVP.

### Paso 5 — Tools MVP (condicional)

Solo si el outline pide entregables MVP (Lean Canvas, FODA, AS-IS/TO-BE, etc.):

1. Leer `config.tools["mvp-N"]` (`N = config.mvp`).
2. **Integrar** en prosa profesional; **no** volcar el MD ni labels `hipótesis`/`pendiente_campo`.

### Paso 6 — Redactar `draft.md`

1. Crear `docs/v<N>-<tag>/draft.md`.
2. Portada breve: FOLDER, tema, fecha, versión — sin contradecir el contenido.
3. **1.1 / presentación de empresa** (si aplica): redactar desde `company.md`:
   - **1.1.1 Reseña histórica:** varios párrafos (fundación, hitos, expansión global/sector) con citas a fuentes de la ficha.
   - Misión, visión, valores: desarrollados, no un bullet cada uno.
4. Resto del outline: densidad alta, coherencia narrativa.
5. Citas según `citation_style`. Falta de fuente → solo `TODO: citar — …`.
6. **Referencias** al final (entradas reales usadas).
7. Anexos solo si el alcance/modelo lo pide.

**Forbidden en redacción:** inventar DOI/papers; Sci-Hub; verbatim largos; sobrescribir `vN`; labels de pipeline; disclaimers de “no auditoría”.

### Paso 7 — Registrar y Graphify

```json
"make-report": {
  "last": "./docs/v<N>-<tag>/draft.md"
}
```

```bash
pnpm graphify:project -- <FOLDER>
```

### Paso 8 — Cerrar TODOs de citación

1. Listar `TODO: citar — …`.
2. Si hay ≥1 → **bibliographic-search**.
3. Reemplazar TODOs + Referencias; Graphify de nuevo.
4. Si un TODO queda sin OA → dejar el `TODO: citar` (único residual aceptable); no inventar.

### Paso 9 — Chat

Path, tag/N, secciones, uso de `company.md` sí/no, TODOs restantes, search sí/no, Graphify ok.

## Forbidden

- Confundir con **rsl-make-report**.
- Salida fuera de `docs/v<N>-<tag>/draft.md`.
- Sobrescribir versión existente.
- Omitir Referencias.
- Volcar tools MVP; inventar fuentes.
- Redactar empresa sin `company.md` cuando el sujeto es empresa/entidad.
- Meter `pendiente_campo` / disclaimers de pipeline en el draft.
- Resultados de search en `bibliography/auto`.
- Refresh graphify-root / graphify-theme.

## Relación con otras skills

| Skill | Rol |
|-------|-----|
| **init-project** | Crea `company.md` + profile |
| **graphify-project** | Lookup + refresh |
| **bibliographic-search** | Cerrar `TODO: citar` |
| **bibliography-auto** | Corpus base previo (opcional) |
| **rsl-make-report** | Otro dominio |
