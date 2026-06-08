---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/byterover/__init__.py

Symbols in `plugins/memory/byterover/__init__.py`.

- L51 `_resolve_brv_path()` (function) — Find the brv binary on PATH or well-known install locations.
- L78 `_run_brv(args: List[str], timeout: int=_QUERY_TIMEOUT, cwd: str=None)` (function) — Run a brv CLI command. Returns {success, output, error}.
- L116 `_get_brv_cwd()` (function) — Profile-scoped working directory for the brv context tree.
- L171 `ByteRoverMemoryProvider` (class) — ByteRover persistent memory via the brv CLI.
- L174 `__init__(self)` (method)
- L181 `name(self)` (method)
- L184 `is_available(self)` (method) — Check if brv CLI is installed. No network calls.
- L188 `get_config_schema(self)` (method)
- L199 `initialize(self, session_id: str, **kwargs)` (method)
- L205 `system_prompt_block(self)` (method)
- L215 `prefetch(self, query: str, *, session_id: str='')` (method) — Run brv query synchronously before the agent's first LLM call.
- L233 `queue_prefetch(self, query: str, *, session_id: str='')` (method) — No-op: prefetch() now runs synchronously at turn start.
- L237 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Curate the conversation turn in background (non-blocking).
- L264 `on_memory_write(self, action: str, target: str, content: str)` (method) — Mirror built-in memory writes to ByteRover.
- L282 `on_pre_compress(self, messages: List[Dict[str, Any]])` (method) — Extract insights before context compression discards turns.
- L314 `get_tool_schemas(self)` (method)
- L317 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method)
- L326 `shutdown(self)` (method)
- L332 `_tool_query(self, args: dict)` (method)
- L355 `_tool_curate(self, args: dict)` (method)
- L370 `_tool_status(self)` (method)
- L381 `register(ctx)` (function) — Register ByteRover as a memory provider plugin.
