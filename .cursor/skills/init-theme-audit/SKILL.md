---
name: init-theme-audit
description: >-
  Audit one user-proposed theme: company research when required, brainstorm-theme
  (ángulos), benchmark-theme; write theme-audit-brainstorm.md and theme-audit.md.
  Use when user says init-theme-audit or already has a concrete tema/empresa/alcance.
---

# init-theme-audit

Rama de la familia **init-*** cuando **ya tienes un tema propuesto** (no exploras 3 alternativas).

Siguiente skill: **`init-theme-audit-polish`**.

Contraste:

| Skill | Input | Salida |
|-------|--------|--------|
| `init-theme` | 3–4 tópicos abiertos | `theme-brainstorm.md` + `theme.md` (3 alts) |
| `init-theme-audit` | **1 tema** ya planteado | `theme-audit-brainstorm.md` + `theme-audit.md` |

## Layout

```text
docs/topics/<FOLDER>/
  theme-audit-brainstorm.md   # acta lluvia (esta skill)
  theme-audit.md              # tema afinado + ficha + benchmark (esta skill)
  theme-audit-debate.md       # init-theme-audit-polish
  theme-audit-polish.md       # init-theme-audit-polish
```

Al re-ejecutar: **sobrescribir** `theme-audit-brainstorm.md` y `theme-audit.md` sin preguntar.

## Invoke

```text
Usa init-theme-audit

Carpeta: ITD
Tema: …
Descripción: …
Problema: …
Alcance: …
Empresa: …   # si el tema es de una organización real
```

Sin tema → preguntar. No inventar empresa ni hechos no dados / no hallados en fuentes públicas.

## Clasificación del sujeto (obligatoria, antes de todo)

| `tipo_sujeto` | Cuándo | Investigación de empresa |
|---------------|--------|---------------------------|
| `empresa` / `entidad` | Organización real (Komatsu, municipalidad, hospital…) | **Obligatoria** — sin ficha pública usable no seguir como si hubiera empresa |
| `dominio_sin_empresa` | Problema de dominio sin org. ancla | Declarar N/A; no inventar empresa |
| `ficticio` | Usuario pide empresa inventada | Solo si lo dice; no fingir fuentes |

**Regla dura:** si el tema nombra empresa/entidad real → investigar **primero**. Reseña histórica pública ≠ AS-IS operativo interno.

## Investigación de empresa / entidad (si `tipo_sujeto` = empresa|entidad)

**Antes** del brainstorm, con WebSearch / sitios oficiales / reportes públicos:

1. Identidad (nombre legal, país, sector, escala pública).
2. Reseña histórica (fundación, hitos) con fuentes.
3. Misión, visión, valores publicados.
4. Oferta / líneas relevantes al tema.
5. Presencia geográfica **solo** con fuente.
6. Lista de **Fuentes**.

Si no hay evidencia mínima → `evidencia_empresa: insuficiente` o pedir aclaración (no inventar).

## Procedure

1. Leer tema (+ descripción, problema, alcance, empresa, carpeta).
2. **Clasificar `tipo_sujeto`**.
3. Si empresa/entidad → **investigación de empresa**.
4. **Resolver `FOLDER`:** código o slug; crear carpeta si falta.
5. Armar CONTEXTO con `modo: una_alternativa` + resumen ficha.
6. Lanzar **`brainstorm-theme`** (ángulos del mismo tema) → escribir **`theme-audit-brainstorm.md`**.
7. Lanzar **`benchmark-theme`** con CONTEXTO + tema + ficha + ángulos. Si evidencia insuficiente → proxies en el md.
8. Escribir **`theme-audit.md`** bien definido (plantilla abajo).
9. No lanzar polish aquí.
10. Chat: paths + `tipo_sujeto` + resumen → **`init-theme-audit-polish`**.

### Plantilla `theme-audit-brainstorm.md`

```markdown
# Brainstorm de auditoría — [FOLDER]

## CONTEXTO
- modo: una_alternativa
- tipo_sujeto: …
- empresa: … | N/A

## Tema de entrada
…

## Acta (brainstorm-theme)
… (lentes + ángulos/variantes del mismo tema)
```

### Plantilla `theme-audit.md`

```markdown
# Auditoría de tema — [FOLDER]

## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: diagnostico | informe | mvp | producto
- restricciones: …
- modo: una_alternativa
- tipo_sujeto: empresa | entidad | dominio_sin_empresa | ficticio
- empresa: …   # si dominio_sin_empresa → N/A + justificación breve

## Tema propuesto (entrada)
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …

## Ficha de empresa (investigación)
*(Obligatoria si tipo_sujeto = empresa|entidad. Omitir si dominio_sin_empresa.)*
**Identidad:** …
**Reseña histórica (pública):** …
**Misión / visión / valores:** …
**Oferta / sector relevante:** …
**Evidencia_empresa:** suficiente | insuficiente
**Fuentes de empresa:** …

## Brainstorm
Acta: theme-audit-brainstorm.md — ángulos retenidos: …

## Benchmarking (`benchmark-theme`)
**Casos (directo|proxy):** …
**Mini-matriz:** … (o omitida — evidencia insuficiente)
**Qué adaptar:** …
**Diferenciador posible:** …
**Evidencia:** suficiente | insuficiente

## Tema afinado (pre-polish)
*(Ajustes tras brainstorm + benchmark; sin inventar hechos de empresa.)*
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …

## Fuentes
- …
```

## Forbidden

- Generar 3 alternativas sueltas (usa **init-theme**).
- Inventar empresas/casos / datos no hallados.
- Saltar investigación cuando hay empresa real.
- Skills externas competitive-analysis / brainstorm ajenas.
- Lanzar crítico/defensor/impacto/viabilidad aquí.
- Escribir en `docs/content/` (**init-project**).
- Regenerar Graphify.
