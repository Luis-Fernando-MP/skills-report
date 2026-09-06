#!/usr/bin/env node
/**
 * Create empty project mold under docs/content/<FOLDER>.
 * Usage: pnpm project:init <FOLDER>
 * Only argument: folder name. Does not fill profile or interpret topic.
 */
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const folder = (process.argv[2] || '').trim();

const FOLDER_RE = /^[A-Za-z][A-Za-z0-9_-]{0,63}$/;

if (!folder) {
  console.error('Usage: pnpm project:init <FOLDER>\nExample: pnpm project:init MOST');
  process.exit(1);
}

if (!FOLDER_RE.test(folder) || folder.includes('..') || folder.includes('/') || folder.includes('\\')) {
  console.error(
    `Invalid folder name: ${folder}\nUse letters, digits, _ or - (e.g. MOST, FIS-2). No paths.`
  );
  process.exit(1);
}

const projectRel = path.join('docs', 'content', folder);
const projectAbs = path.join(root, projectRel);

if (existsSync(projectAbs)) {
  console.error(`Project already exists: ${projectRel}`);
  process.exit(1);
}

const profileTemplate = `# Perfil del proyecto

## Tema


## Descripción


## Problema identificado


## Alcance


## MVP entregables

### MVP de arranque (recomendado al equipo)


### Secuencia
| MVP | Objetivo | Entregables | Criterio de éxito | Estado |
|-----|----------|-------------|-------------------|--------|
| 1 | | | | se trabaja ahora |

### Fuera de secuencia / descartado


## Origen
- polish:
- veredicto:
`;

const config = {
  citation_style: 'common/citation-style/APA7.md',
  modelo: 'common/structure/model1.md',
  alcance: [],
  mvp: 1,
  playbooks: {
    'design-thinking': 'common/design-thinking/model1.md',
    'lean-canvas': 'common/lean-canvas/model1.md',
    rat: 'common/rat/model1.md',
    foda: 'common/foda/model1.md',
    'as-is-to-be': 'common/as-is-to-be/model1.md',
  },
  tools: {},
};

mkdirSync(path.join(projectAbs, 'docs'), { recursive: true });
writeFileSync(path.join(projectAbs, 'config.json'), JSON.stringify(config, null, 2) + '\n', 'utf8');
writeFileSync(path.join(projectAbs, 'profile.md'), profileTemplate, 'utf8');
writeFileSync(path.join(projectAbs, 'docs', '.gitkeep'), '', 'utf8');

console.log(`PASS: project mold → ${projectRel}`);
console.log(
  '  config.json  (citation_style+modelo paths, playbooks=all model1, tools={}, mvp=1)'
);
console.log('  profile.md   (empty template — mirror polish via init-project)');
console.log('  docs/        (apuntes)');
console.log('  structure.md not created — optional override; else config.modelo path');
process.exit(0);
