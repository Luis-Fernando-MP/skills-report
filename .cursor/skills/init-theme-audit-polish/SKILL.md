---
name: init-theme-audit-polish
description: >-
  Stress-test one audited theme (theme-audit.md) with critico-estricto,
  defensor-fundamento, impacto-social, viabilidad-mvp in una_alternativa mode;
  write theme-audit-debate.md (scores + diagrama + Q&A) and
  theme-audit-polish.md (veredicto + tema final + MVP entregables). Use when
  user says init-theme-audit-polish.
---

# init-theme-audit-polish

Estresa **el tema único** producido por `init-theme-audit`. Reutiliza los mismos agentes que `init-theme-polish`, en modo `una_alternativa` (no debate entre A1/A2/A3).

## Layout

```text
docs/topics/<FOLDER>/
  theme-audit.md           # entrada (init-theme-audit)
  theme-audit-debate.md    # acta: scores, diagrama mermaid, Q&A, debate MVP
  theme-audit-polish.md    # veredicto + tema final + MVP entregables
```

## Invoke

```text
Usa init-theme-audit-polish sobre ITD
```

Sin `theme-audit.md` → pedir **init-theme-audit** primero. No inventar el tema.

## Standard of rigor

Mismos agentes y límites de búsqueda. Debate **componentes internos** (problema, alcance, evidencia/aporte, MVP), no comparación entre alternativas.

### Umbral orquestador

**NO_GO** si el crítico marca `NO_GO` **o** (promedio dimensiones crítico ≤ 2 **y** viabilidad ≤ 2) **o** ≥2 ataques fuertes sin mitigar tras ronda 2.  
**GO_con_cambios** si resiste con ajustes de alcance/MVP.  
**GO** si crítico y viabilidad ≥ 3 y no quedan ataques fuertes abiertos.

## Procedure

### CONTEXTO + tema único

```text
## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: …
- restricciones: …
- modo: una_alternativa

## BLOQUE_TEMA
(pegar tema afinado de theme-audit.md + benchmarking)
```

### Round 1 — parallel

`critico-estricto`, `defensor-fundamento`, `impacto-social`, `viabilidad-mvp` — todos con `modo: una_alternativa`.

### Round 2 — cross-debate

1. Pasar ataques/preguntas del crítico → `defensor-fundamento`.
2. Pasar alcance cuestionado → `viabilidad-mvp` (debe devolver `### MVP entregables` con 2–4 MVPs: objetivo, entregables concretos, criterio de éxito, dependencias).
3. Pasar el bloque MVP entregables → `critico-estricto` (¿inflado / paperware / núcleo equivocado?), `defensor-fundamento` e `impacto-social` (¿cuál arrancar y por qué).
4. Orquestador fija **MVP de arranque** (casi siempre 1) o documenta disenso; consolidar scores por dimensión.

### Write `theme-audit-debate.md`

```markdown
# Debate de auditoría — [FOLDER]

## Puntuación (dimensiones)
| Dimensión / eje | Critico | Defensa | Impacto | Viabilidad | Notas |
|-----------------|---------|---------|---------|------------|-------|
| problema | | | | | |
| alcance | | | | | |
| evidencia_aporte | | | | | |
| manejabilidad / MVP | | | | | |
| Total / veredicto | | | | | pasa / cae |

## Preguntas y respuestas (cronológico)
- [critico-estricto] …
  - [defensor-fundamento] …
- [impacto-social] …
- [viabilidad-mvp] …

## Cruce global
…

### Debate MVP entregables
- [viabilidad-mvp] propuesta de secuencia / arranque: …
- [critico-estricto] …
- [defensor-fundamento] …
- [impacto-social] …
- Orquestador — MVP de arranque: N — …

## Diagrama del debate
\`\`\`mermaid
flowchart TD
  audit[theme-audit.md] --> r1[Ronda1]
  r1 --> crit[critico-estricto]
  r1 --> def[defensor-fundamento]
  r1 --> soc[impacto-social]
  r1 --> neg[viabilidad-mvp]
  crit -->|"objecion"| def
  def -->|"respuesta"| crit
  soc -->|"exigencia"| out[Veredicto]
  neg -->|"MVP entregables"| out
  crit --> r2[Ronda2]
  def --> r2
  neg --> r2
  r2 --> out
\`\`\`
*(Personalizar edges con objeciones reales.)*

## Fuentes consultadas
- …
```

### Write `theme-audit-polish.md`

```markdown
# Veredicto auditoría — [FOLDER]

## Veredicto global
GO | GO_con_cambios | NO_GO

## Detalle
Ver `theme-audit-debate.md`.

## Tema final
*(Solo si GO o GO_con_cambios.)*

### Tema
…
### Descripción
…
### Problema identificado
…
### Alcance
…

## MVP entregables
*(Solo si GO o GO_con_cambios. Resultado del debate R2.)*

### MVP de arranque (recomendado al equipo)
MVP N — una frase + por qué gana el debate

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | … | … | … | se trabaja ahora |
| 2 | … | … | … | después |

### Fuera de secuencia / descartado
- …

## Si NO_GO
El tema no pasó. Reformular o cambiar de eje; volver a `init-theme-audit` o explorar con `init-theme`.

## Listo para
`init-project` (espejar tema final + MVP entregables en `profile.md`) → `init-project-mvp mvp-<N>`.
```

### Chat

Paths + veredicto + **MVP de arranque** en una línea. Si NO_GO: indicar reformulación.

## Forbidden

- Tratar el input como 3 alternativas (`init-theme-polish`).
- Soft consensus / inventar fuentes.
- Forzar GO si el umbral dice NO_GO.
- Escribir proyecto en `docs/content/` aquí.
- Tocar skills `rsl-*` / regenerar Graphify.
- Dejar solo un bullet “MVP acordado” sin tabla de entregables debatidos.
