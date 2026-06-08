---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_interrupt_key_match.py

Symbols in `tests/gateway/test_interrupt_key_match.py`.

- L18 `StubAdapter` (class) — Minimal adapter for interrupt tests.
- L21 `__init__(self)` (method)
- L24 `connect(self)` (method)
- L27 `disconnect(self)` (method)
- L30 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L33 `send_typing(self, chat_id, metadata=None)` (method)
- L36 `get_chat_info(self, chat_id)` (method)
- L40 `_source(chat_id='123456', chat_type='dm', thread_id=None)` (function)
- L49 `TestInterruptKeyConsistency` (class) — Ensure adapter interrupt methods are queried with session_key, not chat_id.
- L52 `test_session_key_differs_from_chat_id_for_dm(self)` (method) — Session key for a DM is namespaced and includes the DM chat_id.
- L59 `test_session_key_differs_from_chat_id_for_group(self)` (method) — Session key for a group chat includes prefix, unlike raw chat_id.
- L68 `test_has_pending_interrupt_requires_session_key(self)` (method) — has_pending_interrupt returns True only when queried with session_key.
- L86 `test_get_pending_message_requires_session_key(self)` (method) — get_pending_message returns the event only with session_key.
- L103 `test_handle_message_stores_under_session_key(self)` (method) — handle_message stores pending messages under session_key, not chat_id.
- L128 `test_photo_followup_is_queued_without_interrupt(self)` (method) — Photo follow-ups should queue behind the active run instead of interrupting it.
