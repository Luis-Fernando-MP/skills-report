# Draft — skills futuras / estado bibliography

## Hecho

### `bibliography-picoct`

- Playbook: [`common/bibliography-picoct/model1.md`](common/bibliography-picoct/model1.md)
- Skill: [`.cursor/skills/bibliography-picoct/SKILL.md`](.cursor/skills/bibliography-picoct/SKILL.md)
- Salida: `bibliography/<PICO|PICOC|PICOCT>/{picoct,keywords,debate}.md`

Orden actual: **bibliography-picoct** → (manual | auto) → **make-informe**.

---

## Pendiente — no crear skill aún

### `make-informe`

Genera el informe según structure + config.

**Inputs:** `config.json`, índice (`structure.md` override o `config.modelo`), `citation_style`, `mvp`, `tools["mvp-N"]`, `alcance`.

**Alcance:** `[]` / `*` = todo; `{ capitulo, secciones: ["*"] | ["1.1",…] }` con prefijo inclusivo.

**Tools:** pegar solo si el índice lo pide.

**Salida:** `informe/<mvp>/informe-<DD-MM-YYYY>-<capitulo|completo>-vN.md` (nunca sobrescribe: v1, v2…).

### `prepare-bibliography-manual` (nombre TBD)

```text
bibliography/manual/document.csv   # cabeceras Scopus (ver header.md)
bibliography/manual/…              # usuario puebla filas
```

Cabeceras útiles: Author(s), Document title, Year, EID, Source title, Volume/issues/pages, Citation count, Source & document type, Publication stage, DOI, Open access, Abstract, Author keywords, Indexed keywords.

### `prepare-bibliography-automatic` (nombre TBD)

≥5 fuentes en Scopus/IEEE/WoS usando ecuaciones de `keywords.md`. Detalle TBD.

---

## Notas abiertas

- ¿Nombre final manual/auto?
- ¿make-informe un md por capítulo o uno solo según alcance? (hoy: un archivo versionado)
