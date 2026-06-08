---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_circuit_breaker.py

Symbols in `tests/tools/test_mcp_circuit_breaker.py`.

- L28 `_install_stub_server(mcp_tool_module, name: str, call_tool_impl)` (function) — Install a fake MCP server in the module's registry.
- L50 `_cleanup(mcp_tool_module, name: str)` (function)
- L62 `test_circuit_breaker_half_opens_after_cooldown(monkeypatch, tmp_path)` (function) — After a tripped breaker's cooldown elapses, the *next* call must
- L131 `test_circuit_breaker_reopens_on_probe_failure(monkeypatch, tmp_path)` (function) — If the half-open probe fails, the breaker must re-arm the
- L182 `test_circuit_breaker_cleared_on_reconnect(monkeypatch, tmp_path)` (function) — When the auth-recovery path successfully reconnects the server,
