# Mapa de supuestos / RAT - Confiabilidad de Inventario PT

## RAT 1
- ID: R1
- Supuesto: El descuadre entre el stock físico y el stock declarado en el sistema (hoja de cálculo) es manejable (<10%) y no invalida la utilidad del piloto.
- Etiqueta actual: hipótesis
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: Realizar un conteo físico aleatorio de 20 SKU-ubicación y compararlo con el registro en la hoja de cálculo.
  - con_quien: Almacenero
  - umbral: Si el % de discrepancia de stock_declarado vs físico es > 10% en la muestra, R1 es falsado.
  - ventana: Durante la Fase 0 (gate), en la primera semana de uso del piloto.
- Dueño_entregable: estudiante
- Contraparte_campo: Gerente de Operaciones
- Origen: FODA-A# (Inconsistencia alta entre stock físico y registrado)

## RAT 2
- ID: R2
- Supuesto: Los operarios de almacén registrarán los movimientos (entrada/salida/traslado/ajuste) de manera consistente y precisa al cierre de turno.
- Etiqueta actual: hipótesis
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: Monitorear el registro de 10 movimientos de inventario durante una semana, verificando la consistencia entre el movimiento físico real y el registro en la hoja de cálculo.
  - con_quien: Almacenero
  - umbral: Si > 20% de los movimientos registrados contienen errores de cantidad, tipo de movimiento o SKU en la semana, R2 es falsado.
  - ventana: Después de la primera semana de capacitación y uso del piloto.
- Dueño_entregable: estudiante
- Contraparte_campo: Supervisor de Almacén
- Origen: FODA-A# (Errores humanos en el registro manual)

## RAT 3
- ID: R3
- Supuesto: El equipo comercial confiará en la información de stock proporcionada por la hoja de cálculo y la usará para confirmar la disponibilidad a los clientes.
- Etiqueta actual: hipótesis
- Impacto si falso: medio
- Incertidumbre: media
- Falsación:
  - observar: Realizar encuestas a 5 comerciales después de un mes de uso del piloto, preguntando sobre su nivel de confianza y frecuencia de uso de la herramienta.
  - con_quien: Equipo comercial
  - umbral: Si < 80% de los encuestados reporta confiar en la herramienta y usarla al menos 3 veces al día para consultas de stock, R3 es falsado.
  - ventana: Después del primer mes de uso del piloto.
- Dueño_entregable: estudiante
- Contraparte_campo: Jefe Comercial
- Origen: Lean Canvas (Métricas Clave), Design Thinking (Test)
