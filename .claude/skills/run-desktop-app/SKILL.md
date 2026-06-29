---
name: run-desktop-app
description: Build, launch, and verify the Electron desktop app in apps/desktop — full workspace install, complete the allow-scripts-blocked Electron binary, build the renderer, run the 102 main-process tests, and launch it headlessly via playwright-core _electron with a screenshot. Use when asked to run, build, screenshot, or verify the Janus desktop/GUI app.
---

# Run / verify the Janus desktop app (`apps/desktop`)

Verified recipe (2026-06-29, Electron 40, macOS x64). The app is an Electron + Vite/React
GUI whose main process boots the Python backend; you can **fake** that boot for a UI-only
launch. Follow the steps in order — the gotchas below are why naive `npm start` fails.

## Gotchas this skill exists to skip

1. **Partial install masquerades as complete.** A fresh checkout often has only a root-level
   install (someone ran `npm install --workspaces=false` / `install:root`), so `apps/desktop`'s
   deps (`@tanstack/react-query`, `katex`, the `unified`/`hast` stack, `node-pty`, `electron`)
   are missing. `apps/desktop/scripts/assert-root-install.cjs` only checks for `vite`, so it
   **falsely reports OK**. Always do a full root `npm install` first.
2. **`allow-scripts` hardening blocks native installs.** npm is configured to block install
   scripts, so Electron's binary download and `node-pty`'s native build don't run. You must
   complete Electron manually (step 2). **`node-pty` is NOT required** — `electron/main.cjs`
   requires it in a try/catch and falls back to `null`, so the UI launches without it.
3. **This repo may be opened inside an IDE that is itself Electron** (Trae/VSCode set
   `ELECTRON_RUN_AS_NODE`, `ELECTRON_FORCE_IS_PACKAGED`, `ICUBE_*`, `VSCODE_*`). You MUST strip
   those before launching or Electron runs as headless Node / loads the packaged path. The
   driver in step 4 does this for you.

## 1. Install the workspace (from repo ROOT)

```bash
npm install          # full workspace link — NOT install:root / --workspaces=false
```

## 2. Complete the Electron binary (allow-scripts blocked it)

```bash
node node_modules/electron/install.js || true
# If node_modules/electron/path.txt is still missing, extract the cached zip.
# The arch in the filename MUST match `uname -m` (x64 ↔ x86_64, arm64 ↔ arm64):
ZIP=$(ls ~/Library/Caches/electron/electron-v*-darwin-*.zip | head -1)
rm -rf node_modules/electron/dist && mkdir -p node_modules/electron/dist
unzip -q "$ZIP" -d node_modules/electron/dist
printf 'Electron.app/Contents/MacOS/Electron' > node_modules/electron/path.txt
```

## 3. Static checks + renderer build + main-process tests (from `apps/desktop`)

```bash
cd apps/desktop
npm run type-check                 # tsc -b — must be clean
npm run lint                       # eslint; style-only, `npm run lint:fix` is safe
npx vite build                     # renderer bundle → dist/ (skips native-dep staging)
npm run test:desktop:platforms     # 102 main-process unit tests (probes, hardening, IPC)
```

`npm run build` also works but runs `stage-native-deps.cjs`, which needs `node-pty` present;
`npx vite build` is the quickest path to a renderer bundle.

## 4. Launch headlessly + screenshot

```bash
# Install the driver dep anywhere resolvable (a scratch dir is fine):
#   npm install playwright-core    # then export PW_CORE=/abs/path/to/node_modules/playwright-core
# From the repo ROOT:
JANUS_ROOT="$PWD" SHOT=/tmp/janus-desktop.png \
  node .claude/skills/run-desktop-app/drive-electron.cjs
```

The driver strips the IDE Electron env, sets `JANUS_DESKTOP_BOOT_FAKE=1` (no real Python
backend) + a throwaway user-data dir, loads the built `dist/index.html`, waits, and writes a
PNG. **A rendered window (title "Janus", the "Let's get you setup" onboarding card, the
sidebar/status-bar chrome) = success. A blank frame = failure to launch.** Then `Read` the PNG.

## What "working" looks like

- `type-check`: clean · `vite build`: `✓ built` · `test:desktop:platforms`: 102/102 pass.
- Launch renders the onboarding/boot screen; it stalls at "Waiting for Janus backend… 90%"
  *only because* the backend is faked. A real `janus desktop` connects past it.
