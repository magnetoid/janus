---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/mcp_oauth_manager.py

Symbols in `tools/mcp_oauth_manager.py`.

- L52 `_ProviderEntry` (class) — Per-server OAuth state tracked by the manager.
- L84 `_make_hermes_provider_class()` (function) — Lazy-import the SDK base class and return our subclass.
- L339 `MCPOAuthManager` (class) — Single source of truth for per-server MCP OAuth state.
- L347 `__init__(self)` (method)
- L353 `get_or_build_provider(self, server_name: str, server_url: str, oauth_config: Optional[dict])` (method) — Return a cached OAuth provider for ``server_name`` or build one.
- L388 `_build_provider(self, server_name: str, entry: _ProviderEntry)` (method) — Build the underlying OAuth provider.
- L448 `remove(self, server_name: str)` (method) — Evict the provider from cache AND delete tokens from disk.
- L466 `invalidate_if_disk_changed(self, server_name: str)` (method) — If the tokens file on disk has a newer mtime than last-seen, force
- L506 `handle_401(self, server_name: str, failed_access_token: Optional[str]=None)` (method) — Handle a 401 from a tool call, deduplicated across concurrent callers.
- L594 `get_manager()` (function) — Return the process-wide :class:`MCPOAuthManager` singleton.
- L603 `reset_manager_for_tests()` (function) — Test-only helper: drop the singleton so fixtures start clean.
