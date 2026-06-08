---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_config_null_guard.py

Symbols in `tests/tools/test_config_null_guard.py`.

- L13 `TestTTSProviderNullGuard` (class) — tools/tts_tool.py — _get_provider()
- L16 `test_explicit_null_provider_returns_default(self)` (method) — YAML ``tts: {provider: null}`` should fall back to default.
- L23 `test_missing_provider_returns_default(self)` (method) — No ``provider`` key at all should also return default.
- L30 `test_valid_provider_passed_through(self)` (method)
- L39 `TestWebBackendNullGuard` (class) — tools/web_tools.py — _get_backend()
- L43 `test_explicit_null_backend_does_not_crash(self, _cfg)` (method) — YAML ``web: {backend: null}`` should not raise AttributeError.
- L52 `test_missing_backend_does_not_crash(self, _cfg)` (method)
- L61 `TestMCPAuthNullGuard` (class) — tools/mcp_tool.py — MCPServerTask.__init__() auth config line
- L64 `test_explicit_null_auth_does_not_crash(self)` (method) — YAML ``auth: null`` in MCP server config should not raise.
- L71 `test_missing_auth_defaults_to_empty(self)` (method)
- L76 `test_valid_auth_passed_through(self)` (method)
- L84 `TestTrajectoryCompressorNullGuard` (class) — trajectory_compressor.py — _detect_provider() and config loading
- L87 `test_null_base_url_does_not_crash(self)` (method) — base_url=None should not crash _detect_provider().
- L101 `test_config_loading_null_base_url_keeps_default(self)` (method) — YAML ``summarization: {base_url: null}`` should keep default.
