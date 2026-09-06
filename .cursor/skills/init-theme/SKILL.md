---
name: init-theme
description: >-
  First step of the init family: from 3–4 topics, create docs/topics/<FOLDER>/theme.md
  with 3 project alternatives (tema, descripción, problema, alcance) after
  benchmarking via benchmark-theme. Use when user says init-theme.
---

# init-theme

Primer paso de la familia **init-*** cuando **exploras** desde tópicos. Define 3 alternativas en `docs/topics/<FOLDER>/`.

Si **ya tienes un tema concreto** (empresa + problema + alcance) → usa **`init-theme-audit`**, no esta skill.

## Layout

```text
docs/topics/<FOLDER>/
  theme.md           # 3 alternativas (esta skill)
  theme-debate.md    # lo escribe init-theme-polish
  theme-polish.md    # lo escribe init-theme-polish
```

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

Por cada tópico/alternativa que **nombre una empresa u organización real** → investigar fuentes públicas (identidad, historia, misión/visión/valores, sector) **antes** de fijar la alternativa. Si el tópico es de dominio sin org. (p. ej. sismos en Lima) → `tipo_sujeto: dominio_sin_empresa` y no inventar empresa.

Si una alternativa depende de empresa real y no hay evidencia pública mínima → marcar `evidencia_empresa: insuficiente` o descartar esa alt. (no inventar).

## Procedure

1. Leer tópicos (3–4) y carpeta opcional.
2. **Resolver `FOLDER`:**
   - Si el usuario da código (`ITD`, `MOST`) → usarlo.
   - Si no → slug corto (mayúsculas o kebab) a partir del curso/tema; si `docs/topics/<FOLDER>/` ya existe con `theme.md`, preguntar antes de sobrescribir.
3. Crear `docs/topics/<FOLDER>/` si no existe.
4. Clasificar sujeto por tópico; **investigar empresa** cuando aplique (WebSearch / oficiales).
5. Lanzar **un** agente `benchmark-theme` con CONTEXTO + tópicos + fichas de empresa halladas. Si `evidencia: insuficiente`, reflejarlo en `theme.md` (proxies explícitos; no inventar casos).
6. Escribir **`theme.md`** con **exactamente 3 alternativas**, cada una:

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

## Alternativa 1
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …
**Tipo de sujeto:** empresa | entidad | dominio_sin_empresa | ficticio
**Ficha de empresa (si aplica):** identidad · reseña histórica pública · misión/visión/valores · fuentes (o N/A justificado)
**Benchmarking:** … (marcar directo|proxy; si insuficiente, decirlo)
**Diferenciador propuesto:** …

## Alternativa 2
…

## Alternativa 3
…

## Fuentes del benchmarking
- …
```

7. No inventar empresas ni casos. No escribir `theme-debate.md` ni `theme-polish.md` aquí.
8. Chat: path de `theme.md`, resumen de las 3, y siguiente skill **`init-theme-polish`**.

## Forbidden

- Inventar soluciones/empresas del benchmark o datos corporativos no hallados.
- Omitir investigación cuando una alternativa nombra empresa real.
- Lanzar el panel de 4 agentes (eso es **init-theme-polish**).
- Crear proyecto en `docs/content/` (eso es **init-project**).
- Regenerar Graphify.
- Tocar skills `rsl-*`.
