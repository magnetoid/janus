---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_cancel_background_drain.py

Symbols in `tests/gateway/test_cancel_background_drain.py`.

- L21 `_StubAdapter` (class)
- L22 `connect(self)` (method)
- L25 `disconnect(self)` (method)
- L28 `send(self, chat_id, text, **kwargs)` (method)
- L31 `get_chat_info(self, chat_id)` (method)
- L35 `_make_adapter()` (function)
- L41 `_event(text, cid='42')` (function)
- L50 `test_cancel_background_tasks_drains_late_arrivals()` (function) — A message that arrives during the gather window must be picked
- L122 `test_cancel_background_tasks_handles_no_tasks()` (function) — Regression guard: no tasks, no hang, no error.
- L130 `test_cancel_background_tasks_bounded_rounds()` (function) — Regression guard: the drain loop is bounded — it does not spin
