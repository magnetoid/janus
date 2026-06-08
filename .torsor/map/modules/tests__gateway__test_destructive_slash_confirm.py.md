---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_destructive_slash_confirm.py

Symbols in `tests/gateway/test_destructive_slash_confirm.py`.

- L23 `_make_source()` (function)
- L33 `_make_event(text: str)` (function)
- L37 `_make_runner()` (function) — Mirror tests/gateway/test_unknown_command.py::_make_runner.
- L81 `test_gate_off_runs_execute_immediately(monkeypatch)` (function) — When approvals.destructive_slash_confirm is False, the destructive
- L104 `test_gate_on_text_fallback_returns_prompt_without_executing(monkeypatch)` (function) — When the gate is on and the adapter has no button UI, the user gets
- L129 `test_gate_on_pending_confirm_registered(monkeypatch)` (function) — When the gate is on, a pending slash-confirm entry is registered for
- L156 `test_resolve_once_runs_execute_and_returns_result()` (function) — Resolving the pending confirm with 'once' runs the destructive
- L190 `test_resolve_cancel_does_not_run_execute()` (function) — Resolving with 'cancel' must NOT run the destructive action.
- L222 `test_resolve_always_persists_opt_out_and_runs_execute(monkeypatch)` (function) — Resolving with 'always' must (a) flip the config gate to False,
