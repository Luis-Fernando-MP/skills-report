# Informe del proyecto — DS

| Campo | Valor |
|-------|--------|
| **Proyecto** | DS |
| **Tema** | Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu |
| **Versión** | `v1-capitulo-1` |
| **Fecha** | 2026-09-05 |
| **Alcance de esta versión** | Capítulo 1 (completo) según `config.alcance` |
| **Estilo de citación** | APA 7 |

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

El presente informe documenta una **propuesta empresarial (PoC/MVP)** dirigida a **Komatsu**, orientada a demostrar un núcleo de gestión de pedidos e inventario de partes/repuestos sobre arquitectura cloud, con invariante de reserva de stock al crear pedido y camino de evolución hacia contenedores, AWS y microservicios. El destinatario del valor es la empresa; el entregable debe ser evaluable frente a cuellos de integración y escala en operaciones de partes, sin afirmar el reemplazo unilateral de plataformas productivas ya existentes (p. ej. NPS/WMS), salvo acuerdo explícito con la organización.

#### 1.1.1. Reseña histórica

Komatsu es un fabricante global de maquinaria de construcción, minería y equipos relacionados, con más de un siglo de trayectoria industrial. La compañía articula su identidad corporativa en torno a la innovación en manufactura y tecnología como eje histórico de creación de valor (Komatsu, n.d.). En el marco de esta propuesta no se reconstruye la historia operativa interna de pedidos e inventario de partes de una sede o país concreto: ese AS-IS permanece como **hipótesis a validar con sponsor** y no se inventan KPIs ni procedimientos no aportados por la empresa.

#### 1.1.2. Misión

En fuentes corporativas públicas, Komatsu formula su *purpose* como crear valor mediante manufactura e innovación tecnológica para empoderar un futuro sostenible en el que personas, negocios y el planeta prosperen juntos (Komatsu, n.d.). El principio de gestión asociado enfatiza maximizar la confianza de los *stakeholders* mediante compromiso con calidad y confiabilidad (Komatsu, n.d.). Esta propuesta se alinea con ese marco en la medida en que busca demostrar **confiabilidad operativa** (consistencia pedido↔stock, 0 oversell) en un dominio de partes/repuestos, sin confundir el PoC con un programa de sostenibilidad corporativa.

#### 1.1.3. Visión

En el plan de crecimiento estratégico FY2025–FY2027, Komatsu redefine su visión como convertirse en un *partner* colaborativo comprometido con optimizar lugares de trabajo seguros, productivos y limpios (Komatsu, 2025). El PoC de pedidos e inventario no pretende cubrir automatización de obra o Smart Construction; sí busca aportar una capa demostrable de **disponibilidad y consistencia** en la promesa de stock de partes, evaluable por IT/ops y compatible con la narrativa de digitalización y convivencia con sistemas existentes.

#### 1.1.4. Valores

Komatsu publica valores corporativos (ambición, perseverancia, colaboración y autenticidad) y principios fundacionales de expansión global, calidad primero, innovación tecnológica y desarrollo de personas (Komatsu, n.d.; Komatsu, 2025). Para el proyecto, el valor operativo más relevante es la **calidad/confiabilidad** aplicada a la promesa de inventario: un pedido no debe confirmarse si el stock no puede reservarse de forma consistente bajo concurrencia. Ese criterio es falsable en el MVP 1 y constituye el núcleo de credibilidad de la propuesta.

### 1.2. Diagnóstico situacional

El diagnóstico que sigue combina (a) el framing de problemática propuesto en el perfil del proyecto —aún por priorizar con Komatsu— y (b) el análisis FODA del MVP 1 documentado en los artefactos del proyecto. No se afirma como auditoría interna certificada de Komatsu.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas (del PoC / capacidad de entrega):** el criterio de éxito es falsable (reserva al crear pedido, 0 oversell, rechazo sin mutar stock ni pedido); el prototipo está acotado (API + seed + ADR) sin bloquearse en EKS ni SSO enterprise; y el posicionamiento declara coexistencia con NPS/WMS, no reemplazo unilateral. Esas fortalezas permiten abrir una evaluación técnica sin pretender un ERP completo.

**Debilidades:** el AS-IS interno de Komatsu (cómo se traban hoy los pedidos de partes, con qué herramientas y con qué métricas) **no ha sido observado in situ**; el dolor operativo sigue siendo hipótesis. Tampoco está garantizado el acceso a un sponsor de campo, ni se ha demostrado aún una ventaja especial frente al *stack* aftermarket ya desplegado. En consecuencia, el diagnóstico micro debe tratarse como **propuesta de trabajo**, no como hallazgos de campo cerrados.

