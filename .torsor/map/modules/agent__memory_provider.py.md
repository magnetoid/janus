---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/memory_provider.py

Symbols in `agent/memory_provider.py`.

- L42 `MemoryProvider` (class) — Abstract base class for memory providers.
- L47 `name(self)` (method) — Short identifier for this provider (e.g. 'builtin', 'honcho', 'hindsight').
- L53 `is_available(self)` (method) — Return True if this provider is configured, has credentials, and is ready.
- L61 `initialize(self, session_id: str, **kwargs)` (method) — Initialize for a session.
- L84 `system_prompt_block(self)` (method) — Return text to include in the system prompt.
- L93 `prefetch(self, query: str, *, session_id: str='')` (method) — Recall relevant context for the upcoming turn.
- L107 `queue_prefetch(self, query: str, *, session_id: str='')` (method) — Queue a background recall for the NEXT turn.
- L115 `sync_turn(self, user_content: str, assistant_content: str, *, session_id: str='', messages: Optional[List[Dict[str, Any]]]=None)` (method) — Persist a completed turn to the backend.
- L134 `get_tool_schemas(self)` (method) — Return tool schemas this provider exposes.
- L143 `handle_tool_call(self, tool_name: str, args: Dict[str, Any], **kwargs)` (method) — Handle a tool call for one of this provider's tools.
- L151 `shutdown(self)` (method) — Clean shutdown — flush queues, close connections.
- L156 `on_turn_start(self, turn_number: int, message: str, **kwargs)` (method) — Called at the start of each turn with the user message.
- L165 `on_session_end(self, messages: List[Dict[str, Any]])` (method) — Called when a session ends (explicit exit or timeout).
- L175 `on_session_switch(self, new_session_id: str, *, parent_session_id: str='', reset: bool=False, rewound: bool=False, **kwargs)` (method) — Called when the agent switches session_id mid-process.
- L219 `on_pre_compress(self, messages: List[Dict[str, Any]])` (method) — Called before context compression discards old messages.
- L231 `on_delegation(self, task: str, result: str, *, child_session_id: str='', **kwargs)` (method) — Called on the PARENT agent when a subagent completes.
- L244 `get_config_schema(self)` (method) — Return config fields this provider needs for setup.
- L262 `save_config(self, values: Dict[str, Any], hermes_home: str)` (method) — Write non-secret config to the provider's native location.
- L279 `on_memory_write(self, action: str, target: str, content: str, metadata: Optional[Dict[str, Any]]=None)` (method) — Called when the built-in memory tool writes an entry.
