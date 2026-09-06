# RAT — MVP 1

Umbral de exactitud: contraste externo (no es dato de Romantex) — en una MYPE comercializadora de calzado de Lima el ERI de una muestra de 10 SKU partió en 70% y subió a 90% en seis semanas (Universidad Peruana de Ciencias Aplicadas, tesis 2024, hdl.handle.net/10757/675267); metas de precisión de inventario en literatura de kárdex se sitúan ~90–95%. El 10% de discrepancia es umbral **académico** para el gate, `hipótesis` de corte, no baseline de la empresa.

## R1

- ID: R1
- Supuesto: El soporte actual (estante, memoria u anotación) permite confirmar «¿hay talla X en Y?» con descuadre ≤ 10% en la muestra (el dato actual es suficientemente coincidente con el físico).
- Etiqueta actual: `pendiente_campo`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: para ≥20 pares variante-ubicación (1 colección, ≤2 ubicaciones propias) registrar (a) lo que comercial habría confirmado y (b) conteo físico de planta; marcar discrepancia si (a) ≠ (b)
  - con_quien: almacenero/planta + comercial (ambos presentes en el recuento)
  - umbral: si el % de pares con discrepancia **> 10%** → R1 falsado (el soporte actual no es fuente confiable; el problema de inventario queda demostrado en la muestra)
  - ventana: 1–2 visitas de Fase 0 (conteo en el mismo turno)
- Dueño_entregable: estudiante
- Contraparte_campo: almacenero/planta (conteo) y comercial (dato declarado)
- Origen: FODA-D (descuadre no medido) | profile Fase 0 | DT HMW-2

Si no hay acceso a planta: `contraste: diferido` + evidencia mínima (foto de cuaderno/kárdex, lista de lo confirmado vs foto de estante, testimonio fechado). R1 no se marca como no falsado solo con reflexión del equipo. `pendiente_campo`

## R2

- ID: R2
- Supuesto: El almacenero/planta asentará en la bitácora los movimientos PT (entrada/salida/traslado/ajuste) **el mismo turno**, sin POS.
- Etiqueta actual: `hipótesis`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: durante turnos con prototipo, contar movimientos físicos vistos (pares que entran, salen, se trasladan o se ajustan) y cruzar con filas de `Movimientos` con la misma fecha/turno
  - con_quien: almacenero/planta (registrador); estudiante no dicta las filas
  - umbral: en ≥3 turnos, si **< 70%** de los movimientos físicos observados tienen fila el mismo turno → R2 falsado
  - ventana: piloto Sheets tras (o en paralelo acotado a) Fase 0; mínimo 3 turnos
- Dueño_entregable: estudiante
- Contraparte_campo: almacenero/planta
- Origen: FODA-D | DT Prototype bitácora | Lean solución-3

## R3

- ID: R3
- Supuesto: Existe un rol interno dueño del saldo en cada ubicación piloto que puede **cerrar el turno** y deja rastro (papel, Excel o celda de cierre).
- Etiqueta actual: `pendiente_campo`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: gerencia nombra al dueño; ese rol ejecuta un cierre (marca turno cerrado) y muestra el rastro
  - con_quien: dueño/gerencia (nombra) + almacenero/planta (ejecuta)
  - umbral: **binario** — si en las visitas de Fase 0 nadie acepta cerrar ni se nombra dueño del saldo → R3 falsado
  - ventana: mismas visitas de Fase 0 que R1
- Dueño_entregable: estudiante
- Contraparte_campo: dueño/gerencia y almacenero/planta
- Origen: FODA-D | DT plan Fase 0 ítem 4 | profile ownership

## R4

- ID: R4
- Supuesto: Comercial consultará la vista `Consulta` (saldo de último cierre) en vez de confirmar solo de memoria o pregunta verbal.
- Etiqueta actual: `hipótesis`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: consultas reales «¿hay talla X en Y?»; anotar si abre/usa la vista y si cita `fuente = cierre turno`; si hay que explicar la hoja para que la use, contar como hallazgo (no como éxito)
  - con_quien: comercial/ventas
  - umbral: en ≥5 consultas post-prototipo, si **< 3** usan la vista de último cierre → R4 falsado
  - ventana: tras existir al menos un cierre de turno en el Sheets
- Dueño_entregable: estudiante
- Contraparte_campo: comercial/ventas
- Origen: FODA-A | TOWS FA | DT HMW primario

## R5

- ID: R5
- Supuesto: Los descuadres de la muestra se explican por cantidad física vs saldo, no por talla mal anotada en el maestro (el cuello es inventario, no fichas).
- Etiqueta actual: `hipótesis`
- Impacto si falso: alto
- Incertidumbre: alta
- Falsación:
  - observar: sobre cada discrepancia de R1, la contraparte de planta clasifica causa: (i) cantidad en estante ≠ lo declarado, o (ii) el par «no calza» el código de talla/modelo
  - con_quien: almacenero/planta (clasifica); relevamiento de cómo se anota la talla hoy (soporte, sin implantar fichas)
  - umbral: si **≥ 50%** de las discrepancias de la muestra se atribuyen a código/talla y no a cantidad → R5 falsado (priorizar maestro de tallaje / MVP2, no vestir el kárdex)
  - ventana: misma muestra que R1
- Dueño_entregable: estudiante
- Contraparte_campo: almacenero/planta
- Origen: FODA-O | profile separar cuello inventario vs tallaje | DT HMW-4

## Cola no RAT

- Latencia de turno aceptable para comercial (no exigen «tiempo real») — impacto medio × incertidumbre media; fuera de alcance si aparece como requisito.
- Añadir la segunda ubicación propia aporta señal vs una sola — impacto medio; el perfil ya permite 1 de arranque y ≤2 de extensión.
- Identidad legal del caso vs ROMANTEX textil Lima — `conflicto` de ficha, no supuesto operativo del kárdex; se resuelve preguntando al equipo (no cierra R1–R5).
