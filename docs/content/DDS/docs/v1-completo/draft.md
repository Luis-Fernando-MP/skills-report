# Informe del proyecto — DDS

| Campo | Valor |
|-------|--------|
| **Proyecto** | DDS |
| **Tema** | Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu |
| **Versión** | `v1-completo` |
| **Fecha** | 2026-09-06 |
| **Alcance de esta versión** | Informe completo según `config.alcance` = `[]` (índice `common/structure/model1.md`, contenido remapeado al dominio partes/PoC) |
| **Estilo de citación** | APA 7 |

---

## Capítulo 1: Presentación de la empresa

### 1.1. Presentación de la empresa

Este informe documenta una propuesta empresarial (PoC/MVP) dirigida a **Komatsu Ltd.** para demostrar un núcleo de gestión de **pedidos e inventario de partes/repuestos** sobre arquitectura cloud, con invariante de **reserva de stock al crear el pedido** y evolución hacia contenedores, despliegue en AWS y microservicios. El destinatario del valor es la empresa: el entregable debe ser evaluable frente a cuellos de integración y escala en operaciones de partes, en convivencia con plataformas productivas ya existentes (p. ej. sistemas de partes/WMS documentados públicamente), sin pretender su reemplazo unilateral en esta fase.

#### 1.1.1. Reseña histórica

Komatsu Ltd. se estableció el **13 de mayo de 1921**. Sus orígenes se vinculan a la actividad industrial de Komatsu Iron Works y a la visión de Meitaro Takeuchi sobre el desarrollo de la industria de maquinaria en Japón; desde temprano la compañía asoció su identidad a la idea de que la alta calidad trasciende fronteras nacionales (Komatsu, n.d.-a; Komatsu, 2025b).

A lo largo del siglo XX, Komatsu transitó de un foco industrial local a un fabricante global de equipos de construcción y minería, con presencia manufacturera y comercial en múltiples regiones. En décadas recientes ha reforzado, además del hardware, soluciones digitales y de automatización en obra y mina —por ejemplo *Smart Construction* y el *Autonomous Haulage System* (AHS)— en línea con una narrativa de socio colaborativo orientado a lugares de trabajo más seguros, productivos y limpios (Komatsu, 2025a; Komatsu, 2025b).

En el ciclo FY2025–FY2027 la compañía publica el plan estratégico de crecimiento *Driving value with ambition*, con pilares de creación de valor al cliente mediante innovación, crecimiento y rentabilidad, y transformación de la base de negocio. Ese marco sitúa la digitalización y la cadena de valor —incluidos servicios y aftermarket— como ejes de competitividad (Komatsu, 2025a). Datos corporativos públicos a 1 de abril de 2026 sitúan a Komatsu como grupo con centenares de entidades, decenas de miles de empleados consolidados y ventas netas consolidadas del orden de billones de yenes (Komatsu, n.d.-a; Komatsu, 2026).

Para este proyecto académico, la reseña histórica pública fundamenta el **contexto OEM** y la relevancia del aftermarket de partes; no sustituye un diagnóstico operativo interno de pedidos e inventario de una sede concreta.

#### 1.1.2. Misión

En fuentes corporativas, Komatsu formula su propósito como crear valor mediante fabricación e innovación tecnológica para un futuro sostenible en el que prosperen personas, negocios y el planeta (Komatsu, 2025b). El principio de gestión publicado enfatiza **Quality and Reliability** (calidad y fiabilidad) junto con la maximización del valor corporativo y la responsabilidad social (Komatsu, n.d.-a; Komatsu, 2025a). La propuesta de este informe se alinea con ese marco al buscar demostrar **confiabilidad operativa** en la promesa de stock de partes: un pedido solo se confirma si el inventario puede reservarse de forma consistente bajo concurrencia.

#### 1.1.3. Visión

En el Strategic Growth Plan FY2025–FY2027, Komatsu redefine su visión como socio colaborativo comprometido con optimizar lugares de trabajo **seguros, productivos y limpios** (Komatsu, 2025a). El PoC de pedidos e inventario no cubre automatización de obra ni Smart Construction; aporta una capa demostrable de **disponibilidad y consistencia** en la promesa de stock de partes, evaluable por áreas de IT/operaciones y compatible con la narrativa de digitalización y convivencia con sistemas existentes.

