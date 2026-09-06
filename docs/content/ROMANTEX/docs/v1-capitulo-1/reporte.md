# Informe académico — ROMANTEX

**Proyecto:** Digitalización del inventario (rollos/metraje) y fichas técnicas mínimas en Romantex S.A.C.  
**Organización:** Romantex S.A.C.  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v1-capitulo-1 (polish)

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Romantex S.A.C. es una empresa peruana con sede en Lima dedicada a la comercialización de telas para decoración, revestimientos para paredes y accesorios asociados. Opera como sociedad anónima cerrada (RUC 20293975036), importa productos de firmas internacionales y atiende los segmentos residencial y contract mediante showrooms y almacén propio. Este capítulo presenta a la organización a partir de fuentes públicas y encuadra el PoC académico de inventario de metraje y fichas técnicas mínimas como propuesta de diseño. No afirma partnership de implementación productiva ni auditoría del sistema interno de inventarios.

#### 1.1.1. Reseña histórica

Según directorios basados en registros públicos, Romantex S.A.C. inicia actividades el 1 de octubre de 1995 (Universidad Peru, n.d.). El sitio corporativo sitúa la consolidación del showroom y de la marca hacia 1996, cuando se posiciona como especialista en telas para decoración, revestimientos y accesorios importados (Romantex, n.d.-a).

Desde entonces ha ampliado showroom con stock selecto, pedidos por catálogo de firmas internacionales, línea Contract (hoteles, restaurantes y áreas públicas) y un almacén con miles de metros disponibles para entrega inmediata (Romantex, n.d.-a; Romantex, n.d.-b; Romantex, n.d.-c). Esa trayectoria hace relevante la disponibilidad de metraje y la coherencia de la información de producto para su modelo de servicio.

#### 1.1.2. Misión

No se publica un enunciado formal de misión en la página Empresa. La narrativa funcional describe a Romantex como especialista que ofrece productos importados para uso residencial y comercial, con atención personalizada de diseñadores de interiores (Romantex, n.d.-a). El PoC toma de esa narrativa el compromiso implícito de disponibilidad y servicio, sin atribuir una misión institucional no documentada.

#### 1.1.3. Visión

Tampoco figura un bloque explícito de visión. El discurso de mejora continua, inversión en operaciones y satisfacción del cliente (Romantex, n.d.-a) sugiere la voluntad de consolidarse como referencia premium en decoración textil en el Perú. El informe no inventa una visión corporativa.

#### 1.1.4. Valores

No hay listado público de valores corporativos. Los principios inferibles del material institucional son calidad del producto, actualización de moda, servicio integral y rigor técnico en contract, incluidas menciones a normas y fichas técnicas en esa línea (Romantex, n.d.-a; Romantex, n.d.-c). El PoC se alinea con la confiabilidad de la información de stock y de la ficha operativa mínima, no con un módulo completo de certificaciones.

### 1.2. Diagnóstico situacional

El diagnóstico distingue hechos públicos de Romantex y decisiones de diseño del PoC académico. No constituye una auditoría de campo.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas de Romantex (fuentes públicas):**

- Posicionamiento de especialista con showroom y almacén de stock amplio para entrega inmediata (Romantex, n.d.-a).
- Diversificación residencial, catálogo y contract, con entrega de fichas técnicas en proyectos contract (Romantex, n.d.-c).
- Trayectoria de casi tres décadas en Lima y presencia en San Isidro y Surco (Romantex, n.d.-b; Universidad Peru, n.d.).

**Debilidades o fricciones relevantes al PoC (hipótesis de diseño):**

- Las variantes (color, ancho, rollo, metraje residual) no se agotan en un modelo de SKU discreto simple.
- Las fichas técnicas de proveedor o de contract no equivalen automáticamente a una ficha operativa unificada con metros residuales del almacén.
- El grado de digitalización actual no está publicado; el informe lo trata como hipótesis hasta disponer de evidencia de campo.

**Implicación para el MVP 1:** modelar el flujo rollo → metros residuales y una ficha mínima en una sede y una familia de producto, frente a una gestión fragmentada, no frente a un ERP textil completo.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades:**

- El vertical textil cuenta con referentes de inventario a nivel rollo (PolyPM, Datatex), lo que valida el dominio técnico (PolyPM, n.d.; Datatex, n.d.).
- En el mercado peruano existen soluciones de inventario textil o de decoración; el PoC se plantea como capa delgada académica, no como entrante comercial.

**Amenazas:**

- Un PoC genérico sin baseline pierde aporte frente a software ya desplegado.
- Expectativas de multi-sede, EDI o RFID exceden un semestre.
- Confundir la ficha PDF del proveedor con la estandarización operativa interna diluye el problema.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El lienzo describe el PoC académico, no el modelo financiero de Romantex.

| Bloque | Contenido (PoC) |
|--------|-----------------|
| Problema | Visibilidad incompleta de metraje residual por variante frente a la promesa de disponibilidad (hipótesis) |
| Segmentos | Personal de showroom y almacén; diseñadores internos |
| Propuesta de valor | Consulta de metros, ficha mínima y alertas, sin ERP textil |
| Solución | Catálogo seed; rollo→metros; ficha de 5 a 7 campos; alertas; CSV |
| Canales | Demostración o piloto en una sede |
| Ingresos | No aplica en fase de curso |
| Costos | Tiempo del equipo e infraestructura de demostración |
| Métricas | Exactitud de consulta en una muestra; alerta ante umbral |
| Ventaja evaluable | Alcance de curso y modelo rollo→metros, no una suite empresarial |

**Tesis de valor:** reducir la sobrepromesa y la fricción al consultar metraje. En esta fase no hay retorno comercial ni sponsor documentado.

---

## Referencias

Datatex. (n.d.). *Inventory management software – textile & apparel*. https://datatex.com/portfolio-items/inventory/

PolyPM. (n.d.). *ERP inventory software for textile manufacturing*. https://polypm.com/erp-inventory-software-for-textile-manufacturing/

Romantex. (n.d.-a). *Empresa*. https://www.romantex.com.pe/empresa

Romantex. (n.d.-b). *Línea residencial*. https://www.romantex.com.pe/linea-residencial-1

Romantex. (n.d.-c). *Contract*. https://www.romantex.com.pe/contract

Universidad Peru. (n.d.). *Romantex S.A.C.* https://www.universidadperu.com/empresas/romantex.php
