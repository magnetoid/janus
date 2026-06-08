---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_service.py

Symbols in `tests/agent/lsp/test_service.py`.

- L27 `_install_mock_server(monkeypatch, script: str='errors', server_id: str='pyright')` (function) — Replace one registered server with a wrapper that spawns the mock.
- L63 `mock_pyright(monkeypatch, tmp_path)` (function) — Install the mock as ``pyright`` and create a fake git workspace.
- L79 `test_service_returns_empty_when_disabled(tmp_path)` (function)
- L93 `test_service_skips_files_outside_workspace(tmp_path)` (function) — Files outside any git worktree must not trigger LSP.
- L108 `test_service_e2e_delta_filter(mock_pyright)` (function) — End-to-end: snapshot baseline → wait → delta returned.
- L131 `test_service_e2e_delta_filter_with_line_shift(mock_pyright)` (function) — End-to-end: an edit that shifts the diagnostic's line still
- L160 `test_service_status_includes_clients(mock_pyright)` (function)
