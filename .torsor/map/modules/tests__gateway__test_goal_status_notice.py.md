---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_goal_status_notice.py

Symbols in `tests/gateway/test_goal_status_notice.py`.

- L14 `FakeAdapter` (class)
- L15 `__init__(self)` (method)
- L20 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L31 `register_post_delivery_callback(self, session_key, callback, *, generation=None)` (method)
- L35 `_goal_continuation_event(source, goal='finish the task')` (function)
- L44 `test_goal_status_notice_uses_adapter_send_with_thread_metadata()` (function) — Regression: /goal judge status must use BasePlatformAdapter.send().
- L74 `test_goal_status_notice_defers_until_post_delivery_callback()` (function) — Regression: goal status must appear after the agent's visible reply.
- L113 `test_clear_goal_pending_continuations_removes_slot_and_overflow_only()` (function) — Regression: /goal pause/clear must cancel queued self-continuations.
