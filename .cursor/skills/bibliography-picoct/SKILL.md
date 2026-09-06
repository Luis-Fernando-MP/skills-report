---
name: bibliography-picoct
description: >-
  Build PICO/PICOC/PICOCT framework from project profile, debate controlled
  keywords (EN/ES) with critico-estricto and defensor-fundamento, write
  bibliography/<MARCO>/picoct.md, keywords.md, debate.md with Scopus equations.
  Use when user says bibliography-picoct.
---

# bibliography-picoct

Arma el **marco de búsqueda bibliográfica** (PICO / PICOC / **PICOCT** default) para un proyecto en `docs/content/<FOLDER>/`.

**SoT del cómo:** `common/bibliography-picoct/model1.md`. Seguir ese playbook al pie.

## Layout

```text
docs/content/<FOLDER>/
  profile.md
  bibliography/
    PICOCT/              # o PICO | PICOC
      picoct.md          # marco lleno
      keywords.md        # tabla EN|ES + ecuaciones Scopus
      debate.md          # acta crítico ↔ defensor
```

## Invoke

```text
/bibliography-picoct PASS
/bibliography-picoct PASS PICOC
/bibliography-picoct PASS PICO
```

Sin arg de marco → **PICOCT**.

Sin `profile.md` → pedir **init-project** primero.

## Procedure

1. Resolver `FOLDER`; leer `profile.md`. Si existe **`## Marco PICOCT`**, usarlo como base del marco (no reinventar). Opcional: `config.tools["mvp-"+mvp]` solo como contexto de dominio — **no** pegar artefactos enteros.
2. Leer playbook `common/bibliography-picoct/model1.md`.
3. Si existe `bibliography/<MARCO>/` con archivos → **preguntar** antes de sobrescribir.
4. Escribir **`picoct.md`**: desde Marco PICOCT del profile (filtrando componentes según PICO/PICOC/PICOCT) o construir si falta; completar `pendiente_campo` sin inventar empresa.
5. Proponer keywords candidatas EN/ES por componente (controladas; ver playbook).
6. **Debate** (Task / agentes), modo `keywords_picoct`:
   - `critico-estricto` — ataca inventadas / ruido / localismos; WebSearch ≤3.
   - Luego o en paralelo con ataques en prompt: `defensor-fundamento` — evidencia o `punto_debil`; WebSearch ≤3.
7. Consolidar (desempate `candidato_débil` según playbook); checklist de sintaxis de ecuaciones; escribir **`debate.md`** y **`keywords.md`**.
8. Chat: paths, marco, años T, keywords descartadas, componentes `pendiente_campo`, siguiente paso (CSV manual / auto — draft).

## Formato esperado `keywords.md` (resumen)

1. Tabla `| Componente | Keywords (EN) | Keywords (ES) |`
2. `## Ecuaciones de búsqueda`
   - `### Scopus (English)` — bloques `TITLE-ABS-KEY (… OR …)` unidos por `AND` + filtros T
   - `### Scopus (Español)` — análogo

## Forbidden

- Ignorar el playbook.
- Inventar keywords sin debate / sin verificación.
- Usar `config.playbooks` o nombres de empresa como eje único de la query.
- Ejecutar make-informe, Graphify, o skills de CSV/auto aquí.
- Sobrescribir en silencio.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../agents/defensor-fundamento.md)

CONTEXTO mínimo al lanzarlos:

```text
modo: keywords_picoct
FOLDER / MARCO
bloque: componentes PICOCT llenos + lista candidata EN/ES por componente
objetivo: keywords usadas en literatura; no inventar
```
