---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_tool_401_handling.py

Symbols in `tests/tools/test_mcp_tool_401_handling.py`.

- L19 `test_is_auth_error_detects_oauth_flow_error()` (function)
- L26 `test_is_auth_error_detects_oauth_non_interactive()` (function)
- L33 `test_is_auth_error_detects_httpx_401()` (function)
- L43 `test_is_auth_error_rejects_httpx_500()` (function)
- L53 `test_is_auth_error_rejects_generic_exception()` (function)
- L59 `test_call_tool_handler_returns_needs_reauth_on_unrecoverable_401(monkeypatch, tmp_path)` (function) — When session.call_tool raises 401 and handle_401 returns False,
- L111 `test_call_tool_handler_non_auth_error_still_generic(monkeypatch, tmp_path)` (function) — Non-auth exceptions still surface via the generic error path, not needs_reauth.
