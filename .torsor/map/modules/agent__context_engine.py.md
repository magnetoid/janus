---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/context_engine.py

Symbols in `agent/context_engine.py`.

- L32 `ContextEngine` (class) — Base class all context engines must implement.
- L39 `name(self)` (method) — Short identifier (e.g. 'compressor', 'lcm').
- L71 `update_from_response(self, usage: Dict[str, Any])` (method) — Update tracked token usage from an API response.
- L83 `should_compress(self, prompt_tokens: int=None)` (method) — Return True if compaction should fire this turn.
- L87 `compress(self, messages: List[Dict[str, Any]], current_tokens: int=None, focus_topic: str=None)` (method) — Compact the message list and return the new message list.
- L110 `should_compress_preflight(self, messages: List[Dict[str, Any]])` (method) — Quick rough check before the API call (no real token count yet).
- L118 `should_defer_preflight_to_real_usage(self, rough_tokens: int)` (method) — Return True when preflight should trust recent real usage instead.
- L129 `has_content_to_compress(self, messages: List[Dict[str, Any]])` (method) — Quick check: is there anything in ``messages`` that can be compacted?
- L144 `on_session_start(self, session_id: str, **kwargs)` (method) — Called when a new conversation session begins.
- L151 `on_session_end(self, session_id: str, messages: List[Dict[str, Any]])` (method) — Called at real session boundaries (CLI exit, /reset, gateway expiry).
- L158 `on_session_reset(self)` (method) — Called on /new or /reset. Reset per-session state.
- L170 `get_tool_schemas(self)` (method) — Return tool schemas this engine provides to the agent.
- L178 `handle_tool_call(self, name: str, args: Dict[str, Any], **kwargs)` (method) — Handle a tool call from the agent.
- L192 `get_status(self)` (method) — Return status dict for display/logging.
- L210 `update_model(self, model: str, context_length: int, base_url: str='', api_key: str='', provider: str='', api_mode: str='')` (method) — Called when the user switches models or on fallback activation.
