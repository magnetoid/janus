---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_chromium_check.py

Symbols in `tests/tools/test_browser_chromium_check.py`.

- L17 `_reset_chromium_cache()` (function)
- L23 `TestChromiumSearchRoots` (class)
- L24 `test_respects_playwright_browsers_path_env(self, monkeypatch, tmp_path)` (method)
- L29 `test_ignores_playwright_browsers_path_zero(self, monkeypatch)` (method)
- L35 `test_always_includes_default_ms_playwright_cache(self, monkeypatch)` (method)
- L42 `TestChromiumInstalled` (class)
- L43 `test_true_when_plain_chromium_on_path(self, monkeypatch)` (method)
- L53 `test_true_when_chromium_dir_present(self, monkeypatch, tmp_path)` (method)
- L58 `test_true_when_headless_shell_present(self, monkeypatch, tmp_path)` (method)
- L66 `test_result_cached(self, monkeypatch, tmp_path)` (method)
- L75 `TestCheckBrowserRequirementsChromium` (class)
- L77 `test_local_mode_with_chromium_returns_true(self, monkeypatch, tmp_path)` (method)
- L87 `test_cloud_mode_does_not_require_local_chromium(self, monkeypatch, tmp_path)` (method) — Cloud browsers (Browserbase etc.) host their own Chromium.
- L105 `test_camofox_mode_does_not_require_chromium(self, monkeypatch, tmp_path)` (method)
- L114 `TestRunBrowserCommandChromiumGuard` (class) — Verify _run_browser_command fails fast (no timeout hang) when
