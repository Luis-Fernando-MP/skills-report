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

**SoT del cómo:** `common/make-report/model1.md`. Seguir ese playbook al pie (incluye **Reglas Capítulo 1**).

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
5. **Validación pre-redacción** (obligatoria): coherencia profile / company / MVP / bib. Si hay dudas o contradicciones → lanzar subagente `critico-estricto` (modo `validacion_informe`) **antes** de escribir. Corregir o acotar con hechos públicos; **no** volcar meta-dudas al draft.
6. Graphify query mientras se redacta (`company`, profile, bib, MVP activo si aplica). Si existe theme-audit/benchmark del tema → usar **nombres** de vendors/referentes.
7. Tools `mvp-N` **integran** puente al proyecto; **no** sustituyen FODA/Lean de la empresa (ver Reglas Cap. 1 del playbook). Cap. presentación → `company.md` + fuentes; ampliar ficha si es corta.
8. Escribir `docs/vN-tag/draft.md` **detallado y concreto** (reseña real, FODA sujeto empresa, Lean empresa + contraste PoC). Huecos de cita → `TODO: citar — …`.
9. Autochequeo Cap. 1 del playbook. Escanear TODOs; **append** `docs/reports-trace.json`; registrar `config.tools["make-report"]`.
10. `pnpm graphify:project -- <FOLDER>`.
11. Si hay TODOs de citación → **bibliography-search** → reemplazar → Graphify otra vez.
12. Chat: path draft, trace, secciones, TODOs restantes, search sí/no.

## Estándar de calidad del draft (no negociable)

- Informe **verídico, concreto, sustancial** — base para polish, no borrador evasivo ni genérico.
- **Prohibido en el cuerpo:** labels de pipeline (`pendiente_campo`, etc.); “valídalo tú”; FODA/Lean solo-PoC; frases “existen soluciones” sin nombres cuando el corpus los tiene.
- **Permitido:** acotar con fuentes públicas; decir que no hay misión formal publicada (sin repetir disclaimer en cada subsección).
- Separar hechos públicos de diseño del proyecto **en prosa**, sin etiquetas internas.
- Reseña histórica: ≥3 párrafos útiles con hitos; no confundir falta de AS-IS con falta de historia pública.
- Citas necesarias; evitar spam. Metadato de portada alineado con el contenido.

## Forbidden

- Draft fuera de `docs/vN-tag/`; sobrescribir versión.
- Inventar fuentes; omitir Referencias; volcar MVP entero.
- Redactar cap. empresa **sin** `company.md` cuando el sujeto es empresa/entidad.
- Meter labels de pipeline en el draft.
- Sustituir diagnóstico/modelo de negocio de la empresa por solo riesgos/demo del curso.
- Mezclar catálogo search con `bibliography/auto`; graphify-root.
- Editar `reporte.md` aquí (eso es **make-report-polish**).
