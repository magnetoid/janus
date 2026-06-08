---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/base.py

Symbols in `agent/transports/base.py`.

- L16 `ProviderTransport` (class) — Base class for provider-specific format conversion and normalization.
- L21 `api_mode(self)` (method) — The api_mode string this transport handles (e.g. 'anthropic_messages').
- L26 `convert_messages(self, messages: List[Dict[str, Any]], **kwargs)` (method) — Convert OpenAI-format messages to provider-native format.
- L35 `convert_tools(self, tools: List[Dict[str, Any]])` (method) — Convert OpenAI-format tool definitions to provider-native format.
- L43 `build_kwargs(self, model: str, messages: List[Dict[str, Any]], tools: Optional[List[Dict[str, Any]]]=None, **params)` (method) — Build the complete API call kwargs dict.
- L60 `normalize_response(self, response: Any, **kwargs)` (method) — Normalize a raw provider response to the shared NormalizedResponse type.
- L67 `validate_response(self, response: Any)` (method) — Optional: check if the raw response is structurally valid.
- L75 `extract_cache_stats(self, response: Any)` (method) — Optional: extract provider-specific cache hit/creation stats.
- L83 `map_finish_reason(self, raw_reason: str)` (method) — Optional: map provider-specific stop reason to OpenAI equivalent.
