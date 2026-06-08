---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_goal_verdict_send.py

Symbols in `tests/gateway/test_goal_verdict_send.py`.

- L24 `hermes_home(tmp_path, monkeypatch)` (function)
- L37 `_make_source()` (function)
- L47 `_RecordingAdapter` (class) — Minimal adapter that records send() invocations.
- L50 `__init__(self)` (method)
- L54 `send(self, chat_id: str, content: str, reply_to=None, metadata=None)` (method)
- L64 `_make_runner_with_adapter(session_id: str=None)` (function)
- L100 `test_goal_verdict_done_sent_via_adapter_send(hermes_home)` (function) — When the judge says done, the '✓ Goal achieved' message must reach
- L127 `test_goal_verdict_continue_enqueues_continuation(hermes_home)` (function) — When the judge says continue, both the 'continuing' status and the
- L155 `test_goal_verdict_budget_exhausted_sends_pause(hermes_home)` (function) — When the budget is exhausted, a '⏸ Goal paused' message must be sent
- L184 `test_goal_verdict_skipped_when_no_active_goal(hermes_home)` (function) — No goal set → the hook is a no-op. Nothing is sent, nothing enqueued.
- L200 `test_goal_verdict_survives_adapter_without_send(hermes_home)` (function) — Bad adapter (no ``send`` attribute) must not crash the judge hook.
