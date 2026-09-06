# Mapa de supuestos / RAT — MVP 1

## R1
  - Supuesto: Los procesos manuales de inventario (cuadernos, ficheros) generan un porcentaje de error en el metraje residual mayor al 10% que impacta la promesa de entrega.
  - Etiqueta actual: hipótesis
  - Impacto si falso: alto
  - Incertidumbre: alta
  ### Falsación:
    - observar: Conteo físico del metraje residual en 20 rollos seleccionados al azar, contrastado con el registro manual actual.
    - con_quien: Almacenero, Jefe de Almacén.
    - umbral: Si el porcentaje de discrepancia entre el conteo físico y el registro manual es <= 10% en al menos 15 de los 20 rollos, entonces el supuesto es falsado (el error manual no es significativo).
    - ventana: Durante una visita al almacén de 4 horas.
  - Dueño_entregable: estudiante
  - Contraparte_campo: Almacenero
  - Origen: FODA-D1

## R2
  - Supuesto: La falta de información de stock en tiempo real provoca sobrepromesas de venta y consecuentes retrasos o pérdidas de cliente.
  - Etiqueta actual: hipótesis
  - Impacto si falso: alto
  - Incertidumbre: alta
  ### Falsación:
    - observar: Entrevista a 3 vendedores sobre casos recientes de sobrepromesas, su origen (falta de información, error en el registro) y el impacto en la venta/cliente.
    - con_quien: Vendedores (3), Jefe de Ventas.
    - umbral: Si menos de 2 de los 3 vendedores reportan que las sobrepromesas son frecuentes (más de 3 veces al mes) y directamente atribuibles a la falta de información de stock, el supuesto es falsado.
    - ventana: Entrevistas individuales de 30 minutos cada una.
  - Dueño_entregable: estudiante
  - Contraparte_campo: Vendedor
  - Origen: FODA-D2

## R3
  - Supuesto: El personal del almacén y ventas mostrará resistencia significativa al uso de una nueva aplicación móvil para el registro y consulta de inventario.
  - Etiqueta actual: hipótesis
  - Impacto si falso: medio
  - Incertidumbre: alta
  ### Falsación:
    - observar: Realización de una prueba de usabilidad con el prototipo (Design Thinking Prototype) con 2 almaceneros y 2 vendedores, observando su interacción, preguntas y comentarios espontáneos.
    - con_quien: Almacenero (2), Vendedor (2).
    - umbral: Si el 75% de los participantes expresa dificultad o rechazo explícito a la interfaz o flujo de la aplicación durante la prueba, el supuesto no es falsado. Si el 75% muestra adaptación y comentarios constructivos, es falsado (no hay resistencia significativa).
    - ventana: Sesiones individuales de 45 minutos.
  - Dueño_entregable: estudiante
  - Contraparte_campo: n/a
  - Origen: FODA-A1
