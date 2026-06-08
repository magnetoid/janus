---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_execute_code_approval_cluster.py

Symbols in `tests/tools/test_execute_code_approval_cluster.py`.

- L32 `test_helper_propagates_contextvar_and_approval_callback()` (function)
- L58 `test_helper_clears_callbacks_on_teardown()` (function) — A recycled worker thread must not retain the propagated callback after
- L84 `test_both_rpc_threads_use_propagation_helper()` (function) — Source guard: both execute_code RPC threads must wrap their target with
- L107 `gw_session(monkeypatch)` (function) — A clean gateway session: HERMES_GATEWAY_SESSION set, a bound session
- L131 `_register_resolver(session_key: str, result)` (function) — Register a gateway notify callback that immediately resolves the most
- L145 `test_guard_isolated_backend_approved()` (function)
- L150 `test_guard_headless_local_approved(monkeypatch)` (function)
- L160 `test_guard_cron_deny_blocks(monkeypatch)` (function)
- L170 `test_guard_gateway_user_approves_is_one_shot(gw_session)` (function)
- L179 `test_guard_gateway_user_approves_session_persists(gw_session)` (function) — 'Approve session' stores session-level approval (#39275).
- L196 `test_guard_gateway_user_approves_always_persists(gw_session)` (function) — 'Always' stores permanent approval (#39275).
- L211 `test_guard_session_approval_short_circuits_prompt(gw_session)` (function) — Once session-approved, execute_code skips the approval prompt (#39275).
- L226 `test_guard_gateway_user_denies_blocks(gw_session)` (function)
- L234 `test_guard_gateway_timeout_blocks(gw_session, monkeypatch)` (function)
- L244 `test_guard_gateway_missing_notify_is_pending(gw_session)` (function)
- L251 `test_guard_smart_mode(gw_session, monkeypatch)` (function)
- L269 `test_guard_session_yolo_bypasses(gw_session)` (function)
- L283 `test_env_scrub_hermes_allowlist_and_secret_blocks()` (function)
- L311 `test_env_scrub_passthrough_overrides_secret_block()` (function) — A skill/config-declared passthrough var is an explicit user opt-in and
- L326 `test_execute_code_entry_blocks_before_spawn_when_guard_denies(monkeypatch, tmp_path)` (function) — Behavioral wiring test: execute_code() consults the entry guard and, on
- L355 `test_env_scrub_logs_dropped_hermes_vars(caplog)` (function) — Dropping a non-allowlisted, non-secret HERMES_* var must be diagnosable:
- L384 `test_env_scrub_no_log_when_nothing_dropped(caplog)` (function) — No diagnostic noise when there are no dropped HERMES_* vars.
