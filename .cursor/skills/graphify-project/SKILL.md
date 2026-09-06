---
name: graphify-project
description: >-
  Create or refresh Graphify memory for one docs/content/{FOLDER} academic
  project (profile, structure/modelo, course notes). Use when user says
  graphify-project.
---

# graphify-project

Memoria **por proyecto** en `docs/content/<FOLDER>/graphify-out/` para consultar apuntes y perfil sin releer todo.

## Flujo

```text
A prepare → (B agent headings si needs_agent) → C build → D verify
```

| Stage | Comando |
|-------|---------|
| **A** | `pnpm graphify:project -- <FOLDER> --prepare-only` |
| **B** | Enriquecer `##`/`###` en apuntes pobres; luego stamp |
| **C+D** | `pnpm graphify:project -- <FOLDER>` |

## Corpus

- `profile.md`
- `structure.md` local **o** `common/structure/{config.modelo}.md`
- `docs/**/*.{md,qmd}` (apuntes del curso)
- `bibliography/auto/docs.md` + `bibliography/docs/**/*.md` (fuentes de **bibliography-auto**)
- Manifest: `docs/content/<FOLDER>/index-manifest.json`
- Copias resueltas (qmd / modelo): `graphify-out/_corpus/` (gitignored)

## Procedure

1. Resolver `FOLDER` (`docs/content/<FOLDER>/`). Preguntar si falta.
2. **A** — `pnpm graphify:project -- <FOLDER> --prepare-only`
3. Si exit 2 / `needs_agent`:
   - Añadir headings reales al md/qmd (o al `index_md` en `_corpus`).
   - Stamp:
     ```bash
     ~/.local/share/pipx/venvs/graphifyy/bin/python \
       scripts/graphify-project-offline.py docs/content/<FOLDER> \
       --stamp-agent "docs/S01/nota.md" \
       --stamp-notes "agent-rag"
     ```
4. **C+D** — `pnpm graphify:project -- <FOLDER>` (exit 0).
5. Chat: path del grafo, nodos, skipped vs nuevos, `needs_agent` restantes.

`--force` solo si el usuario pide rebuild total.

## Lookup

```bash
graphify query "<q>" --graph docs/content/<FOLDER>/graphify-out/graph.json
graphify explain "<concept>" --graph docs/content/<FOLDER>/graphify-out/graph.json
```

Papers de **bibliography-auto** llevan finding hooks EN + alias ES y locators `[PDF p.N]` en el MD. Preferir queries con términos del paper (EN o ES). **No** abrir el PDF a mano si Graphify ya devolvió `src` + nodo Finding/Hallazgo + página.

Preferir este grafo para profile / structure / apuntes / bib-auto del proyecto. Root → **graphify-root**. Temas RSL legado → **graphify-theme**.

`--force` regenera y re-enriquece MD de bib-auto.

## Forbidden

- Refresh root o theme desde esta skill.
- Skip verify.
- Re-indexar entradas `graphify_indexed` con mismo hash sin `--force`.
- Inventar contenido del grafo si el build falla.
