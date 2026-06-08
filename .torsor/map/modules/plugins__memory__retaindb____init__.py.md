---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/retaindb/__init__.py

Symbols in `plugins/memory/retaindb/__init__.py`.

- L179 `_Client` (class)
- L180 `__init__(self, api_key: str, base_url: str, project: str)` (method)
- L185 `_headers(self, path: str)` (method)
- L196 `request(self, method: str, path: str, *, params=None, json_body=None, timeout: float=8.0)` (method)
- L219 `query_context(self, user_id: str, session_id: str, query: str, max_tokens: int=1200)` (method)
- L229 `search(self, user_id: str, session_id: str, query: str, top_k: int=8)` (method)
- L239 `get_profile(self, user_id: str)` (method)
- L245 `add_memory(self, user_id: str, session_id: str, content: str, memory_type: str='factual', importance: float=0.7)` (method)
- L257 `delete_memory(self, memory_id: str)` (method)
- L263 `ingest_session(self, user_id: str, session_id: str, messages: list, timeout: float=15.0)` (method)
- L269 `ask_user(self, user_id: str, query: str, reasoning_level: str='low')` (method)
- L274 `get_agent_model(self, agent_id: str)` (method)
- L277 `seed_agent_identity(self, agent_id: str, content: str, source: str='soul_md')` (method)
- L284 `upload_file(self, data: bytes, filename: str, remote_path: str, mime_type: str, scope: str, project_id: str | None)` (method)
- L297 `list_files(self, prefix: str | None=None, limit: int=50)` (method)
- L303 `get_file(self, file_id: str)` (method)
- L306 `read_file_content(self, file_id: str)` (method)
- L314 `ingest_file(self, file_id: str, user_id: str | None=None, agent_id: str | None=None)` (method)
- L322 `delete_file(self, file_id: str)` (method)
- L330 `_WriteQueue` (class) — SQLite-backed async write queue. Survives crashes — pending rows replay on startup.
- L333 `__init__(self, client: _Client, db_path: Path)` (method)
- L347 `_get_conn(self)` (method) — Return a cached connection for the current thread.
- L356 `_init_db(self)` (method)
- L365 `_pending_rows(self)` (method)
- L369 `enqueue(self, user_id: str, session_id: str, messages: list)` (method)
- L380 `_flush_row(self, row_id: int, user_id: str, session_id: str, messages: list)` (method)
- L393 `_loop(self)` (method)
- L405 `shutdown(self)` (method)
- L414 `_build_overlay(profile: dict, query_result: dict, local_entries: list[str] | None=None)` (function)
- L452 `RetainDBMemoryProvider` (class) — RetainDB cloud memory — durable queue, semantic search, dialectic synthesis, shared files.
- L455 `__init__(self)` (method)
- L474 `name(self)` (method)
- L477 `is_available(self)` (method)
- L480 `get_config_schema(self)` (method)
- L489 `initialize(self, session_id: str, **kwargs)` (method)
- L525 `_seed_soul(self, content: str)` (method)
- L531 `system_prompt_block(self)` (method)
- L542 `queue_prefetch(self, query: str, *, session_id: str='')` (method) — Fire context + dialectic + agent model prefetches in background.
- L559 `_prefetch_context(self, query: str)` (method)
- L569 `_prefetch_dialectic(self, query: str)` (method)
- L579 `_prefetch_agent_model(self)` (method)
- L589 `_reasoning_level(query: str)` (method)
- L597 `prefetch(self, query: str, *, session_id: str='')` (method) — Consume prefetched results and return them as a context block.
- L627 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method) — Queue turn for async ingest. Returns immediately.
- L643 `get_tool_schemas(self)` (method)
- L651 `handle_tool_call(self, tool_name: str, args: dict, **kwargs)` (method)
- L659 `_dispatch(self, tool_name: str, args: dict)` (method)
- L747 `on_memory_write(self, action: str, target: str, content: str)` (method) — Mirror built-in memory writes to RetainDB.
- L757 `shutdown(self)` (method)
- L764 `register(ctx)` (function) — Register RetainDB as a memory provider plugin.