#### 1.1.4. Valores

La identidad de gestión publicada se articula en torno a calidad y fiabilidad, innovación de producto, transformación digital y expansión del negocio de cadena de valor, con compromisos públicos de sostenibilidad y descarbonización de largo plazo (Komatsu, 2025a; Komatsu, 2025b). Para el proyecto, el valor operativo más relevante es la **calidad/confiabilidad aplicada a la promesa de inventario**: el criterio de aceptación del PoC exige 0 oversell en el perímetro demostrable y rechazo limpio cuando el stock no alcanza.

### 1.2. Diagnóstico situacional

El diagnóstico combina el framing de problemática del perfil del proyecto con el análisis situacional del MVP 1 (fortalezas, debilidades, oportunidades y amenazas del movimiento propuesto). Se distingue entre hechos corporativos públicos y el diseño del PoC.

#### 1.2.1. Análisis del microentorno (fortalezas y debilidades)

**Fortalezas del PoC.** El criterio de éxito es falsable: reserva de stock al crear pedido, 0 oversell bajo concurrencia tipificada y rechazo HTTP sin mutar pedido ni inventario cuando el stock es insuficiente. El prototipo está acotado (API, seed de partes, ADR de arquitectura objetivo) sin bloquearse en EKS ni SSO empresarial. El posicionamiento declara coexistencia con plataformas de partes/WMS, no reemplazo unilateral, lo que reduce el riesgo de presentar el entregable como ERP completo.

**Debilidades del PoC.** No se dispone de observación in situ del flujo real de pedidos de partes en Komatsu; las métricas internas de la empresa no han sido aportadas. Tampoco está garantizado un sponsor de campo nombrado, ni se ha demostrado aún una ventaja comercial frente al *stack* aftermarket ya desplegado. Desde la literatura de consistencia en arquitecturas de microservicios, fragmentar el dominio pedido–inventario sin una estrategia explícita de transacciones eleva el riesgo de promesas incoherentes de stock (Bashtovyi & Fechan, 2024). El MVP 1 responde a ese riesgo con un invariante **local** de reserva antes de escalar a microservicios.

#### 1.2.2. Análisis del macroentorno (oportunidades y amenazas)

**Oportunidades.** Demostrar una capa de reserva concurrente-segura como PoC evaluable; alinear el ADR con un roadmap contenedores → AWS (MVP 2–3); y aprovechar la relevancia pública del aftermarket de partes en el grupo OEM (Komatsu, 2025a). En alta concurrencia, la literatura muestra que el overselling surge cuando la validación de cupo y la persistencia no se coordinan de forma atómica; patrones de deducción/reserva previa a completar la operación mitigan ese fallo (Zhang et al., 2025).

**Amenazas.** Percepción del PoC como silo o *shadow IT* frente a sistemas productivos; implementación ingenua *check-then-act* que genera oversell bajo carga y destruye la tesis del núcleo; y que la prioridad real de la organización sea otra (pricing, multi-almacén, EDI), de modo que el PoC no entre en agenda de evaluación. La respuesta de diseño prioriza narrativa de coexistencia, métricas del PoC (p95, tasa de error, 0 oversell) y tipificación con datos seed antes de inflar infraestructura cloud.

### 1.3. Modelo de negocio

#### 1.3.1. Lienzo Lean Canvas

El Lean Canvas organiza, en una página, los supuestos del PoC hacia Komatsu. No constituye un plan de monetización del producto.

**Problema.** (1) Los pedidos de partes pueden prometerse sin reserva atómica, con riesgo de oversell o doble asignación bajo concurrencia. (2) Los cuellos de integración/escala en atención a demanda de partes requieren una demo evaluable, no solo arquitectura en diapositivas. (3) Sin un invariante ejecutable, la propuesta cloud/microservicios no compite como evidencia frente a plataformas ya existentes. Alternativas de referencia en el entorno público incluyen sistemas de partes/NPS, WMS y prácticas manuales o fragmentadas en sitios no modelados por este PoC.

