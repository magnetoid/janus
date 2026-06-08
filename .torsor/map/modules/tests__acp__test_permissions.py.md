---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_permissions.py

Symbols in `tests/acp/test_permissions.py`.

- L18 `_make_response(outcome)` (function)
- L22 `_invoke_callback(outcome, *, allow_permanent=True, timeout=60.0, use_prompt_path=False)` (function)
- L62 `TestApprovalBridge` (class)
- L63 `test_bridge_schedules_request_on_the_given_loop(self)` (method)
- L96 `test_tool_call_ids_are_unique(self)` (method)
- L106 `test_prompt_path_keeps_session_option_when_permanent_disabled(self)` (method)
- L118 `test_reject_always_outcome_denies_without_changing_policy(self)` (method)
- L130 `test_allow_always_maps_correctly(self)` (method)
- L138 `test_denied_and_unknown_outcomes_deny(self)` (method)
- L147 `test_timeout_returns_deny_and_cancels_future(self)` (method)
- L170 `test_none_response_returns_deny(self)` (method) — When request_permission resolves to None, the callback returns 'deny'.
- L201 `TestSchedulerFailure` (class)
- L202 `test_scheduler_failure_closes_permission_coroutine(self)` (method) — If run_coroutine_threadsafe raises, the coro is closed and we return 'deny'.
