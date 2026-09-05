# Veredicto auditoría — ITD

## Veredicto global
GO_con_cambios

## Detalle
Ver `theme-audit-debate.md`.

## Tema final

### Tema
Diagnóstico y diseño de MVP de confiabilidad de inventario de producto terminado por variante en Calzados Romantex S.A.C.

### Descripción
Propuesta académica de transformación digital acotada para una PYME de calzado en Trujillo: diagnosticar la inconsistencia entre la disponibilidad por variante (modelo × color × talla) que usa el área comercial y el stock físico en ubicaciones controladas por la empresa, y diseñar un MVP ligero (sin ERP/POS) con maestro de variantes, saldos por ubicación propia y bitácora de movimientos con latencia de turno. La estandarización de fichas técnicas de tallaje queda como diagnóstico de soporte y fase posterior, priorizable solo si la evidencia de campo muestra que el cuello es el maestro de tallaje y no el descuadre de inventario.

### Problema identificado
La disponibilidad por variante que el canal comercial puede confirmar puede no coincidir con el stock físico en ubicaciones de Romantex; sin evidencia de campo aún no se afirma magnitud ni se empaqueta “tiempo real”, analítica de ventas ni e-commerce. El diagnóstico debe medir descuadre y tiempo de confirmación, y separar si el cuello es inventario o maestro de tallaje.

### Alcance
- **Fase 0 (gate):** mapa AS-IS (dónde vive el stock, roles, muestra de descuadre por variante, ownership en talleres); sin esta evidencia el problema no se da por demostrado.
- **MVP1:** inventario PT por variante en ≤2 ubicaciones **propias** + operación mínima de actualización **sin POS** (entrada/salida/traslado/ajuste; cierre de turno).
- **Soporte en MVP1 (sin implantar):** relevamiento de cómo se anotan tallas hoy.
- **Fuera ahora:** tiempo real, POS, SUNAT/contabilidad, BOM/MRP, e-commerce, ATP en talleres tercerizados, ISO 19407 como criterio de ajuste, estandarización operativa de fichas (MVP2).

### MVP acordado
- MVP 1: Diagnóstico + diseño + piloto operable (Sheets u equivalente) de inventario PT por variante en ≤2 ubicaciones propias, con bitácora sin POS y métricas de exactitud / registro en el turno; 1 familia o colección de corte.
- MVP 2 (fuera ahora): plantilla y versionado de fichas técnicas de tallaje ligadas a SKU (ISO 19407 solo como anexo opcional de equivalencias de marcado).
- MVP 3 (condicional): más ubicaciones o reglas para tercerizados, solo si MVP1 demostró disciplina operativa.
- Fuera ahora: ERP/POS comercial, facturación, e-commerce, “tiempo real”, dashboards de tendencias de venta.

## Si NO_GO
*(No aplica.)*

## Listo para
`init-project` (usar este tema final en `profile.md`).