**Solución (MVP 1).** El endpoint `POST /pedidos` materializa el caso de uso `ReservarStockAlCrearPedido` (acepta con stock reservado o responde 4xx sin mutar); demo concurrente con seed de partes (p. ej. part number de stock unitario); ADR de arquitectura objetivo (microservicios + AWS) sin exigir EKS en el primer corte.

**Propuesta de valor única.** Para operadores y evaluadores de pedidos e inventario de partes en Komatsu que necesitan prometer stock sin oversell bajo demanda concurrente, el PoC Spring Boot con reserva atómica es una capa demostrable de consistencia pedido↔inventario (perímetro seed), distinta de presentaciones sin invariante, de un ERP completo o de afirmar el reemplazo de plataformas ya desplegadas.

**Segmentos.** Sponsor/evaluador Komatsu; operador de pedidos de partes; responsable de inventario/centro de partes; arquitecto de integración. Early adopters del PoC: sponsor que agenda la demo y operador que ejecuta la colección HTTP del flujo feliz y de rechazo.

**Métricas clave.** Pedido que reserva stock; stock insuficiente → 4xx sin mutar; 0 oversell bajo concurrencia tipificada; paquete de propuesta (ADR + resumen ejecutivo) comprensible para el evaluador.

**Canales.** Demo técnica y paquete de propuesta al sponsor (no marketplace).

**Estructura de costos / flujo de ingresos.** Costos en implementación Spring Boot + PostgreSQL, diseño ADR y sesiones de evaluación; ingresos no aplican en el PoC (monetización fuera de MVP 1).

**Ventaja especial.** Ninguna demostrada aún frente al *stack* productivo de Komatsu; el invariante es reproducible técnicamente en el perímetro del PoC.

---

## Capítulo 2: Planteamiento del problema

### 2.1. Descripción de la realidad problemática

En OEM de maquinaria, la disponibilidad de partes/repuestos condiciona el uptime de equipos en campo y la calidad del servicio postventa. Komatsu opera a escala global con un portafolio amplio de equipos y un aftermarket asociado (Komatsu, n.d.-a; Komatsu, 2025a). En ese contexto, la propuesta identifica como problemática operativa la tensión entre **prometer stock** ante demanda concurrente y **mantener consistencia** entre pedido e inventario cuando los procesos o sistemas no garantizan una reserva atómica en el momento de crear el pedido.

La literatura de sistemas de alta concurrencia ilustra el fallo clásico: dos solicitudes leen disponibilidad suficiente, ambas avanzan y el cupo se sobreasigna —overselling— si la deducción no es atómica respecto del ledger (Zhang et al., 2025). Trasladado al dominio de partes, el síntoma es doble promesa, cancelaciones, retrabajo y pérdida de confianza del canal. La propuesta no afirma magnitudes internas de Komatsu no aportadas; sí formula un PoC cuyos criterios de aceptación hacen falsable ese mecanismo.

### 2.2. Formulación del problema

#### 2.2.1. Problema general

¿De qué manera una arquitectura orientada a microservicios sobre infraestructura cloud permite optimizar la disponibilidad, escalabilidad y tiempo de respuesta en la gestión de pedidos e inventario de partes/repuestos para Komatsu, garantizando consistencia stock–pedido (0 oversell) bajo carga tipificada en el perímetro del PoC?

#### 2.2.2. Problemas específicos

1. ¿Cómo diseñar e implementar un caso de uso `ReservarStockAlCrearPedido` que acepte el pedido solo con reserva exitosa y rechace sin mutar cuando el stock es insuficiente?  
2. ¿Cómo demostrar 0 oversell bajo concurrencia tipificada (seed/demo) con métricas observables (éxitos 201 vs rechazos 4xx y saldos de inventario coherentes)?  
3. ¿Cómo empaquetar y desplegar el sistema (contenedores → AWS ECS/Fargate + PostgreSQL + monitoreo) midiendo p95 y tasa de error HTTP bajo umbrales de referencia del PoC?  
4. ¿Cómo documentar la arquitectura objetivo (API Gateway y hasta tres servicios acotados) sin exigir integración productiva con NPS/WMS ni EKS como bloqueante del primer entregable?

