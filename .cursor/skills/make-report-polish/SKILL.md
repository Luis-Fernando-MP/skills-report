---
name: make-report-polish
description: >-
  Polish the latest make-report draft into reporte.md + reporte-debate.md with
  7 agents (critico, defensor, impacto, viabilidad, inversor, gramatica-continuidad,
  revisor-cientifico). Never edits draft.md. Use when user says make-report-polish.
---

# make-report-polish

Pule el **último** `draft.md` de `make-report` en un informe profesional limpio. El draft **no se toca**.

**SoT del cómo:** `common/make-report-polish/model1.md`. Seguir ese playbook al pie.

## Salida

```text
docs/content/<FOLDER>/docs/vN-tag/
  draft.md              # read-only
  reporte.md
  reporte-debate.md
```

## Invoke

```text
/make-report-polish
/make-report-polish DDS
```

Sin draft / sin `docs/reports-trace.json` → pedir **make-report** primero.

## Lookup Graphify

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (+ `company.md` si aplica).
2. Leer `common/make-report-polish/model1.md`.
3. Resolver draft vía `docs/reports-trace.json` → **última** entrada `has_draft: true` (o `config.tools["make-report"].last`).
4. Round 1 (5): critico, defensor, impacto, viabilidad, **inversor**.
5. Round 2: cruce; propuestas de valor del inversor; soft-veto (no tumbar solo).
6. Orquestador: borrador de `reporte.md` (misma estructura que draft; prosa limpia).
7. Round 3: `gramatica-continuidad` + `revisor-cientifico`.
8. Escribir `reporte-debate.md` + `reporte.md`; actualizar trace (`has_polish`); `config.tools["make-report-polish"].last`.
9. `pnpm graphify:project -- <FOLDER>`.
10. Chat: paths, tesis de valor, TODOs residuales.

## Forbidden

- Editar `draft.md`.
- Pulir versión que no sea la última del trace.
- Inventar fuentes; graphify-root.
- Soft consensus vacío.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../agents/defensor-fundamento.md)
- [`.cursor/agents/impacto-social.md`](../agents/impacto-social.md)
- [`.cursor/agents/viabilidad-mvp.md`](../agents/viabilidad-mvp.md)
- [`.cursor/agents/inversor.md`](../agents/inversor.md)
- [`.cursor/agents/gramatica-continuidad.md`](../agents/gramatica-continuidad.md)
- [`.cursor/agents/revisor-cientifico.md`](../agents/revisor-cientifico.md)
