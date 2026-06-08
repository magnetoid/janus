---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pending_drain_race.py

Symbols in `tests/gateway/test_pending_drain_race.py`.

- L38 `_StubAdapter` (class)
- L39 `connect(self)` (method)
- L42 `disconnect(self)` (method)
- L45 `send(self, chat_id, text, **kwargs)` (method)
- L48 `get_chat_info(self, chat_id)` (method)
- L52 `_make_adapter()` (function)
- L58 `_make_event(text='hi', chat_id='42')` (function)
- L66 `_sk(chat_id='42')` (function)
- L73 `test_pending_drain_keeps_active_session_guard_live()` (function) — Fix for R5: during pending-drain cleanup, _active_sessions must stay
- L134 `test_finally_cleanup_drains_late_arrival_pending()` (function) — Fix for R6: if a message lands in _pending_messages during the
- L188 `test_no_pending_cleans_up_normally()` (function) — Regression guard: when no pending message exists, the finally