### 2.3. Justificación del proyecto

La justificación es técnica y de propuesta empresarial. Técnicamente, la consistencia pedido↔inventario bajo concurrencia es un problema conocido en sistemas distribuidos y de microservicios; basar el primer entregable en un invariante local reduce el riesgo de introducir oversell al particionar el dominio (Bashtovyi & Fechan, 2024; Zhang et al., 2025). Empresarialmente, Komatsu publica una estrategia de digitalización y cadena de valor que hace plausible evaluar un PoC de partes con métricas claras, sin confundirlo con un reemplazo de WMS/ERP (Komatsu, 2025a). Académicamente, el proyecto articula Design Thinking, Lean Canvas, FODA y RAT del MVP 1 en una secuencia de entrega demostrable (dominio → Compose/carga → cloud).

### 2.4. Objetivos

#### 2.4.1. Objetivo general

Desarrollar y demostrar un PoC de gestión de pedidos e inventario de partes/repuestos para Komatsu, con reserva de stock al crear pedido, 0 oversell bajo concurrencia en el perímetro del PoC, y camino de despliegue en contenedores y AWS, dejando documentada la arquitectura objetivo en microservicios.

#### 2.4.2. Objetivos específicos

1. Implementar el núcleo de dominio (catálogo, clientes, usuarios, pedidos, inventario) con `ReservarStockAlCrearPedido` y colección HTTP reproducible.  
2. Validar 0 oversell y rechazo sin mutar bajo escenario concurrente tipificado (seed).  
3. Empaquetar con Docker Compose y prueba de carga (umbrales locales).  
4. Desplegar en AWS (ECS/Fargate, RDS PostgreSQL, gateway/ALB, monitoreo) y medir p95/error contra umbrales cloud de referencia.  
5. Entregar ADR, diagrama de arquitectura objetivo y resumen ejecutivo para evaluación Komatsu.

### 2.5. Alcances y limitaciones del proyecto

**Alcance.** PoC/MVP secuenciado: (1) dominio + reserva de stock; (2) Compose + prueba de carga; (3) ECS/Fargate + RDS + monitoreo. Arquitectura objetivo con API Gateway y microservicios; K8s/EKS como evolución. Frontend web funcional mínimo. Autenticación de PoC (JWT/API key).

**Limitaciones / fuera de alcance en esta fase.** ERP/MRP/EDI completos; multi-almacén global; IoT de flota; reemplazo unilateral de NPS/WMS; multi-región / service mesh; integración productiva con sistemas legacy; SSO empresarial en MVP 1; afirmación de KPIs internos de Komatsu no aportados por la empresa. El 0 oversell se garantiza en el **perímetro del PoC** (datos seed/demo), no como verdad global de inventario corporativo.

---

## Capítulo 3: Marco teórico

### 3.1. Antecedentes de la investigación

Como antecedentes técnicos del PoC se consideran: (a) trabajos sobre prevención de overselling en sistemas de alta concurrencia basados en microservicios, que formalizan la carrera entre lectura de disponibilidad y persistencia (Zhang et al., 2025); y (b) marcos de decisión sobre transacciones distribuidas al migrar de monolitos a microservicios, relevantes para no fragmentar prematuramente el invariante pedido–stock (Bashtovyi & Fechan, 2024). En el plano corporativo, la documentación pública de Komatsu sobre perfil, estrategia FY2025–FY2027 e informes financieros contextualiza el dominio OEM/aftermarket (Komatsu, n.d.-a; Komatsu, 2025a; Komatsu, 2026).

### 3.2. Bases teóricas

#### 3.2.1. Aftermarket OEM y cadena de suministro de partes

