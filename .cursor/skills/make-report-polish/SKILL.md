---
name: make-report-polish
description: >-
  Polish the latest make-report draft into reporte.md + reporte-debate.md with
  7 agents (critico, defensor, impacto, viabilidad, inversor, gramatica-continuidad,
  revisor-cientifico). Never edits draft.md. Use when user says make-report-polish.
---

# make-report-polish

Pule el **último** `draft.md` de `make-report` en un informe profesional limpio. El draft **no se toca**.

**SoT del cómo:** `common/make-report-polish/model1.md`. Seguir ese playbook al pie (incluye **gate anti-genérico**).

**Polish = más claro y breve, no más genérico.** Conservar nombres, fechas, vendors, cifras y matices del draft (salvo corrección factual). Si el draft falló en FODA/Lean (sujeto PoC), el **reporte** debe corregirlo.

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

Sin draft usable → pedir **make-report** primero.

Resolución del draft (en orden):

1. Última entrada con `has_draft: true` en `docs/reports-trace.json`, o
2. `config.tools["make-report"].last` si apunta a un `draft.md` existente.

Si hay draft vía `last` pero **no** hay trace → crear/actualizar `docs/reports-trace.json` al cerrar el polish (misma versión del draft).

## Lookup Graphify

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json` (+ `company.md` si aplica).
2. Leer `common/make-report-polish/model1.md`.
3. Resolver draft; **extraer lista de anclas** (nombres propios, fechas, RUC, vendors) del draft.
4. Round 1 (5): critico, defensor, impacto, viabilidad, **inversor** — crítico ataca FODA/Lean sujeto, pérdida de sustancia, reseña delgada.
5. Round 2: cruce; si FODA/Lean mal → corregir en borrador.
6. Orquestador: borrador `reporte.md` (misma estructura; prosa limpia **con** anclas).
7. **Gate anti-genérico** (playbook 4b). Fallo → reescribir antes de R3.
8. Round 3: `gramatica-continuidad` + `revisor-cientifico` (`modo: make_report_polish`); revisor compara draft vs borrador.
9. Escribir `reporte-debate.md` **con sustancia** (≥3 Q&A, ataques, gate) + `reporte.md`; actualizar trace; `config.tools["make-report-polish"].last`.
10. `pnpm graphify:project -- <FOLDER>`.
11. Chat: paths, veredicto **honesto**, anclas conservadas, tesis de valor, TODOs residuales.

## Forbidden

- Editar `draft.md`.
- Pulir versión que no sea la última del trace.
- Inventar fuentes; graphify-root.
- Soft consensus vacío.
- Vaciar sustancia / quitar vendors “para limpio”.
- Acta scorecard-only o mermaid solo del pipeline de skills.

## Agentes

- [`.cursor/agents/critico-estricto.md`](../../agents/critico-estricto.md)
- [`.cursor/agents/defensor-fundamento.md`](../../agents/defensor-fundamento.md)
- [`.cursor/agents/impacto-social.md`](../../agents/impacto-social.md)
- [`.cursor/agents/viabilidad-mvp.md`](../../agents/viabilidad-mvp.md)
- [`.cursor/agents/inversor.md`](../../agents/inversor.md)
- [`.cursor/agents/gramatica-continuidad.md`](../../agents/gramatica-continuidad.md)
- [`.cursor/agents/revisor-cientifico.md`](../../agents/revisor-cientifico.md)
