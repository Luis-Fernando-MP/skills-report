# Debate bibliography-auto — DDS

Modo: `bibliography_auto_utilidad`. Profile: PoC Komatsu pedidos↔inventario partes; reserva al crear pedido; 0 oversell (perímetro PoC); Docker→AWS ECS/Fargate+PostgreSQL; microservicios objetivo; sin NPS/WMS/ERP.

## Resumen orquestador

| # | Candidato | Crítico | Defensor | Decisión descarga |
|---|-----------|---------|----------|-------------------|
| 1 | cloud-based-inventory-management-aws-ecs (CBIMS) | NO_GO | GO_con_cambios | **NO** (empate / duda → no descargar; paperware + alcance IoT/ERP) |
| 2 | securing-high-concurrency-ticket-sales-microservice | GO_con_cambios | GO | **SÍ** |
| 3 | microservices-event-driven-ecommerce (WJARR) | NO_GO | GO_con_cambios* | **NO** |
| 4 | event-driven-microservices-supply-chain (Nilisetty) | NO_GO | NO_GO | **NO** |
| 5 | distributed-transactions-microservice-architecture | GO_con_cambios | GO_con_cambios | **SÍ** |
| 6 | oze-concurrency-control-manufacturing | NO_GO | insuficiente / débil | **NO** |

\*Defensor sin abstract verificado en ronda.

**Descargas:** 2 PDFs (tope 5).  
**pendiente_oa:** ninguno (los rechazados tenían PDF OA; se rechazaron por utilidad, no por paywall).

## Acta por candidato

### 1. CBIMS (IRJIET) — NO descargar
- **Crítico:** stack-match engañoso (ECS/Postgres) sin prueba de 0 oversell; IoT/LSTM/multi-warehouse/ERP integration fuera de alcance; venue/métricas paperware.
- **Defensor:** blueprint ECS Fargate + Postgres útil; concede que no prueba 0 oversell ni IoT.
- **Orquestador:** ante duda → no descargar.

### 2. Securing High-Concurrency Ticket Sales (arXiv 2512.24941) — GO
- **Crítico:** ancla anti-oversell (tokens Redis/`INCRBY`); adaptar dominio/stack (no Redis obligatorio).
- **Defensor:** mejor ancla al invariante 0 oversell / reserva antes de persistir.
- **Orquestador:** descargar; citar como **mecanismo**, no como dominio de partes.

### 3. WJARR EDA e-commerce — NO
- Buzzword-only / sin ancla de reserva concurrente demostrada para el PoC.

### 4. Nilisetty supply-chain EDA — NO
- SobreAlcance cadena autónoma; no núcleo reserva al pedido.

### 5. Bashtovyi & Fechan (2024) — GO
- Marco de decisión sobre transacciones distribuidas / consistencia en MSA; justifica tx local pedido+stock en PoC vs microservicios prematuros.
- No es blueprint de stock ni ECS.

### 6. Oze — NO
- Protocolo CC de investigación / BoMB manufacturing; fuera del flujo pedidos de partes del PoC.

## Fuentes consultadas (debate)
- https://arxiv.org/abs/2512.24941
- https://doi.org/10.23939/sisn2024.15.449
- https://irjiet.com/common_src/article_file/IRJIET1050341778639233.pdf (rechazado)
- https://wjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-1663.pdf (rechazado)
- https://ijsrcseit.com/home/article/download/CSEIT25112355/CSEIT25112355 (rechazado)
- https://arxiv.org/abs/2210.04179 (rechazado)
