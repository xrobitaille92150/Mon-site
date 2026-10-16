import { spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { homedir } from 'node:os';
import { build } from 'esbuild';
await build({entryPoints:['assets/members.source.js'],outfile:'assets/members.js',bundle:true,format:'esm',platform:'browser',target:'es2022',minify:true});
const bundled=homedir()+'/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
const python=process.env.ADVISORY_PYTHON || (existsSync(bundled)?bundled:'python3');
const result=spawnSync(python,['gen/build_advisory.py'],{stdio:'inherit'});
process.exit(result.status??1);
