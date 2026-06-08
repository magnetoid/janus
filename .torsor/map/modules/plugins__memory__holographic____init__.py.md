---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/holographic/__init__.py

Symbols in `plugins/memory/holographic/__init__.py`.

- L97 `_load_plugin_config()` (function)
- L115 `HolographicMemoryProvider` (class) — Holographic memory with structured facts, entity resolution, and HRR retrieval.
- L118 `__init__(self, config: dict | None=None)` (method)
- L125 `name(self)` (method)
- L128 `is_available(self)` (method)
- L131 `save_config(self, values, hermes_home)` (method) — Write config to config.yaml under plugins.hermes-memory-store.
- L148 `get_config_schema(self)` (method)
- L158 `initialize(self, session_id: str, **kwargs)` (method)
- L183 `system_prompt_block(self)` (method)
- L206 `prefetch(self, query: str, *, session_id: str='')` (method)
- L222 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method)
- L227 `get_tool_schemas(self)` (method)
- L230 `handle_tool_call(self, tool_name: str, args: Dict[str, Any], **kwargs)` (method)
- L237 `on_session_end(self, messages: List[Dict[str, Any]])` (method)
- L244 `on_memory_write(self, action: str, target: str, content: str)` (method) — Mirror built-in memory writes as facts.
- L253 `shutdown(self)` (method)
- L259 `_handle_fact_store(self, args: dict)` (method)
- L346 `_handle_fact_feedback(self, args: dict)` (method)
- L359 `_auto_extract_facts(self, messages: list)` (method)
- L404 `register(ctx)` (function) — Register the holographic memory provider with the plugin system.
