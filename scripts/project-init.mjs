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

**Nombre del proyecto:**

**Descripción:**

**Problema identificado:**

**Alcance de la propuesta:**
`;

const config = {
  citation_style: 'APA7',
  modelo: 'model1',
  alcance: [],
};

mkdirSync(path.join(projectAbs, 'docs'), { recursive: true });
writeFileSync(path.join(projectAbs, 'config.json'), JSON.stringify(config, null, 2) + '\n', 'utf8');
writeFileSync(path.join(projectAbs, 'profile.md'), profileTemplate, 'utf8');
writeFileSync(path.join(projectAbs, 'docs', '.gitkeep'), '', 'utf8');

console.log(`PASS: project mold → ${projectRel}`);
console.log('  config.json  (citation_style=APA7, modelo=model1, alcance=[])');
console.log('  profile.md   (empty template)');
console.log('  docs/        (apuntes)');
console.log('  structure.md not created — index from common/structure/model1.md via config.modelo');
process.exit(0);
