# FODA — MVP 1

## FODA

| Fortalezas | Debilidades |
|------------|-------------|
| - Criterio de éxito falsable: reserva + 0 oversell (perímetro PoC) + rechazo sin mutar. `evidencia` profile <br> - Prototipo acotado (API + seed + ADR) entregable sin EKS/SSO ni sync WMS. `evidencia` DT Prototype <br> - Posicionamiento explícito de coexistencia con NPS/WMS (no reemplazo unilateral). `evidencia` pública + profile | - AS-IS interno Komatsu no observado; dolor operativo sigue `hipótesis`. → R1 <br> - Acceso a sponsor/contraparte de campo no garantizado. → R5 <br> - Sin ventaja especial demostrada vs stack aftermarket existente. `hipótesis` Lean |

| Oportunidades | Amenazas |
|---------------|----------|
| - Demostrar capa de reserva concurrente-segura como PoC evaluable por IT/ops. `hipótesis` <br> - Roadmap ADR → contenedores → AWS (MVP 2–3) alineado a interés cloud. `hipótesis` <br> - Evidencia pública de digitalización de partes refuerza relevancia del dominio. `evidencia` | - Sponsor percibe el PoC como silo / shadow IT frente a NPS/WMS. → R3 <br> - Implementación naive check-then-act genera oversell bajo carga (falla el núcleo). → R2 <br> - Prioridad real de Komatsu es otra (pricing, multi-almacén, EDI) y el PoC no entra en agenda. → R1 |

## TOWS

| | Oportunidades (O) | Amenazas (A) |
|--|-------------------|--------------|
| **Fortalezas (F)** | **FO:** Usar invariante 0 oversell + demo HTTP para abrir evaluación de capa de reserva junto a NPS/WMS. → R2 / Prototype | **FA:** Anclar narrativa en ADR de coexistencia y métricas del PoC para no vender “reemplazo de WMS”. → R3 |
| **Debilidades (D)** | **DO:** Protocolo Fase 0 con sponsor (observar última vez pedido trabado) antes de inflar infra. → R1 / Prototype | **DA:** Si no hay acceso, tipificar solo con seed + umbrales PoC y declarar `contraste: diferido` — no fingir validación in-company. → R5 |

## Amarre post-RAT

| Candidato (texto corto) | R# |
|-------------------------|----|
| AS-IS / dolor no observado; tipificar con sponsor o seed | R1 |
| Oversell por check-then-act bajo concurrencia | R2 |
| Shadow IT / exigencia de reemplazo NPS/WMS | R3 |
| Demo no usable sin explicación | R4 |
| Sin sponsor nombrado / fecha de revisión | R5 |

**Implicación de la semana:** ejecutar **R2** (carrera sobre `KT-SEAL-014`) y pedir a sponsor **R1+R3** por escrito antes de inflar Docker/AWS.
