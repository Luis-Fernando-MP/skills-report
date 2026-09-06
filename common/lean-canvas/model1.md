# Lean Canvas — model1

Playbook Ash Maurya (9 bloques) para el **MVP N**. Una hoja de hipótesis vivas, no plan de 40 páginas. Alineado a curso ITD S03 (orden de riesgo, UVP con fórmula, 3 problemas ↔ 3 features).

**Pedagogía vs salida:** este archivo enseña al orquestador. La salida `lean-canvas.md` es el **lienzo aplicado** al caso (varias tablas en layout de canvas), no una explicación del método.

## Posición en el pipeline

Después de DT Prototype (si hay DT); antes de FODA/RAT. Si no hay DT → `ref: profile`.

## Propósito

Mapear hipótesis del modelo alrededor del MVP. **Llenar** en el orden que reduce más riesgo; **mostrar** en layout de lienzo (como la plantilla “LIENZO LEAN CANVAS”).

### Orden de llenado (obligatorio para el orquestador — no va en la salida)

1. Problema → 2. Segmentos → 3. UVP → 4. Solución → 5. Canales → 6. Costos → 7. Ingresos → 8. Métricas → 9. Ventaja especial

**Prohibido en `lean-canvas.md`:** lista vertical “Bloque 1…9”, diagrama de orden de llenado, diagrama de zonas del método.

## Layout de salida (SoT visual)

El archivo **no** es una tabla de 9 filas. Es un **lienzo** con **varias tablas** que imitan la plantilla:

```text
┌──────────┬──────────┬────────────┬──────────┬────────────┐
│ PROBLEMA │ SOLUCIÓN │ PROPUESTA  │ VENTAJA  │ SEGMENTO   │
│          │          │ DE VALOR   │ ESPECIAL │ DE         │
│          ├──────────┤ ÚNICA      ├──────────┤ CLIENTES   │
│          │ MÉTRICAS │            │ CANALES  │            │
│          │ CLAVE    │            │          │            │
├──────────┴──────────┴─────┬──────┴──────────┴────────────┤
│ ESTRUCTURA DE COSTOS      │ FLUJO DE INGRESOS            │
└───────────────────────────┴──────────────────────────────┘
```

### Plantilla obligatoria en `lean-canvas.md`

```markdown
# Lean Canvas — MVP N

## Lienzo

### Tabla 1 — fila superior (5 columnas)

| PROBLEMA | SOLUCIÓN | PROPUESTA DE VALOR ÚNICA | VENTAJA ESPECIAL | SEGMENTO DE CLIENTES |
|----------|----------|--------------------------|------------------|----------------------|
| … | … | … | … | … |

### Tabla 2 — fila media (bajo Solución y Ventaja)

| MÉTRICAS CLAVE | CANALES |
|----------------|---------|
| … | … |

### Tabla 3 — base del lienzo

| ESTRUCTURA DE COSTOS | FLUJO DE INGRESOS |
|----------------------|-------------------|
| … | … |
```

Opcional: un mermaid **del feature central** (dominio), debajo del lienzo — no del método Lean. Si se incluye, **paso a paso nodo a nodo** (emoji o número + qué ocurre + si cambia de rol); mismo criterio que `common/as-is-to-be/model1.md` (no resumir tres cajas en un bullet). Definir X/Y u otras letras en el paso donde aparecen.

## Reglas de contenido

- Cada celda: contenido + `evidencia` | `hipótesis` | `pendiente_campo`.
- Máx. **2 frases o 3 bullets** por celda.
- Trazas: Problema/Segmentos/Solución ← DT o profile.
- **PROBLEMA:** hasta **3** dolores + **alternativas existentes**.
- **SEGMENTO:** específicos + **early adopters**.
- **UVP** — fórmula: *“Para [segmento] que [problema], [producto] es [categoría] que [beneficio], a diferencia de [alternativa].”*
- **SOLUCIÓN:** hasta **3 features** 1:1 con los 3 problemas.
- **MÉTRICAS:** comportamiento / criterio_éxito del profile (no vanidad).
- **VENTAJA:** costosa de copiar; si no → `ninguna aún`.
- N/A solo en Canales (interno), Ingresos (sin cobro), Ventaja (`ninguna aún`).

## Salida mínima

Archivo `lean-canvas.md`: **3 tablas del lienzo** (+ mermaid de feature si aplica). Número `##` = orquestador.
