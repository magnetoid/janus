---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_sse_transport.py

Symbols in `tests/tools/test_mcp_sse_transport.py`.

- L25 `_noop_initialize()` (function)
- L29 `_build_server_with_sse(oauth: bool=False)` (function) — Stand up an MCPServerTask configured for SSE transport, with mocks
- L42 `patch_sse_client()` (function) — Replace ``sse_client`` with a MagicMock that records its kwargs.
- L82 `TestSSEReadTimeout` (class)
- L83 `test_sse_read_timeout_is_300s_not_tool_timeout(self, patch_sse_client)` (method) — ``sse_read_timeout`` must be 300s regardless of the configured
- L114 `test_sse_read_timeout_still_300s_when_tool_timeout_is_large(self, patch_sse_client)` (method) — Even if user sets a large ``timeout``, ``sse_read_timeout`` stays
- L143 `TestSSEOAuthForwarding` (class)
- L144 `test_sse_client_receives_oauth_auth_when_configured(self, patch_sse_client)` (method) — If ``_auth_type == 'oauth'``, ``sse_client`` must receive the
- L180 `test_sse_client_omits_auth_when_no_oauth_configured(self, patch_sse_client)` (method) — Without OAuth, ``sse_client`` should not receive an ``auth=`` kwarg.
