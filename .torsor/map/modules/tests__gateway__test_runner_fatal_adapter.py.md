---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_runner_fatal_adapter.py

Symbols in `tests/gateway/test_runner_fatal_adapter.py`.

- L10 `_FatalAdapter` (class)
- L11 `__init__(self)` (method)
- L14 `connect(self)` (method)
- L22 `disconnect(self)` (method)
- L25 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L28 `get_chat_info(self, chat_id)` (method)
- L32 `_RuntimeRetryableAdapter` (class)
- L33 `__init__(self)` (method)
- L36 `connect(self)` (method)
- L39 `disconnect(self)` (method)
- L42 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L45 `get_chat_info(self, chat_id)` (method)
- L50 `test_runner_requests_clean_exit_for_nonretryable_startup_conflict(monkeypatch, tmp_path)` (function)
- L69 `test_runner_queues_retryable_runtime_fatal_for_reconnection(monkeypatch, tmp_path)` (function) — Retryable runtime fatal errors queue the platform for reconnection
