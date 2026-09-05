---
name: init-theme-audit
description: >-
  Audit one user-proposed theme: run benchmark-theme on that single topic and
  write docs/topics/<FOLDER>/theme-audit.md. Use when user says init-theme-audit
  or already has a concrete tema/empresa/alcance.
---

# init-theme-audit

Rama de la familia **init-*** para cuando **ya tienes un tema propuesto** (no exploras 3 alternativas).

Contraste:

| Skill | Input | Salida |
|-------|--------|--------|
| `init-theme` | 3–4 tópicos abiertos | `theme.md` (3 alts) |
| `init-theme-audit` | **1 tema** ya planteado | `theme-audit.md` (tema único + benchmark) |

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
Tema: Digitalización del inventario y estandarización de tallaje en Calzados Romantex S.A.C
Descripción: …
Problema: …
Alcance: …
Empresa: …   # opcional
```

Sin tema → preguntar. No inventar empresa ni hechos no dados.

## Procedure

1. Leer tema (+ descripción, problema, alcance, empresa, carpeta si vienen).
2. **Resolver `FOLDER`:** código del usuario (`ITD`) o slug corto; si ya existe `theme-audit.md`, preguntar antes de sobrescribir.
3. Crear `docs/topics/<FOLDER>/` si falta.
4. Armar **CONTEXTO** con `modo: una_alternativa`.
5. Lanzar **solo** `benchmark-theme` con CONTEXTO + el tema único (no 3 alternativas). Si `evidencia: insuficiente`, reflejar proxies en el md.
6. Escribir **`theme-audit.md`**:

```markdown
# Auditoría de tema — [FOLDER]

## CONTEXTO
- dominio: …
- pais_region: …
- fase_entregable: diagnostico | informe | mvp | producto
- restricciones: …
- modo: una_alternativa
- empresa: …   # si aplica

## Tema propuesto (entrada)
**Tema:** …
**Descripción:** …
**Problema identificado:** …
**Alcance:** …

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

7. No lanzar el panel de 4 agentes (eso es **init-theme-audit-polish**).
8. Chat: path + resumen del benchmark + siguiente skill **`init-theme-audit-polish`**.

## Forbidden

- Generar 3 alternativas (usa **init-theme**).
- Inventar empresas/casos del benchmark.
- Lanzar crítico/defensor/impacto/viabilidad aquí.
- Escribir en `docs/content/` (**init-project**).
- Tocar skills `rsl-*` / regenerar Graphify.
