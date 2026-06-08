---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_keep_typing_timeout.py

Symbols in `tests/gateway/test_keep_typing_timeout.py`.

- L37 `_StubAdapter` (class)
- L38 `__init__(self)` (method)
- L41 `connect(self)` (method)
- L44 `disconnect(self)` (method)
- L47 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L50 `get_chat_info(self, chat_id)` (method)
- L54 `TestKeepTypingTimeoutPerTick` (class)
- L56 `test_slow_send_typing_does_not_block_cadence(self, monkeypatch)` (method) — A send_typing that hangs longer than the per-tick budget must be
- L106 `test_fast_send_typing_still_gets_awaited(self, monkeypatch)` (method) — When send_typing is fast (normal case), it must still complete
- L139 `test_send_typing_exception_does_not_kill_loop(self, monkeypatch)` (method) — A send_typing that raises (e.g. transient HTTP 500) must be
- L172 `test_paused_chat_skips_send_typing(self, monkeypatch)` (method) — When a chat is in _typing_paused (e.g. awaiting approval), the
