#!/usr/bin/env node
/**
 * Local consistency checks for the ITD academic skill pipeline.
 * Usage: node scripts/check-pipeline.mjs
 *        npm run check:pipeline
 */
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const errors = [];
const warns = [];

function fail(msg) {
  errors.push(msg);
}
function warn(msg) {
  warns.push(msg);
}

const REQUIRED_PLAYBOOKS = {
  'bibliography-auto': 'common/bibliography-auto/model1.md',
  'bibliography-search': 'common/bibliography-search/model1.md',
  'bibliography-oa-sources': 'common/bibliography-oa-sources/model1.md',
  'bibliography-picoct': 'common/bibliography-picoct/model1.md',
  'make-report': 'common/make-report/model1.md',
  'make-report-polish': 'common/make-report-polish/model1.md',
};

const FORBIDDEN_SKILLS = [
  'graphify-theme',
  'rsl-make-report',
  'rsl-make-paper',
  'rsl-polish-report',
  'rsl-polish-paper',
  'bibliographic-search',
];

// 1) Forbidden leftover skills
for (const name of FORBIDDEN_SKILLS) {
  const p = join(root, '.cursor', 'skills', name);
  if (existsSync(p)) fail(`forbidden skill still present: .cursor/skills/${name}`);
}

// 2) Required playbooks
for (const [skill, pb] of Object.entries(REQUIRED_PLAYBOOKS)) {
  const skillDir = join(root, '.cursor', 'skills', skill);
  if (!existsSync(join(skillDir, 'SKILL.md'))) fail(`missing skill: ${skill}`);
  if (!existsSync(join(root, pb))) fail(`missing playbook for ${skill}: ${pb}`);
}

// 3) bibliographic-search must NOT exist
{
  const stub = join(root, '.cursor', 'skills', 'bibliographic-search');
  if (existsSync(stub)) fail('forbidden skill present: bibliographic-search');
  const stubCommon = join(root, 'common', 'bibliographic-search');
  if (existsSync(stubCommon)) fail('forbidden path present: common/bibliographic-search');
}

// 4) Broken relative links in skills
const linkRe = /\]\(([^)]+)\)/g;
const skillsRoot = join(root, '.cursor', 'skills');
for (const name of readdirSync(skillsRoot)) {
  const skillMd = join(skillsRoot, name, 'SKILL.md');
  if (!existsSync(skillMd)) continue;
  const text = readFileSync(skillMd, 'utf8');
  let m;
  while ((m = linkRe.exec(text))) {
    const rel = m[1];
    if (!rel.startsWith('.')) continue;
    if (rel.startsWith('http')) continue;
    const target = resolve(dirname(skillMd), rel.split('#')[0]);
    if (!existsSync(target)) fail(`broken link in ${name}/SKILL.md → ${rel}`);
  }
}

