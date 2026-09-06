# Informe académico — ROMANTEX

**Proyecto:** Digitalización del inventario (rollos/metraje residual) y fichas técnicas mínimas en Romantex S.A.C.  
**Organización:** Romantex S.A.C.  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v2-capitulo-1 (polish)  
**Fecha:** 2026-09-06

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Romantex S.A.C. es una sociedad anónima cerrada peruana (RUC 20293975036) con sede pública en Av. Paz Soldán 185, San Isidro (Lima), y showroom adicional en Av. El Polo 376, Surco. Comercializa telas para decoración, revestimientos para paredes y pisos, pasamanería y accesorios; importa firmas internacionales y atiende segmentos residencial y contract (Romantex, n.d.-a; Universidad Peru, n.d.).

Este capítulo se basa en fuentes abiertas. El proyecto académico —metraje residual consultable y ficha operativa mínima— es una propuesta de diseño de un semestre, no un partnership de implementación productiva.

#### 1.1.1. Reseña histórica

Los directorios basados en registros públicos sitúan el inicio de actividades el **1 de octubre de 1995** (Universidad Peru, n.d.). Ese hito societario marca la aparición formal de la empresa en el mercado limeño de textiles para decoración.

El sitio corporativo sitúa hacia **1996** la consolidación del showroom y de la marca como especialista en telas, revestimientos y accesorios importados para uso residencial y comercial (Romantex, n.d.-a). Ahí se fija el posicionamiento premium: stock selecto, firmas internacionales y servicio a diseñadores de interiores.

En las décadas siguientes, según la narrativa pública, la oferta se organiza en showroom con entrega inmediata, pedidos por catálogo de firmas internacionales y línea **Contract** (hoteles, restaurantes y áreas públicas), con menciones a fichas técnicas y normas de producto (Romantex, n.d.-a; Romantex, n.d.-b; Romantex, n.d.-c). La empresa comunica un almacén con miles de metros disponibles. El techo de fuentes abiertas no aporta hitos datados posteriores independientes del sitio corporativo; lo que sigue se lee como trayectoria comunicada, no como crónica auditada año a año.

#### 1.1.2. Misión

No hay enunciado formal de misión en la página Empresa. La narrativa describe a Romantex como especialista en productos importados para uso residencial y comercial, con atención personalizada de diseñadores y énfasis en calidad y moda (Romantex, n.d.-a). El compromiso operativo implícito es disponibilidad y asesoría premium.

#### 1.1.3. Visión

Sin bloque explícito de visión, el discurso de mejora continua, inversión en operaciones y satisfacción del cliente (Romantex, n.d.-a) apunta a consolidarse como referencia premium de decoración textil en el Perú. No se inventa una visión corporativa.

#### 1.1.4. Valores

Sin listado público de valores. Del material institucional se infieren calidad de producto, actualización de moda, servicio integral y rigor técnico en contract —incluidas menciones a normas (p. ej. Oeko-Tex 100) y fichas técnicas en proyectos contract (Romantex, n.d.-a; Romantex, n.d.-c). Eso refuerza la importancia de información de producto confiable, sin convertir el informe en un módulo de certificaciones.

### 1.2. Diagnóstico situacional

Sujeto del diagnóstico: **Romantex y su entorno**. Hechos públicos e inferencias de diseño se distinguen en el texto. Al cierre de cada bloque, la implicación para el proyecto académico.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas**

- Trayectoria societaria desde 1995 y presencia en San Isidro y Surco (Universidad Peru, n.d.; Romantex, n.d.-b).
- Posicionamiento premium con showroom, catálogo de firmas internacionales y discurso de stock amplio para entrega inmediata (Romantex, n.d.-a).
- Diversificación residencial / catálogo / contract, con entrega de fichas técnicas en contract (Romantex, n.d.-c).

**Debilidades** (hechos de estructura + inferencias de diseño a partir del discurso público; no son hallazgos de campo)

