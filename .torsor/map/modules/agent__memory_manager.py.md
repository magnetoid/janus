---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/memory_manager.py

Symbols in `agent/memory_manager.py`.

- L54 `sanitize_context(text: str)` (function) — Strip fence tags, injected context blocks, and system notes from provider output.
- L62 `StreamingContextScrubber` (class) — Stateful scrubber for streaming text that may contain split memory-context spans.
- L91 `__init__(self)` (method)
- L96 `reset(self)` (method)
- L101 `feed(self, text: str)` (method) — Return the visible portion of ``text`` after scrubbing.
- L147 `flush(self)` (method) — Emit any held-back buffer at end-of-stream.
- L164 `_max_partial_suffix(buf: str, tag: str)` (method) — Return the length of the longest buf-suffix that is a tag-prefix.
- L177 `_find_boundary_open_tag(self, buf: str)` (method) — Find an opening fence only when it starts a block-like span.
- L189 `_max_pending_open_suffix(self, buf: str)` (method) — Hold a complete boundary tag until the following char confirms it.
- L198 `_has_block_opener_suffix(self, buf: str, idx: int)` (method)
- L204 `_is_block_boundary(self, buf: str, idx: int)` (method)
- L213 `_append_visible(self, out: list[str], text: str)` (method)
- L219 `_update_block_boundary(self, text: str)` (method)
- L227 `build_memory_context_block(raw_context: str)` (function) — Wrap prefetched memory in a fenced block with system note.
- L244 `MemoryManager` (class) — Orchestrates the built-in provider plus at most one external provider.
- L251 `__init__(self)` (method)
- L258 `add_provider(self, provider: MemoryProvider)` (method) — Register a memory provider.
- L324 `providers(self)` (method) — All registered providers in order.
- L328 `get_provider(self, name: str)` (method) — Get a provider by name, or None if not registered.
- L337 `build_system_prompt(self)` (method) — Collect system prompt blocks from all providers.
- L358 `prefetch_all(self, query: str, *, session_id: str='')` (method) — Collect prefetch context from all providers.
- L377 `queue_prefetch_all(self, query: str, *, session_id: str='')` (method) — Queue background prefetch on all providers for the next turn.
- L391 `_provider_sync_accepts_messages(provider: MemoryProvider)` (method) — Return whether sync_turn accepts a messages keyword.
- L402 `sync_all(self, user_content: str, assistant_content: str, *, session_id: str='', messages: Optional[List[Dict[str, Any]]]=None)` (method) — Sync a completed turn to all providers.
- L434 `get_all_tool_schemas(self)` (method) — Collect tool schemas from all providers.
- L463 `get_all_tool_names(self)` (method) — Return set of all tool names across all providers.
- L467 `has_tool(self, tool_name: str)` (method) — Check if any provider handles this tool.
- L471 `handle_tool_call(self, tool_name: str, args: Dict[str, Any], **kwargs)` (method) — Route a tool call to the correct provider.
- L493 `on_turn_start(self, turn_number: int, message: str, **kwargs)` (method) — Notify all providers of a new turn.
- L507 `on_session_end(self, messages: List[Dict[str, Any]])` (method) — Notify all providers of session end.
- L518 `on_session_switch(self, new_session_id: str, *, parent_session_id: str='', reset: bool=False, rewound: bool=False, **kwargs)` (method) — Notify all providers that the agent's session_id has rotated.
- L566 `on_pre_compress(self, messages: List[Dict[str, Any]])` (method) — Notify all providers before context compression.
- L586 `_provider_memory_write_metadata_mode(provider: MemoryProvider)` (method) — Return how to pass metadata to a provider's memory-write hook.
- L611 `on_memory_write(self, action: str, target: str, content: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Notify external providers when the built-in memory tool writes.
- L641 `on_delegation(self, task: str, result: str, *, child_session_id: str='', **kwargs)` (method) — Notify all providers that a subagent completed.
- L655 `shutdown_all(self)` (method) — Shut down all providers (reverse order for clean teardown).
- L666 `initialize_all(self, session_id: str, **kwargs)` (method) — Initialize all providers.
