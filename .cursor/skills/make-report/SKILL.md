---
name: make-report
description: >-
  Draft a versioned professional academic report under docs/content/<FOLDER>/docs/vN-tag/draft.md
  from config.modelo + alcance + company.md, using Graphify and bibliography-search
  for citation gaps; appends docs/reports-trace.json. Alias make-informe. Use when
  user says make-report or make-informe.
---

# make-report

Redacta un **draft versionado, profesional y sustancial** del informe del proyecto en `docs/content/<FOLDER>/` según `config.modelo` y `config.alcance`.

**SoT del cómo:** `common/make-report/model1.md`. Seguir ese playbook al pie.

**Alias:** `make-informe` → esta skill.

Esta skill deja la **base completa** del informe (detalle, prosa, secciones llenas). **`make-report-polish`** produce `reporte.md` sin tocar el draft; **aquí no se entrega un “casi informe” ni un “valídalo tú”**.

## Salida

```text
docs/content/<FOLDER>/docs/v<N>-<tag>/draft.md
docs/content/<FOLDER>/docs/reports-trace.json   # append por versión
```

| Alcance | tag típico |
|---------|------------|
| `[]` / completo | `completo` |
| solo cap. 1 | `capitulo-1` |
| caps. 1–2 | `capitulo-1-2` |

Nueva versión en cada run (nunca sobrescribir). **Referencias** siempre al final.

## Invoke

```text
/make-report
/make-report DS
/make-informe DS
```

Sin `profile.md` → pedir **init-project**.  
Si el profile indica empresa/entidad y **falta** `company.md` → pedir **init-project** (o regenerar ficha) **antes** de redactar cap. 1.1.

## Lookup Graphify (durante redacción)

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

No volcar PDFs/MD al contexto. Preferir findings + `src` + página. Incluir queries a **`company.md`** cuando el outline toque presentación de la empresa.

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (+ **`company.md`** si existe / es requerido).
2. Leer `common/make-report/model1.md` + playbook de `citation_style`.
3. Resolver índice: `structure.md` local útil → override; si no → `config.modelo`.
4. Filtrar outline por `alcance` (`[]` = todo). Decidir `vN-tag`.
5. **Validación pre-redacción** (obligatoria): coherencia profile / company / MVP / bib. Si hay dudas o contradicciones → lanzar subagente `critico-estricto` (modo validación de informe) **antes** de escribir. Corregir o acotar con hechos públicos; **no** volcar meta-dudas al draft.
6. Graphify query mientras se redacta (`company`, profile, bib, MVP activo si aplica).
7. Tools `mvp-N` **solo** si el outline lo pide — integrar, no volcar. Cap. presentación de empresa → **solo** desde `company.md` + fuentes allí listadas (ampliar investigación pública si la ficha es corta).
8. Escribir `docs/vN-tag/draft.md` **detallado y profesional** (ver playbook: densidad, reseña histórica real, sin hedges). Huecos de cita → `TODO: citar — …` (únicos placeholders permitidos).
9. Escanear TODOs; **append** entrada en `docs/reports-trace.json` (`has_draft: true`, `has_polish: false`, `todos[]`). Registrar `config.tools["make-report"]` con `last` + `trace`.
10. `pnpm graphify:project -- <FOLDER>`.
11. Si hay TODOs de citación → **bibliography-search** → reemplazar → marcar `todos[].status: "done"` en el trace de esa versión → Graphify otra vez.
12. Chat: path draft, trace, secciones, TODOs restantes, search sí/no.

## Estándar de calidad del draft (no negociable)

- Informe **verídico, bien explicado, sustancial** — base para polish, no borrador evasivo.
- **Prohibido en el cuerpo del informe:** `pendiente_campo`, “hipótesis a validar con sponsor”, “no se afirma como auditoría”, “propuesta de trabajo no hallazgos”, “casi”, “valídalo tú”, disclaimers metodológicos meta. Eso pertenece a skills de auditoría/MVP, **no** al draft.
- Separar hechos públicos confirmados de proyecciones del proyecto **sin** etiquetas internas de pipeline.
- Reseña histórica (1.1.1): sustancia con fuentes públicas (fundación, hitos, expansión). No confundir con falta de AS-IS interno.
- Citas: necesarias donde hay afirmación teórica/corporativa; evitar spam de la misma cita en cada frase (el polish posterior afinará densidad).
- Metadato de portada alineado con el contenido (si el capítulo está completo según alcance, no contradecir en la prosa).

## Forbidden

- Draft fuera de `docs/vN-tag/`; sobrescribir versión.
- Inventar fuentes; omitir Referencias; volcar MVP entero.
- Redactar cap. empresa **sin** `company.md` cuando el sujeto es empresa/entidad.
- Meter labels de pipeline (`pendiente_campo`, etc.) en el draft.
- Mezclar catálogo search con `bibliography/auto`; graphify-root.
- Editar `reporte.md` aquí (eso es **make-report-polish**).
