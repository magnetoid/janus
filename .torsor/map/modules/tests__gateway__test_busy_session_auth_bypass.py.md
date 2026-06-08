---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_busy_session_auth_bypass.py

Symbols in `tests/gateway/test_busy_session_auth_bypass.py`.

- L40 `_make_event(text='hello', chat_id='123', user_id='user1', user_name='TestUser', platform_val='slack', thread_id='thread-abc')` (function) — Build a MessageEvent for a shared thread.
- L60 `_make_runner(authorized_users=None)` (function) — Build a minimal GatewayRunner with configurable auth.
- L85 `_make_adapter(platform_val='slack')` (function) — Build a minimal adapter mock.
- L100 `TestBusySessionAuthBypass` (class) — #17775: Unauthorized users in shared threads must be blocked in the busy path.
- L104 `test_unauthorized_user_dropped_in_busy_path(self)` (method) — An unauthorized user's message must be silently dropped, not queued.
- L141 `test_authorized_user_still_processed_in_busy_path(self)` (method) — An authorized user's message must still be processed normally.
- L168 `test_unauthorized_user_during_drain_still_blocked(self)` (method) — Even during drain mode, unauthorized users must be dropped.
- L196 `test_unauthorized_user_cannot_steer_active_agent(self)` (method) — Steer mode must not allow unauthorized users to inject mid-run guidance.
