# Veredicto auditoría — DS

## Veredicto global
GO_con_cambios

## Detalle
Ver `theme-audit-debate.md`.

## Tema final

### Tema
Sistema de gestión de pedidos e inventario de partes/repuestos basado en microservicios y contenedores para Komatsu

### Descripción
Propuesta empresarial (PoC/MVP) dirigida a **Komatsu** para gestionar clientes, catálogo de partes, pedidos, inventario y usuarios sobre arquitectura cloud. Camino de entrega: dominio con **reserva de stock al crear pedido** → contenedores (Docker) → despliegue en **AWS** (ECS/Fargate + PostgreSQL + monitoreo) → extracción a **microservicios** (API Gateway, hasta 3 servicios acotados) como arquitectura objetivo. El entregable es un sistema demostrable y desplegable que Komatsu pueda evaluar frente a cuellos de integración/escala en pedidos e inventario; la convivencia o integración con plataformas ya existentes (p. ej. NPS/WMS documentados públicamente) queda fuera de esta fase salvo acuerdo explícito.

### Problema identificado
**Propuesta de problemática (a validar/priorizar con Komatsu):** la falta de integración y escalabilidad en la gestión manual o centralizada de pedidos e inventario genera cuellos de botella en la atención a clientes, riesgo de desabastecimiento e ineficiencia operacional ante picos imprevistos de demanda. No se afirma como auditoría del AS-IS interno de Komatsu ni como falla demostrada de portales/WMS/ERP ya publicados (p. ej. Global Supplier Portal, KOM-MICS, ONEsLOGI, Swisslog SynQ).

**Pregunta de diseño de la propuesta:** ¿de qué manera una arquitectura orientada a microservicios sobre infraestructura cloud permite optimizar la disponibilidad, escalabilidad y tiempo de respuesta en la gestión de pedidos e inventario de partes/repuestos para Komatsu?

**Métricas de aceptación del PoC (obligatorias en la propuesta):** (a) `p95` de `POST /pedidos` bajo carga tipificada; (b) tasa de error HTTP; (c) **0 oversell** / consistencia stock–pedido bajo concurrencia (mecanismo de reserva) **dentro del perímetro del PoC** (datos seed/demo). Umbrales de referencia del PoC: local p95 &lt; 500 ms y failed &lt; 1 %; en AWS p95 &lt; 1200 ms y failed &lt; 2 % (ajustables con Komatsu en el acuerdo de alcance).

### Alcance
PoC/MVP para Komatsu, secuenciado: (1) dominio + reserva de stock; (2) Compose + prueba de carga; (3) ECS/Fargate + RDS + monitoreo (CloudWatch y/o Prometheus/Grafana). Arquitectura objetivo con API Gateway y microservicios; K8s/EKS como evolución. Frontend web funcional mínimo. Auth de PoC (JWT/API key); enterprise IdP en fase posterior.

**Fuera de alcance esta fase:** ERP/MRP/EDI completos; multi-almacén global; IoT de flota; reemplazo unilateral de NPS/Infor Nexus o WMS; multi-región / service mesh; integración productiva con sistemas legacy de Komatsu; afirmar KPIs internos no aportados por la empresa.

### Tipo de sujeto
empresa

### Ficha de empresa (para init-project → company.md)
**Identidad:** Komatsu Ltd.
**Razón social / marca:** Komatsu Ltd.
**País / sede pública:** Japón (Shiodome Building, 1-2-20, Kaigan, Minato-ku, Tokio 105-8316)
**Sector:** Fabricación y venta de maquinaria de construcción, minería, utilidades, forestal e industrial
**Escala (pública):** ~211 subsidiarias consolidadas; ~67 279 empleados consolidados (datos públicos a 1 abr 2026); ventas netas consolidadas ~4 132,8 mil millones de yenes
**Reseña histórica (pública):** Fundación 13 may 1921 (origen Komatsu Iron Works / Meitaro Takeuchi); expansión global; plan estratégico FY2025–FY2027 “Driving value with ambition”
**Misión / visión / valores:** Socio colaborativo para lugares de trabajo seguros, productivos y limpios; propósito de crear valor vía fabricación e innovación tecnológica hacia un futuro sostenible; principio Quality and Reliability
**Oferta relevante al proyecto:** Aftermarket / partes y repuestos de maquinaria; digitalización (Smart Construction, AHS); cadena de valor y DX — el PoC se sitúa como **propuesta demostrable** en pedidos/inventario de partes, no como sustituto de WMS/ERP existentes
**Evidencia_empresa:** suficiente
**Fuentes:**
- https://www.komatsu.jp/en/aboutus/profile
- https://www.komatsu.jp/en/-/media/home/ir/library/financial/en/2603q4_e.pdf
- https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_strategy.pdf
- https://www.komatsu.jp/en/-/media/home/ir/library/annual/2025/en/kr25e_introduction.pdf
- https://www.plantmachineryvehicles.com/power-lists/pmv-power-list/manufacturers-power-list-2025