En fabricantes de maquinaria, el aftermarket de partes sostiene la continuidad operativa de la flota instalada. Komatsu describe un portafolio de construcción, minería y soluciones digitales, e incorpora la cadena de valor y servicios en su plan de crecimiento (Komatsu, n.d.-a; Komatsu, 2025a). Para el informe, este marco sitúa el problema de **promesa de disponibilidad** de partes como problema de servicio y competitividad, distinto de la mera manufactura del equipo nuevo. TODO: citar — marco académico de gestión de inventarios de spare parts / aftermarket OEM (fill rate, demanda intermitente).

#### 3.2.2. Digitalización de inventario y gestión de stock

La digitalización del inventario busca una fuente consultable de saldos (on-hand, reservado, disponible) y reglas de actualización ante movimientos. En el PoC, el modelo mínimo asocia a cada part number cantidades coherentes bajo la invariante `disponible = onHand − reservado` (o equivalente). La literatura de overselling muestra que digitalizar el saldo no basta: sin actualización atómica condicional, dos flujos concurrentes pueden sobreasignar el mismo cupo (Zhang et al., 2025).

#### 3.2.3. Catálogo de partes y consistencia pedido↔stock

El catálogo (part numbers, atributos mínimos) es el maestro que enlaza líneas de pedido con filas de inventario. La consistencia pedido↔stock exige que un pedido confirmado corresponda a una reserva efectiva, y que un rechazo no deje efectos parciales. En arquitecturas de microservicios, decidir si esa consistencia se resuelve en una transacción local o con patrones distribuidos (saga, outbox, etc.) es una decisión de diseño con trade-offs de complejidad y rendimiento (Bashtovyi & Fechan, 2024). El MVP 1 prioriza la transacción local del caso de uso de reserva.

#### 3.2.4. Transacciones, microservicios y camino cloud

Bashtovyi y Fechan (2024) discuten estrategias informadas para transacciones distribuidas en microservicios, subrayando que la descomposición prematura del dominio puede encarecer la consistencia. Zhang et al. (2025) ilustran, en otro dominio (venta de tickets), un mecanismo de cupo atómico previo a completar la operación para impedir overselling. El PoC adopta la lección del **mecanismo** (reserva/deducción atómica) y la lección de **no repartir** Order/Inventory en el primer entregable, dejando microservicios + AWS como arquitectura objetivo documentada en ADR, con contenedores y ECS/Fargate en la secuencia de MVPs.

### 3.3. Marco conceptual (glosario de términos)

| Término | Definición operativa en este proyecto |
|---------|----------------------------------------|
| **PoC / MVP** | Entregable demostrable y acotado para evaluación Komatsu, no sistema productivo completo. |
| **Reserva de stock** | Compromiso atómico de cantidad de un part number al crear el pedido. |
| **0 oversell** | Bajo concurrencia tipificada, el stock nunca se asigna por encima de lo disponible; a lo sumo un ganador por unidad en conflicto. |
| **Perímetro del PoC** | Datos seed/demo y servicios del PoC; no inventario global corporativo. |
| **Part number** | Identificador de catálogo de una parte/repuesto en el seed. |
| **ADR** | Architecture Decision Record de la arquitectura objetivo (microservicios + AWS). |
| **NPS / WMS** | Plataformas de partes/almacén referidas públicamente; fuera de reemplazo en esta fase. |
| **p95** | Percentil 95 de latencia de `POST /pedidos` bajo carga tipificada. |

---

## Capítulo 4: Metodología

### 4.1. Tipo y diseño de la investigación

El trabajo se enmarca como **investigación aplicada / desarrollo tecnológico** con enfoque de propuesta empresarial: se diseña, implementa y valida un PoC medible. El diseño combina análisis documental (fuentes públicas Komatsu y literatura técnica) con construcción iterativa del software y pruebas de aceptación definidas en el perfil (concurrencia, latencia, error).

### 4.2. Metodología de desarrollo de software

Se adopta un enfoque incremental alineado a los tres MVP del perfil: núcleo de dominio → empaquetado y carga → cloud. El descubrimiento de problema–solución del MVP 1 se apoyó en Design Thinking (empatizar–definir–idear–prototipar–evaluar) y en Lean Canvas para comunicar la propuesta de valor. La priorización de supuestos riesgosos se formalizó en un mapa RAT (p. ej. demostración de 0 oversell, narrativa de coexistencia). La implementación prevista usa Spring Boot modular, PostgreSQL y, en fases posteriores, Docker y AWS ECS/Fargate.

