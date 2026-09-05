#!/usr/bin/env node
/**
 * Project Graphify orchestrator (docs/content/<FOLDER>).
 *
 *   pnpm graphify:project -- <FOLDER>
 *   pnpm graphify:project -- <FOLDER> --prepare-only
 *   pnpm graphify:project -- <FOLDER> --build-only
 *   pnpm graphify:project -- <FOLDER> --verify-only
 *   pnpm graphify:project -- <FOLDER> --force
 */
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
process.chdir(root);

const args = process.argv.slice(2);
const flags = new Set(args.filter((a) => a.startsWith('--')));
const positional = args.filter((a) => !a.startsWith('--'));
const raw = positional[0];

if (!raw) {
  console.error(
    [
      'Usage:',
      '  pnpm graphify:project -- <FOLDER>',
      '  pnpm graphify:project -- <FOLDER> --prepare-only',
      '  pnpm graphify:project -- <FOLDER> --build-only',
      '  pnpm graphify:project -- <FOLDER> --verify-only',
      '  pnpm graphify:project -- <FOLDER> --force',
    ].join('\n')
  );
  process.exit(1);
}

let projectRel = raw.replace(/\/+$/, '');
if (projectRel.startsWith('docs/content/')) {
  // keep
} else if (projectRel.startsWith('docs/')) {
  projectRel = path.join('docs', 'content', path.basename(projectRel));
} else {
  projectRel = path.join('docs', 'content', projectRel);
}

const projectAbs = path.resolve(root, projectRel);

if (!existsSync(projectAbs)) {
  console.error(`Project folder not found: ${projectRel}`);
  process.exit(1);
}

const projectIgnore = path.join(projectAbs, '.graphifyignore');
if (!existsSync(projectIgnore)) {
  writeFileSync(
    projectIgnore,
    ['# Re-include this project for Graphify AST.', '!**', '!*', ''].join('\n'),
    'utf8'
  );
}

mkdirSync(path.join(projectAbs, 'docs'), { recursive: true });

const home = process.env.USERPROFILE || process.env.HOME || homedir();
const graphifyPy = path.join(home, '.local', 'share', 'pipx', 'venvs', 'graphifyy', 'bin', 'python');
const py = existsSync(graphifyPy) ? graphifyPy : 'python3';
const offline = path.join(root, 'scripts', 'graphify-project-offline.py');
const pathEnv = [path.join(home, '.local', 'bin'), process.env.PATH || ''].join(path.delimiter);

const pyArgs = [offline, projectAbs];
if (flags.has('--force')) pyArgs.push('--force');
if (flags.has('--prepare-only')) pyArgs.push('--prepare-only');
if (flags.has('--build-only')) pyArgs.push('--build-only');
if (flags.has('--verify-only')) pyArgs.push('--verify-only');

console.log(`[graphify-project] project=${projectRel}`);
console.log(`[graphify-project] python=${py}`);
console.log(`[graphify-project] flags=${[...flags].join(' ') || '(full: prepare→build→verify)'}`);

const result = spawnSync(py, pyArgs, {
  encoding: 'utf8',
  shell: false,
  cwd: root,
  env: { ...process.env, PATH: pathEnv },
});
if (result.stdout) process.stdout.write(result.stdout);
if (result.stderr) process.stderr.write(result.stderr);

const code = result.status ?? 1;
if (code === 0) {
  const graphJson = path.join(projectAbs, 'graphify-out', 'graph.json');
  const manifest = path.join(projectAbs, 'index-manifest.json');
  if (existsSync(graphJson)) console.log('[graphify-project] PASS graph →', path.relative(root, graphJson));
  if (existsSync(manifest)) console.log('[graphify-project] PASS manifest →', path.relative(root, manifest));
}
process.exit(code);
