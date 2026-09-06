# Marco PICOCT — DS

## Componentes

| Componente | Definición breve | Criterios / descripción del caso | Etiqueta |
|---|---|---|---|
| P | Population / Problem | Operaciones de pedidos e inventario de partes/repuestos (OEM de maquinaria); problemática propuesta: integración/escalabilidad insuficiente ante cuellos de atención, riesgo de desabastecimiento y picos de demanda. Caso: propuesta a Komatsu (la empresa no es término único de búsqueda). | `hipótesis` (dolor in-company a validar) · ancla de dominio `evidencia` pública de aftermarket/partes |
| I | Intervention | PoC de sistema en nube (AWS) con contenedores, arquitectura orientada a microservicios (API Gateway, servicios de dominio, PostgreSQL, monitoreo) e invariante de reserva de stock al crear pedido (0 oversell). | `evidencia` profile / MVP 1 |
| C | Comparison | Gestión manual o centralizada / sistemas fragmentados; convivencia con WMS/SCM productivos existentes fuera del núcleo del PoC (no reemplazo unilateral). | `hipótesis` + `evidencia` de existencia de plataformas OEM (contexto, no brazo control medido) |
| O | Outcome | Latencia (p95 de creación de pedido), tasa de error, consistencia stock–pedido (0 oversell / no overselling), escalabilidad bajo carga, despliegue cloud reproducible. | `evidencia` métricas profile |
| Context | Context | Sector OEM industrial / maquinaria / spare parts aftermarket; operaciones de partes; despliegue cloud AWS; no usar solo el nombre comercial como filtro de query. | `evidencia` tipo de entorno · `pendiente_campo` país/sede si se acota después |
| T | Time / Type of study | Últimos 5 años (2022-2026); tipo preferente: artículos (`ar`). | `evidencia` profile + regla playbook |

## Notas de inclusión / exclusión (breves)

- Incluir: literature sobre order/inventory consistency, stock reservation, microservices/cloud for order management, spare parts / aftermarket inventory, performance under concurrency/load.
- Excluir: ERP/MRP/EDI completos como foco; IoT de flota; papers solo de pricing aftermarket sin inventario/pedidos; uso del nombre “Komatsu” como único eje de Intervention.
- Empresa: Komatsu = caso de propuesta; en keywords de Context preferir *OEM*, *spare parts*, *heavy machinery*, no la razón social como único término.