### 4.3. Técnicas e instrumentos de recolección de datos

| Técnica | Instrumento | Uso |
|---------|-------------|-----|
| Revisión documental | Ficha `company.md`, IR/estrategia Komatsu, papers OA | Contexto empresa y bases teóricas |
| Prototipado | Contrato API + seed + colección HTTP | Demostración del flujo pedido→reserva |
| Prueba concurrente | Script de hilos / k6 sobre stock unitario | Falsar 0 oversell (criterio R2 del MVP) |
| Prueba de carga | k6 + umbrales p95/error | MVP 2–3 |
| Entrevista/demo con evaluador | Sesión muda + checklist de alcance | Evaluación de usabilidad de la demo y coexistencia |

### 4.4. Población y muestra (si aplica)

No se realiza muestreo estadístico de población humana. La “muestra” técnica del PoC es el **seed de partes** (p. ej. `KT-FILTER-001`, `KT-SEAL-014` con `onHand=1`, `KT-PUMP-220` en cero, etc.) y los escenarios de concurrencia/carga tipificados. Cualquier subset anonimizado aportado por Komatsu quedaría fuera del diseño actual hasta acuerdo explícito.

---

## Capítulo 5: Desarrollo de la propuesta (MVP)

### 5.1. Análisis de requerimientos

#### 5.1.1. Requerimientos funcionales

1. Gestionar catálogo mínimo de partes (alta/consulta).  
2. Gestionar clientes y usuarios de PoC.  
3. Crear pedido (`POST /pedidos`) que **reserve stock** en todas las líneas o falle sin efectos parciales.  
4. Consultar pedido e inventario (`disponible`, `reservado`, `onHand`).  
5. Rechazar con 4xx cuando el stock es insuficiente.  
6. Exponer colección HTTP reproducible del flujo feliz y de rechazo.  
7. Documentar ADR de arquitectura objetivo (microservicios + AWS).

#### 5.1.2. Requerimientos no funcionales

1. **Consistencia:** 0 oversell bajo concurrencia tipificada en perímetro PoC.  
2. **Desempeño (referencia):** local p95 &lt; 500 ms y failed &lt; 1 %; cloud p95 &lt; 1200 ms y failed &lt; 2 % (ajustables con Komatsu).  
3. **Seguridad PoC:** JWT o API key; sin SSO enterprise en MVP 1.  
4. **Desplegabilidad:** contenedorización y ruta a ECS/Fargate + RDS.  
5. **Observabilidad:** métricas básicas en cloud (CloudWatch y/o Prometheus/Grafana).  
6. **Alcance ético-técnico:** no sustituir NPS/WMS sin acuerdo.

### 5.2. Diseño de la solución

#### 5.2.1. Arquitectura del sistema

**MVP 1:** monolito modular Spring Boot + PostgreSQL. El caso de uso `ReservarStockAlCrearPedido` concentra la transacción de dominio. **Arquitectura objetivo:** API Gateway y hasta tres servicios acotados (p. ej. pedidos, inventario, catálogo), despliegue en AWS (ECR, ECS/Fargate, RDS), con K8s/EKS como evolución. La decisión de mantener la reserva en una unidad transaccional local en el primer corte sigue la lógica de no introducir transacciones distribuidas prematuras (Bashtovyi & Fechan, 2024). El mecanismo anti-oversell se inspira en la necesidad de coordinación atómica del cupo bajo concurrencia (Zhang et al., 2025), implementable vía actualización condicional / bloqueo de fila en PostgreSQL dentro del PoC.

#### 5.2.2. Modelo de datos

Entidades mínimas: `Parte` (partNumber, atributos), `Cliente`, `Usuario`, `Pedido` / `LineaPedido`, `Inventario` (onHand, reservado). Invariante: no permitir `reservado &gt; onHand`. El seed tipifica casos feliz, concurrencia y rechazo inmediato.

