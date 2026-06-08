---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pending_drain_no_recursion.py

Symbols in `tests/gateway/test_pending_drain_no_recursion.py`.

- L37 `_StubAdapter` (class)
- L38 `connect(self)` (method)
- L41 `disconnect(self)` (method)
- L44 `send(self, chat_id, text, **kwargs)` (method)
- L47 `get_chat_info(self, chat_id)` (method)
- L51 `_make_adapter()` (function)
- L57 `_make_event(text='hi', chat_id='42')` (function)
- L65 `_sk(chat_id='42')` (function)
- L71 `_count_pmb_frames()` (function) — Walk the current call stack and count nested
- L85 `test_in_band_drain_does_not_grow_stack()` (function) — Issue #17758: chained pending-message drains must not recurse.
- L133 `test_in_band_drain_preserves_active_session_guard()` (function) — The original task must NOT release ``_active_sessions[session_key]``
- L201 `test_normal_path_releases_session_guard()` (function) — The common path — one message, nothing queued — must still
- L241 `test_drain_task_cancellation_releases_session()` (function) — If the in-band drain task is cancelled (e.g. user sent ``/stop``
- L303 `test_late_arrival_drain_still_fires_when_no_in_band_drain()` (function) — The late-arrival drain in ``finally`` must still spawn a fresh
