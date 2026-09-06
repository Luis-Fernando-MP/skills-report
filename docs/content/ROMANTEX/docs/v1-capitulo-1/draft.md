# Informe académico — ROMANTEX

**Proyecto:** Digitalización del inventario (rollos/metraje) y fichas técnicas mínimas en Romantex S.A.C.  
**Organización:** Romantex S.A.C.  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v1-capitulo-1

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Romantex S.A.C. es una empresa peruana de Lima dedicada a la comercialización de telas para decoración, revestimientos para paredes y accesorios asociados, con presencia en showrooms y almacén propio. Opera como sociedad anónima cerrada (RUC 20293975036) e importa productos de firmas internacionales para los segmentos residencial y contract. El presente capítulo presenta a la organización a partir de fuentes públicas y sitúa el PoC académico de inventario de metraje y fichas técnicas mínimas como propuesta de diseño, sin afirmar partnership de implementación productiva ni auditoría del AS-IS interno.

#### 1.1.1. Reseña histórica

Según directorios basados en registros públicos, Romantex S.A.C. inicia actividades el 1 de octubre de 1995 (Universidad Peru, n.d.). El sitio corporativo sitúa la consolidación del showroom y de la marca hacia 1996, cuando se posiciona como especialista en telas para decoración, revestimientos y accesorios importados de alta calidad (Romantex, n.d.-a).

Desde entonces ha ampliado su oferta a un showroom con stock selecto, un área de pedidos por catálogo de firmas internacionales, una línea Contract orientada a hoteles, restaurantes y áreas públicas, y un almacén con miles de metros disponibles para entrega inmediata (Romantex, n.d.-a; Romantex, n.d.-b; Romantex, n.d.-c). Esa trayectoria explica por qué la disponibilidad de metraje y la coherencia de información de producto son relevantes para su modelo de servicio.

#### 1.1.2. Misión

No se publica un enunciado formal de misión en la página Empresa. La narrativa funcional describe a Romantex como especialista que ofrece productos importados sofisticados para uso residencial y comercial, con atención personalizada de diseñadores de interiores (Romantex, n.d.-a). El PoC toma de esa narrativa el compromiso implícito de disponibilidad y servicio, sin atribuir una misión institucional no documentada.

#### 1.1.3. Visión

Tampoco figura un bloque explícito de visión. El discurso de mejora continua, inversión en operaciones y satisfacción del cliente (Romantex, n.d.-a) sugiere una orientación a consolidarse como referencia premium en decoración textil en el Perú. El informe no inventa una visión corporativa; usa ese horizonte solo como contexto.

#### 1.1.4. Valores

No hay listado público de valores corporativos. Los principios inferibles del material institucional son calidad del producto, actualización de moda, servicio integral y rigor técnico en contract (incluidas menciones a normas y fichas técnicas en la línea contract) (Romantex, n.d.-a; Romantex, n.d.-c). El PoC se alinea con la **confiabilidad de la información de stock y ficha operativa**, no con la certificación normativa completa.

### 1.2. Diagnóstico situacional

El diagnóstico distingue: (a) hechos públicos de Romantex; (b) diseño del PoC académico. No es una auditoría de campo.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas de Romantex (fuentes públicas):**

- Posicionamiento de especialista con showroom y almacén de stock amplio para entrega inmediata (Romantex, n.d.-a).
- Diversificación residencial / catálogo / contract, con entrega de fichas técnicas en proyectos contract (Romantex, n.d.-c).
- Trayectoria de casi tres décadas en Lima y presencia multi-local (San Isidro, Surco) (Romantex, n.d.-b; Universidad Peru, n.d.).

**Debilidades / fricciones relevantes al PoC (hipótesis de diseño):**

- La complejidad de variantes (color, ancho, rollo, metraje residual) supera el modelo de SKU discreto simple.
- Las fichas técnicas de proveedor/contract no necesariamente equivalen a una ficha operativa unificada con metros residuales del almacén.
- Sin evidencia de campo publicada, el grado de digitalización actual de la empresa permanece como hipótesis de trabajo del proyecto, no como hallazgo auditado.

**Implicación:** el MVP 1 modela **rollo → metros residuales** + ficha mínima en una sede y una familia de producto, frente a gestión fragmentada, no frente a un ERP textil completo.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades:**

- El vertical textil dispone de referentes de inventario a nivel rollo (p. ej. PolyPM, Datatex), lo que valida el dominio técnico (PolyPM, n.d.; Datatex, n.d.).
- En Perú existen soluciones comerciales de inventario textil/decoración (p. ej. Cuenti, Kaypi, Invy); el PoC académico se posiciona como capa delgada pedagógica, no como entrante de mercado.

**Amenazas:**

- Saturación de software local/vertical: un PoC genérico sin baseline pierde aporte.
- Expectativas de multi-sede, EDI o RFID fuera del semestre.
- Confundir ficha PDF de proveedor con estandarización operativa interna.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El lienzo describe el **PoC académico**, no el P&L de Romantex.

| Bloque | Contenido (PoC) |
|--------|-----------------|
| Problema | Visibilidad incompleta de metraje residual por variante vs promesa de disponibilidad (hipótesis) |
| Segmentos | Personal showroom/almacén; diseñadores internos |
| Propuesta de valor | Consulta de metros + ficha mínima + alertas, sin ERP textil |
| Solución | Catálogo seed; rollo→metros; ficha 5–7 campos; alertas; CSV |
| Canales | Demo / piloto 1 sede |
| Ingresos | N/A en fase curso |
| Costos | Tiempo de equipo; infraestructura de demo |
| Métricas | Exactitud de consulta en muestra; alerta ante umbral |
| Ventaja evaluable | Alcance de curso + modelo rollo→metros (no suite enterprise) |

**Tesis de valor:** reducir sobrepromesa y fricción de consulta de metraje; sin ROI comercial en esta fase.

---

## Referencias

Datatex. (n.d.). *Inventory management software – textile & apparel*. https://datatex.com/portfolio-items/inventory/

PolyPM. (n.d.). *ERP inventory software for textile manufacturing*. https://polypm.com/erp-inventory-software-for-textile-manufacturing/

Romantex. (n.d.-a). *Empresa*. https://www.romantex.com.pe/empresa

Romantex. (n.d.-b). *Línea residencial*. https://www.romantex.com.pe/linea-residencial-1

Romantex. (n.d.-c). *Contract*. https://www.romantex.com.pe/contract

Universidad Peru. (n.d.). *Romantex S.A.C.* https://www.universidadperu.com/empresas/romantex.php