#### 5.2.3. Diseño de interfaz (mockups/wireframes)

La interfaz primaria del MVP 1 es la **colección HTTP** (cliente API). Un frontend web mínimo puede exponerse en fases posteriores; no es el núcleo de aceptación del invariante. La demo muda exige que un operador complete el flujo 201 y el 4xx sin explicación extendida del equipo.

### 5.3. Implementación del MVP

#### 5.3.1. Módulo de inventario digital

Persiste saldos por part number; expone consulta de disponibilidad; aplica incrementos de `reservado` (o decrementos de `disponible`) solo dentro de la transacción de creación de pedido. Es el ancla del 0 oversell.

#### 5.3.2. Módulo de pedidos y reserva atómica

Implementa `ReservarStockAlCrearPedido`: valida catálogo y cliente; por cada línea verifica disponibilidad bajo control de concurrencia; si alguna falla → rollback total y 4xx; si todas OK → crea pedido y confirma reservas → 201. Este módulo sustituye, en el índice genérico del modelo, cualquier bloque ajeno al dominio (p. ej. “fichas de tallaje”).

### 5.4. Pruebas y validación

#### 5.4.1. Plan de pruebas

| ID | Escenario | Umbral |
|----|-----------|--------|
| T1 | Camino feliz multi-línea | 201; saldos coherentes |
| T2 | Stock insuficiente | 4xx; sin pedido ni cambio de stock |
| T3 | Concurrencia stock=1 (≥20 hilos/k6) | Exactamente un 201; resto 4xx; 0 oversell |
| T4 | Auth PoC | Rechazo sin credencial válida |
| T5 | Carga local (MVP 2) | p95 y failed según umbral local |
| T6 | Carga cloud (MVP 3) | p95 y failed según umbral cloud |

#### 5.4.2. Resultados de pruebas

A la fecha de este draft, el plan de pruebas y los umbrales están **definidos como criterios de aceptación del PoC**. La ejecución de T3 (0 oversell) constituye el núcleo de credibilidad del MVP 1; T5–T6 corresponden a MVP 2–3. Los resultados numéricos de corridas se incorporarán en versiones posteriores del informe conforme se ejecuten los scripts.

---

## Capítulo 6: Resultados y análisis

### 6.1. Presentación de resultados

Los resultados consolidados de esta versión corresponden a **artefactos de diseño y criterios de aceptación**:

1. Perfil de propuesta y ficha pública de Komatsu.  
2. Pack MVP 1: Design Thinking, Lean Canvas, FODA/TOWS, RAT, flujos AS-IS/TO-BE del dominio.  
3. Contrato API y flujo `ReservarStockAlCrearPedido`.  
4. Corpus bibliográfico OA anclado a oversell concurrente y transacciones en microservicios (Zhang et al., 2025; Bashtovyi & Fechan, 2024).  
5. Secuencia de MVPs y umbrales p95/error/0 oversell.

### 6.2. Análisis e interpretación de resultados

El diseño prioriza el **riesgo técnico del invariante** antes que la infraestructura cloud: sin 0 oversell demostrable, el despliegue en ECS no aporta credibilidad. El Lean Canvas muestra que la ventaja especial frente al *stack* Komatsu aún no está demostrada; el valor inmediato es una demo falsable y una narrativa de coexistencia. El FODA advierte el riesgo de sombra frente a NPS/WMS y responde anclando el alcance a “capa demostrable”, no a reemplazo.

### 6.3. Discusión (contraste con antecedentes/marco teórico)

Zhang et al. (2025) confirman que el overselling es un fallo de coordinación bajo concurrencia y que la deducción atómica de cupo es una respuesta viable; el PoC traslada ese principio al dominio de partes vía reserva en PostgreSQL, sin imponer Redis ni el dominio de tickets. Bashtovyi y Fechan (2024) respaldan mantener la consistencia pedido–stock en una frontera transaccional clara en el primer entregable. El contraste con la estrategia pública de Komatsu (Komatsu, 2025a) sitúa el PoC como contribución evaluable a la digitalización de cadena de valor, no como auditoría de plantas ni de WMS regionales.

