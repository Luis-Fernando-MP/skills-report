# Informe académico — SMOKEVAL

**Proyecto:** Alertas de stock mínimo para ferretería pequeña (PoC)  
**Organización ancla:** Pulpos (referente de mercado)  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v1-capitulo-1

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Pulpos es una plataforma de software de gestión y punto de venta orientada a pequeñas y medianas empresas en México, con una línea de producto específicamente dirigida a ferreterías. Su oferta pública combina inventario multi-SKU, operación de mostrador, crédito a clientes habituales y, en el contexto mexicano, capacidades de facturación electrónica. El presente capítulo sitúa a Pulpos como **referente de mercado** para el proyecto académico SMOKEVAL: un PoC de alertas de stock mínimo para ferretería pequeña, sin afirmar partnership comercial ni auditoría del AS-IS interno de la compañía.

#### 1.1.1. Reseña histórica

En las fuentes públicas de producto consultadas, Pulpos se presenta como solución cloud para ordenar el día a día de comercios de mostrador. En la vertical ferretería documenta el control de catálogos extensos (tornillería, herramientas y materiales), la sincronización de inventario y la generación de alertas o listados de productos por reponer antes del cierre (Pulpos, n.d.-a; Pulpos, n.d.-b).

No se halló en esas páginas una cronología fundacional detallada (año exacto de constitución, rondas de inversión o hitos corporativos tipo “primera sucursal”). Lo verificable es el **posicionamiento vigente**: plataforma de gestión en la nube para PyME mexicanas, con narrativa de acompañamiento a más de 12 000 negocios según el propio sitio de ferreterías (Pulpos, n.d.-a). Para efectos de este informe, esa evidencia basta para anclar el contexto competitivo; no se inventan hitos históricos no publicados.

#### 1.1.2. Misión

Las páginas de producto revisadas no publican un enunciado formal de “misión” corporativa. La narrativa funcional equivalente enfatiza ayudar al comercio a dejar de operar con cuaderno o Excel fragmentado, centralizando inventario, ventas y reportes para decidir con visibilidad (Pulpos, n.d.-a). El PoC SMOKEVAL adopta ese problema de visibilidad de stock como justificación de diseño, sin atribuir a Pulpos una misión institucional no documentada.

#### 1.1.3. Visión

Tampoco se encontró un bloque explícito de “visión” a largo plazo. El discurso comercial apunta a un mostrador digitalizado donde el dueño conoce qué se vende, qué falta y qué reponer, incluyendo asistencia conversacional sobre inventario en planes avanzados (Pulpos, n.d.-a). El proyecto académico no proyecta la visión corporativa de Pulpos; solo usa ese horizonte de producto como contraste: el mercado ya ofrece suites amplias, mientras el PoC se concentra en alertas.

#### 1.1.4. Valores

No hay un listado público de valores corporativos (p. ej. integridad, innovación) en las URLs citadas. Los principios de producto inferibles del material de marketing son: foco en PyME de mostrador, control fino de catálogos grandes y reducción de pérdidas por falta de información de stock (Pulpos, n.d.-a; Pulpos, n.d.-b). El PoC SMOKEVAL se alinea solo con el valor de **visibilidad de reposición**, no con el paquete completo POS/CFDI/multi-sucursal.

### 1.2. Diagnóstico situacional

El diagnóstico siguiente combina (a) hechos públicos del referente Pulpos y del segmento ferretero digitalizado, y (b) el diseño del PoC SMOKEVAL como propuesta académica acotada. No constituye una auditoría de campo de una ferretería concreta ni de los sistemas internos de Pulpos.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas (referente / oportunidad de producto):**

- Oferta madura de inventario multi-SKU para ferreterías, con búsqueda por código/categoría y sincronización entre sucursales en planes que lo incluyen (Pulpos, n.d.-a).
- Capacidad pública de anticipar productos por reponer y de consultar el estado del inventario sin depender solo del cuaderno (Pulpos, n.d.-b).
- Narrativa de acompañamiento a un volumen amplio de PyME mexicanas, lo que sugiere product-market fit en el segmento (Pulpos, n.d.-a).

**Debilidades / fricciones para el arquetipo “ferretería de barrio + curso”:**

- Las suites POS+inventario+CFDI pueden resultar sobredimensionadas para un MVP académico de un semestre o para un negocio que solo necesita umbrales y alertas.
- La dependencia de API, planes comerciales y contexto fiscal mexicano (CFDI) no es transferable 1:1 a un PoC pedagógico en otro país sin redesign.
- Ausencia de reseña histórica corporativa detallada en fuentes abiertas limita el análisis organizacional profundo; el informe lo declara y no lo inventa.

**Implicación para SMOKEVAL:** el PoC se diseña como **capa mínima** (catálogo 50–100 SKUs, umbral, alerta, lista de reposición), usando a Pulpos como evidencia de que el problema de reposición es real en el mercado, no como plantilla a clonar.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades:**

- Digitalización de inventario en PyME de retail especializado (ferretería) sigue siendo un problema visible: catálogos grandes, unidades mixtas y riesgo de quiebre.
- Herramientas cloud reducen la barrera de infraestructura para el comerciante, pero dejan espacio a soluciones **más delgadas** cuando el dolor es solo “qué reponer mañana”.
- El formato PoC académico permite demostrar el flujo de alerta sin cargar POS ni facturación.

**Amenazas:**

- Competidores de suite completa (Pulpos y análogos) pueden absorber el caso de uso de alertas dentro de un plan más amplio, reduciendo diferenciación si el PoC no acota bien el alcance.
- Expectativas del usuario real pueden exigir código de barras, multi-almacén o integración con proveedores fuera del perímetro del curso.
- Riesgo de tema vacío si el entregable queda en un dashboard genérico sin umbrales ni lista de reposición operable.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El Lean Canvas siguiente describe el **PoC SMOKEVAL** (propuesta académica), no el modelo de negocio corporativo de Pulpos.

| Bloque | Contenido (PoC SMOKEVAL) |
|--------|---------------------------|
| Problema | Quiebres y compras de emergencia por inventario a ojo en ferretería pequeña |
| Segmentos de clientes | Dueño/encargado de ferretería de barrio (1 tienda, catálogo acotado) |
| Propuesta única de valor | Alertas de stock mínimo + lista de reposición semanal sin adoptar POS completo |
| Solución | Catálogo seed, umbrales, pantalla/lista de alertas, export CSV |
| Canales | Demo académica / piloto simulado en curso |
| Flujos de ingreso | N/A en fase PoC de curso (sin monetización) |
| Estructura de costos | Tiempo de desarrollo del equipo; infra mínima de demo |
| Métricas clave | Alerta ante quiebre simulado; lista de reposición coherente con umbrales |
| Ventaja injusta | Alcance deliberadamente estrecho y evaluable en un semestre |

Pulpos, en contraste, monetiza una suite de gestión/POS; SMOKEVAL no compite en ese plano: usa el referente para justificar el problema y se diferencia por **no** incluir cobro, CFDI ni multi-sucursal en el MVP 1.

---

## Referencias

Pulpos. (n.d.-a). *Software de gestión para ferreterías*. https://pulpos.com/ferreterias/

Pulpos. (n.d.-b). *Punto de venta para ferreterías*. https://pulpos.com/giros/ferreterias/punto-de-venta/
