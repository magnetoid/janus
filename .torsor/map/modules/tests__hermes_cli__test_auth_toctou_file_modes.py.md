---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_auth_toctou_file_modes.py

Symbols in `tests/hermes_cli/test_auth_toctou_file_modes.py`.

- L41 `test_save_auth_store_writes_0o600_with_0o700_parent(tmp_path, monkeypatch)` (function) — ``_save_auth_store`` must land ``auth.json`` at 0o600 and parent at 0o700.
- L77 `test_save_qwen_cli_tokens_writes_0o600_with_0o700_parent(tmp_path, monkeypatch)` (function) — ``_save_qwen_cli_tokens`` must land the token file at 0o600 and parent at 0o700.
- L115 `test_shared_nous_store_writes_0o600_with_0o700_parent(tmp_path, monkeypatch)` (function) — The Nous shared-credential store must land at 0o600 / parent 0o700.
- L163 `test_save_auth_store_uses_os_open_with_0o600_mode(tmp_path, monkeypatch)` (function) — Regression: the writer must call ``os.open`` with an explicit restricted
