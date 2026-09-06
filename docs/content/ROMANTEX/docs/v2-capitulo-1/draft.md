# Informe académico — ROMANTEX

**Proyecto:** Digitalización del inventario (rollos/metraje residual) y fichas técnicas mínimas en Romantex S.A.C.  
**Organización:** Romantex S.A.C.  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v2-capitulo-1  
**Fecha:** 2026-09-06

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Romantex S.A.C. es una sociedad anónima cerrada peruana (RUC 20293975036) con sede pública en Av. Paz Soldán 185, San Isidro (Lima), y showroom adicional en Av. El Polo 376, Surco. Su actividad pública se centra en la comercialización de telas para decoración, revestimientos para paredes y pisos, pasamanería y accesorios asociados, con importación de firmas internacionales y atención a segmentos residencial y contract (Romantex, n.d.-a; Universidad Peru, n.d.).

Este capítulo presenta a la organización a partir de fuentes abiertas. El proyecto académico asociado —visibilidad de metraje residual y ficha operativa mínima en showroom/almacén— se encuadra como propuesta de diseño acotada a un semestre; no implica partnership de implementación productiva.

#### 1.1.1. Reseña histórica

Los directorios basados en registros públicos sitúan el inicio de actividades de Romantex S.A.C. el **1 de octubre de 1995**, con inscripción societaria en ese mismo mes (Universidad Peru, n.d.). Ese hito legal marca la aparición formal de la empresa en el mercado limeño de textiles para el hogar y la decoración.

El sitio corporativo sitúa hacia **1996** la consolidación del showroom y de la marca como especialista en telas para decoración, revestimientos y accesorios importados de alta calidad, orientados tanto a uso residencial como comercial (Romantex, n.d.-a). En esa etapa se define el posicionamiento premium que aún estructura su discurso: stock selecto, firmas internacionales y servicio cercano a diseñadores de interiores.

En las décadas siguientes la oferta pública se diversifica en tres frentes: (1) showroom con stock disponible para entrega inmediata; (2) pedidos por catálogo de firmas internacionales; y (3) línea **Contract** para hoteles, restaurantes y áreas públicas, con menciones a fichas técnicas y normas de producto (Romantex, n.d.-a; Romantex, n.d.-b; Romantex, n.d.-c). La empresa comunica un almacén con miles de metros disponibles, lo que convierte la coherencia entre variante, metraje y promesa de disponibilidad en un eje operativo de su modelo de servicio.

#### 1.1.2. Misión

Romantex no publica un enunciado formal titulado “misión” en su página Empresa. La narrativa institucional describe a la firma como especialista que ofrece productos importados para uso residencial y comercial, con atención personalizada de diseñadores de interiores y énfasis en calidad y actualización de moda (Romantex, n.d.-a). Esa promesa de servicio —disponibilidad, asesoría y producto premium— es el núcleo funcional de su identidad comercial.

#### 1.1.3. Visión

Tampoco figura un bloque explícito de “visión”. El discurso de mejora continua, inversión en operaciones y satisfacción del cliente (Romantex, n.d.-a) orienta la lectura hacia la consolidación como referencia premium de decoración textil en el Perú. El presente informe no formula una visión corporativa inventada; usa ese horizonte solo como contexto de posicionamiento.

#### 1.1.4. Valores

No hay listado público de valores corporativos. Del material institucional se infieren principios operativos: calidad del producto, actualización de moda, servicio integral y rigor técnico en contract —incluidas menciones a normas (p. ej. Oeko-Tex 100) y entrega de fichas técnicas en proyectos contract (Romantex, n.d.-a; Romantex, n.d.-c). Esos principios refuerzan la relevancia de información de producto confiable (stock y ficha), distinta de un módulo completo de certificaciones.

### 1.2. Diagnóstico situacional

El diagnóstico siguiente tiene por sujeto a **Romantex y su entorno competitivo-operativo**, con base en fuentes públicas. Al cierre de cada bloque se indica la implicación para el proyecto académico.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas**

- Trayectoria de casi tres décadas (desde 1995) y presencia multi-local en Lima (San Isidro y Surco) (Universidad Peru, n.d.; Romantex, n.d.-b).
- Posicionamiento de especialista premium con showroom, catálogo de firmas internacionales y almacén con stock amplio para entrega inmediata (Romantex, n.d.-a).
- Diversificación residencial / catálogo / contract, con entrega de fichas técnicas en proyectos contract (Romantex, n.d.-c).

**Debilidades**

- La complejidad intrínseca del surtido (color, ancho, rollo, metraje residual) tensiona un control de inventario pensado solo en SKU discreto; la propia promesa de “miles de metros” eleva el costo de error si el residual no es consultable de forma única (Romantex, n.d.-a).
- Las fichas técnicas de proveedor o de contract no equivalen, por sí solas, a una ficha operativa unificada que combine variante, ubicación y metros residuales del almacén (Romantex, n.d.-c).
- Operar dos sedes de atención (San Isidro y Surco) introduce riesgo de desalineación de información de stock si los canales de consulta no están unificados (Romantex, n.d.-b; Universidad Peru, n.d.).
- El grado de digitalización interna del inventario no se describe en fuentes abiertas; cualquier lectura de madurez digital permanece fuera de lo auditado públicamente.

