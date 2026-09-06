# Perfil del proyecto

## Tema
Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu

## Descripción
Propuesta empresarial (PoC/MVP) dirigida a **Komatsu** para gestionar clientes, catálogo de partes, pedidos, inventario y usuarios sobre arquitectura cloud. Camino de entrega: dominio con **reserva de stock al crear pedido** → contenedores (Docker) → despliegue en **AWS** (ECS/Fargate + PostgreSQL + monitoreo) → extracción a **microservicios** (API Gateway, hasta 3 servicios acotados) como arquitectura objetivo. El entregable es un sistema demostrable y desplegable que Komatsu pueda evaluar frente a cuellos de integración/escala en pedidos e inventario; la convivencia o integración con plataformas ya existentes (p. ej. NPS/WMS documentados públicamente) queda fuera de esta fase salvo acuerdo explícito.

## Problema identificado
**Propuesta de problemática (a validar/priorizar con Komatsu):** la falta de integración y escalabilidad en la gestión manual o centralizada de pedidos e inventario genera cuellos de botella en la atención a clientes, riesgo de desabastecimiento e ineficiencia operacional ante picos imprevistos de demanda.

**Pregunta de diseño de la propuesta:** ¿de qué manera una arquitectura orientada a microservicios sobre infraestructura cloud permite optimizar la disponibilidad, escalabilidad y tiempo de respuesta en la gestión de pedidos e inventario de partes/repuestos para Komatsu?

**Métricas de aceptación del PoC (obligatorias en la propuesta):** (a) `p95` de `POST /pedidos` bajo carga tipificada; (b) tasa de error HTTP; (c) **0 oversell** / consistencia stock–pedido bajo concurrencia (mecanismo de reserva). Umbrales de referencia del PoC: local p95 &lt; 500 ms y failed &lt; 1 %; en AWS p95 &lt; 1200 ms y failed &lt; 2 % (ajustables con Komatsu en el acuerdo de alcance).

## Alcance
PoC/MVP para Komatsu, secuenciado: (1) dominio + reserva de stock; (2) Compose + prueba de carga; (3) ECS/Fargate + RDS + monitoreo (CloudWatch y/o Prometheus/Grafana). Arquitectura objetivo con API Gateway y microservicios; K8s/EKS como evolución. Frontend web funcional mínimo. Auth de PoC (JWT/API key); enterprise IdP en fase posterior.

**Fuera de alcance esta fase:** ERP/MRP/EDI completos; multi-almacén global; IoT de flota; reemplazo unilateral de NPS/Infor Nexus o WMS; multi-región / service mesh.

## MVP entregables

### MVP de arranque (recomendado al equipo)
MVP 1 — Núcleo de negocio pedido↔stock con reserva (0 oversell) como base creíble de la propuesta a Komatsu — el debate técnico sigue priorizando dominio correcto antes de inflar infra; el destinatario del valor es Komatsu, no un curso.

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | Núcleo de propuesta: pedidos e inventario correctos | Spring Boot (modular o servicios iniciales); `ReservarStockAlCrearPedido`; catálogo/clientes/usuarios; seed de demo orientado a partes; ADR de arquitectura objetivo (microservicios + AWS); colección HTTP; resumen ejecutivo 1–2 págs. para Komatsu | Pedido reserva stock; stock insuficiente → rechazo sin mutar; 0 oversell bajo concurrencia; narrativa de propuesta clara para la empresa | se trabaja ahora |
| 2 | Empaquetar y demostrar carga | Docker + Compose; script k6; umbrales pass/fail; primer corte a gateway + servicios si el ADR lo fija | `k6 run` pasa umbrales locales; demo reproducible del flujo pedido→stock | después |
| 3 | PoC cloud en AWS para Komatsu | ECR + ECS/Fargate; RDS PostgreSQL; API Gateway/ALB; monitoreo; k6 contra endpoint cloud; diagrama de arquitectura objetivo (microservicios + evolución K8s) | Endpoint cloud alcanzable; umbrales cloud cumplidos; paquete de propuesta (arquitectura + métricas + roadmap) listo para revisión Komatsu | después |

### Fuera de secuencia / descartado
- Presentar el PoC como reemplazo ya decidido de NPS/WMS sin acuerdo de Komatsu
- ERP, EDI, multi-almacén global, IoT de flota en esta fase
- EKS/K8s como bloqueante del primer PoC (queda en roadmap)
- Auth enterprise (Cognito/SSO corporativo) en MVP 1
- Afirmar KPIs internos de Komatsu no aportados por la empresa

## Marco PICOCT (para bibliography)

| Componente | Definición | Criterios / descripción del caso |
| :---: | :--- | :--- |
| **P** | Population / Problem | Operaciones de pedidos e inventario de partes/repuestos en Komatsu; problemática propuesta de integración/escalabilidad (cuellos de atención, riesgo de desabastecimiento, picos de demanda) |
| **I** | Intervention | PoC de sistema cloud (AWS) con contenedores y arquitectura orientada a microservicios (API Gateway, servicios de dominio, PostgreSQL, monitoreo) e invariante de reserva de stock al pedido |
| **C** | Comparison | Gestión manual o centralizada actual / sistemas fragmentados; convivencia eventual con plataformas productivas existentes (NPS/WMS u otras) fuera del núcleo del PoC |
| **O** | Outcome | Disponibilidad y tiempo de respuesta (p95 `POST /pedidos`); tasa de error; consistencia stock–pedido (0 oversell); escalabilidad demostrable bajo carga; paquete de arquitectura desplegable en AWS |
| **C** | Context | OEM industrial de maquinaria / partes (Komatsu); propuesta empresarial PoC; dominio partes/repuestos; despliegue cloud AWS |
| **T** | Time / Type of study | Año 2026 (sin rango indicado en audit); tipo preferente: artículos (`ar`) |

## Origen
Espejo de `docs/topics/DS/theme-audit-polish.md` (veredicto GO_con_cambios; framing propuesta/PoC para Komatsu).