Desde la literatura de consistencia en arquitecturas distribuidas, la fragmentación de servicios sin una estrategia explícita de transacciones/consistencia eleva el riesgo de promesas incoherentes de inventario cuando el dominio se descompone (Bashtovyi & Fechan, 2024). El MVP 1 responde a ese riesgo con un invariante local de reserva antes de escalar a microservicios.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades:** demostrar una capa de reserva concurrente-segura como PoC evaluable; alinear el ADR con un roadmap contenedores → AWS (MVP 2–3); y aprovechar la relevancia pública del dominio de partes/aftermarket en el grupo OEM. Patrones como Saga/CQRS documentan técnicas para gestionar consistencia eventual cuando el dominio se distribuye (Ghanta, 2018); el PoC los deja como referencia de evolución, no como obligación del primer entregable modular.

**Amenazas:** percepción del PoC como silo o *shadow IT* frente a NPS/WMS; implementación ingenua *check-then-act* que genera oversell bajo carga y destruye la tesis del núcleo; y que la prioridad real de Komatsu sea otra (pricing, multi-almacén, EDI), de modo que el PoC no entre en agenda. La estrategia TOWS del proyecto prioriza anclar la narrativa en coexistencia + métricas (p95, error, 0 oversell) y un protocolo de observación con sponsor antes de inflar infraestructura.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El Lean Canvas se utiliza aquí como mapa de una página para comunicar supuestos riesgosos del PoC hacia Komatsu, no como plan de monetización del producto. En la literatura de ingeniería de software, el Lean Canvas se describe como una adaptación del *Business Model Canvas* orientada a necesidades *lean startup*, con una parte de producto (problema–solución, métricas clave, costos) y una parte de mercado (ventaja injusta, canales, clientes, ingresos), unidas por la propuesta de valor (Ros et al., 2022).

**Problema (hipótesis):** (1) pedidos de partes pueden prometerse sin reserva atómica, con riesgo de oversell bajo concurrencia; (2) el dolor de integración/escala aún no está priorizado ni medido con sponsor; (3) sin demo ejecutable, la propuesta cloud/microservicios no es evaluable frente a plataformas ya existentes. Alternativas públicas de referencia incluyen NPS/Infor Nexus, WMS y prácticas manuales no observadas (`pendiente_campo`).

**Solución (MVP 1):** `POST /pedidos` materializa `ReservarStockAlCrearPedido` (acepta con stock o responde 4xx sin mutar); demo concurrente con seed de partes; ADR de arquitectura objetivo (microservicios + AWS) sin exigir EKS en el primer corte.

**Propuesta de valor única:** para operadores y evaluadores de pedidos/inventario de partes en Komatsu que necesitan prometer stock sin oversell bajo demanda concurrente, el PoC Spring Boot con reserva atómica es una capa demostrable de consistencia pedido↔inventario, distinta de diapositivas sin invariante, de un ERP completo o de afirmar el reemplazo de plataformas ya desplegadas.

**Segmentos:** sponsor/evaluador Komatsu; operador de pedidos de partes; responsable de inventario/centro de partes; arquitecto de integración. *Early adopters* hipotéticos: sponsor que agenda demo y operador que ejecuta la colección HTTP sin explicación extendida del prototipo (`pendiente_campo`).

**Métricas clave:** pedido reserva stock; stock insuficiente → 4xx sin mutar; 0 oversell bajo concurrencia tipificada; narrativa de propuesta (ADR + resumen ejecutivo) aceptable para el sponsor.

**Canales:** demo técnica + paquete de propuesta al sponsor (no marketplace).

**Estructura de costos / ingresos:** costo principal en implementación Spring Boot + PostgreSQL, diseño ADR y sesiones con sponsor; ingresos N/A en el PoC (monetización fuera de MVP 1).

**Ventaja especial:** ninguna demostrada aún frente al *stack* Komatsu; el invariante es reproducible técnicamente, pero la ventaja comercial permanece hipótesis.

---

## Referencias bibliográficas

Bashtovyi, A., & Fechan, A. (2024). Distributed transactions in microservice architecture: Informed decision-making strategies. *Information Systems and Networks*, (15), 449–459. https://doi.org/10.23939/sisn2024.15.449

Ghanta, S. (2018). SAGA and CQRS implementation techniques for distributed transaction management. *Journal of Artificial Intelligence, Machine Learning and Data Science, 1*(1), 3203–3208. https://doi.org/10.51219/jaimld/sriram-ghanta/650

Komatsu. (n.d.). *Corporate identity*. Komatsu Global Site. https://www.komatsu.jp/en/aboutus/corporate-identity

Komatsu. (2025). *Komatsu Report 2025* (introduction / corporate identity excerpts). https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_introduction.pdf

Ros, R., Bjarnason, E., & Runeson, P. (2022). A theory of factors affecting continuous experimentation (FACE). *arXiv*. https://doi.org/10.48550/arXiv.2210.05192
