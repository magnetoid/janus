---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_shell_linter_lsp_skip.py

Symbols in `tests/agent/lsp/test_shell_linter_lsp_skip.py`.

- L40 `_make_fops()` (function)
- L47 `test_shell_linter_skipped_when_lsp_will_handle(ext, tmp_path)` (function) — When LSP is active and enabled_for(path), shell linter is skipped.
- L73 `test_shell_linter_runs_when_lsp_inactive(ext, tmp_path)` (function) — When LSP is inactive (default config, no service, remote backend, ...),
- L95 `test_lsp_does_not_skip_non_redundant_extensions(ext, tmp_path)` (function) — ``py_compile`` and ``node --check`` keep running even when an LSP
- L122 `test_lsp_will_handle_returns_false_when_service_is_none(tmp_path)` (function) — ``_lsp_will_handle`` must return False when the LSP service hasn't
- L135 `test_lsp_will_handle_returns_false_on_remote_backend(tmp_path)` (function) — LSP servers run on the host process — remote backends (Docker,
- L153 `test_lsp_will_handle_swallows_enabled_for_exception(tmp_path)` (function) — A flaky LSP service must never break the shell-linter fallback —
- L169 `test_tsx_stays_out_of_linters_table_for_default_compatibility()` (function) — Regression: keep ``.tsx`` out of ``LINTERS`` so users with LSP
- L190 `test_tsx_default_check_lint_returns_skipped(tmp_path)` (function) — End-to-end: ``.tsx`` files get ``LintResult(skipped=True)`` from
