# Informe académico — SMOKEVAL

**Proyecto:** Alertas de stock mínimo para ferretería pequeña (PoC)  
**Organización ancla:** Pulpos (referente de mercado)  
**Alcance de esta versión:** Capítulo 1 — Presentación de la empresa  
**Versión:** v1-capitulo-1 (polish)

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Pulpos es una plataforma de software de gestión y punto de venta orientada a pequeñas y medianas empresas en México, con una línea de producto dirigida a ferreterías. Su oferta pública combina inventario multi-SKU, operación de mostrador, crédito a clientes habituales y, en el contexto mexicano, capacidades de facturación electrónica. Este capítulo sitúa a Pulpos como **referente de mercado** para el proyecto académico SMOKEVAL: un PoC de alertas de stock mínimo para ferretería pequeña. No se afirma partnership comercial ni auditoría del AS-IS interno de la compañía.

#### 1.1.1. Reseña histórica

En las fuentes públicas de producto, Pulpos se presenta como solución cloud para comercios de mostrador. En ferretería documenta control de catálogos extensos, sincronización de inventario y listados o alertas de productos por reponer (Pulpos, n.d.-a; Pulpos, n.d.-b). Esas mismas fuentes muestran que las alertas de reposición ya forman parte del producto del referente; el PoC no inventa esa función, sino que la **aísla** en una capa mínima evaluable en curso.

No se halló en esas páginas una cronología fundacional detallada. Lo verificable es el posicionamiento vigente como plataforma cloud para PyME mexicanas, con narrativa de acompañamiento a más de 12 000 negocios según el propio sitio (dato de marketing corporativo, no auditado de forma independiente) (Pulpos, n.d.-a). No se inventan hitos históricos no publicados.

#### 1.1.2. Misión, visión y valores (fuentes públicas)

En las fuentes consultadas no figura un enunciado formal de misión, visión ni valores corporativos. Lo verificable es una narrativa de producto: centralizar inventario y ventas para decidir con visibilidad, orientar al dueño hacia un mostrador digitalizado (incluida asistencia conversacional en planes avanzados) y enfatizar control de catálogos grandes y reducción de pérdidas por falta de información de stock (Pulpos, n.d.-a; Pulpos, n.d.-b). El PoC SMOKEVAL toma solo el eje de **visibilidad de reposición**, sin atribuir formulaciones institucionales no documentadas ni replicar POS, CFDI o multi-sucursal.

### 1.2. Diagnóstico situacional

El diagnóstico combina hechos públicos del referente Pulpos con el diseño del PoC SMOKEVAL. No es una auditoría de campo de una ferretería concreta ni de los sistemas internos de Pulpos.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas (referente / producto documentado):**

- Oferta documentada de inventario multi-SKU para ferreterías, con búsqueda y sincronización entre sucursales en planes que lo incluyen (Pulpos, n.d.-a).
- Capacidad pública de anticipar productos por reponer y consultar inventario sin depender solo del cuaderno (Pulpos, n.d.-b).
- Tracción comercial **declarada** por la empresa (más de 12 000 negocios en su sitio), útil como señal de mercado pagador por gestión de inventario, no como estadística sectorial independiente (Pulpos, n.d.-a).

**Debilidades / fricciones para el arquetipo “ferretería de barrio + curso”:**

- Las suites POS+inventario+CFDI resultan sobredimensionadas para un MVP académico de un semestre: el PoC no compite por simplicidad comercial frente al referente, sino por **alcance acotado y criterios de evaluación del curso**.
- El contexto fiscal mexicano (CFDI) y la suite completa no son transferibles 1:1 a un PoC pedagógico en otro país sin redesign.
- La ausencia de reseña histórica corporativa detallada en fuentes abiertas limita el análisis organizacional profundo; el informe lo declara.

**Implicación para SMOKEVAL:** el PoC se diseña como capa mínima (catálogo 50–100 SKUs, umbral, alerta, lista de reposición). Pulpos evidencia que la reposición anticipada es un caso de uso comercializado; el aporte académico es demostrar ese flujo de forma aislada y evaluable, no cubrir un vacío de mercado inexistente.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades (marco analítico del informe):**

- La digitalización de inventario en PyME de retail especializado sigue siendo un problema visible (catálogos grandes, unidades mixtas, riesgo de quiebre). TODO: citar — evidencia sectorial LATAM/MX de digitalización o quiebres en retail especializado.
- La digitalización cloud confirma que la reposición oportuna es un problema reconocido; el PoC no explora un nicho ignorado, sino que modela el flujo de alertas en un perímetro acotado para demostrar competencias técnicas.
- El formato PoC académico permite demostrar el flujo de alerta sin cargar POS ni facturación.

**Amenazas:**

- Suites y referentes del segmento (Pulpos y análogos) ya empaquetan alertas dentro de planes más amplios; la diferenciación del PoC depende de acotar el alcance pedagógico, no de afirmar exclusividad de función.
- Expectativas de usuario real pueden exigir código de barras, multi-almacén o integración con proveedores fuera del perímetro del curso.
- Riesgo de entregable sin aporte evaluable si el prototipo se limita a un tablero genérico, sin umbrales ni lista de reposición operable.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El Lean Canvas describe el **PoC SMOKEVAL** (propuesta académica), no el modelo de negocio corporativo de Pulpos.

| Bloque | Contenido (PoC SMOKEVAL) |
|--------|---------------------------|
| Problema | Quiebres y compras de emergencia por inventario a ojo en ferretería pequeña |
| Segmentos de clientes | Dueño/encargado de ferretería de barrio (1 tienda, catálogo acotado) |
| Propuesta única de valor | Alertas de stock mínimo y lista de reposición semanal orientadas a reducir quiebres simulados en top-SKUs (hipótesis de valor), sin POS ni facturación — alcance de curso, no sustituto comercial de suite |
| Solución | Catálogo seed, umbrales, pantalla/lista de alertas, export CSV |
| Canales | Demo académica / piloto simulado en curso |
| Flujos de ingreso | N/A en fase PoC de curso (sin monetización) |
| Estructura de costos | Tiempo de desarrollo del equipo; infraestructura mínima de demo |
| Métricas clave | Alerta ante quiebre simulado en SKUs de alta rotación; lista coherente con umbrales; reducción observable de eventos de quiebre en escenario de prueba (hipótesis; sin ROI comercial en esta fase) |
| Ventaja evaluable (PoC) | Alcance deliberadamente estrecho, demostrable y calificable en un semestre — no ventaja comercial frente a suites como Pulpos |

**Tesis de valor (inversor, soft):** una capa mínima de alertas puede convertir inventario “a ojo” en reposición anticipada y reducir quiebres en SKUs críticos **si** umbrales y lista son operables y medibles. En esta fase no hay retorno monetario ni sponsor; el camino de valor es hipótesis de ahorro/adopción anclada al MVP 1, no inversión comercial.

Pulpos monetiza una suite de gestión/POS; SMOKEVAL no compite en ese plano: usa el referente para justificar el problema y se diferencia por **no** incluir cobro, CFDI ni multi-sucursal en el MVP 1.

---

## Referencias

Pulpos. (n.d.-a). *Software de gestión para ferreterías*. https://pulpos.com/ferreterias/

Pulpos. (n.d.-b). *Punto de venta para ferreterías*. https://pulpos.com/giros/ferreterias/punto-de-venta/
