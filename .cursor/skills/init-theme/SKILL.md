---
name: init-theme
description: >-
  First step of the init family: from 3–4 topics, run brainstorm-theme then
  company research and benchmark-theme; write theme-brainstorm.md and theme.md
  with 3 project alternatives. Use when user says init-theme.
---

# init-theme

Primer paso de la familia **init-*** cuando **exploras** desde tópicos. Define 3 alternativas en `docs/topics/<FOLDER>/`.

Si **ya tienes un tema concreto** (empresa + problema + alcance) → usa **`init-theme-audit`**, no esta skill.

Siguiente skill: **`init-theme-polish`**.

## Layout

```text
docs/topics/<FOLDER>/
  theme-brainstorm.md   # acta lluvia (esta skill)
  theme.md              # 3 alternativas definidas (esta skill)
  theme-debate.md       # init-theme-polish
  theme-polish.md       # init-theme-polish
```

Al re-ejecutar: **sobrescribir** `theme-brainstorm.md` y `theme.md` sin preguntar.

## Invoke

```text
Usa init-theme

Carpeta: ITD
Tópicos:
1. …
2. …
3. …
4. …   # opcional
```

Sin tópicos → preguntar. No inventar el dominio del usuario.

## Clasificación del sujeto

Por cada tópico/candidata que **nombre una empresa u organización real** → investigar fuentes públicas (identidad, historia, misión/visión/valores, sector) **antes del benchmark**. Si es dominio sin org. → `tipo_sujeto: dominio_sin_empresa` y no inventar empresa.

Si una alternativa depende de empresa real y no hay evidencia pública mínima → marcar `evidencia_empresa: insuficiente` o descartar esa alt. (no inventar).

## Procedure

1. Leer tópicos (3–4) y carpeta opcional.
2. **Resolver `FOLDER`:** código del usuario (`ITD`, `MOST`, …) o slug corto; crear `docs/topics/<FOLDER>/` si no existe.
3. Armar CONTEXTO con `modo: N_alternativas`.
4. Lanzar **`brainstorm-theme`** (3 lentes) → escribir **`theme-brainstorm.md`** con la salida del agente (plantilla abajo).
5. Clasificar sujeto por candidata; **investigar empresa** cuando aplique (WebSearch / oficiales).
6. Lanzar **`benchmark-theme`** con CONTEXTO + candidatas + fichas. Si `evidencia: insuficiente`, reflejar proxies en `theme.md`.
7. Escribir **`theme.md`** con **exactamente 3 alternativas** (plantilla abajo). Bien definido: listo para polish. Ante conflicto: evidencia del benchmark manda en “qué existe”; brainstorm en ángulos de problema/alcance.
8. No escribir `theme-debate.md` ni `theme-polish.md` aquí.
9. Chat: paths de `theme-brainstorm.md` + `theme.md`, resumen de las 3, siguiente **`init-theme-polish`**.

### Plantilla `theme-brainstorm.md`

```markdown
# Brainstorm de temas — [FOLDER]

## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: …
- restricciones: …
- modo: N_alternativas

## Entrada (tópicos)
1. …
2. …
3. …

## Acta (brainstorm-theme)
… (pegar salida del agente: lentes + síntesis de candidatas)
```

### Plantilla `theme.md`

```markdown
# Temas propuestos — [FOLDER]

## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: diagnostico | informe | mvp | producto
- restricciones: …
- modo: N_alternativas

## Entrada
- Tópicos del usuario: …
- Carpeta: …
- Acta brainstorm: theme-brainstorm.md

## Alternativa 1
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …
**Tipo de sujeto:** empresa | entidad | dominio_sin_empresa | ficticio
**Ficha de empresa (si aplica):** identidad · reseña histórica pública · misión/visión/valores · fuentes (o N/A justificado)
**Benchmarking (`benchmark-theme`):** casos (directo|proxy) · mini-matriz breve · qué adaptar · diferenciador · evidencia suficiente|insuficiente
**Diferenciador propuesto:** …

## Alternativa 2
…

## Alternativa 3
…

## Fuentes del benchmarking
- …
```

## Forbidden

- Inventar soluciones/empresas del benchmark o datos corporativos no hallados.
- Omitir investigación cuando una alternativa nombra empresa real.
- Invocar skills externas de competitive-analysis / brainstorm ajenas.
- Lanzar el panel de polish (**init-theme-polish**).
- Crear proyecto en `docs/content/` (**init-project**).
- Regenerar Graphify.
