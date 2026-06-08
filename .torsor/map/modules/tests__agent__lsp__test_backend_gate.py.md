---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_backend_gate.py

Symbols in `tests/agent/lsp/test_backend_gate.py`.

- L19 `_reset()` (function)
- L23 `test_local_only_helper_returns_true_for_local_env()` (function)
- L31 `test_local_only_helper_returns_false_for_non_local_env()` (function) — A mocked non-local env (Docker/Modal/SSH stand-in) returns False.
- L44 `test_snapshot_baseline_skipped_for_non_local(monkeypatch)` (function) — Verify the LSP service's snapshot_baseline is NOT called when
- L66 `test_maybe_lsp_diagnostics_returns_empty_for_non_local(monkeypatch)` (function)
- L91 `test_snapshot_baseline_called_for_local_env(tmp_path, monkeypatch)` (function)
