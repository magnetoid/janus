---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_openai_client_lifecycle.py

Symbols in `tests/run_agent/test_openai_client_lifecycle.py`.

- L18 `FakeRequestClient` (class)
- L19 `__init__(self, responder)` (method)
- L28 `_create(self, **kwargs)` (method)
- L31 `close(self)` (method)
- L36 `FakeSharedClient` (class)
- L40 `OpenAIFactory` (class)
- L41 `__init__(self, clients)` (method)
- L45 `__call__(self, **kwargs)` (method)
- L52 `_build_agent(shared_client=None)` (function)
- L72 `_connection_error()` (function)
- L79 `test_retry_after_api_connection_error_recreates_request_client(monkeypatch)` (function)
- L98 `test_stale_non_stream_close_is_single_owner(monkeypatch)` (function)
- L116 `test_closed_shared_client_is_recreated_before_request(monkeypatch)` (function)
- L135 `test_concurrent_requests_do_not_break_each_other_when_one_client_closes(monkeypatch)` (function)
- L178 `test_streaming_call_recreates_closed_shared_client_before_request(monkeypatch)` (function)
