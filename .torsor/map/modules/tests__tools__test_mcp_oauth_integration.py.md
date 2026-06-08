---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_oauth_integration.py

Symbols in `tests/tools/test_mcp_oauth_integration.py`.

- L22 `test_external_refresh_picked_up_without_restart(tmp_path, monkeypatch)` (function) — Simulate Cthulhu's cron workflow end-to-end.
- L97 `test_handle_401_deduplicates_concurrent_callers(tmp_path, monkeypatch)` (function) — Ten concurrent 401 handlers for the same token should fire one recovery.
- L148 `test_handle_401_returns_false_when_no_provider(tmp_path, monkeypatch)` (function) — handle_401 for an unknown server returns False cleanly.
- L160 `test_invalidate_if_disk_changed_handles_missing_file(tmp_path, monkeypatch)` (function) — invalidate_if_disk_changed returns False when tokens file doesn't exist.
- L175 `test_provider_is_reused_across_reconnects(tmp_path, monkeypatch)` (function) — The manager caches providers; multiple reconnects reuse the same instance.
