---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_conflict.py

Symbols in `tests/gateway/test_telegram_conflict.py`.

- L11 `_ensure_telegram_mock()` (function)
- L41 `_no_auto_discovery(monkeypatch)` (function) — Disable DoH auto-discovery so connect() uses the plain builder chain.
- L51 `test_connect_rejects_same_host_token_lock(monkeypatch)` (function)
- L68 `test_polling_conflict_retries_before_fatal(monkeypatch)` (function) — A single 409 should trigger a retry, not an immediate fatal error.
- L132 `test_polling_conflict_becomes_fatal_after_retries(monkeypatch)` (function) — After exhausting retries, the conflict should become fatal.
- L211 `test_connect_marks_retryable_fatal_error_for_startup_network_failure(monkeypatch)` (function)
- L246 `test_connect_clears_webhook_before_polling(monkeypatch)` (function)
- L291 `test_disconnect_skips_inactive_updater_and_app(monkeypatch)` (function)
