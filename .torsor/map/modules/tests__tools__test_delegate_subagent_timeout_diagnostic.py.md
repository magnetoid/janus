---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_delegate_subagent_timeout_diagnostic.py

Symbols in `tests/tools/test_delegate_subagent_timeout_diagnostic.py`.

- L28 `hermes_home(tmp_path, monkeypatch)` (function)
- L35 `_StubChild` (class) — Minimal stand-in for an AIAgent subagent.
- L37 `__init__(self, *, api_call_count: int=0, hang_seconds: float=5.0, subagent_id: str='sa-0-stubabc', tool_schema=None)` (method)
- L68 `get_activity_summary(self)` (method)
- L76 `run_conversation(self, user_message, task_id=None)` (method)
- L80 `interrupt(self)` (method)
- L86 `TestDumpSubagentTimeoutDiagnostic` (class)
- L88 `test_writes_log_with_expected_sections(self, hermes_home)` (method)
- L148 `test_truncates_very_long_goal(self, hermes_home)` (method)
- L169 `test_missing_worker_thread_is_handled(self, hermes_home)` (method)
- L184 `test_exited_worker_thread_is_handled(self, hermes_home)` (method)
- L204 `test_returns_none_on_unwritable_logs_dir(self, tmp_path, monkeypatch)` (method)
- L233 `TestRunSingleChildTimeoutDump` (class) — The timeout branch in _run_single_child must emit the diagnostic
- L237 `_invoke_with_short_timeout(self, child, monkeypatch)` (method) — Run _run_single_child with a tiny timeout to force the timeout branch.
- L253 `test_zero_api_calls_writes_dump_and_surfaces_path(self, hermes_home, monkeypatch)` (method)
- L269 `test_nonzero_api_calls_skips_dump_and_uses_old_message(self, hermes_home, monkeypatch)` (method)
