---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/supermemory/__init__.py

Symbols in `plugins/memory/supermemory/__init__.py`.

- L56 `_default_config()` (function)
- L73 `_sanitize_tag(raw: str)` (function)
- L79 `_clamp_entity_context(text: str)` (function)
- L86 `_as_bool(value: Any, default: bool)` (function)
- L98 `_load_supermemory_config(hermes_home: str)` (function)
- L144 `_save_supermemory_config(values: dict, hermes_home: str)` (function)
- L159 `_detect_category(text: str)` (function)
- L170 `_format_relative_time(iso_timestamp: str)` (function)
- L190 `_deduplicate_recall(static_facts: list, dynamic_facts: list, search_results: list)` (function)
- L209 `_format_prefetch_context(static_facts: list, dynamic_facts: list, search_results: list, max_results: int)` (function)
- L254 `_clean_text_for_capture(text: str)` (function)
- L260 `_is_trivial_message(text: str)` (function)
- L264 `_SupermemoryClient` (class)
- L265 `__init__(self, api_key: str, timeout: float, container_tag: str, search_mode: str='hybrid')` (method)
- L279 `_merge_metadata(self, metadata: Optional[dict])` (method)
- L289 `add_memory(self, content: str, metadata: Optional[dict]=None, *, entity_context: str='', container_tag: Optional[str]=None, custom_id: Optional[str]=None)` (method)
- L306 `search_memories(self, query: str, *, limit: int=5, container_tag: Optional[str]=None, search_mode: Optional[str]=None)` (method)
- L326 `get_profile(self, query: Optional[str]=None, *, container_tag: Optional[str]=None)` (method)
- L351 `forget_memory(self, memory_id: str, *, container_tag: Optional[str]=None)` (method)
- L355 `forget_by_query(self, query: str, *, container_tag: Optional[str]=None)` (method)
- L367 `ingest_conversation(self, session_id: str, messages: list[dict], metadata: dict | None=None)` (method)
- L440 `SupermemoryMemoryProvider` (class)
- L441 `__init__(self)` (method)
- L472 `name(self)` (method)
- L475 `is_available(self)` (method)
- L485 `get_config_schema(self)` (method)
- L493 `save_config(self, values, hermes_home)` (method)
- L501 `initialize(self, session_id: str, **kwargs)` (method)
- L548 `on_turn_start(self, turn_number: int, message: str, **kwargs)` (method)
- L551 `system_prompt_block(self)` (method)
- L567 `prefetch(self, query: str, *, session_id: str='')` (method)
- L584 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='')` (method)
- L596 `on_session_end(self, messages: List[Dict[str, Any]])` (method)
- L629 `on_session_switch(self, new_session_id: str, *, parent_session_id: str='', reset: bool=False, **kwargs)` (method) — Flush any buffered turns from the old session as one document, then reset for the new session.
- L674 `on_memory_write(self, action: str, target: str, content: str)` (method)
- L696 `shutdown(self)` (method)
- L728 `_resolve_tool_container_tag(self, args: dict)` (method) — Validate and resolve container_tag from tool call args.
- L748 `get_tool_schemas(self)` (method)
- L781 `_tool_store(self, args: dict)` (method)
- L804 `_tool_search(self, args: dict)` (method)
- L834 `_tool_forget(self, args: dict)` (method)
- L851 `_tool_profile(self, args: dict)` (method)
- L875 `handle_tool_call(self, tool_name: str, args: Dict[str, Any], **kwargs)` (method)
- L896 `register(ctx)` (function)
