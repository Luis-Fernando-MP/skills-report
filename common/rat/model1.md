# Mapa de supuestos / RAT — model1

Riskiest Assumption Test aplicado al **MVP N**.

**Pedagogía vs salida:** este playbook guía al orquestador. La salida `rat.md` son fichas **aplicadas** al caso (sin tutorial RAT).

## Posición en el pipeline

Se escribe **después** de FODA (y DT Prototype / Lean). Es la **fuente de verdad (SoT)** de supuestos riesgosos y falsaciones. DT Test y la brecha AS-IS→TO-BE **consumen** IDs `R#`; no inventan otro set.

## Propósito

Priorizar qué falsificar primero en campo (Fase 0 / piloto) para no construir sobre humo.

## Pasos

1. Listar supuestos detrás del MVP (datos, adopción, proceso, ownership, latencia, herramientas), incluyendo candidatos marcados en FODA (`→ candidato RAT`).
2. Clasificar cada uno: impacto si es falso (alto/medio/bajo) × incertidumbre (alta/media/baja).
3. **Regla de corte (top RAT):**
   - Incluir **todos** los `alto × alta`.
   - Si hay **&lt; 3**, completar con los siguientes mejores (priorizar mayor impacto; empate → mayor incertidumbre) hasta **mínimo 3**.
   - **Máximo 5** en la lista RAT. Si hay &gt;5 en `alto × alta`, quedar con los 5 de mayor impacto y listar el resto en **Cola no RAT** (una línea cada uno, sin ficha completa).
4. Por cada RAT: falsación con plantilla obligatoria (abajo).
5. Ligar cada RAT a un entregable o métrica del profile.

## Formato de cada supuesto

```text
- ID: R1
- Supuesto: …
- Etiqueta actual: hipótesis | pendiente_campo
- Impacto si falso: alto | medio | bajo
- Incertidumbre: alta | media | baja
- Falsación:
  - observar: …
  - con_quien: …          # contraparte de campo (rol interno)
  - umbral: …             # numérico o binario explícito (obligatorio)
  - ventana: …            # cuándo / en cuántas visitas
- Dueño_entregable: estudiante   # default académico
- Contraparte_campo: rol interno | n/a
- Origen: FODA-A# | DT | Lean | profile
```

**Ejemplo de umbral:** “Muestra de 20 SKU-ubicación; si % con discrepancia stock_declarado vs físico &gt; 10% → R1 falsado.”

## Reglas

- No inventar “ya validado” sin evidencia de empresa.
- Al menos un RAT debe atacar la **confiabilidad del dato** o la **adopción del registrador** si el MVP es de inventario/proceso.
- Si el profile exige Fase 0 gate, el primer RAT (R1) debe poder resolverse en esa fase.
- **Dueño:** el entregable del curso / ficha RAT es del **estudiante** (campo fijo de plantilla académica; el control real es anti-autoevaluación + contraparte/umbral observable — no se cuestiona salvo que el usuario lo pida). El rol interno es solo contraparte de campo.
- **Anti-autoevaluación (obligatorio):** el estudiante escribe el RAT, pero **no** puede ser la única fuente de falsación.
  1. Cada ficha RAT debe nombrar **contraparte_campo** realista (rol en empresa) **o**, si el acceso es imposible en el plazo, declarar `contraste: diferido` + qué evidencia externa mínima se pedirá (foto de cuaderno, export, testimonio fechado) antes de marcar el supuesto como no falsado.
  2. El **umbral** debe ser observable por un tercero (docente/tutor o contraparte) sin depender del “me pareció que…” del estudiante.
  3. Al menos **R1** exige protocolo con dato **fuera de la cabeza del equipo** (conteo, captura de pantalla del sistema actual, entrevista registrada). Si no hay acceso: R1 queda `pendiente_campo` y el paquete lo dice en chat — no fingir validación.
  4. Prohibido cerrar un RAT como `evidencia` solo con reflexión del estudiante.
- **vs FODA:** no duplicar texto; en pase FODA solo `candidato`; tras amarre orquestador → `R#`.
- **vs DT Test:** Test solo operacionaliza `R1…Rk` (mismos IDs y umbrales; puede detallar protocolo pero no cambiar el umbral sin `conflicto:`).
- **Sin FODA en tools:** originar supuestos desde DT / Lean / profile; `Origen:` no use `FODA-*`.
- **Sin DT en tools:** originar desde Lean / profile.
- **Sin DT ni Lean:** `Origen: profile` únicamente.

## Salida mínima

Archivo `rat.md`: 3–5 fichas + cola opcional. Numeración `##` dentro del archivo.