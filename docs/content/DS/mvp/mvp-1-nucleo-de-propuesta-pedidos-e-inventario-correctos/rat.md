# RAT — MVP 1

Contraste técnico externo (no es KPI de Komatsu): la prevención de oversell bajo concurrencia exige actualización atómica condicional (`UPDATE … WHERE available >= qty` / locks), no check-then-act (literatura y patrones de motores de reserva; p. ej. decremento atómico + prueba concurrente con stock fijo). Umbrales del PoC vienen del profile (`0 oversell`; p95/error en MVP 2–3). `evidencia` técnica externa · `hipótesis` de aplicabilidad al sitio Komatsu.

## R1

- ID: R1
- Supuesto: Existe (o el sponsor prioriza) un escenario de **doble promesa / stock insuficiente bajo demanda concurrente** en pedidos de partes que justifica evaluar una capa de reserva atómica — no solo un problema genérico de “falta de sistema”.
- Etiqueta actual: `pendiente_campo`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: sponsor aporta incidente fechado, ticket, o ventana observada (“última vez que…”) donde dos canales prometieron el mismo part; **o** declara por escrito que el PoC se evalúa solo con seed sintético
  - con_quien: sponsor / evaluador Komatsu (IT u operaciones partes)
  - umbral: **binario** — si en la primera sesión no hay incidente ni mandato escrito de tipificar con seed → R1 no desbloquea narrativa de “dolor in-company” (solo PoC sintético)
  - ventana: 1 sesión Fase 0 / kickoff
- Dueño_entregable: estudiante
- Contraparte_campo: sponsor Komatsu
- Origen: FODA-D (AS-IS no observado) | profile problema | DT Empathizar plan
- Si no hay acceso: `contraste: diferido` + evidencia mínima (mail sponsor, foto de pantalla de proceso actual, testimonio fechado). No cerrar como `evidencia` solo con reflexión del equipo.

## R2

- ID: R2
- Supuesto: La implementación de `ReservarStockAlCrearPedido` (transacción + actualización condicional / control de concurrencia) logra **0 oversell** cuando N clientes concurrentes compiten por stock insuficiente.
- Etiqueta actual: `hipótesis`
- Impacto si falso: alto
- Incertidumbre: media
- Falsación:
  - observar: seed `KT-SEAL-014` con `onHand=1`; lanzar ≥20 hilos (o k6) de `POST /pedidos` con cantidad 1; auditar pedidos 201 vs stock final
  - con_quien: responsable técnico del PoC ejecuta; tutor/sponsor observa resultado (captura + query)
  - umbral: exactamente **1** pedido 201; resto 4xx; `reservado + disponible` coherente; **0** unidades oversold (stock nunca negativo ni doble reserva)
  - ventana: al cerrar núcleo MVP 1 (antes de inflar AWS)
- Dueño_entregable: estudiante
- Contraparte_campo: tutor o sponsor técnico (tercero que ve el resultado)
- Origen: FODA-A (check-then-act) | DT Prototype | Lean métricas | contraste técnico externo

## R3

- ID: R3
- Supuesto: El sponsor acepta la narrativa de **coexistencia** (PoC = capa de reserva demostrable) y **no** exige que MVP 1 reemplace NPS/WMS.
- Etiqueta actual: `pendiente_campo`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: en kickoff, sponsor marca por escrito alcance: “coexiste / no reemplaza” vs “debe integrar/sustituir NPS o WMS en esta fase”
  - con_quien: sponsor + arquitecto integración (si existe)
  - umbral: **binario** — si exige integración/reemplazo NPS/WMS en MVP 1 → R3 falsado (alcance del profile queda en conflicto; hay que renegociar o NO_GO de entrega)
  - ventana: misma sesión que R1
- Dueño_entregable: estudiante
- Contraparte_campo: sponsor / arquitectura Komatsu
- Origen: FODA-A (shadow IT) | TOWS FA | DT HMW-2 | profile fuera de alcance

## R4

- ID: R4
- Supuesto: Un operador de pedidos (o el early adopter designado) completa el flujo feliz y el de rechazo en la **colección HTTP** sin que el equipo explique el prototipo.
- Etiqueta actual: `hipótesis`
- Impacto si falso: medio
- Incertidumbre: alta
- Falsación:
  - observar: sesión de demo muda; contar intervenciones de ayuda; anotar si llega a 201 y a 4xx por stock
  - con_quien: operador de pedidos o proxy designado por sponsor
  - umbral: en 1 sesión, si necesita **≥3** intervenciones explicativas para completar ambos caminos → R4 falsado
  - ventana: tras existir colección + seed estables
- Dueño_entregable: estudiante
- Contraparte_campo: operador de pedidos (o sponsor en su defecto)
- Origen: Lean early adopters | DT Test (post)

## R5

- ID: R5
- Supuesto: Habrá **contraparte de campo nombrada** (sponsor) y al menos una fecha de revisión del paquete (demo + resumen ejecutivo) dentro del plazo del PoC.
- Etiqueta actual: `pendiente_campo`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: nombre + rol + fecha en acta/mail
  - con_quien: sponsor
  - umbral: **binario** — sin nombre y fecha en ≤10 días hábiles tras kickoff interno → R5 falsado (`contraste: diferido`; el PoC sigue con tipificación sintética pero la “propuesta a Komatsu” queda sin receptor)
  - ventana: kickoff + 10 días hábiles
- Dueño_entregable: estudiante
- Contraparte_campo: sponsor Komatsu
- Origen: FODA-D (acceso) | TOWS DA | DT preguntas al equipo

## Cola no RAT

- Prioridad real distinta (pricing Syncron, multi-DC, EDI) desplaza el PoC — impacto alto × incertidumbre media; se vigila vía R1/R3.
- p95/error bajo carga cloud — diferido a MVP 2–3 (`evidencia` umbrales profile; no núcleo MVP 1).
