---
name: init-theme-polish
description: >-
  Debate 3 theme alternatives with critico-estricto, defensor-fundamento,
  impacto-social, viabilidad-mvp, inversor; write theme-debate.md (scores +
  diagrama + Q&A) and theme-polish.md (GO/NO_GO + final theme). Use when user
  says init-theme-polish.
---

# init-theme-polish

Estresa las **3 alternativas** de `theme.md`. Si el input es un **tema único** auditado → usa **`init-theme-audit-polish`**.

## Layout

```text
docs/topics/<FOLDER>/
  theme.md           # entrada (init-theme)
  theme-debate.md    # acta: scores, diagrama mermaid, preguntas, respuestas
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

**Inversor (soft-veto):** un `NO_GO` solo del inversor **no tumba** la alternativa si el resto sostiene PoC con tesis de valor (ahorro, riesgo evitado, adopción o beneficio social vendible) tras R2. Documentar disenso y exigir bloque **Tesis de valor** en el polish.

## Empresa / sujeto

Si alguna alternativa tiene `tipo_sujeto: empresa|entidad`:

- Exigir ficha usable en CONTEXTO (completar investigación pública si falta).
- El crítico puede tumbar una alt. por empresa inventada o sin fuentes.
- Distinguir reseña histórica **pública** vs AS-IS interno no publicado.
- Si gana una alt. con empresa → el polish debe llevar **Ficha de empresa** lista para `init-project` → `company.md`.

## Procedure

### CONTEXTO (mismo bloque a los 5)

Tomar de `theme.md` / usuario; si falta, declarar supuestos:

```text
## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: …
- restricciones: …
- modo: N_alternativas

## FICHAS_EMPRESA_POR_ALT
(A1/A2/A3: ficha o N/A dominio_sin_empresa)

## BLOQUE_ALTERNATIVAS
...
```

### Round 1 — parallel

Lanzar en paralelo: `critico-estricto`, `defensor-fundamento`, `impacto-social`, `viabilidad-mvp`, `inversor` — con FICHAS_EMPRESA_POR_ALT.

### Round 2 — cross-debate

1. Pasar **ataques/preguntas del crítico** a `defensor-fundamento` (follow-up).
2. Pasar **alcance cuestionado** a `viabilidad-mvp` para anclar MVP.
3. Pasar **propuestas de valor del inversor** a impacto-social, defensor y viabilidad (¿cabe sin re-inflar?).
4. Extraer choques impacto vs viabilidad vs valor; consolidar scores.

### Write `theme-debate.md` (primero)

Acta legible para el humano. Plantilla:

```markdown
# Debate de temas — [FOLDER]

## Puntuación
| Alternativa | Critico | Defensa | Impacto | Viabilidad | Inversor | Total | Veredicto |
|-------------|---------|---------|---------|------------|----------|-------|-----------|
| A1 … | | | | | | | pasa / cae |
| A2 … | | | | | | | |
| A3 … | | | | | | | |

## Alternativa 1 — [título corto]
### Por qué esta puntuación
### Preguntas y respuestas (cronológico)
- [critico-estricto] pregunta/ataque: …
  - [defensor-fundamento] responde: …
- [impacto-social] exige/pregunta: …
  - respuesta / resolución: …
- [viabilidad-mvp] objeción MVP: …
  - respuesta / resolución: …
- [inversor] tesis / propuesta de valor: …
  - respuesta / resolución: …
### Fuentes

## Alternativa 2 — …
## Alternativa 3 — …

## Cruce global
Choques, réplicas ronda 2, propuestas de valor debatidas, y por qué se eligió (o no) una.

## Diagrama del debate
\`\`\`mermaid
flowchart TD
  theme[theme.md] --> r1[Ronda1]
  r1 --> crit[critico-estricto]
  r1 --> def[defensor-fundamento]
  r1 --> soc[impacto-social]
  r1 --> neg[viabilidad-mvp]
  r1 --> inv[inversor]
  crit -->|"objecion"| def
  def -->|"contraataque"| crit
  inv -->|"propuesta_valor"| r2[Ronda2]
  soc -->|"exigencia"| out[Veredicto]
  neg -->|"MVP"| out
  crit --> r2
  def --> r2
  r2 --> out
\`\`\`
*(Personalizar edges con objeciones reales de esta corrida.)*

## Fuentes consultadas (panel)
- …
```

### Write `theme-polish.md`

```markdown
# Veredicto — [FOLDER]

## Veredicto global
GO | GO_con_cambios | NO_GO

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
### Tipo de sujeto
empresa | entidad | dominio_sin_empresa | ficticio
### Ficha de empresa (para init-project → company.md)
*(Si empresa|entidad: identidad, reseña histórica pública, misión/visión/valores, oferta, fuentes. Si dominio_sin_empresa → N/A.)*
### MVP acordado
- MVP 1 (se trabaja): …
- Fuera de alcance ahora: …

### Tesis de valor (inversor)
*(Obligatoria si GO o GO_con_cambios: camino a beneficio — dinero, ahorro, riesgo evitado, adopción o valor social vendible.)*
…

## Si NO_GO
Ninguna alternativa fue aceptada. Traer otros tópicos o áreas e invocar de nuevo `init-theme`.

## Listo para siguiente skill
`init-project` (espejar tema final + ficha → `company.md` si aplica, `profile.md`, `config.mvp`) → `init-project-mvp mvp-<N>`.
```

### Chat

Path de ambos archivos + veredicto en una línea. Si NO_GO: pedir nuevos tópicos.

## Forbidden

- Soft consensus sin presión del crítico.
- Inventar fuentes o empresas.
- Elegir ganador con empresa real **sin** ficha pública.
- Elegir un ganador si las lecturas fuertes (crítico+viabilidad) son NO_GO.
- Tumbar solo por `NO_GO` del inversor cuando hay tesis de valor social/adopción mitigada.
- Escribir `informe.md` / proyecto en `docs/content/` aquí.
- Regenerar Graphify.
