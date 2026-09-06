# Auditoría de tema — DS

## CONTEXTO
- dominio: sistemas de información / arquitectura cloud — gestión de pedidos e inventario con microservicios, contenedores y despliegue AWS
- pais_region: no fijada por el usuario; evidencia pública de Komatsu es global (no LatAm específica en fuentes usadas)
- fase_entregable: mvp
- tipo_entrega: **propuesta empresarial / PoC para Komatsu** (no proyecto solo estudiantil; el destinatario del valor es la empresa)
- restricciones: MVP software básico (CRUD: clientes, productos, pedidos, inventario, usuarios); prioridad en arquitectura microservicios + contenedores + AWS; stack propuesto Java/Spring Boot, REST, Docker, Kubernetes (evolución), PostgreSQL, frontend HTML/CSS/JS, Prometheus/Grafana; no ERP enterprise completo; no inventar hechos internos de Komatsu no aportados por el usuario
- modo: una_alternativa
- empresa: Komatsu (**cliente / destinatario de la propuesta**)

## Tema propuesto (entrada)
**Tema:** Sistema de Gestión de Inventario y Pedidos Basado en Microservicios y Contenedores para Komatsu

**Descripción:** Sistema web empresarial basado en servicios cloud para la gestión de pedidos e inventario. Módulos: clientes, productos, pedidos, inventario y usuarios. Arquitectura propuesta: Frontend Web/App → API Gateway → microservicios (Clientes, Productos, Pedidos) → base de datos cloud → monitoreo/métricas. Enfoque: demostrar infraestructura cloud (IaaS/PaaS, virtualización, contenedores, orquestación, redes, almacenamiento, BD cloud, monitoreo, escalabilidad y tolerancia a fallos) con un MVP funcional sencillo.

**Problema identificado:** La falta de integración y escalabilidad en la gestión manual o centralizada de pedidos e inventario en Komatsu genera cuellos de botella en la atención a clientes, riesgo de desabastecimiento e ineficiencia operacional ante picos imprevistos de demanda.

**Alcance:** MVP / PoC de propuesta para Komatsu: software básico + arquitectura microservicios contenedorizada desplegada en AWS para resolver la problemática de pedidos e inventario. No es requisito implementar desde el día 1 Kubernetes completo, multi-región ni un ERP.

## Benchmarking
**Casos (directo|proxy):**
1. **Komatsu — New Parts System (NPS) sobre Infor Nexus** — refresco global del supply chain de piezas de mantenimiento: visibilidad del estado de partes, menos silos/batch, plataforma cloud SaaS — https://dcross.impress.co.jp/docs/usecase/001098.html — (**directo**)
2. **Komatsu Ltd. + LOGISTEED ONEsLOGI / WMS** — WMS y picking digital en centros de partes (multi-país): entrada/salida de partes, paperless — https://sol.logisteed.com/en/case/voice/komatsu.html — (**directo**)
3. **AWS Guidance — Order & Inventory Management (QSR)** — arquitectura de referencia order+inventory en AWS (contenedores ECS/Fargate, sincronización, escalado) — https://aws.amazon.com/solutions/guidance/implementing-order-and-inventory-management-for-quick-service-restaurants-on-aws/ — (**proxy**)
4. **AWS Architecture Blog — ECS + API Gateway** — patrón API Gateway → VPC Link → APIs en ECS; encaja con Frontend → Gateway → microservicios — https://aws.amazon.com/blogs/architecture/field-notes-serverless-container-based-apis-with-amazon-ecs-and-amazon-api-gateway/ — (**proxy**)
5. **Sparity — microservicios para service supply chain / spare parts** — inventario de partes, órdenes, APIs REST en AWS — https://www.sparity.com/case-studies/microservices-platform-for-service-supply-chain-transformation/ — (**proxy**)

