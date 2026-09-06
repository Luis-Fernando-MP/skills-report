---
name: init-theme-audit-polish
description: >-
  Stress-test one audited theme (theme-audit.md) with critico-estricto,
  defensor-fundamento, impacto-social, viabilidad-mvp, inversor in
  una_alternativa mode; write theme-audit-debate.md (scores + diagrama + Q&A)
  and theme-audit-polish.md (veredicto + tema final + MVP entregables). Use when
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

**Inversor (soft-veto):** un `NO_GO` solo del inversor **no tumba** el tema si impacto/defensor mitigan con beneficio (ahorro, riesgo evitado, adopción o valor social vendible). Documentar disenso; exigir **Tesis de valor (inversor)** en el polish.

## Empresa / sujeto

Leer `tipo_sujeto` y **`## Ficha de empresa (investigación)`** de `theme-audit.md`.

- Si `empresa|entidad` y ficha ausente o `evidencia_empresa: insuficiente` → **completar investigación pública** (WebSearch / sitios oficiales) **antes** de Round 1; volcar hallazgos al CONTEXTO. Sin ficha usable → **NO_GO** o pedir reformulación (no inventar).
- Distinguir siempre: **reseña histórica pública** ≠ **AS-IS operativo interno** no publicado.
- Si `dominio_sin_empresa` → no exigir ficha corporativa; el debate se centra en el problema de dominio.
- Pasar la ficha (o N/A justificado) a los **5** agentes en CONTEXTO.

## Procedure

### CONTEXTO + tema único

```text
## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: …
- restricciones: …
- modo: una_alternativa
- tipo_sujeto: empresa | entidad | dominio_sin_empresa | ficticio

## FICHA_EMPRESA
(pegar ficha de theme-audit.md o “N/A — dominio_sin_empresa: …”)

## BLOQUE_TEMA
(pegar tema afinado de theme-audit.md + benchmarking)
```

### Round 1 — parallel

`critico-estricto`, `defensor-fundamento`, `impacto-social`, `viabilidad-mvp`, `inversor` — todos con `modo: una_alternativa` + FICHA_EMPRESA.

### Round 2 — cross-debate

1. Pasar ataques/preguntas del crítico → `defensor-fundamento`.
2. Pasar alcance cuestionado → `viabilidad-mvp` (debe devolver `### MVP entregables` con 2–4 MVPs: objetivo, entregables concretos, criterio de éxito, dependencias).
3. Pasar **propuestas de valor del inversor** → impacto-social, defensor y viabilidad (¿cabe sin re-inflar?).
4. Pasar el bloque MVP entregables → `critico-estricto` (¿inflado / paperware / núcleo equivocado?), `defensor-fundamento`, `impacto-social` e `inversor` (¿cuál arrancar y por qué / valor).
5. Orquestador fija **MVP de arranque** (casi siempre 1) o documenta disenso; consolidar scores por dimensión.

### Write `theme-audit-debate.md`

```markdown
# Debate de auditoría — [FOLDER]

## Puntuación (dimensiones)
| Dimensión / eje | Critico | Defensa | Impacto | Viabilidad | Inversor | Notas |
|-----------------|---------|---------|---------|------------|----------|-------|
| problema | | | | | | |
| alcance | | | | | | |
| evidencia_aporte | | | | | | |
| manejabilidad / MVP | | | | | | |
| camino_valor | | | | | | |
| Total / veredicto | | | | | | pasa / cae |

## Preguntas y respuestas (cronológico)
- [critico-estricto] …
  - [defensor-fundamento] …
- [impacto-social] …
- [viabilidad-mvp] …
- [inversor] …

## Cruce global
…

### Debate MVP entregables
- [viabilidad-mvp] propuesta de secuencia / arranque: …
- [critico-estricto] …
- [defensor-fundamento] …
- [impacto-social] …
- [inversor] tesis / propuestas de valor: …
- Orquestador — MVP de arranque: N — …

## Diagrama del debate
\`\`\`mermaid
flowchart TD
  audit[theme-audit.md] --> r1[Ronda1]
  r1 --> crit[critico-estricto]
  r1 --> def[defensor-fundamento]
  r1 --> soc[impacto-social]
  r1 --> neg[viabilidad-mvp]
  r1 --> inv[inversor]
  crit -->|"objecion"| def
  def -->|"respuesta"| crit
  inv -->|"propuesta_valor"| r2[Ronda2]
  soc -->|"exigencia"| out[Veredicto]
  neg -->|"MVP entregables"| out
  crit --> r2
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
### Tipo de sujeto
empresa | entidad | dominio_sin_empresa | ficticio
### Ficha de empresa (para init-project → company.md)
*(Obligatoria si empresa|entidad: identidad, reseña histórica pública, misión/visión/valores, oferta, fuentes. Si dominio_sin_empresa → “N/A” + justificación.)*

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

## Tesis de valor (inversor)
*(Obligatoria si GO o GO_con_cambios.)*
…

## Marco PICOCT (para bibliography)
*(Obligatorio si GO o GO_con_cambios. Alimenta `bibliography-picoct` y se espeja en `profile.md`.)*

| Componente | Definición | Criterios / descripción del caso |
| :---: | :--- | :--- |
| **P** | Population / Problem | Sujetos o problemática central (desde Problema + quién vive el dolor) |
| **I** | Intervention | Método/herramienta a evaluar (alineada al MVP de arranque) |
| **C** | Comparison | Práctica actual o alternativa (cuaderno, WhatsApp, Excel, POS/ERP…) |
| **O** | Outcome | Métricas / desenlaces (criterio de éxito, métricas de diagnóstico) |
| **C** | Context | País, sector, tipo de organización (no solo razón social) |
| **T** | Time / Type of study | Años de búsqueda + tipo documental si aplica |

**Reglas al llenar PICOCT:**
- Derivar de Tema / Descripción / Problema / Alcance / MVP. No inventar hechos de empresa.
- Si un componente falta dato: hipótesis breve (no vacío).
- **T — años:** si el usuario **no** indicó rango en el invoke → solo el **año corriente** del sistema (p. ej. `2026`) + tipo default `article` si aplica. Si indicó rango → usarlo.

Fuente para `bibliography-picoct` / espejo en `profile.md` vía `init-project`.

## Si NO_GO
El tema no pasó. Reformular o cambiar de eje; volver a `init-theme-audit` o explorar con `init-theme`.

## Listo para
`init-project` (espejar tema final + MVP + **Marco PICOCT** en `profile.md`) → `init-project-mvp mvp-<N>` → `bibliography-picoct`.
```

### Chat

Paths + veredicto + **MVP de arranque** + si T usó solo año corriente. Si NO_GO: indicar reformulación.

## Forbidden

- Tratar el input como 3 alternativas (`init-theme-polish`).
- Soft consensus / inventar fuentes o datos de empresa.
- GO/GO_con_cambios con empresa real **sin** ficha pública usable.
- Forzar GO si el umbral dice NO_GO.
- Escribir proyecto en `docs/content/` aquí.
- Regenerar Graphify.
- Dejar solo un bullet “MVP acordado” sin tabla de entregables debatidos.
- Omitir **Marco PICOCT**, **Tesis de valor (inversor)** o la ficha de sujeto cuando el veredicto es GO o GO_con_cambios.
- Tumbar solo por `NO_GO` del inversor cuando hay mitigación de valor social/adopción.
