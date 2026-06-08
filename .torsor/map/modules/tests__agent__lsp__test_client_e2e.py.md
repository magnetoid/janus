---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_client_e2e.py

Symbols in `tests/agent/lsp/test_client_e2e.py`.

- L23 `_client(workspace: Path, script: str='clean')` (function)
- L35 `test_client_lifecycle_clean(tmp_path: Path)` (function) — Full lifecycle: spawn, initialize, open, get clean diagnostics, shutdown.
- L55 `test_client_receives_published_errors(tmp_path: Path)` (function)
- L76 `test_client_didchange_bumps_version(tmp_path: Path)` (function)
- L97 `test_client_handles_crashing_server(tmp_path: Path)` (function) — When the server exits right after initialize, subsequent requests
- L118 `test_client_shutdown_idempotent(tmp_path: Path)` (function) — Calling shutdown twice must be safe.
- L129 `test_client_diagnostics_are_deduped(tmp_path: Path)` (function) — Repeated identical pushes must not produce duplicate diagnostics.
