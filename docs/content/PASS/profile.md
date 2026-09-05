# Perfil del proyecto

## Tema
Diagnóstico y diseño de MVP de confiabilidad de inventario de producto terminado por variante en Calzados Romantex S.A.C.

## Descripción
Propuesta académica de transformación digital acotada para una PYME de calzado en Trujillo: diagnosticar la inconsistencia entre la disponibilidad por variante (modelo × color × talla) que usa el área comercial y el stock físico en ubicaciones controladas por la empresa, y diseñar un MVP ligero (sin ERP/POS) con maestro de variantes, saldos por ubicación propia y bitácora de movimientos con latencia de turno. La estandarización de fichas técnicas de tallaje queda como diagnóstico de soporte y fase posterior, priorizable solo si la evidencia de campo muestra que el cuello es el maestro de tallaje y no el descuadre de inventario.

## Problema identificado
La disponibilidad por variante que el canal comercial puede confirmar puede no coincidir con el stock físico en ubicaciones de Romantex; sin evidencia de campo aún no se afirma magnitud ni se empaqueta “tiempo real”, analítica de ventas ni e-commerce. El diagnóstico debe medir descuadre y tiempo de confirmación, y separar si el cuello es inventario o maestro de tallaje.

## Alcance
- **Fase 0 (gate):** mapa AS-IS (dónde vive el stock, roles, muestra de descuadre por variante, ownership en talleres); sin esta evidencia el problema no se da por demostrado.
- **MVP1:** inventario PT por variante en ≤2 ubicaciones **propias** + operación mínima de actualización **sin POS** (entrada/salida/traslado/ajuste; cierre de turno).
- **Soporte en MVP1 (sin implantar):** relevamiento de cómo se anotan tallas hoy.
- **Fuera ahora:** tiempo real, POS, SUNAT/contabilidad, BOM/MRP, e-commerce, ATP en talleres tercerizados, ISO 19407 como criterio de ajuste, estandarización operativa de fichas (MVP2).

## MVP entregables

### MVP de arranque (recomendado al equipo)
MVP 1 — Piloto de confiabilidad de inventario PT por variante en ≤2 ubicaciones propias con bitácora sin POS; desbloquea evidencia de campo y evita paperware / doble núcleo (fichas quedan en MVP 2).

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | Confiabilidad de stock PT por variante en ubicaciones propias | Mapa AS-IS (Fase 0); maestro variante; bitácora movimientos sin POS; piloto Sheets (1 colección, ≤2 ubic. propias); métricas de exactitud / registro en turno | Usuario planta/almacén responde “¿hay talla X en Y?” con fuente de cierre de turno; % descuadre medido en muestra | se trabaja ahora |
| 2 | Estandarizar fichas técnicas de tallaje | Plantilla ficha; versionado/responsable; ligue ficha→SKU; ISO 19407 solo anexo de equivalencias de marcado | Ficha consultable por variante priorizada; criterios de ajuste documentados sin invocar ISO como norma de horma | después |
| 3 | Ampliar ubicaciones / tercerizados (condicional) | Reglas ATP taller; evidencia bilateral; >2 ubicaciones | Solo si MVP1 demostró disciplina operativa | condicional |

### Fuera de secuencia / descartado
- ERP/POS comercial, facturación SUNAT, BOM/MRP, e-commerce, “tiempo real”, dashboards de tendencias de venta, ISO 19407 como criterio de ajuste.

## Origen
- polish: docs/topics/ITD/theme-audit-polish.md
- veredicto: GO_con_cambios
