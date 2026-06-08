---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/mem0/__init__.py

Symbols in `plugins/memory/mem0/__init__.py`.

- L40 `_load_config()` (function) — Load config from env vars, with $HERMES_HOME/mem0.json overrides.
- L119 `Mem0MemoryProvider` (class) — Mem0 Platform memory with server-side extraction and semantic search.
- L122 `__init__(self)` (method)
- L139 `name(self)` (method)
- L142 `is_available(self)` (method)
- L146 `save_config(self, values, hermes_home)` (method) — Write config to $HERMES_HOME/mem0.json.
- L161 `get_config_schema(self)` (method)
- L169 `_get_client(self)` (method) — Thread-safe client accessor with lazy initialization.
- L181 `_is_breaker_open(self)` (method) — Return True if the circuit breaker is tripped (too many failures).
- L191 `_record_success(self)` (method)
- L194 `_record_failure(self)` (method)
- L204 `initialize(self, session_id: str, **kwargs)` (method)
- L213 `_read_filters(self)` (method) — Filters for search/get_all — scoped to user only for cross-session recall.
- L217 `_write_filters(self)` (method) — Filters for add — scoped to user + agent for attribution.
- L222 `_unwrap_results(response: Any)` (method) — Normalize Mem0 API response — v2 wraps results in {"results": [...]}.
- L230 `system_prompt_block(self)` (method)
- L238 `prefetch(self, query: str, *, session_id: str='')` (method)
- L248 `queue_prefetch(self, query: str, *, session_id: str='')` (method)
- L273 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Send the turn to Mem0 for server-side fact extraction (non-blocking).
- L298 `get_tool_schemas(self)` (method)
- L301 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method)
- L364 `shutdown(self)` (method)
- L372 `register(ctx)` (function) — Register Mem0 as a memory provider plugin.