## MVP entregables

### MVP de arranque (recomendado al equipo)
MVP 1 — Núcleo de negocio pedido↔stock con reserva (0 oversell en perímetro PoC) como base creíble de la propuesta a Komatsu — gana el debate porque mitiga el NO_GO del crítico (no auditar landscape legacy; no sync WMS como gate) y prioriza dominio correcto antes de inflar infra.

### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | Núcleo de propuesta: pedidos e inventario correctos | Spring Boot (modular o servicios iniciales); `ReservarStockAlCrearPedido`; catálogo/clientes/usuarios; seed de demo orientado a partes; ADR de arquitectura objetivo (microservicios + AWS); colección HTTP; resumen ejecutivo 1–2 págs. para Komatsu | Pedido reserva stock; stock insuficiente → rechazo sin mutar; 0 oversell bajo concurrencia (perímetro PoC); narrativa de propuesta clara para la empresa | se trabaja ahora |
| 2 | Empaquetar y demostrar carga | Docker + Compose; script k6; umbrales pass/fail; primer corte a gateway + servicios si el ADR lo fija | `k6 run` pasa umbrales locales; demo reproducible del flujo pedido→stock | después |
| 3 | PoC cloud en AWS para Komatsu | ECR + ECS/Fargate; RDS PostgreSQL; API Gateway/ALB; monitoreo; k6 contra endpoint cloud; diagrama de arquitectura objetivo (microservicios + evolución K8s) | Endpoint cloud alcanzable; umbrales cloud cumplidos; paquete de propuesta (arquitectura + métricas + roadmap) listo para revisión Komatsu | después |

### Fuera de secuencia / descartado
- Presentar el PoC como reemplazo ya decidido de NPS/WMS sin acuerdo de Komatsu
- ERP, EDI, multi-almacén global, IoT de flota en esta fase
- EKS/K8s como bloqueante del primer PoC (queda en roadmap)
- Auth enterprise (Cognito/SSO corporativo) en MVP 1
- Afirmar KPIs internos de Komatsu no aportados por la empresa
- Integración productiva con WMS/ERP/portales como criterio de éxito de MVP 1

## Marco PICOCT (para bibliography)

| Componente | Definición | Criterios / descripción del caso |
| :---: | :--- | :--- |
| **P** | Population / Problem | Operaciones de pedidos e inventario de partes/repuestos en Komatsu; problemática propuesta de integración/escalabilidad (cuellos de atención, riesgo de desabastecimiento, picos de demanda) a validar con la empresa |
| **I** | Intervention | PoC de sistema cloud (AWS) con contenedores y arquitectura orientada a microservicios (API Gateway, servicios de dominio, PostgreSQL, monitoreo) e invariante de reserva de stock al pedido (0 oversell en perímetro PoC) |
| **C** | Comparison | Gestión manual o centralizada / sistemas fragmentados; convivencia eventual con plataformas productivas existentes (NPS/WMS u otras) fuera del núcleo del PoC |
| **O** | Outcome | Disponibilidad y tiempo de respuesta (p95 `POST /pedidos`); tasa de error; consistencia stock–pedido (0 oversell); escalabilidad demostrable bajo carga; paquete de arquitectura desplegable en AWS |
| **C** | Context | OEM industrial de maquinaria / partes (Komatsu); propuesta empresarial PoC; dominio partes/repuestos; despliegue cloud AWS |
| **T** | Time / Type of study | Año 2026 (sin rango indicado en audit); tipo preferente: artículos (`ar`) |

Fuente para `bibliography-picoct` / espejo en `profile.md` vía `init-project`.

## Listo para
`init-project` (espejar tema final + MVP + **Marco PICOCT** + ficha empresa → `company.md`) → `init-project-mvp mvp-1` → `bibliography-picoct`.
