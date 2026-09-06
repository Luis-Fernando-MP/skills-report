# Veredicto auditoría — ITD

## Veredicto global
GO_con_cambios

## Detalle
Ver `theme-audit-debate.md`.

## Tema final

### Tema
Diagnóstico del registro de inventario de producto terminado por variante (modelo × color × talla) en Calzados Romantex S.A.C.

### Descripción
Propuesta académica de transformación digital en fase diagnóstico para una PYME de calzado en Trujillo: verificar con evidencia AS-IS si el registro actual de stock de producto terminado por variante en ubicaciones propias permite responder de forma consistente a consultas de disponibilidad, y diseñar un modelo de datos mínimo (consulta en un punto propio) sin desplegar ERP/POS ni asumir integración con talleres tercerizados.

### Problema identificado
**Hipótesis a verificar (no hecho afirmado):** se desconoce, con evidencia medible, si el registro de stock PT por variante en ubicaciones propias de Romantex permite responder de forma consistente a consultas de disponibilidad. La informalidad de inventario declarada en el perfil motiva un diagnóstico AS-IS antes de adoptar POS/ERP o ampliar a terceros.

**Métricas de diagnóstico (obligatorias en campo):** en muestra de SKU variante y ≤2 ubicaciones propias — (a) % coincidencia conteo físico vs registro; (b) tiempo/esfuerzo para responder “¿hay stock de variante X?”; (c) rol que actualiza el dato y latencia declarada/observada entre movimiento físico y registro. Umbrales de “problema confirmado” se fijan tras el piloto de conteo.

### Alcance
Diagnóstico AS-IS + diseño de MVP de consulta de inventario PT por variante en **una** ubicación propia de arranque (máx. **2** propias en extensión). Incluye mapa ownership (quién carga/corrige) y campos mínimos de variante. Ficha de tallaje solo como **anexo muestral no bloqueante** (pocos modelos, campos mínimos; sin equivalencias ISO como sistema).

**Fuera de alcance esta fase:** talleres tercerizados / El Porvenir como ubicaciones operativas; “tiempo real”; analytics de ventas; POS/ERP; contabilidad/SUNAT; BOM/MRP; e-commerce; estandarización completa de fichas de tallaje; implementación de ISO 19407 como sistema de ajuste/horma.

## MVP entregables

### MVP de arranque (recomendado al equipo)
MVP 1 — Consulta de disponibilidad PT por variante en un punto propio (métricas AS-IS + modelo de datos como criterio de éxito; ficha tallaje solo anexo no bloqueante) — gana el debate porque mitiga el doble núcleo, excluye tercerizados y convierte el problema literario en hipótesis falsable.

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | Diagnóstico + diseño de fuente de verdad: stock PT por variante en **una** ubicación propia | Informe AS-IS; modelo de datos (Variante, Ubicación, Saldo/ajuste); métricas match/tiempo/ownership; wireframes opcionales de consulta; anexo ficha muestral N≤10 **no bloqueante** | Tutor/empresa validan AS-IS; métricas de diagnóstico ejecutadas o protocolizadas sobre muestra; consulta diseñada para ese punto sin POS | se trabaja ahora |
| 2 | Gobierno del dato y frecuencia realista (turno/día, no tiempo real) | RACI planta vs comercial; protocolo de ajuste de saldo; checklist consistencia; SLAs de actualización | Dueño único del saldo en ubicación piloto y frecuencia acordada ≠ tiempo real | después |
| 3 | Extensión opcional a ≤2 ubicaciones **propias** | Vista stock por ubicación; mockup U1/U2; backlog post-curso | Diseño muestra stock por variante en ≤2 puntos propios sin sync inventado ni terceros | después (condicional) |

### Fuera de secuencia / descartado
- Digitalización de talleres tercerizados / El Porvenir en esta fase
- “Tiempo real”, analytics de ventas, reposición predictiva
- ISO 19407 completa / ficha de tallaje como co-núcleo o gate de MVP1
- POS, ERP, SUNAT, BOM/MRP, e-commerce
- Vender el entregable como alternativa comercial a INVY / iSiore

## Marco PICOCT (para bibliography)

| Componente | Definición | Criterios / descripción del caso |
| :---: | :--- | :--- |
| **P** | Population / Problem | PYME de calzado / personal planta-comercial; hipótesis de inconsistencia entre disponibilidad confirmable por variante (modelo×color×talla) y stock físico en ubicaciones propias |
| **I** | Intervention | Diagnóstico AS-IS + diseño de fuente de consulta de inventario PT por variante (modelo de datos mínimo; sin ERP/POS) en ≤1–2 ubicaciones propias |
| **C** | Comparison | Prácticas actuales informales (memoria, WhatsApp, cuaderno, Excel suelto) y alternativa de mercado POS/ERP (fuera de alcance del piloto) |
| **O** | Outcome | % coincidencia físico vs registro; tiempo/esfuerzo para responder “¿hay stock de variante X?”; ownership/latencia de actualización; consultabilidad diseñada sin POS |
| **C** | Context | Perú / Trujillo; manufactura de calzado; PYME; ubicaciones propias (no talleres tercerizados en esta fase) |
| **T** | Time / Type of study | Año 2026 (sin rango indicado en audit); tipo preferente: artículos (`ar`) |

Fuente para `bibliography-picoct` / espejo en `profile.md` vía `init-project`.

## Listo para
`init-project` (espejar tema final + MVP + Marco PICOCT en `profile.md`) → `init-project-mvp mvp-1` → `bibliography-picoct`.
