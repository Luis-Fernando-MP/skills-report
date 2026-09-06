---
name: init-theme-audit
description: >-
  Audit one user-proposed theme: research company/entity when required, run
  benchmark-theme on that single topic, write docs/topics/<FOLDER>/theme-audit.md.
  Use when user says init-theme-audit or already has a concrete tema/empresa/alcance.
---

# init-theme-audit

Rama de la familia **init-*** para cuando **ya tienes un tema propuesto** (no exploras 3 alternativas).

Contraste:

| Skill | Input | Salida |
|-------|--------|--------|
| `init-theme` | 3–4 tópicos abiertos | `theme.md` (3 alts) |
| `init-theme-audit` | **1 tema** ya planteado | `theme-audit.md` (tema único + benchmark + ficha empresa si aplica) |

## Layout

```text
docs/topics/<FOLDER>/
  theme-audit.md           # esta skill
  theme-audit-debate.md    # init-theme-audit-polish
  theme-audit-polish.md    # init-theme-audit-polish
```

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

Clasificar el tema en **una** de estas:

| `tipo_sujeto` | Cuándo | Investigación de empresa |
|---------------|--------|---------------------------|
| `empresa` / `entidad` | Hay razón social u organización real (Komatsu, Romantex, municipalidad, hospital…) | **Obligatoria** — sin ficha pública usable **no hay informe** (NO seguir como si hubiera empresa) |
| `dominio_sin_empresa` | El problema es de dominio/territorio sin org. ancla (p. ej. IA predictiva de sismos en Lima) | **No** — declarar por qué no aplica; historia/misión corporativa N/A |
| `ficticio` | El usuario pide explícitamente empresa inventada | Solo si el usuario lo dice; marcar `ficticio: true` y no fingir fuentes |

**Regla dura:** si el tema nombra una empresa/entidad real → investigar **primero**. Mezclar “no hay AS-IS interno” con “no hay reseña histórica pública” está **prohibido**: son cosas distintas. La reseña global pública **sí** se documenta cuando la empresa existe.

## Investigación de empresa / entidad (si `tipo_sujeto` = empresa|entidad)

**Antes** del benchmark, con WebSearch / sitios oficiales / reportes integrados públicos:

1. Identidad (nombre legal, país, sector, escala pública).
2. Reseña histórica (fundación, hitos, expansión) con fuentes.
3. Misión, visión, valores / principios de gestión publicados.
4. Oferta / líneas de negocio relevantes al tema (p. ej. partes/aftermarket).
5. Presencia geográfica o filiales **solo** si hay fuente pública.
6. Lista de **Fuentes** (URLs oficiales / reportes).

Escribir en `theme-audit.md` la sección **`## Ficha de empresa (investigación)`**.  
Si no se encuentra evidencia mínima (identidad + historia o identidad corporativa oficial) → detenerse y pedir al usuario aclaración o declarar `evidencia_empresa: insuficiente` (no inventar).

## Procedure

1. Leer tema (+ descripción, problema, alcance, empresa, carpeta).
2. **Clasificar `tipo_sujeto`** (tabla arriba).
3. Si empresa/entidad → **investigación de empresa** (bloque anterior) → sección ficha.
4. **Resolver `FOLDER`:** código del usuario o slug; si ya existe `theme-audit.md`, preguntar antes de sobrescribir.
5. Crear `docs/topics/<FOLDER>/` si falta.
6. Armar **CONTEXTO** con `modo: una_alternativa` + `tipo_sujeto` + resumen ficha (si hay).
7. Lanzar **solo** `benchmark-theme` con CONTEXTO + el tema único. Si `evidencia: insuficiente`, reflejar proxies en el md.
8. Escribir **`theme-audit.md`**:

```markdown
# Auditoría de tema — [FOLDER]

## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: diagnostico | informe | mvp | producto
- restricciones: …
- modo: una_alternativa
- tipo_sujeto: empresa | entidad | dominio_sin_empresa | ficticio
- empresa: …   # si aplica; si dominio_sin_empresa → N/A + justificación breve

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

## Benchmarking
**Casos (directo|proxy):** …
**Qué adaptar:** …
**Diferenciador posible:** …
**Evidencia:** suficiente | insuficiente

## Tema afinado (pre-polish)
*(Ajustes mínimos tras benchmark; sin inventar hechos de empresa.)*
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …

## Fuentes
- …
```

9. No lanzar el panel de 4 agentes (eso es **init-theme-audit-polish**).
10. Chat: path + `tipo_sujeto` + resumen ficha/benchmark + siguiente **`init-theme-audit-polish`**.

## Forbidden

- Generar 3 alternativas (usa **init-theme**).
- Inventar empresas/casos / datos corporativos no hallados.
- Saltar la investigación cuando hay empresa real.
- Lanzar crítico/defensor/impacto/viabilidad aquí.
- Escribir en `docs/content/` (**init-project**).
- Tocar skills `rsl-*` / regenerar Graphify.
