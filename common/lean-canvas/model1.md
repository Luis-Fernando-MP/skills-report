# Lean Canvas — model1

Playbook Ash Maurya (9 bloques) para el **MVP N**, no para el negocio completo soñado.

## Posición en el pipeline

Se llena **después** de DT Empathize→Prototype **si** `design-thinking` está en `config.tools`; si no, es el primer nodo presente tras el profile. **Antes** de FODA/RAT.

DT es **opcional** (como toda tool): puede omitirse en `config.tools`. Por eso la trazabilidad tiene dos anclas.

## Propósito

Mapear hipótesis de modelo alrededor del MVP acordado. Una hoja mental; reescribible tras campo.

## Orden de llenado (obligatorio)

1. Problema  
2. Segmentos de clientes  
3. Propuesta de valor única  
4. Solución  
5. Canales  
6. Flujos de ingreso  
7. Estructura de costos  
8. Métricas clave  
9. Ventaja especial  

## Reglas

- Cada celda: contenido + etiqueta `evidencia` | `hipótesis` | `pendiente_campo`.
- **Longitud:** máx. **2 frases o 3 bullets** por celda.
- **Trazabilidad (obligatoria):**
  - Si corrió DT: Problema ← Empathize (`ref: DT Empathize`); Segmentos ← roles (`ref: DT roles`); Solución ← Prototype (`ref: DT Prototype`).
  - Si **no** corrió DT: los tres anclan a profile (`ref: profile` — problema/alcance/entregables MVP). No inventar POV/HMW fantasma.
- **Problema** y **Segmentos** anclados a roles del MVP, no a “el mercado peruano” genérico.
- **Solución** = entregables del MVP N / Prototype / profile, no ERP/POS fuera de alcance.
- **Métricas clave** alineadas al criterio de éxito del profile (máx. 3).
- Prohibido BMC Osterwalder completo ni VPC largo.

### N/A — cuándo sí y cuándo no

| Bloque | N/A |
|--------|-----|
| Problema, Segmentos, UVP, Solución, Costos, Métricas | **Prohibido.** Vacío = error de llenado. |
| Canales | **Permitido** si la adopción es 100% interna y ya está en Segmentos → `N/A interno (ver Segmentos)`. |
| Flujos de ingreso | **Permitido** en MVP operativo sin cobro → `N/A operativo`. |
| Ventaja especial | **Permitido** → `ninguna aún` + `pendiente_campo` o hipótesis débil explícita. |

Si N/A aparece en un bloque prohibido, reescribir el bloque; no dejarlo vacío disfrazado.

## Preguntas por bloque

| Bloque | Preguntas |
|--------|-----------|
| Problema | ¿Top 1–3 dolores del usuario del MVP? ¿Alternativas actuales (cuaderno, WhatsApp, Excel)? |
| Segmentos | ¿Quién usa el entregable día a día? ¿Quién decide adoptarlo? |
| UVP | ¿Qué promesa única cumple el MVP vs status quo? |
| Solución | ¿Qué artefactos concretos entrega el MVP N? (¿igual al Prototype?) |
| Canales | ¿Cómo llega el prototipo a los usuarios internos? |
| Ingresos | ¿Hay ingreso directo o solo valor operativo? |
| Costos | ¿Tiempo, herramientas, capacitación del piloto? |
| Métricas | ¿Cómo sabemos que el criterio de éxito se cumple? |
| Ventaja | ¿Qué no puede copiar un POS genérico en *este* contexto? |

## Salida mínima

Tabla de 9 bloques en la sección semántica **Lean Canvas** de `mvp-N.md`. El **número** (`## N`) lo asigna el orquestador (no hardcodear).