// 5) Forbidden path strings in live skills (except stub)
const badPatterns = [
  { re: /bibliographic\//, allowIn: [] },
  { re: /\bbibliographic-search\b/, allowIn: [] },
  { re: /graphify-theme/, allowIn: [] },
  { re: /graphify:theme/, allowIn: [] },
  { re: /rsl-make-report/, allowIn: [] },
  { re: /rsl-polish-/, allowIn: [] },
  { re: /\bDEPRECATED\b/, allowIn: [] },
  { re: /\*\(deprecated\)\*/, allowIn: [] },
];
for (const name of readdirSync(skillsRoot)) {
  const skillMd = join(skillsRoot, name, 'SKILL.md');
  if (!existsSync(skillMd)) continue;
  const text = readFileSync(skillMd, 'utf8');
  for (const { re, allowIn } of badPatterns) {
    if (allowIn.includes(name)) continue;
    if (re.test(text)) fail(`legacy pattern ${re} in skill ${name}`);
  }
}

// 5c) Theme flow: agents + init skills must wire brainstorm → benchmark
{
  const agents = ['brainstorm-theme', 'benchmark-theme'];
  for (const a of agents) {
    if (!existsSync(join(root, '.cursor', 'agents', `${a}.md`))) {
      fail(`missing agent: .cursor/agents/${a}.md`);
    }
  }
  const initTheme = readFileSync(join(skillsRoot, 'init-theme', 'SKILL.md'), 'utf8');
  for (const needle of [
    'brainstorm-theme',
    'benchmark-theme',
    'theme-brainstorm.md',
    'sobrescribir',
  ]) {
    if (!initTheme.includes(needle)) fail(`init-theme missing: ${needle}`);
  }
  if (/Lanzar \*\*`?competitive-analysis/.test(initTheme) || initTheme.includes('Skill externa (aparte)')) {
    fail('init-theme still wires external competitive-analysis as a step');
  }
  const initAudit = readFileSync(join(skillsRoot, 'init-theme-audit', 'SKILL.md'), 'utf8');
  for (const needle of [
    'brainstorm-theme',
    'benchmark-theme',
    'theme-audit-brainstorm.md',
    'sobrescribir',
  ]) {
    if (!initAudit.includes(needle)) fail(`init-theme-audit missing: ${needle}`);
  }
  if (initAudit.includes('Skill externa (aparte)')) {
    fail('init-theme-audit still wires external competitive-analysis as a step');
  }
  const polishA = readFileSync(join(skillsRoot, 'init-theme-polish', 'SKILL.md'), 'utf8');
  if (!polishA.includes('theme-brainstorm.md')) {
    fail('init-theme-polish should mention theme-brainstorm.md as optional context');
  }
  const polishB = readFileSync(join(skillsRoot, 'init-theme-audit-polish', 'SKILL.md'), 'utf8');
  if (!polishB.includes('theme-audit-brainstorm.md')) {
    fail('init-theme-audit-polish should mention theme-audit-brainstorm.md as optional context');
  }
}

// 6) Python import + bib listing for DDS/DS
const py = spawnSync(
  'python3',
  [
    '-c',
    `
import importlib.util, sys
from pathlib import Path
root = Path(${JSON.stringify(root)})
spec = importlib.util.spec_from_file_location('off', root / 'scripts' / 'graphify-project-offline.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
for folder in ['DDS', 'DS']:
    p = root / 'docs' / 'content' / folder
    if not p.is_dir():
        print('SKIP', folder)
        continue
    auto = m.list_bib_auto_files(p)
    search = m.list_bib_search_files(p)
    for path, kind in auto:
        rel = str(path.relative_to(p)).replace('\\\\', '/')
        if '/search/' in rel or rel.startswith('bibliography/docs/search'):
            raise SystemExit(f'auto listed search path: {rel}')
    for path, kind in search:
        rel = str(path.relative_to(p)).replace('\\\\', '/')
        if 'bibliography/docs/' in rel and '/search/' not in rel and not rel.endswith('search/docs.md'):
            if rel == 'bibliography/search/docs.md':
                continue
            if kind == 'bib_search' and not rel.startswith('bibliography/docs/search'):
                raise SystemExit(f'search MD not under docs/search: {rel}')
    print(folder, 'auto', len(auto), 'search', len(search))
# modelo path resolution (full path in config)
dds = root / 'docs' / 'content' / 'DDS'
if dds.is_dir():
    import json
    cfg = json.loads((dds / 'config.json').read_text())
    src, kind = m.resolve_structure_source(dds, cfg)
    if kind != 'modelo' or not src or not src.is_file():
        raise SystemExit(f'modelo resolve failed: {kind} {src}')
    print('modelo_ok', src.name)
print('BIB_OK')
`,
  ],
  { encoding: 'utf8', cwd: root }
);
if (py.status !== 0) {
  fail(`bib listing failed: ${py.stderr || py.stdout}`);
} else {
  process.stdout.write(py.stdout);
}

// 7) DDS reports-trace sanity
const tracePath = join(root, 'docs/content/DDS/docs/reports-trace.json');
if (existsSync(tracePath)) {
  const trace = JSON.parse(readFileSync(tracePath, 'utf8'));
  if (!Array.isArray(trace) || !trace.length) fail('DDS reports-trace.json empty');
  const last = trace[trace.length - 1];
  const draftRel = (last.draft || '').replace(/^\.\//, '');
  const draftAbs = join(root, 'docs/content/DDS', draftRel);
  if (!existsSync(draftAbs)) fail(`DDS trace draft missing: ${last.draft}`);
  if (last.has_polish && !last.reporte) fail('DDS has_polish true but reporte null');
  if (!last.has_polish && last.reporte) warn('DDS reporte set but has_polish false');
} else {
  warn('DDS reports-trace.json missing (ok if no make-report yet)');
}

// 8) No bibliographic/ dirs under content
function walkDirs(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (!statSync(p).isDirectory()) continue;
    if (name === 'graphify-out' || name === 'node_modules' || name === '.git') continue;
    if (name === 'bibliographic') out.push(p);
    walkDirs(p, out);
  }
  return out;
}
for (const p of walkDirs(join(root, 'docs/content'))) {
  fail(`legacy bibliographic/ directory: ${p.replace(root + '/', '')}`);
}


// 9) Corpus structure header must not double-prefix modelo path
const corpusStruct = join(root, 'docs/content/DDS/graphify-out/_corpus/structure.md');
if (existsSync(corpusStruct)) {
  const first = readFileSync(corpusStruct, 'utf8').split('\n')[0] || '';
  if (first.includes('common/structure/common/structure') || first.includes('model1.md.md')) {
    fail(`bad modelo comment in DDS corpus: ${first}`);
  }
}

// Report
for (const w of warns) console.warn('WARN:', w);
if (errors.length) {
  console.error('\nFAIL:', errors.length, 'issue(s)');
  for (const e of errors) console.error(' -', e);
  process.exit(1);
}
console.log('\nPASS check-pipeline');
process.exit(0);
