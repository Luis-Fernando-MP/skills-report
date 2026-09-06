# FODA del MVP — model1

FODA del **movimiento del MVP N** + **matriz cruzada (TOWS)** para pasar de lista a acción. Alineado a curso ITD S03.

**Pedagogía vs salida:** este archivo enseña al orquestador. La salida `foda.md` es matriz visual **del caso** (como plantilla FODA 2×2), no tutorial.

## Posición en el pipeline

Después de Lean; antes de RAT. Pase FODA: solo `→ candidato RAT`. Post-RAT: orquestador amarra `→ R#` (cuadrantes **y** celdas TOWS).

## Propósito

Foto del presente (interno/externo × ayuda/perjudica) y **cuatro tipos de estrategia** al cruzar.

## Layout de salida (SoT visual)

El FODA se presenta como **cuadrante 2×2** (plantilla tipo imagen FODA), **no** como lista suelta ni como una sola columna rota con `\n` literales.

```text
┌─────────────────┬─────────────────┐
│ FORTALEZAS      │ DEBILIDADES     │
│ (interno/ayuda) │ (interno/perj.) │
├─────────────────┼─────────────────┤
│ OPORTUNIDADES   │ AMENAZAS        │
│ (externo/ayuda) │ (externo/perj.) │
└─────────────────┴─────────────────┘
```

### Opción A — una tabla 2×2 (preferida)

```markdown
## FODA

| Fortalezas | Debilidades |
|------------|-------------|
| - … `etiqueta` | - … `etiqueta` → candidato RAT |

| Oportunidades | Amenazas |
|---------------|----------|
| - … | - … → candidato RAT |
```

### Opción B — cuatro tablas (una por cuadrante)

```markdown
### Fortalezas
| Ítem |
|------|
| - … |

### Debilidades
| Ítem |
|------|
| - … |

### Oportunidades
| Ítem |
|------|
| - … |

### Amenazas
| Ítem |
|------|
| - … |
```

Usar **A** por defecto; **B** solo si el contenido de cada celda es muy largo.

Luego **TOWS** (obligatorio) y amarre post-RAT.

### TOWS

```markdown
## TOWS

| | Oportunidades (O) | Amenazas (A) |
|--|-------------------|--------------|
| **Fortalezas (F)** | **FO:** … → candidato RAT / Prototype | **FA:** … → candidato RAT |
| **Debilidades (D)** | **DO:** … → Prototype | **DA:** … → candidato RAT |
```

### Amarre post-RAT (si hubo RAT)

Reescribir **todos** los `→ candidato RAT` de cuadrantes **y** TOWS a `→ R#`. Añadir tabla breve:

| Candidato (texto corto) | R# |
|-------------------------|----|
| … | R1 |

## Reglas

1. Máx. 3–4 bullets/cuadrante; etiquetas evidencia.
2. Prohibido FODA corporativo genérico no ligado al MVP.
3. Pase pre-RAT: Amenazas/Debilidades de alto impacto → `→ candidato RAT` (nunca `R#` aún).
4. Al menos **1 estrategia** FO / FA / DO / DA, accionable en el piloto.
5. Cada estrategia TOWS enlaza a `→ candidato RAT` / `→ Prototype` / `→ DT Test`.
6. **Markdown válido:** celdas con saltos reales o `<br>` / bullets `-`; **nunca** la secuencia literal `\n` dentro del archivo.
7. Implicación final (1 frase) = estrategia TOWS prioritaria de la semana.

## Salida mínima

Archivo `foda.md`: FODA 2×2 (opción A o B) + TOWS + amarre post-RAT si hubo RAT + implicación. Número = orquestador.
