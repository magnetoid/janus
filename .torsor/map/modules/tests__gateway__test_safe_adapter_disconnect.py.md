---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_safe_adapter_disconnect.py

Symbols in `tests/gateway/test_safe_adapter_disconnect.py`.

- L24 `bare_runner()` (function) — A GatewayRunner shell that only needs to support _safe_adapter_disconnect.
- L30 `test_safe_disconnect_calls_adapter_disconnect(bare_runner)` (function) — The helper forwards to adapter.disconnect().
- L41 `test_safe_disconnect_swallows_exceptions(bare_runner)` (function) — An exception in adapter.disconnect() must not propagate — the
- L54 `test_safe_disconnect_handles_none_platform(bare_runner)` (function) — Logging path must tolerate platform=None.
- L65 `test_safe_disconnect_times_out_and_continues(bare_runner, monkeypatch, caplog)` (function) — A wedged adapter disconnect must not block gateway shutdown.
