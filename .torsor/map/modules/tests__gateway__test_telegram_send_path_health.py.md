---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_send_path_health.py

Symbols in `tests/gateway/test_telegram_send_path_health.py`.

- L16 `_ensure_telegram_mock()` (function)
- L33 `_make_adapter()` (function)
- L41 `test_send_succeeds_when_path_healthy()` (function) — Healthy adapter delivers normally; send_message is called.
- L53 `test_send_short_circuits_when_path_degraded()` (function) — Degraded adapter returns failure WITHOUT calling send_message,
- L68 `test_reconnect_storm_sets_and_heartbeat_clears_flag(monkeypatch)` (function) — _handle_polling_network_error sets the flag; a successful heartbeat
