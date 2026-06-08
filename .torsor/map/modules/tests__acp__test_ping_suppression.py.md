---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_ping_suppression.py

Symbols in `tests/acp/test_ping_suppression.py`.

- L27 `_make_record(msg: str, exc: BaseException | None)` (function)
- L40 `_bake_tb(exc: BaseException)` (function)
- L48 `test_filter_suppresses_benign_probe(method: str)` (function)
- L55 `test_filter_allows_real_method_not_found()` (function)
- L62 `test_filter_allows_non_request_error()` (function)
- L69 `test_filter_allows_different_message_even_for_ping()` (function) — Only 'Background task failed' is muted — other messages pass through.
- L77 `test_filter_allows_request_error_with_different_code()` (function)
- L84 `test_filter_allows_log_without_exc_info()` (function)
- L93 `_FakeAgent` (class) — Minimal acp.Agent stub — we only need the router to build.
- L96 `initialize(self, **kwargs)` (method)
- L101 `new_session(self, cwd, mcp_servers=None, **kwargs)` (method)
- L106 `prompt(self, session_id, prompt, **kwargs)` (method)
- L111 `cancel(self, session_id, **kwargs)` (method)
- L114 `authenticate(self, **kwargs)` (method)
- L117 `on_connect(self, conn)` (method)
- L122 `test_bare_ping_request_produces_proper_response_and_no_stderr_noise(caplog: pytest.LogCaptureFixture)` (function) — A bare ``ping`` must get a JSON-RPC -32601 back AND leave stderr clean
