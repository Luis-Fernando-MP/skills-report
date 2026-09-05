# Debate de auditoría — ITD

## Puntuación (dimensiones)

| Dimensión / eje | Critico | Defensa | Impacto | Viabilidad | Notas |
|-----------------|---------|---------|---------|------------|-------|
| problema | 2 → *condicional 3 si se reescribe* | 4 → 3 (R2, honesto) | 4 (relevancia) | — | Crítico: hipótesis sectorial sin baseline Romantex; “tiempo real” sobrepromesa |
| alcance | 3 | 5 → 4 (R2 partido) | 5 (alineación fase) | manejabilidad 4→5 | Dual inventario+fichas+multi-ubicación = doble MVP |
| evidencia_aporte | 2 | 3 | 3 (proxy público) | — | Matriz = commodity (INVY/Uphance); ISO 19407 mal usado como ajuste |
| manejabilidad / MVP | — | — | impacto entregable actual: 2 | claridad 4→5; ajuste 5 | R2: un núcleo inventario; fichas solo soporte |
| Total / veredicto | NO_GO (texto actual) | GO_con_cambios si gates | relevancia **baja** (fase diagnóstico) | GO_condicionado | Orquestador: **GO_con_cambios** |

*Promedio crítico R1 ≈ 2,3 (no ≤ 2). Viabilidad R2 ≥ 3. Ataques fuertes mitigados tras R2 con cambio de núcleo/alcance → no aplica NO_GO por ≥2 abiertos.*

## Preguntas y respuestas (cronológico)

### Ronda 1

- [critico-estricto] NO_GO. Ataques: (1) problema empaqueta 3 dolores sin baseline; “tiempo real” sin captura de movimientos; (2) inventario ≠ fichas como misma causa; (3) matriz+consulta = commodity INVY/Uphance; (4) ISO 19407 no define criterios de ajuste; (5) alcance doble + riesgo ownership en talleres tercerizados. Saturación: **adyacente**. Condiciones NO_GO: evidencia observada Romantex; aporte residual tras restar vendors; recalibrar ISO; partir (a)|(b); operación mínima sin POS.
- [defensor-fundamento] (sin crítico aún) Defiende diagnóstico+MVP ligero vs ERP/POS; concede ausencia de baseline Romantex e ISO solo conversión. Scores: problema 4 | alcance 5 | evidencia_aporte 3. Pregunta retorno: fuente primaria de descuadre/tiempos.
- [impacto-social] Relevancia social **baja** en fase diagnóstico (preparación organizacional). Beneficiarios directos: dueños, almacén, comercial de Romantex. Proxies: MYPE Digital, CITEccal, tesis Trujillo. Riesgos dominio: bajos (exclusión digital, carga laboral, dependencia proveedor).
- [viabilidad-mvp] GO condicionado. Criterio R1: `dependencias_datos`. MVP1: ficha+inventario+piloto 1 colección ≤2 ubicaciones. Scores: 4 | 4 | 5. Exige artefacto operable (no solo PDF).

### Ronda 2

- [critico-estricto → defensor-fundamento] Cinco preguntas (evidencia Romantex; gap vs INVY; campos ficha/ISO; ownership talleres; implementación vs diseño).
  - [defensor-fundamento] **Concede los 5 ataques.** Sin evidencia primaria de Romantex el NO_GO sobre el texto actual permanece válido. Mitigaciones: un solo dolor (inconsistencia disponibilidad declarada vs físico); retirar tiempo real / datos de ventas; aporte = diagnóstico de gobierno + reglas sin POS + priorización falsable (a)|(b); ISO 19407 solo anexo de conversión; talleres: mapear en Fase 0, no inventar SLA. Scores condicionales: 3 | 4 | 3. Pregunta al crítico: ¿Fase 0 + decisión (a)|(b) basta para GO_con_cambios en fase diagnóstico?
- [alcance cuestionado → viabilidad-mvp] Ancla a crítico. Prioriza núcleo **(a) inventario**. Fichas = diagnóstico de soporte / MVP2. Operación mínima sin POS: registrador + supervisor; movimientos entrada/salida/traslado/ajuste; latencia **cierre de turno** (máx. T+1); ≤2 ubicaciones **propias**; tercerizados fuera. Métricas: exactitud tras conteos cíclicos; % movimientos registrados en el turno; respuesta con fuente de cierre (no “en vivo”). Scores R2: 5 | 5 | 5. Veredicto: **GO_condicionado**.

## Cruce global

El panel coincide en que el **dolor de stock por variante es real a nivel de mercado**, pero el enunciado afinado pre-polish **sobrepromete** (tiempo real, doble núcleo, ISO como ajuste, multi-ubicación con tercerizados) y **no trae evidencia de caso**.

Tras R2, el tema **resiste solo con cambios**:
1. **Fase 0 (gate):** observar en Romantex dónde vive el stock, muestra de descuadre, mapa ownership; si no hay descuadre medible → el problema cae.
2. **MVP1 = solo (a):** confiabilidad de inventario PT por variante en ≤2 ubicaciones propias + bitácora sin POS (latencia de turno).
3. **Fichas de tallaje:** soporte diagnóstico en MVP1; estandarización implementable = MVP2 (si el hallazgo lo prioriza, se puede invertir la prioridad, pero no ambos como núcleo).
4. **Aporte:** no la matriz (commodity), sino gobierno de maestros/eventos y priorización falsable frente a “comprar INVY”.
5. **ISO 19407:** fuera del núcleo; anexo opcional de equivalencias de marcado.

Impacto social no bloquea (fase diagnóstico = peso bajo esperado). Viabilidad alta tras el recorte.

**Veredicto orquestador:** `GO_con_cambios` (crítico tumbó el texto actual; ataques fuertes quedan mitigados *si* se adoptan los recortes; no quedan ≥2 ataques fuertes abiertos tras R2).

## Fuentes consultadas

- INVY — https://www.invyperu.com/tienda-de-calzado-punto-de-venta
- iSiore GO — https://www.isiorego.com/blog/erp/erp-para-fabricas-de-calzado-en-peru/
- Uphance footwear inventory / PLM — https://www.uphance.com/footwear-inventory-system/
- ISO 19407:2023 — https://www.iso.org/standard/83106.html
- MYPE Digital / PRODUCE — https://www.gob.pe/mype-digital
- CITEccal / ITP (proxy sector) — gob.pe/institucion/itp
- Tesis UCV / UPN inventario calzado Trujillo (proxy académico, ALICIA/repositorio UPN)
- theme-audit.md — docs/topics/ITD/theme-audit.md
