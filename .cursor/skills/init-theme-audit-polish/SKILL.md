---
name: init-theme-audit-polish
description: >-
  Stress-test one audited theme (theme-audit.md) with critico-estricto,
  defensor-fundamento, impacto-social, viabilidad-mvp in una_alternativa mode;
  write theme-audit-debate.md (scores + diagrama + Q&A) and
  theme-audit-polish.md (veredicto + tema final). Use when user says
  init-theme-audit-polish.
---

# init-theme-audit-polish

Estresa **el tema único** producido por `init-theme-audit`. Reutiliza los mismos agentes que `init-theme-polish`, en modo `una_alternativa` (no debate entre A1/A2/A3).

## Layout

```text
docs/topics/<FOLDER>/
  theme-audit.md           # entrada (init-theme-audit)
  theme-audit-debate.md    # acta: scores, diagrama mermaid, Q&A
  theme-audit-polish.md    # veredicto + tema final o NO_GO
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
2. Pasar alcance cuestionado → `viabilidad-mvp`.
3. Consolidar scores por dimensión.

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
  neg -->|"MVP"| out
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
### MVP acordado
- MVP 1: …
- Fuera ahora: …

## Si NO_GO
El tema no pasó. Reformular o cambiar de eje; volver a `init-theme-audit` o explorar con `init-theme`.

## Listo para
`init-project` (usar este tema final en `profile.md`).
```

### Chat

Paths + veredicto en una línea. Si NO_GO: indicar reformulación.

## Forbidden

- Tratar el input como 3 alternativas (`init-theme-polish`).
- Soft consensus / inventar fuentes.
- Forzar GO si el umbral dice NO_GO.
- Escribir proyecto en `docs/content/` aquí.
- Tocar skills `rsl-*` / regenerar Graphify.