**Implicación para el proyecto / MVP 1:** modelar el flujo rollo → metros residuales y una ficha mínima (código, color, ancho, metros, ubicación) en **una sede y una familia de producto**, frente a gestión fragmentada. Quedan fuera del semestre multi-sede completa, EDI, RFID y ERP textil.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades**

- El vertical textil internacional documenta inventario a nivel rollo/yardaje (ancho, shade, metraje), lo que valida el dominio técnico del problema (PolyPM, n.d.; Datatex, n.d.).
- En el mercado hispanohablante y peruano existen plataformas que digitalizan inventario de telas y retail textil —p. ej. **Cuenti** (unidades en metros/rollos) y **Kaypi** (ERP textil con matriz de variantes)—, lo que indica demanda real de digitalización y un ecosistema de referencia para acotar un PoC pedagógico (Cuenti, n.d.; Kaypi, n.d.).
- La línea contract y la exigencia de fichas técnicas en proyectos abren espacio a una capa operativa mínima alineada al showroom, sin pretender BIM ni PLM (Romantex, n.d.-c).

**Amenazas**

- Suites comerciales locales/regionales (Cuenti, Kaypi y equivalentes) pueden cubrir ya casos de inventario textil; una digitalización genérica aporta poco si no se ancla al modelo rollo→metros del showroom de decoración (Cuenti, n.d.; Kaypi, n.d.).
- Proxies enterprise (PolyPM, Datatex) elevan expectativas de trazabilidad multi-planta y multi-unidad que exceden la escala de una PyME showroom y de un curso de un semestre (PolyPM, n.d.; Datatex, n.d.).
- Dependencia de importaciones y catálogos de firmas internacionales implica variabilidad de fichas de proveedor; confundir el PDF técnico del fabricante con la estandarización operativa interna diluye el problema (Romantex, n.d.-a; Romantex, n.d.-c).

**Implicación para el proyecto / MVP 1:** el PoC se posiciona como capa delgada académica frente a Excel/cuaderno fragmentado, no como entrante comercial frente a Cuenti/Kaypi ni como sustituto de PolyPM/Datatex. Límites de curso (RFID, EDI, multi-sede) se tratan como restricciones de alcance, no como “amenazas del entorno” de Romantex.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El lienzo principal describe el **modelo de negocio de Romantex** según fuentes públicas (no el P&L confidencial).

| Bloque | Contenido (Romantex) |
|--------|----------------------|
| Problema del cliente | Necesidad de telas/revestimientos premium con asesoría y disponibilidad oportuna para proyectos residenciales y contract |
| Segmentos | Hogares y diseñadores de interiores (residencial); hoteles, restaurantes y áreas públicas (contract); pedidos por catálogo |
| Propuesta de valor | Especialista en decoración textil importada, stock selecto, showroom y servicio personalizado |
| Solución / oferta | Telas (cortinas, tapicería, exteriores, cubrecamas), revestimientos, pasamanería; líneas residencial, catálogo y contract |
| Canales | Showrooms San Isidro y Surco; almacén; atención a diseñadores; canal contract |
| Ingresos | Comercialización de telas y revestimientos (detalle de márgenes no público) |
| Costos | Importación, showroom/almacén, personal de atención y operaciones (estructura inferida; no auditada) |
| Métricas clave | Disponibilidad de metraje, rotación de stock selecto, satisfacción en asesoría (indicadores no publicados; relevantes al discurso de servicio) |
| Ventaja | Marca consolidada desde mediados de los 90, posicionamiento premium y presencia multi-local en Lima |

**Encaje del proyecto (contraste MVP 1):** el PoC académico ataca la visibilidad de metraje residual y una ficha operativa mínima para reducir sobrepromesa en consulta de stock. Segmentos del PoC: personal de showroom/almacén y diseñadores internos. Métricas del PoC: exactitud de consulta en una muestra y alerta ante umbral. No sustituye el modelo comercial de Romantex ni compite como SaaS.

---

## Referencias

Cuenti. (n.d.). *¿Por qué gestionar tu inventario de telas con Cuenti?* https://cuenti.com/software-contable/por-que-gestionar-tu-inventario-de-telas-con-cuenti/

Datatex. (n.d.). *Inventory management software – textile & apparel*. https://datatex.com/portfolio-items/inventory/

Kaypi. (n.d.). *Sistema ERP textil \| Inventario 3D, ventas y facturación*. https://kaypi.pe/sistema-erp-para-textileria

PolyPM. (n.d.). *ERP inventory software for textile manufacturing*. https://polypm.com/erp-inventory-software-for-textile-manufacturing/

Romantex. (n.d.-a). *Empresa*. https://www.romantex.com.pe/empresa

Romantex. (n.d.-b). *Línea residencial*. https://www.romantex.com.pe/linea-residencial-1

Romantex. (n.d.-c). *Contract*. https://www.romantex.com.pe/contract

Universidad Peru. (n.d.). *Romantex S.A.C.* https://www.universidadperu.com/empresas/romantex.php
