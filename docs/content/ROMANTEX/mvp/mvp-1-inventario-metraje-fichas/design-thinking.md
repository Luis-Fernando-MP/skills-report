# Design Thinking — MVP 1

## Empatizar — observar comportamiento, no opiniones educadas

1.  **Roles del MVP:**
    *   Almacenero
    *   Vendedor (Comercial)
    *   Gerencia (decisor)
2.  **Observar:**
    *   Proceso actual de consulta de stock de metraje residual: el vendedor pregunta al almacenero, quien busca manualmente en cuadernos o ficheros, o revisa físicamente rollos.
    *   Proceso de registro de metraje después de una venta: el almacenero anota el nuevo metraje a mano, a veces con retraso o errores.
3.  **Mapa de empatía (hipótesis):**
    *   **Dice:**
        *   (Almacenero) "No encuentro el rollo", "Los metros no coinciden", "Necesito esto rápido".
        *   (Vendedor) "El cliente está esperando", "No sé cuánto queda de este producto".
        *   (Gerencia) "Perdemos ventas por falta de visibilidad", "Demora mucho el inventario".
    *   **Piensa:**
        *   (Almacenero) "Esto podría ser más fácil", "Siempre es lo mismo", "Me frustra no tener la información al día".
        *   (Vendedor) "Estoy perdiendo una venta", "Si tuviera la información, podría vender más".
        *   (Gerencia) "Necesitamos mejorar la eficiencia", "Hay que reducir errores de stock".
    *   **Hace:**
        *   (Almacenero) Revisa cuadernos, llama al vendedor, busca en el almacén.
        *   (Vendedor) Llama al almacén, espera respuesta, pierde tiempo con el cliente.
        *   (Gerencia) Solicita informes manuales, nota discrepancias.
    *   **Siente:**
        *   (Almacenero) Frustración, estrés, sobrecarga.
        *   (Vendedor) Impotencia, pérdida de oportunidades.
        *   (Gerencia) Preocupación, ineficiencia.

## Definir — un reto, no “mejorar el sistema”

1.  **POV (Punto de Vista):**
    *   El personal de almacén de Romantex necesita una forma rápida y precisa de consultar y registrar el metraje residual y las fichas técnicas mínimas para asegurar la disponibilidad de stock, evitar sobrepromesas al cliente y optimizar el tiempo de despacho.
2.  **HMW (How Might We / ¿Cómo podríamos…?)**
    *   **Primario:** ¿Cómo podríamos digitalizar el inventario de metraje residual y fichas técnicas mínimas para que el almacenero pueda consultar la disponibilidad en tiempo real y registrar las salidas de forma eficiente, minimizando errores y agilizando el despacho?
    *   ¿Cómo podríamos estandarizar las fichas técnicas mínimas para que el personal comercial tenga información consistente y actualizada al atender al cliente?
    *   ¿Cómo podríamos generar alertas automáticas de bajo stock para que la gerencia pueda tomar decisiones proactivas y reducir pérdidas de venta?

## Idear — cantidad antes que calidad

1.  **Ideas:**
    1.  **App móvil sencilla para el almacén:** Una aplicación que permita escanear códigos de rollo, visualizar metraje actual y ficha técnica mínima, registrar nuevas cantidades después de un corte/venta, y generar alertas.
    2.  **Sistema web básico con interfaz táctil:** Una interfaz basada en navegador web, accesible desde tablets en el almacén, con funcionalidades similares a la app móvil.
    3.  **Hojas de cálculo compartidas y automatizadas (Google Sheets):** Usar hojas de cálculo con macros o scripts para simular una base de datos y un sistema de entrada/consulta (fuera de alcance para un MVP robusto).
2.  **Idea Priorizada:** App móvil sencilla para el almacén, por su facilidad de uso en un entorno de trabajo manual y potencial de integración con escáneres.

## Prototipar — tangible y barato (≤1 día de diseño)

1.  **Artefacto:** Un mockup interactivo de baja fidelidad (ej. en Figma o dibujado a mano) o una serie de diapositivas que simulen la experiencia de usuario de la app móvil.
    *   **Flujo principal:**
        1.  Acceso a la app.
        2.  Opción "Escanear Rollo" o "Buscar Rollo".
        3.  Visualización de la pantalla de detalle del rollo:
            *   Código de rollo, Nombre de la tela, Color, Ancho.
            *   Metraje residual actual (grande y visible).
            *   Botón "Editar Metraje" (para registrar salida).
            *   Botón "Ver Ficha Técnica Mínima".
            *   Alertas visuales (ej. "Bajo stock") si el metraje está por debajo de un umbral.
        4.  Pantalla "Editar Metraje": campo numérico para ingresar nueva cantidad, botón "Guardar".
        5.  Pantalla "Ficha Técnica Mínima": campos predefinidos (composición, uso, cuidados, etc.).
    *   **Roles:** El prototipo se enfoca en el "Almacenero" como usuario principal.
    *   **Maestro mínimo de datos:** Código de rollo (identificador único), metraje actual, código de tela, ancho, color, ubicación en almacén, umbral de alerta.
    *   **Frecuencia de uso:** Varias veces al día por cada movimiento de rollo o consulta.

## Test — después del RAT; usuario usa, tú callas

*   Este paso se definirá con base en los RATs que se identifiquen. Provisionalmente, se testeará la usabilidad del prototipo con el almacenero para validar la eficiencia en la consulta y registro del metraje residual y la facilidad de acceso a la ficha técnica mínima.
