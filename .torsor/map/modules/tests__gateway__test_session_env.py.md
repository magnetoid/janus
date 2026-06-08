---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_env.py

Symbols in `tests/gateway/test_session_env.py`.

- L19 `_reset_contextvars()` (function) — Reset all session contextvars to _UNSET between tests.
- L33 `test_set_session_env_sets_contextvars(monkeypatch)` (function) — _set_session_env should populate contextvars, not os.environ.
- L72 `test_clear_session_env_restores_previous_state(monkeypatch)` (function) — _clear_session_env should restore contextvars to their pre-handler values.
- L109 `test_get_session_env_falls_back_to_os_environ(monkeypatch)` (function) — get_session_env should fall back to os.environ when contextvar is unset.
- L127 `test_get_session_env_default_when_nothing_set(monkeypatch)` (function) — get_session_env returns default when neither contextvar nor env is set.
- L135 `test_set_session_env_handles_missing_optional_fields()` (function) — _set_session_env should handle None chat_name and thread_id gracefully.
- L162 `test_session_key_set_via_contextvars(monkeypatch)` (function) — set_session_vars should set HERMES_SESSION_KEY via contextvars.
- L177 `test_session_key_falls_back_to_os_environ(monkeypatch)` (function) — get_session_env for SESSION_KEY should fall back to os.environ.
- L193 `test_set_session_env_includes_session_key()` (function) — _set_session_env should propagate session_key from SessionContext.
- L221 `test_session_key_no_race_condition_with_contextvars(monkeypatch)` (function) — Prove contextvars isolates SESSION_KEY across concurrent async tasks.
- L259 `test_run_in_executor_with_context_preserves_session_env(monkeypatch)` (function) — Gateway executor work should inherit session contextvars for tool routing.
- L304 `test_run_in_executor_with_context_forwards_args()` (function) — _run_in_executor_with_context should forward *args to the callable.
- L316 `test_run_in_executor_with_context_propagates_exceptions()` (function) — Exceptions inside the executor should propagate to the caller.
