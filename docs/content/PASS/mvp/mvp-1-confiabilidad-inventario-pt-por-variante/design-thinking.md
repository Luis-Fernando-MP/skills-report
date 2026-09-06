# Design Thinking - MVP 1

## Empatizar — observar comportamiento, no opiniones educadas

### Roles del MVP
1. Comercial
2. Almacenero/Operario de planta

### Observación de rutina real
- **Comercial:** ¿Cómo confirman la disponibilidad de un producto (modelo, color, talla) al cliente? ¿Qué procesos internos siguen cuando el stock no coincide con lo esperado?
- **Almacenero/Operario:** ¿Cómo registran las entradas, salidas, traslados y ajustes de inventario? ¿Qué herramientas utilizan? ¿Con qué frecuencia actualizan el stock?
- **Mapa de empatía:**
    - **Dice:** "No tenemos esto en stock", "Déjame revisar en el almacén", "El sistema dice una cosa pero la realidad es otra".
    - **Piensa:** "Necesito una forma rápida y confiable de saber qué tenemos", "No puedo confiar en los números actuales", "Perdemos ventas por falta de información precisa".
    - **Hace:** Llamadas al almacén, revisión manual de inventario, anotaciones en cuadernos o excels desactualizados.
    - **Siente:** Frustración, incertidumbre, presión por cumplir con el cliente.
- **Hipótesis:** La falta de un sistema unificado y actualizado para el inventario de producto terminado por variante genera ineficiencias, errores y pérdida de ventas.

## Definir — un reto, no “mejorar el sistema”

### POV
Para el **equipo comercial** que necesita **confirmar stock con precisión**, un sistema que muestre la **disponibilidad real por variante** es clave para **evitar ventas perdidas** y **mejorar la satisfacción del cliente**.

### HMW (How Might We)
1. **(Primario)** ¿Cómo podríamos **garantizar** que el **comercial** tenga acceso a la **información de stock más confiable** por variante en **tiempo de cierre de turno** para que pueda **confirmar ventas sin errores**?
2. ¿Cómo podríamos **simplificar el registro** de entradas, salidas y movimientos de inventario para el **almacenero** para que **minimice errores** y **maximice la exactitud**?
3. ¿Cómo podríamos **medir el descuadre** entre el stock declarado y el físico para que **identifiquemos la magnitud del problema** y **prioricemos las acciones de mejora**?

## Idear — cantidad antes que calidad

### Ideas
1. **Solución manual mejorada (Hojas de cálculo compartidas):** Implementar un sistema de hojas de cálculo de Google Drive con validación de datos y roles, donde el almacenero registra entradas/salidas/ajustes y el comercial consulta en tiempo real.
2. **Aplicación web simple:** Desarrollar una aplicación web básica para la gestión de inventario, accesible desde cualquier dispositivo, con funciones de registro y consulta de stock por variante.
3. **Integración con sistema existente:** Evaluar la posibilidad de integrar un módulo de inventario simple en el sistema actual de la empresa (si existe) o buscar soluciones de terceros de bajo costo.

### Idea Priorizada
**Solución manual mejorada (Hojas de cálculo compartidas):** Esta opción es la más ligera y económica, no requiere ERP/POS, cumple con el alcance de "sin POS" y permite un piloto rápido para obtener evidencia de campo, alineándose con el MVP de arranque. Además, es escalable a un nivel básico y la empresa ya utiliza herramientas de oficina.

## Prototipar — tangible y barato (≤1 día de diseño)

### Artefacto
Una hoja de cálculo de Google Sheets con las siguientes pestañas:
1.  **Maestro de Variantes:** Modelo, Color, Talla, SKU (clave única)
2.  **Ubicaciones de Stock:** Ubicación (Almacén 1, Almacén 2), SKU, Cantidad
3.  **Bitácora de Movimientos:** Fecha, Hora, Tipo de Movimiento (Entrada, Salida, Traslado, Ajuste), SKU, Cantidad, Origen/Destino (si aplica), Responsable
4.  **Consulta Rápida:** Una interfaz sencilla que permite al comercial ingresar Modelo, Color, Talla y obtener la cantidad disponible en cada ubicación propia.

### Roles y Frecuencia
- **Almacenero:** Registra movimientos de inventario al final de cada turno.
- **Comercial:** Consulta la hoja de cálculo según necesidad.

### Maestro Mínimo
- Maestro de variantes: Modelo, color, talla, SKU único.
- Ubicaciones propias: Solo las dos ubicaciones iniciales del piloto.

## Test — después del RAT; usuario usa, tú callas

El protocolo de prueba operacionaliza los supuestos de riesgo identificados en el RAT:

- **R1 (Descuadre manejable):** Durante la Fase 0, se realizará un conteo físico aleatorio de 20 SKU-ubicación. Si el % de discrepancia es > 10%, el supuesto es falsado.
- **R2 (Registro preciso de operarios):** Después de la primera semana, se monitorearán 10 movimientos de inventario. Si > 20% contienen errores, el supuesto es falsado.
- **R3 (Confianza del equipo comercial):** Después de un mes, se encuestará a 5 comerciales. Si < 80% confía y usa la herramienta al menos 3 veces al día, el supuesto es falsado.
