---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_web_ui_build.py

Symbols in `tests/hermes_cli/test_web_ui_build.py`.

- L18 `_touch(path: Path, offset: float=0.0)` (function)
- L26 `_make_web_dir(tmp_path: Path)` (function) — Return (web_dir, dist_dir) matching real repo layout.
- L35 `TestWebUIBuildNeeded` (class)
- L37 `test_returns_true_when_dist_missing(self, tmp_path)` (method)
- L41 `test_returns_false_when_vite_manifest_fresh(self, tmp_path)` (method)
- L47 `test_returns_true_when_source_newer_than_manifest(self, tmp_path)` (method)
- L53 `test_falls_back_to_index_html_when_manifest_missing(self, tmp_path)` (method)
- L59 `test_web_dist_dir_not_web_dist_subdir(self, tmp_path)` (method) — Regression: sentinel must be in hermes_cli/web_dist/, NOT web/dist/.
- L69 `test_returns_true_when_package_lock_newer_than_dist(self, tmp_path)` (method)
- L77 `test_returns_true_when_vite_config_newer_than_dist(self, tmp_path)` (method)
- L83 `test_ignores_node_modules(self, tmp_path)` (method)
- L91 `test_ignores_dist_subdir_under_web(self, tmp_path)` (method)
- L100 `TestBuildWebUISkipsWhenFresh` (class)
- L102 `test_skips_npm_when_dist_is_fresh(self, tmp_path)` (method)
- L113 `test_runs_npm_when_dist_missing(self, tmp_path)` (method)
- L129 `test_npm_install_uses_utf8_replace_output_decoding(self, tmp_path)` (method)
- L143 `test_npm_install_uses_workspace_web_scope(self, tmp_path)` (method)
- L156 `test_web_build_uses_idle_timeout_helper(self, tmp_path)` (method) — npm run build now goes through _run_with_idle_timeout (issue #33788).
- L180 `test_termux_web_install_is_workspace_scoped(self, tmp_path, monkeypatch)` (method)
- L204 `test_desktop_web_install_uses_existing_workspace_root(self, tmp_path, monkeypatch)` (method)
- L225 `TestBuildWebUIRetryAndStaleFallback` (class) — Coverage for the retry + stale-dist fallback added in #23824 / issue #23817.
- L228 `test_retries_build_once_on_failure(self, tmp_path)` (method)
- L246 `test_falls_back_to_stale_dist_when_retry_also_fails(self, tmp_path, capsys)` (method)
- L269 `test_hard_fails_when_no_dist_to_fall_back_to(self, tmp_path, capsys)` (method)
