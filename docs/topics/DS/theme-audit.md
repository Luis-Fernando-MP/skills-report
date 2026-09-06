# Auditoría de tema — DS

## CONTEXTO
- dominio: Gestión de pedidos e inventario
- pais_region: Global (origen Japón)
- fase_entregable: PoC/MVP
- restricciones: Convivencia con plataformas existentes fuera del alcance inicial
- modo: una_alternativa
- tipo_sujeto: empresa
- empresa: Komatsu

## Tema propuesto (entrada)
**Tema:** Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu
**Descripción:** Propuesta empresarial (PoC/MVP) dirigida a Komatsu para gestionar clientes, catálogo de partes, pedidos, inventario y usuarios sobre arquitectura cloud. Camino de entrega: dominio con reserva de stock al crear pedido → contenedores (Docker) → despliegue en AWS (ECS/Fargate + PostgreSQL + monitoreo) → extracción a microservicios (API Gateway, hasta 3 servicios acotados) como arquitectura objetivo. El entregable es un sistema demostrable y desplegable que Komatsu pueda evaluar frente a cuellos de integración/escala en pedidos e inventario; la convivencia o integración con plataformas ya existentes (p. ej. NPS/WMS documentados públicamente) queda fuera de esta fase salvo acuerdo explícito.
**Problema identificado:** La falta de integración y escalabilidad en la gestión manual o centralizada de pedidos e inventario genera cuellos de botella en la atención a clientes, riesgo de desabastecimiento e ineficiencia operacional ante picos imprevistos de demanda. Pregunta de diseño: ¿de qué manera una arquitectura orientada a microservicios sobre infraestructura cloud permite optimizar la disponibilidad, escalabilidad y tiempo de respuesta en la gestión de pedidos e inventario de partes/repuestos para Komatsu?
**Alcance:** PoC/MVP para Komatsu, secuenciado: (1) dominio + reserva de stock; (2) Compose + prueba de carga; (3) ECS/Fargate + RDS + monitoreo. Arquitectura objetivo con API Gateway y microservicios; K8s/EKS como evolución. Frontend web funcional mínimo. Auth de PoC.

## Ficha de empresa (investigación)
**Identidad:** Komatsu Ltd.
**Razón social / marca:** Komatsu Ltd.
**País / sede pública:** Japón (Oficina principal: Shiodome Building, 1-2-20, Kaigan, Minato-ku, Tokio 105-8316, Japón)
**Sector:** Fabricación y venta de maquinaria de construcción, minería, utilidades, forestal e industrial.
**Escala (pública):** Global, con 211 subsidiarias consolidadas y 67,279 empleados consolidados (a 1 de abril de 2026). Ventas netas consolidadas: 4,132.8 mil millones de yenes.
**Reseña histórica (pública):** Fundada el 13 de mayo de 1921 por Meitaro Takeuchi como Komatsu Iron Works. Se expandió globalmente y en 2025 lanzó un plan de crecimiento estratégico a tres años, "Driving value with ambition".
**Misión / visión / valores:** Ser un socio colaborativo comprometido con la optimización de lugares de trabajo seguros, productivos y limpios a través de la fabricación innovadora, la transformación digital y soluciones de energía sostenibles. Su propósito es crear valor a través de la innovación en fabricación y tecnología para empoderar un futuro sostenible.
**Principios / identidad de gestión (si publicados):** Principio de gestión de compromiso con la calidad y fiabilidad, maximización del valor corporativo, y responsabilidad social corporativa.
**Oferta / sector relevante:** Maquinaria de construcción y minería, sistemas de acarreo autónomos (AHS), plataformas digitales de construcción inteligente (Smart Construction), y maquinaria industrial especializada. Con un enfoque en la sostenibilidad y la reducción de emisiones de CO2.
**Evidencia_empresa:** suficiente
**Fuentes de empresa:**
- https://www.komatsu.jp/en/aboutus/profile
- https://www.komatsu.jp/en/-/media/home/ir/library/financial/en/2603q4_e.pdf
- https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_strategy.pdf
- https://www.plantmachineryvehicles.com/power-lists/pmv-power-list/manufacturers-power-list-2025
- https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_introduction.pdf

## Benchmarking
**Casos (directo|proxy):** Komatsu ya utiliza soluciones digitales como Smart Construction y AHS. El benchmark debe considerar la integración con sus sistemas existentes y cómo un PoC de microservicios se alinea o mejora sus infraestructuras actuales de gestión de operaciones.
**Qué adaptar:** El PoC debe demostrar un valor claro y medible en la eficiencia de pedidos e inventario, complementando o mejorando los sistemas de Komatsu sin reemplazarlos de forma unilateral. El enfoque en 0 oversell y métricas de rendimiento es clave.
**Diferenciador posible:** La propuesta de microservicios y contenedores en AWS ofrece escalabilidad y flexibilidad que podría ser un diferenciador frente a sistemas monolíticos o menos ágiles que Komatsu pueda tener. La reserva de stock al crear pedido es un diferenciador funcional crucial.
**Evidencia:** suficiente

## Tema afinado (pre-polish)
**Tema:** Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores en AWS para Komatsu, enfocado en la resiliencia y el "0 oversell".
**Descripción:** Desarrollo de un PoC/MVP para Komatsu, que aborda la gestión de clientes, catálogo, pedidos e inventario con una arquitectura de microservicios desplegada en AWS (ECS/Fargate, PostgreSQL, monitoreo). El objetivo es demostrar la optimización de la disponibilidad, escalabilidad y tiempo de respuesta en la gestión de pedidos, con un mecanismo de reserva de stock para garantizar cero oversell.
**Problema identificado:** Cuellos de botella en la atención al cliente, riesgo de desabastecimiento e ineficiencia operacional debido a la falta de integración y escalabilidad en los sistemas actuales de gestión de pedidos e inventario de Komatsu, exacerbados por picos de demanda.
**Alcance:** PoC/MVP para Komatsu, abarcando el dominio de gestión de pedidos con reserva de stock, empaquetado en Docker, pruebas de carga, y despliegue en AWS. Arquitectura objetivo microservicios. Excluye ERP/MRP/EDI completos, multi-almacén global, IoT de flota, y reemplazo de NPS/WMS existentes sin acuerdo.

## Fuentes
- Web search realizada el 2026-09-06.
