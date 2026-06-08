---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stop_thread_sibling.py

Symbols in `tests/gateway/test_stop_thread_sibling.py`.

- L18 `_FakeAgent` (class)
- L22 `_thread_source(uid, thread_id='thr1', chat_id='chan1')` (function)
- L32 `_per_user_key(uid, thread_id='thr1', chat_id='chan1')` (function)
- L44 `test_sibling_finds_other_users_run_in_same_thread()` (function)
- L52 `test_sibling_excludes_callers_own_key()` (function)
- L60 `test_sibling_skips_pending_sentinel()` (function)
- L68 `test_sibling_does_not_match_different_thread_same_chat()` (function)
- L77 `test_sibling_returns_empty_for_non_thread_source()` (function)
- L97 `_StoreEntry` (class)
- L98 `__init__(self, session_key)` (method)
- L102 `_FakeStore` (class)
- L103 `__init__(self, session_key)` (method)
- L106 `get_or_create_session(self, source)` (method)
- L111 `test_stop_interrupts_sibling_thread_run_when_authorized(monkeypatch)` (function)
- L137 `test_stop_does_not_interrupt_sibling_when_unauthorized(monkeypatch)` (function)
