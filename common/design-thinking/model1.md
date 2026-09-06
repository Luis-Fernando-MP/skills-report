# Design Thinking — model1

Playbook para `init-project-mvp` / agente `design-thinking`. Aplica **solo al MVP N** del profile. No reabre el tema.

## Posición en el pipeline

Tool **opcional**. Si está en `config.tools`:

1. Ejecutar **Empathize → Define → Ideate → Prototype** en su turno del diagrama (SoT del orden = diagrama de la skill).
2. **No** cerrar Test todavía.
3. Tras los nodos Lean/FODA/**RAT** presentes, completar **Test** (alimentado por `R#` si hubo RAT; si no, criterio_exito profile + umbral).
4. AS-IS/TO-BE (si corre) referencia este Prototype.

Si DT **no** está en tools: no hay sección DT; Lean y demás usan `ref: profile` (ver degradación en la skill).

## Propósito

Traducir el MVP acordado en empatía, POV/HMW, ideación acotada, prototipo concreto y plan de test — etiquetando siempre evidencia.

## Etiquetas de evidencia (obligatorias)

Cada afirmación relevante lleva una de:

- `evidencia` — dato del profile/polish/campo
- `hipótesis` — supuesto razonable sin campo
- `pendiente_campo` — debe validarse en Fase 0 / visitas

## Pasos

### 1. Empathize

1. Listar **roles** del MVP (máx. 5): p. ej. dueño, almacén, comercial, taller.
2. Por rol: qué hace hoy, qué le duele, qué necesita para el criterio de éxito del MVP.
3. Mapa de empatía breve (Dice / Piensa / Hace / Siente) — marcar hipótesis.
4. **Prohibido** inventar citas o métricas de la empresa.

**Preguntas guía (campo / entrevista):**

- ¿Dónde miras hoy para saber si hay talla/variante X?
- ¿Cuánto tardas en confirmar disponibilidad a un cliente?
- ¿Quién actualiza el stock y con qué frecuencia?
- ¿Qué pasa cuando el dato y el físico no coinciden?

### 2. Define

1. Redactar **POV** en una frase: *[Usuario] necesita [necesidad] porque [insight].*
2. Escribir **2–4 HMW** accionables y acotados al MVP (no “¿cómo digitalizamos la empresa?”).
3. Elegir 1 HMW primario alineado a los **entregables** del profile.

### 3. Ideate

1. Generar **3–5** ideas que respondan al HMW primario.
2. Descartar ideas fuera del alcance del MVP (ERP, POS, e-commerce, etc. si están en “Fuera”).
3. Priorizar **1 idea** con criterio: valor al criterio de éxito + esfuerzo académico + dependencias de datos.

### 4. Prototype (SoT del artefacto)

1. Describir el prototipo como **artefacto** (campos, pantallas, hoja, flujo) que materializa los entregables del MVP.
2. Incluir: roles que lo usan, frecuencia de uso, dato maestro mínimo.
3. No prototipar fases MVP+1.
4. Lean Canvas (Solución) y AS-IS/TO-BE (TO-BE) **solo referencian** este Prototype; no inventan otro artefacto.

### 5. Test (después del RAT)

Completar **solo después** de tener la sección RAT (si `rat` está en `config.tools`). Si RAT no corre: Test se basa en el criterio de éxito del profile con umbral explícito.

1. Mapear cada actividad de test a un `R#` del RAT (`R1 → …`). Prohibido un set de pruebas paralelo no trazado al RAT.
2. Por actividad: quién / qué observar / **umbral numérico o binario** / cuándo.
   - Ejemplo: “Muestra 20 SKU-ubicación; si % con |varianza| > 0 supera 10% → falsado el supuesto de stock alineado (R1)”.
3. Lista de `pendiente_campo` que bloquean pasar de hipótesis a evidencia.

## Salida mínima en `mvp-N.md`

Sección semántica **Design Thinking** (Empathize / Define / Ideate / Prototype / Test post-RAT). El **número** (`## N`) lo asigna el orquestador según el diagrama y las tools presentes.