- El surtido por color, ancho, rollo y metraje residual es estructuralmente más complejo que un SKU discreto simple; la promesa de “miles de metros” eleva el costo reputacional de un residual mal consultado (Romantex, n.d.-a).
- Las fichas técnicas de proveedor o de contract no demuestran, por sí solas, una ficha operativa unificada (variante + ubicación + metros residuales) (Romantex, n.d.-c).
- Dos puntos de atención (San Isidro y Surco) crean el riesgo plausible de desalineación informativa si no hay una fuente única de consulta; el informe no observa ese proceso en campo (Romantex, n.d.-b).
- El grado de digitalización interna del inventario no figura en fuentes abiertas.

**Implicación para el proyecto / MVP 1:** flujo rollo → metros residuales y ficha mínima en **una sede y una familia de producto**, frente a consulta fragmentada. Fuera de semestre: multi-sede completa, EDI, RFID y ERP textil.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades**

- Referentes internacionales documentan inventario a nivel rollo/yardaje (ancho, shade, metraje), lo que valida el dominio técnico (PolyPM, n.d.; Datatex, n.d.).
- **Cuenti** publica capacidades de inventario de telas con unidades en metros, yardas, kilos o rollos, señal de demanda de digitalización en el vertical de telas (Cuenti, n.d.).
- La línea contract y la exigencia de fichas técnicas abren espacio a una capa operativa mínima en showroom, sin BIM ni PLM (Romantex, n.d.-c).

**Amenazas**

- **Cuenti** y suites afines pueden absorber casos de inventario de telas; un PoC genérico aporta poco si no se ancla al rollo→metros del showroom de decoración (Cuenti, n.d.).
- **Kaypi** ilustra saturación de ERP/POS textil en el mercado peruano (matriz de variantes color/talla, tienda de ropa); es referente de competencia comercial **adyacente** (apparel), no evidencia directa de metraje residual en decoración (Kaypi, n.d.).
- Proxies enterprise (PolyPM, Datatex) elevan expectativas multi-planta ajenas a una PyME showroom y a un semestre (PolyPM, n.d.; Datatex, n.d.).
- Fichas PDF de proveedores importados pueden confundirse con estandarización operativa interna (Romantex, n.d.-a; Romantex, n.d.-c).

**Implicación para el proyecto / MVP 1:** capa delgada académica frente a fragmentación (p. ej. Excel/cuaderno), no entrante frente a Cuenti ni sustituto de PolyPM/Datatex. RFID, EDI y multi-sede son restricciones de alcance del curso, no amenazas del entorno de Romantex.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

Lienzo principal: **modelo de negocio de Romantex** según fuentes públicas.

| Bloque | Contenido (Romantex) |
|--------|----------------------|
| Problema del cliente | Telas y revestimientos premium con asesoría y disponibilidad oportuna (residencial y contract) |
| Segmentos | Hogares y diseñadores (residencial); hoteles, restaurantes y áreas públicas (contract); pedidos por catálogo |
| Propuesta de valor | Especialista en decoración textil importada, stock selecto, showroom y servicio personalizado |
| Solución / oferta | Telas (cortinas, tapicería, exteriores, cubrecamas), revestimientos, pasamanería; líneas residencial, catálogo y contract |
| Canales | Showrooms San Isidro y Surco; almacén; atención a diseñadores; canal contract |
| Ingresos | Comercialización de telas y revestimientos (márgenes no públicos) |
| Costos | Importación, showroom/almacén y personal (estructura inferida; no auditada) |
| Métricas clave | No publicadas por la empresa |
| Ventaja | Marca consolidada desde mediados de los 90, posicionamiento premium y presencia multi-local en Lima |

**Encaje del proyecto (MVP 1):** el PoC busca que el metraje residual sea consultable y que exista una ficha operativa mínima, para reducir sobrepromesa en la consulta de stock. Usuarios del PoC: personal de showroom/almacén y diseñadores internos. Métricas del PoC (no de Romantex): exactitud de consulta en una muestra de 50–100 rollos y alerta ante umbral. Hipótesis falsable de valor: si el residual es consultable en una fuente única, baja la sobrepromesa en esa muestra. No sustituye el modelo comercial ni compite como SaaS.

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
