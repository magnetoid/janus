---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_create_openai_client_reuse.py

Symbols in `tests/run_agent/test_create_openai_client_reuse.py`.

- L25 `_make_agent()` (function)
- L36 `_make_fake_openai_factory(constructed)` (function) — Return a fake ``OpenAI`` class that records every constructed instance
- L65 `test_second_create_does_not_wrap_closed_transport_from_first()` (function) — Back-to-back _create_openai_client calls on the same _client_kwargs
- L139 `test_replace_primary_openai_client_survives_repeated_rebuilds()` (function) — Full rebuild path: exercise _replace_primary_openai_client three times
- L192 `test_force_close_tcp_sockets_descends_httpcore_1_connection_wrapper()` (function) — httpcore 1.x stores the real stream below conn._connection.
