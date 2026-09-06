---
name: make-report
description: >-
  Draft a versioned academic report under docs/content/<FOLDER>/docs/vN-tag/draft.md
  from config.modelo + alcance, using Graphify during writing and bibliographic-search
  for TODO: citar gaps. Alias make-informe. Use when user says make-report or make-informe.
  Not rsl-make-report.
---

# make-report

Redacta un **draft versionado** del informe del proyecto académico en `docs/content/<FOLDER>/` según `config.modelo` y `config.alcance`.

**SoT del cómo:** `common/make-report/model1.md`. Seguir ese playbook al pie.

**Alias:** `make-informe` → esta skill. **No** es `rsl-make-report`.

## Salida

```text
docs/content/<FOLDER>/docs/v<N>-<tag>/draft.md
```

| Alcance | tag típico |
|---------|------------|
| `[]` / completo | `completo` |
| solo cap. 1 | `capitulo-1` |
| caps. 1–2 | `capitulo-1-2` |

Nueva versión en cada run (nunca sobrescribir). **Referencias** siempre al final.

## Invoke

```text
/make-report
/make-report DS
/make-informe DS
```

Sin `profile.md` → pedir **init-project**.

## Lookup Graphify (durante redacción)

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

No volcar PDFs/MD al contexto. Preferir findings + `src` + página.

## Procedure

1. Resolver `FOLDER`; leer `profile.md` + `config.json`.
2. Leer `common/make-report/model1.md` + playbook de `citation_style`.
3. Resolver índice: `structure.md` local útil → override; si no → `config.modelo`.
4. Filtrar outline por `alcance` (`[]` = todo). Decidir `vN-tag`.
5. Graphify query mientras se redacta (profile, bib, MVP activo si aplica).
6. Tools `mvp-N` **solo** si el outline lo pide — integrar, no volcar.
7. Escribir `docs/vN-tag/draft.md`. Huecos → `TODO: citar — …`.
8. Registrar `config.tools["make-report"].last`; `pnpm graphify:project -- <FOLDER>`.
9. Si hay TODOs de citación → **bibliographic-search** → reemplazar → Graphify otra vez.
10. Chat: path draft, secciones, TODOs restantes, search sí/no.

## Forbidden

- `rsl-make-report` / informe bajo `docs/[titulo-breve]/`.
- Draft fuera de `docs/vN-tag/`; sobrescribir versión.
- Inventar fuentes; omitir Referencias; volcar MVP entero.
- Guardar search en `bibliography/`; graphify-root / graphify-theme.
