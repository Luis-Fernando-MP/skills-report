---
name: init-project-mvp
description: >-
  After init-project, run Design Thinking + Lean Canvas + RAT + FODA for the
  indicated MVP (mvp-N or config.mvp) and write design-thinking/mvp-N.md.
  Use when user says init-project-mvp.
---

# init-project-mvp

Cuarto paso de la familia **init-***: deja **listo** un MVP del proyecto académico (no reabre el tema).

## Layout

```text
docs/content/<FOLDER>/
  config.json                 # incluye "mvp": N
  profile.md                  # debe traer ## MVP entregables
  design-thinking/
    mvp-1.md                  # salida de esta skill
    mvp-2.md                  # si se invoca otro N
```

## Invoke

```text
/init-project-mvp PASS mvp-1
```

```text
Usa init-project-mvp
Carpeta: PASS
MVP: 1
```

Sin `profile.md` o sin sección MVP entregables → pedir **init-project** (desde polish) primero.

## Resolución de N

1. Arg explícito `mvp-N` / `MVP: N` del usuario.
2. Si no → `config.mvp`.
3. Si no → `1`.

Tras escribir el archivo, actualizar `config.mvp` = N.

## Procedure

1. Resolver `docs/content/<FOLDER>/`.
2. Leer `profile.md` + `config.json`; extraer el bloque del MVP N (objetivo, entregables, criterio de éxito). Si N no está en la secuencia del profile → preguntar.
3. Si `design-thinking/mvp-<N>.md` existe → preguntar antes de sobrescribir.
4. Crear `design-thinking/` si falta.
5. Lanzar agente **`design-thinking`** con CONTEXTO + bloque MVP N (no reabrir tema; no inventar hechos de empresa).
6. Escribir `design-thinking/mvp-<N>.md`:

```markdown
# MVP ready — MVP N — [FOLDER]

## Contexto del MVP (desde profile)
…

## 1. Design Thinking
### Empathize
### Define
### Ideate
### Prototype
### Test

## 2. Lean Canvas
…

## 3. Mapa de supuestos (RAT)
…

## 4. FODA del MVP
…

## Listo para
trabajo de campo / prototipo; opcional `graphify-project` si se indexa este md
```

7. Persistir `config.mvp` = N.
8. Chat: path + POV/HMW + top supuesto RAT + recordatorio de `config.mvp`.

## Forbidden

- Reabrir debate de tema / cambiar núcleo del polish.
- Inventar hechos de empresa.
- BMC Osterwalder completo o VPC largo (Lean Canvas basta).
- Escribir otros MVPs no pedidos.
- Regenerar Graphify / tocar RSL.
- Soft consensus sin etiquetar hipótesis vs evidencia.