**Qué adaptar:** acotar el dominio a **pedidos e inventario de partes/repuestos** (alineado a evidencia pública de Komatsu), sin reclamar paridad con NPS/WMS; una fuente de verdad por entidad vía API Gateway y contratos REST; movimientos de stock ligados a pedidos; despliegue AWS con API Gateway + contenedores (ECS/Fargate primero) + RDS PostgreSQL; K8s/EKS y tolerancia avanzada como evolución/demo de curso, no bloqueante del MVP; criterios medibles de disponibilidad/latencia/escala bajo carga simulada.

**Diferenciador posible:**
1. MVP didáctico de arquitectura cloud (microservicios acotados + Docker + AWS + métricas), no producto enterprise.
2. Dominio “partes/repuestos” con reserva simple de stock al crear pedido (consistencia documentada).
3. Camino de madurez IaaS → contenedores → orquestación (VM/demo → Docker → ECS; EKS opcional) para cubrir temas del curso sin inflar alcance funcional.

**Evidencia:** suficiente (4/5 búsquedas)

## Tema afinado (pre-polish)
*(Ajustes mínimos tras benchmark; sin inventar hechos internos. Se acota el objeto a partes/repuestos. Destinatario = Komatsu como propuesta/PoC. El problema operativo se formula como **propuesta a validar con la empresa**, no como auditoría interna ya verificada. Evidencia pública (NPS/WMS) se trata como contexto de industria, no como rechazo de la propuesta.)*

**Tema:** Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu

**Descripción:** Propuesta / PoC empresarial de sistema web sobre servicios cloud para que Komatsu gestione clientes, productos (partes), pedidos, inventario y usuarios. Arquitectura objetivo: Frontend → API Gateway → microservicios Spring Boot contenedorizados → PostgreSQL en la nube → monitoreo. El valor es demostrar y entregar un camino de arquitectura cloud (disponibilidad, escalabilidad, tiempo de respuesta) desplegable en AWS, posicionado frente a procesos fragmentados o centralizados — sin afirmar reemplazo automático de plataformas productivas ya existentes (p. ej. NPS/Infor Nexus o WMS) salvo que Komatsu lo decida en alcance contractual.

**Problema identificado (propuesta a validar):** La falta de integración y escalabilidad en la gestión manual o centralizada de pedidos e inventario genera cuellos de botella en la atención a clientes, riesgo de desabastecimiento e ineficiencia ante picos de demanda. Se propone a Komatsu una arquitectura orientada a microservicios sobre infraestructura cloud para optimizar disponibilidad, escalabilidad y tiempo de respuesta en pedidos e inventario de partes/repuestos.

**Alcance:** PoC/MVP para Komatsu: CRUD de clientes, productos, pedidos, inventario y usuarios + API Gateway + microservicios contenedorizados (Docker) + PostgreSQL en AWS + monitoreo básico. Despliegue preferente ECS/Fargate; Kubernetes/EKS como evolución. Fuera de alcance en esta fase: ERP completo, MRP, EDI, multi-almacén global, IoT de flota; integración profunda con NPS/WMS solo si Komatsu la autoriza como fase posterior.

## Fuentes
- Komatsu NPS / Infor Nexus — https://dcross.impress.co.jp/docs/usecase/001098.html
- Komatsu + LOGISTEED ONEsLOGI — https://sol.logisteed.com/en/case/voice/komatsu.html
- AWS Guidance order & inventory — https://aws.amazon.com/solutions/guidance/implementing-order-and-inventory-management-for-quick-service-restaurants-on-aws/
- AWS Field Notes ECS + API Gateway — https://aws.amazon.com/blogs/architecture/field-notes-serverless-container-based-apis-with-amazon-ecs-and-amazon-api-gateway/
- Sparity spare parts microservices — https://www.sparity.com/case-studies/microservices-platform-for-service-supply-chain-transformation/
- Komatsu DX (contexto estratégico, no operativo de pedidos) — https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_strategy_05.pdf
