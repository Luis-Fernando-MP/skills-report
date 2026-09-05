---
name: init-theme-polish
description: >-
  Debate 3 theme alternatives with critico-estricto, defensor-fundamento,
  impacto-social, viabilidad-mvp; write theme-debate.md (scores + Q&A trail) and
  theme-polish.md (GO/NO_GO + final theme). Use when user says init-theme-polish.
---

# init-theme-polish

Segundo paso de la familia **init-***. Estresa las 3 alternativas de `theme.md` y deja acta + veredicto.

## Layout

```text
docs/topics/<FOLDER>/
  theme.md           # entrada (init-theme)
  theme-debate.md    # acta: scores, preguntas, respuestas
  theme-polish.md    # veredicto + alternativa final o NO_GO
```

## Invoke

```text
Usa init-theme-polish sobre ITD
```

o

```text
Usa init-theme-polish
# (lee docs/topics/<FOLDER>/theme.md)
```

Sin `theme.md` → pedir `init-theme` primero. No inventar alternativas.

## Standard of rigor

No es un brainstorm amable. Respeta límites de búsqueda de cada agente y el protocolo de evidencia insuficiente. Si **ninguna** alternativa resiste → **NO_GO**; no forzar un ganador.

### Umbral orquestador (alineado a `critico-estricto`)

Por alternativa, **cae** si el crítico marca `NO_GO` **o** (puntuación crítico ≤ 2 **y** viabilidad ≤ 2). **Pasa** solo si al menos un eje fuerte (crítico ≥ 3 y viabilidad ≥ 3) y no hay ≥2 ataques fuertes sin mitigar tras ronda 2. Si todas caen → veredicto global `NO_GO`.

## Procedure

### CONTEXTO (mismo bloque a los 4)

Tomar de `theme.md` / usuario; si falta, declarar supuestos:

```text
## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: …
- restricciones: …
- modo: N_alternativas

## BLOQUE_ALTERNATIVAS
...
```

### Round 1 — parallel

Lanzar en paralelo: `critico-estricto`, `defensor-fundamento` (usará checklist si aún no hay crítico), `impacto-social`, `viabilidad-mvp`.

### Round 2 — cross-debate

1. Pasar **ataques/preguntas del crítico** a `defensor-fundamento` (follow-up).
2. Pasar **alcance cuestionado** a `viabilidad-mvp` para anclar MVP.
3. Extraer choques impacto vs viabilidad; consolidar scores.

### Write `theme-debate.md` (primero)

Acta legible para el humano. Plantilla:

```markdown
# Debate de temas — [FOLDER]

## Puntuación
| Alternativa | Critico | Defensa | Impacto | Viabilidad | Total | Veredicto |
|-------------|---------|---------|---------|------------|-------|-----------|
| A1 … | | | | | | pasa / cae |
| A2 … | | | | | | |
| A3 … | | | | | | |

## Alternativa 1 — [título corto]
### Por qué esta puntuación
### Preguntas y respuestas (cronológico)
- [critico-estricto] pregunta/ataque: …
  - [defensor-fundamento] responde: …
- [impacto-social] exige/pregunta: …
  - respuesta / resolución: …
- [viabilidad-mvp] objeción MVP: …
  - respuesta / resolución: …
### Fuentes

## Alternativa 2 — …
## Alternativa 3 — …

## Cruce global
Choques, réplicas ronda 2, y por qué se eligió (o no) una.

## Fuentes consultadas (panel)
- …
```

### Write `theme-polish.md`

```markdown
# Veredicto — [FOLDER]

## Veredicto global
GO | GO_con_cambios | NO_GO

## Diagrama del debate
\`\`\`mermaid
flowchart TD
  theme[theme.md] --> r1[Ronda1]
  r1 --> crit[critico-estricto]
  r1 --> def[defensor-fundamento]
  r1 --> soc[impacto-social]
  r1 --> neg[viabilidad-mvp]
  crit -->|"objecion"| def
  def -->|"contraataque"| crit
  soc -->|"exigencia"| out[Veredicto]
  neg -->|"MVP"| out
  crit --> r2[Ronda2]
  def --> r2
  r2 --> out
\`\`\`
*(Personalizar edges con objeciones reales de esta corrida.)*

## Detalle del debate
Ver `theme-debate.md`.

## Tema final propuesto
*(Solo si GO o GO_con_cambios. Un solo planteamiento.)*

### Tema
…
### Descripción
…
### Problema identificado
…
### Alcance
…
### MVP acordado
- MVP 1 (se trabaja): …
- Fuera de alcance ahora: …

## Si NO_GO
Ninguna alternativa fue aceptada. Traer otros tópicos o áreas e invocar de nuevo `init-theme`.

## Listo para siguiente skill
`init-project` (usar el tema final de este archivo en `profile.md`).
```

### Chat

Path de ambos archivos + veredicto en una línea. Si NO_GO: pedir nuevos tópicos.

## Forbidden

- Soft consensus sin presión del crítico.
- Inventar fuentes o empresas.
- Elegir un ganador si las 4 lecturas son NO_GO.
- Escribir `informe.md` / proyecto en `docs/content/` aquí.
- Tocar skills `rsl-*`.
- Regenerar Graphify.
