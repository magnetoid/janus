---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_runs.py

Symbols in `tests/gateway/test_api_server_runs.py`.

- L32 `_make_adapter(api_key: str='')` (function) — Create an adapter with optional API key.
- L42 `_create_runs_app(adapter: APIServerAdapter)` (function) — Create an aiohttp app with /v1/runs routes registered.
- L55 `_make_slow_agent(**kwargs)` (function) — Create a mock agent that blocks in run_conversation until interrupted.
- L87 `adapter()` (function)
- L92 `auth_adapter()` (function)
- L101 `TestStartRun` (class)
- L103 `test_start_returns_202(self, adapter)` (method)
- L128 `test_start_invalid_json_returns_400(self, adapter)` (method)
- L139 `test_start_missing_input_returns_400(self, adapter)` (method)
- L148 `test_start_empty_input_returns_400(self, adapter)` (method)
- L155 `test_start_invalid_history_does_not_allocate_run(self, adapter)` (method)
- L167 `test_start_requires_auth(self, auth_adapter)` (method)
- L174 `test_start_with_valid_auth(self, auth_adapter)` (method)
- L198 `TestRunStatus` (class)
- L200 `test_status_completed_run_includes_output_and_usage(self, adapter)` (method)
- L229 `test_status_reflects_explicit_session_id(self, adapter)` (method)
- L259 `test_status_not_found_returns_404(self, adapter)` (method)
- L266 `test_status_requires_auth(self, auth_adapter)` (method)
- L278 `TestRunEvents` (class)
- L280 `test_events_stream_returns_completed(self, adapter)` (method) — Events stream should receive run.completed when agent finishes.
- L310 `test_approval_response_without_pending_returns_409(self, adapter)` (method)
- L337 `test_approval_string_false_does_not_resolve_all(self, adapter)` (method) — Quoted false must not fan out approval resolution across the queue.
- L359 `test_events_not_found_returns_404(self, adapter)` (method)
- L366 `test_events_requires_auth(self, auth_adapter)` (method)
- L378 `TestStopRun` (class)
- L380 `test_stop_running_agent(self, adapter)` (method) — Stop should interrupt the agent and cancel the task.
- L422 `test_stop_nonexistent_run_returns_404(self, adapter)` (method)
- L429 `test_stop_requires_auth(self, auth_adapter)` (method)
- L436 `test_stop_already_completed_run_returns_404(self, adapter)` (method) — Stopping a run that already finished should return 404 (refs cleaned up).
- L464 `test_stop_interrupt_exception_does_not_crash(self, adapter)` (method) — If agent.interrupt() raises, stop should still succeed.
- L496 `test_stop_sends_sentinel_to_events_stream(self, adapter)` (method) — After stop, the events stream should close.
