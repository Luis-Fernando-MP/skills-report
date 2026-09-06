# Draft — skills futuras (aún no creadas)

Diseño pendiente. **No** existen como `.cursor/skills/` todavía.

Orden sugerido: `prepare-bibliography-manual` → `prepare-bibliography-automatic` → `make-informe`.

---

## `make-informe` (nombre preferido; alt. `make-structure`)

Genera el informe académico según el índice (structure) y el `config` del proyecto.

### Inputs

- `docs/content/<FOLDER>/config.json`
- Índice: `structure.md` local (override) **o** path `config.modelo`
- `config.citation_style` → `common/citation-style/*.md`
- `config.mvp` (activo) → artefactos en `config.tools["mvp-" + N]`
- `config.alcance`

### `alcance`

| Valor | Efecto |
|-------|--------|
| `[]` o entrada con `"*"` a nivel global | Todo el índice |
| `[{ "capitulo": "1", "secciones": ["*"] }]` | Solo capítulo 1, todas sus secciones |
| `[{ "capitulo": "1", "secciones": ["1.1", "1.2"] }]` | Cap. 1, nodos 1.1 y 1.2 **y todo lo anidado** (1.1.1, …). No escribe hermanos no listados |

Si `secciones` falta → tratar como `["*"]`.

### Tools en el informe

Pegar / reutilizar contenido de `tools["mvp-N"]` **solo** si el índice pide ese artefacto (p. ej. Lean Canvas en 1.3.1). Si no lo pide, no insertar. Nada de más, nada de menos respecto al structure.

### Salida

```text
docs/content/<FOLDER>/informe/<mvp>/
  informe-<DD-MM-YYYY>-<capitulo|completo>-vN.md
```

- `<mvp>` = número activo (`config.mvp`)
- Fecha = día de ejecución
- Sufijo: `completo` si alcance es todo; si un solo capítulo → `cap-1` (o similar); varios → convención a fijar al implementar
- Versionado: si ya existe `…-v1.md`, crear `v2`, … — **nunca sobrescribir**

### Forbidden (borrador)

- Inventar hechos de empresa
- Usar playbooks common como cuerpo del informe (solo tools generados + profile + bib)
- Crear skill hasta que se apruebe este draft

---

## `prepare-bibliography-manual`

Paso previo: el usuario aporta CSV export (Scopus / WoS / etc.).

### Qué crea la skill

```text
docs/content/<FOLDER>/bibliography/
  manual/
    document.csv    # cabeceras + vacío (usuario pega filas)
    picoct.md       # esqueleto PICO/PCT (a definir al implementar)
```

### Cabeceras CSV (desde `header.md`, recorte propuesto)

**Incluir:** Author(s), Document title, Year, EID, Source title, Volume/issues/pages, Citation count, Source & document type, Publication stage, DOI, Open access, Abstract, Author keywords, Indexed keywords.

**Omitir por defecto (ruido):** Affiliations, Serial identifiers, PubMed ID, Publisher, Editor(s), Language, Correspondence address, Abbreviated source title, Number, Acronym, Sponsor, Funding text — salvo que el usuario pida ampliar.

La skill **no** busca papers; solo prepara carpeta + CSV + picoct.

---

## `prepare-bibliography-automatic`

Tras el manual (o en paralelo si no hay CSV): buscar **≥5** fuentes en bases reconocidas (Scopus, IEEE, Web of Science, etc.), con criterio alineado a profile / PICO.

Detalle de queries, filtros y formato de salida: **TBD** al implementar.

---

## Notas abiertas

- ¿`picoct.md` es PICO + criterios de inclusión/exclusión?
- ¿Cabeceras CSV idénticas a export Scopus o normalizadas?
- ¿make-informe escribe un md por capítulo o un solo archivo según alcance? (hoy: un archivo versionado según alcance)