---

## Capítulo 7: Conclusiones y recomendaciones

### 7.1. Conclusiones

1. Komatsu, como OEM global con aftermarket relevante, constituye un destinatario coherente para un PoC de pedidos e inventario de partes con métricas de consistencia y desempeño.  
2. El problema central del proyecto es la **consistencia de la promesa de stock bajo concurrencia**, abordable con reserva atómica al crear pedido.  
3. El MVP 1 concentra el valor en dominio + invariante + narrativa de coexistencia; contenedores y AWS vienen después.  
4. La literatura OA seleccionada sostiene el mecanismo anti-oversell y la prudencia ante transacciones distribuidas prematuras.  
5. El perímetro del PoC (seed) delimita honestamente lo que se demuestra frente a lo que sería integración productiva.

### 7.2. Recomendaciones

1. Ejecutar de inmediato la prueba concurrente de stock unitario y archivar evidencia (logs + query) para terceros.  
2. Acordar por escrito con el evaluador Komatsu el framing de coexistencia (no reemplazo NPS/WMS) antes de MVP 3.  
3. No introducir EKS, SSO ni sync WMS como bloqueantes del núcleo.  
4. Mantener el ADR actualizado al cortar servicios en la arquitectura objetivo.  
5. Ampliar bibliografía de spare parts/aftermarket cuando se profundice el Cap. 3.2.1.

### 7.3. Trabajos futuros

MVP 2 (Compose + k6), MVP 3 (ECS/Fargate + RDS + monitoreo + k6 cloud), extracción a microservicios según ADR, frontend mínimo, y —solo con acuerdo— interfaces de integración documentadas hacia sistemas productivos. Evolución a EKS/service mesh queda fuera del horizonte inmediato.

---

## Referencias bibliográficas

Bashtovyi, A., & Fechan, A. (2024). Distributed transactions in microservice architecture: Informed decision-making strategies. *Information Systems and Networks*, (15), 449–459. https://doi.org/10.23939/sisn2024.15.449

Komatsu. (n.d.-a). *Company info*. Komatsu Ltd. https://www.komatsu.jp/en/aboutus/profile

Komatsu. (2025a). *Strategic Growth Plan* [PDF]. https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_strategy.pdf

Komatsu. (2025b). *Komatsu Report 2025 — Introduction* [PDF]. https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_introduction.pdf

Komatsu. (2026). *Financial results* [PDF]. https://www.komatsu.jp/en/-/media/home/ir/library/financial/en/2603q4_e.pdf

Zhang, Z., Zhang, X., & Li, X. (2025). Securing high-concurrency ticket sales: A framework based on microservice. *arXiv*. https://doi.org/10.48550/arXiv.2512.24941

---

## Anexos

### Anexo A: Matriz de consistencia

| Problema | Objetivo | MVP / entregable | Criterio |
|----------|----------|------------------|----------|
| Oversell / doble promesa | Reserva atómica | MVP 1 `ReservarStockAlCrearPedido` | 0 oversell; 4xx sin mutar |
| Falta de demo evaluable | PoC medible | Colección HTTP + seed | Flujos 201/4xx |
| Escalabilidad cloud | Despliegue AWS | MVP 2–3 | p95/error umbrales |
| Arquitectura objetivo | Microservicios | ADR | Gateway ≤3 servicios |

### Anexo B: Instrumentos de recolección de datos

Checklist de demo muda; protocolo de carrera concurrente (stock=1); umbrales k6 (MVP 2–3).

### Anexo C: Manual de usuario del sistema

Pendiente de la colección HTTP estable (rutas `POST /pedidos`, `GET /inventario/{partNumber}`, etc.).

### Anexo D: Diagramas técnicos

Ver artefactos MVP 1 (diagrama de dominio, flujo Lean del feature, AS-IS/TO-BE en `mvp/mvp-1-nucleo-de-propuesta-pedidos-e-inventario-correctos/`).

### Anexo E: Evidencias / actas con la empresa

Se incorporarán conforme existan actas de evaluación con sponsor Komatsu.
