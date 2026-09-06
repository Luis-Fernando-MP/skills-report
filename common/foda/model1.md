# FODA del MVP — model1

FODA **del movimiento del MVP N**, no de toda la empresa ni del sector completo.

## Posición en el pipeline

Se escribe **después** de Lean Canvas y **antes** del RAT **si** ambas existen. Si FODA está ausente en `config.tools`, este playbook no corre (RAT no espera candidatos FODA).

Escanea riesgos; **no** es la fuente de verdad de supuestos (eso es el RAT).

## Propósito

Radiografía corta para decidir si el piloto es defendible y qué vigilar — alimentando candidatos al RAT.

## Matriz

| | Ayuda | Perjudica |
|--|-------|-----------|
| Interno | **F**ortalezas | **D**ebilidades |
| Externo | **O**portunidades | **A**menazas |

## Reglas

1. Máx. **3–4** bullets por cuadrante; concretos y ligados al MVP.
2. Etiquetar ítems críticos como `hipótesis` / `evidencia` / `pendiente_campo`.
3. **F/D** = recursos, hábitos, datos, roles *respecto al MVP*.
4. **O/A** = entorno inmediato — no PESTEL completo.
5. Prohibido FODA corporativo genérico si no afecta el MVP.
6. **vs RAT (arbitraje):**
   - En el **pase FODA** (antes de RAT): cada Amenaza/Debilidad de impacto alto cierra **solo** con `→ candidato RAT`. **Nunca** `R#` en este pase (RAT aún no asignó IDs).
   - Tras RAT, el **orquestador** hace pasada de amarre: reescribe `→ candidato RAT` → `→ R#` o añade sublista “Candidatos → R#”.
   - **Prohibido** repetir el mismo párrafo narrativo en FODA y en la ficha RAT.
   - FODA nombra y prioriza en lenguaje de negocio; RAT formaliza supuesto + falsación + umbral.
7. **Implicación (1, obligatoria):** una frase con enlace al piloto. En el pase FODA puede ser `→ candidato RAT` / `→ ajusta Prototype` / `→ ajusta DT Test`; tras el amarre, preferir `→ R#` si ya existe.
   Sin enlace = incompleto.

## Preguntas guía

- F: ¿Qué ya existe que acelera el MVP?
- D: ¿Qué falta (disciplina de registro, ownership)?
- O: ¿Qué ventana ayuda ahora?
- A: ¿Qué tumba el piloto (doble carga, dato fantasma)?

## Salida mínima

Tabla FODA + implicación en la sección semántica **FODA del MVP**. El **número** (`## N`) lo asigna el orquestador.