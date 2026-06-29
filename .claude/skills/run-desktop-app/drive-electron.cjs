#!/usr/bin/env node
/**
 * Launch apps/desktop's Electron app headlessly and screenshot it.
 *
 * Env:
 *   JANUS_ROOT  repo root (default: process.cwd())
 *   PW_CORE     path to a playwright-core install (default: normal node resolution)
 *   SHOT        output PNG path (default: /tmp/janus-desktop.png)
 *
 * See SKILL.md (run-desktop-app) for the full recipe (install + electron binary first).
 */
const path = require('path');
const os = require('os');
const fs = require('fs');

const ROOT = process.env.JANUS_ROOT || process.cwd();
const DESKTOP = path.join(ROOT, 'apps/desktop');
const EXE = path.join(ROOT, 'node_modules/electron/dist/Electron.app/Contents/MacOS/Electron');
const SHOT = process.env.SHOT || path.join(os.tmpdir(), 'janus-desktop.png');

let electron;
try {
  ({ _electron: electron } = require(process.env.PW_CORE || 'playwright-core'));
} catch (e) {
  console.log('NO_PLAYWRIGHT: install playwright-core and set PW_CORE. ' + e.message);
  process.exit(3);
}

(async () => {
  const env = { ...process.env };
  for (const k of Object.keys(env)) {
    if (k.startsWith('VSCODE_') || k.startsWith('ICUBE_')) delete env[k];
  }
  delete env.ELECTRON_RUN_AS_NODE;       // else Electron runs as headless Node — no window
  delete env.ELECTRON_FORCE_IS_PACKAGED; // else it loads the packaged path, not dist/
  delete env.ELECTRON_NO_ATTACH_CONSOLE;
  env.JANUS_DESKTOP_BOOT_FAKE = '1';     // skip the real Python backend boot
  env.JANUS_DESKTOP_BOOT_FAKE_STEP_MS = '120';
  env.JANUS_DESKTOP_USER_DATA_DIR = fs.mkdtempSync(path.join(os.tmpdir(), 'janus-desktop-'));

  let app;
  try {
    app = await electron.launch({ executablePath: EXE, args: ['.'], cwd: DESKTOP, env, timeout: 30000 });
  } catch (e) {
    console.log('LAUNCH_FAILED: ' + e.message);
    process.exit(2);
  }
  const logs = [];
  try {
    const win = await app.firstWindow({ timeout: 30000 });
    win.on('console', m => logs.push('[' + m.type() + '] ' + m.text()));
    win.on('pageerror', e => logs.push('[pageerror] ' + e.message));
    await win.waitForLoadState('domcontentloaded').catch(() => {});
    await new Promise(r => setTimeout(r, 5000));
    const title = await win.title().catch(() => '(no title)');
    const info = await win.evaluate(() => ({
      url: location.href,
      nodes: document.querySelectorAll('*').length,
      text: document.body ? document.body.innerText.replace(/\s+/g, ' ').slice(0, 500) : '(no body)',
    })).catch(e => ({ err: e.message }));
    await win.screenshot({ path: SHOT });
    console.log('TITLE: ' + title);
    console.log('INFO: ' + JSON.stringify(info));
    console.log('CONSOLE(' + logs.length + '):\n' + logs.slice(0, 25).join('\n'));
    console.log('SCREENSHOT_SAVED: ' + SHOT);
  } catch (e) {
    console.log('DRIVE_ERROR: ' + e.message);
    console.log('CONSOLE(' + logs.length + '):\n' + logs.slice(0, 25).join('\n'));
  } finally {
    await app.close().catch(() => {});
  }
  process.exit(0);
})();
