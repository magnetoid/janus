---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_network_reconnect.py

Symbols in `tests/gateway/test_telegram_network_reconnect.py`.

- L18 `_ensure_telegram_mock()` (function)
- L40 `_no_auto_discovery(monkeypatch)` (function) — Disable DoH auto-discovery so connect() uses the plain builder chain.
- L47 `_make_adapter()` (function)
- L52 `test_reconnect_self_schedules_on_start_polling_failure()` (function) — When start_polling() raises during a network error retry, the adapter must
- L92 `test_reconnect_does_not_self_schedule_when_fatal_error_set()` (function) — When a fatal error is already set, the failed reconnect should NOT create
- L121 `test_reconnect_success_resets_error_count()` (function) — When start_polling() succeeds, _polling_network_error_count should reset to 0.
- L154 `test_reconnect_triggers_fatal_after_max_retries()` (function) — After MAX_NETWORK_RETRIES attempts, the adapter should set a fatal error
- L179 `_make_mock_app()` (function) — Build a mock Application with an explicit polling request object.
- L200 `test_reconnect_drains_polling_request_only()` (function) — During reconnect, only the polling request (_request[0]) must be cycled.
- L231 `test_reconnect_continues_if_drain_fails()` (function) — If the polling request drain raises, start_polling must still proceed.
- L251 `test_initialize_still_runs_when_shutdown_fails()` (function) — If shutdown() raises, initialize() must still be attempted.
- L273 `test_conflict_retry_also_drains_polling_connections()` (function) — _handle_polling_conflict must also drain the polling pool on retry.
- L291 `test_drain_helper_noop_without_app()` (function) — _drain_polling_connections must be a no-op when _app is None.
- L303 `test_heartbeat_probe_no_op_when_polling_healthy()` (function) — Probe scheduled after a successful reconnect: Updater.running=True and
- L328 `test_heartbeat_probe_reenters_ladder_when_updater_not_running()` (function) — If Updater.running has flipped to False by the heartbeat delay, treat
- L356 `test_heartbeat_probe_reenters_ladder_when_get_me_times_out()` (function) — If bot.get_me() hangs longer than PROBE_TIMEOUT, treat as wedged.
- L389 `test_heartbeat_probe_reenters_ladder_on_get_me_network_error()` (function) — Any exception raised by bot.get_me() (NetworkError, ConnectionError, etc.)
- L416 `test_heartbeat_probe_skips_when_already_fatal()` (function) — If the adapter is already in fatal-error state by the time the probe
- L438 `test_reconnect_schedules_heartbeat_probe_on_success()` (function) — After a successful start_polling() in the reconnect path, a probe task
