---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_tool_session_expired.py

Symbols in `tests/tools/test_mcp_tool_session_expired.py`.

- L25 `test_is_session_expired_detects_invalid_or_expired_session()` (function) — Reporter's exact wpcom-mcp error message (#13383).
- L32 `test_is_session_expired_detects_expired_session_variant()` (function) — Generic ``session expired`` / ``expired session`` phrasings used
- L40 `test_is_session_expired_detects_session_not_found()` (function) — Server-side GC produces ``session not found`` / ``unknown session``
- L48 `test_is_session_expired_detects_session_terminated()` (function) — Remote Playwright MCP reports transport loss as ``Session terminated``.
- L55 `test_is_session_expired_detects_stale_pipe_and_closed_transport_variants()` (function) — Stdio/AnyIO stale-pipe failures usually surface as closed-resource
- L66 `test_is_session_expired_is_case_insensitive()` (function) — Match uses lower-cased comparison so servers that emit the
- L74 `test_is_session_expired_rejects_unrelated_errors()` (function) — Narrow scope: only the specific session-expired markers trigger.
- L85 `test_is_session_expired_rejects_interrupted_error()` (function) — InterruptedError is the user-cancel signal — must never route
- L93 `test_is_session_expired_rejects_empty_message()` (function) — Bare exceptions with no message shouldn't match.
- L105 `_install_stub_server(name: str='wpcom')` (function) — Register a minimal server stub that _handle_session_expired_and_retry
- L139 `test_call_tool_handler_reconnects_on_session_expired(monkeypatch, tmp_path)` (function) — Reporter's exact repro: call_tool raises "Invalid or expired
- L191 `test_call_tool_handler_non_session_expired_error_falls_through(monkeypatch, tmp_path)` (function) — Preserved-behaviour canary: a non-session-expired exception must
- L228 `test_session_expired_handler_returns_none_without_loop(monkeypatch)` (function) — Defensive: if the MCP loop isn't running (cold start / shutdown
- L260 `test_session_expired_handler_returns_none_without_server_record()` (function) — If the server has been torn down / isn't in _servers, fall
- L273 `test_session_expired_handler_returns_none_when_retry_also_fails(monkeypatch, tmp_path)` (function) — If the retry after reconnect also raises, fall through to the
- L320 `test_non_tool_handlers_also_reconnect_on_session_expired(monkeypatch, tmp_path, handler_factory, handler_kwargs, session_method, op_label)` (function) — All four non-``tools/call`` MCP handlers share the recovery
