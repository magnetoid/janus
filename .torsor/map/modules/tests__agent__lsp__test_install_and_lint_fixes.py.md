---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_install_and_lint_fixes.py

Symbols in `tests/agent/lsp/test_install_and_lint_fixes.py`.

- L31 `test_typescript_recipe_includes_typescript_sdk()` (function)
- L41 `test_install_npm_passes_extras_to_npm_command(tmp_path, monkeypatch)` (function) — Verify the npm subprocess is invoked with both pkg AND extras.
- L70 `test_install_npm_works_without_extras(tmp_path, monkeypatch)` (function) — Backwards compat: pyright-style recipes (no extras) still install.
- L97 `test_existing_binary_finds_windows_wrapper_in_staging(tmp_path, monkeypatch)` (function) — Installed Windows shims should satisfy later status/probe calls.
- L114 `test_install_pip_finds_windows_scripts_launcher(tmp_path, monkeypatch)` (function) — pip console scripts can land in Scripts/ on native Windows.
- L143 `test_backend_warnings_quiet_when_bash_not_installed(tmp_path, monkeypatch)` (function) — No bash → no warning.
- L153 `test_backend_warnings_quiet_when_bash_and_shellcheck_both_present(tmp_path, monkeypatch)` (function) — Both installed → no warning.
- L166 `test_backend_warnings_fires_when_bash_installed_but_shellcheck_missing(tmp_path, monkeypatch)` (function) — The exact scenario from the bug report.
- L183 `test_status_output_includes_backend_warnings_section(tmp_path, monkeypatch)` (function) — End-to-end: status command output includes the warning section.
- L209 `test_npx_tsc_missing_treated_as_skipped()` (function) — The original bug: ``npx tsc`` errors when tsc isn't installed.
- L230 `test_real_lint_error_not_classified_as_unusable()` (function) — A genuine TypeScript type error must NOT be misclassified.
- L243 `test_unknown_base_cmd_returns_false()` (function) — Unfamiliar linters fall through and use the normal error path.
- L251 `test_check_lint_returns_skipped_when_npx_tsc_unusable(tmp_path)` (function) — Integration: _check_lint sees npx exit non-zero with the npx banner
- L286 `test_check_lint_returns_error_for_real_ts_type_errors(tmp_path)` (function) — Sanity: real TypeScript errors still go through the error path.
