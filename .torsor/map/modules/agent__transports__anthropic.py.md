---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/anthropic.py

Symbols in `agent/transports/anthropic.py`.

- L13 `AnthropicTransport` (class) — Transport for api_mode='anthropic_messages'.
- L21 `api_mode(self)` (method)
- L24 `convert_messages(self, messages: List[Dict[str, Any]], **kwargs)` (method) — Convert OpenAI messages to Anthropic (system, messages) tuple.
- L35 `convert_tools(self, tools: List[Dict[str, Any]])` (method) — Convert OpenAI tool schemas to Anthropic input_schema format.
- L41 `build_kwargs(self, model: str, messages: List[Dict[str, Any]], tools: Optional[List[Dict[str, Any]]]=None, **params)` (method) — Build Anthropic messages.create() kwargs.
- L80 `normalize_response(self, response: Any, **kwargs)` (method) — Normalize Anthropic response to NormalizedResponse.
- L143 `validate_response(self, response: Any)` (method) — Check Anthropic response structure is valid.
- L160 `extract_cache_stats(self, response: Any)` (method) — Extract Anthropic cache_read and cache_creation token counts.
- L181 `map_finish_reason(self, raw_reason: str)` (method) — Map Anthropic stop_reason to OpenAI finish_reason.
