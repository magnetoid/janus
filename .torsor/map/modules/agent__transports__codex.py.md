---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/codex.py

Symbols in `agent/transports/codex.py`.

- L14 `ResponsesApiTransport` (class) — Transport for api_mode='codex_responses'.
- L28 `api_mode(self)` (method)
- L31 `_resolve_issuer_kind(self, params: Dict[str, Any])` (method) — Classify the current Responses endpoint from transport params.
- L41 `convert_messages(self, messages: List[Dict[str, Any]], **kwargs)` (method) — Convert OpenAI chat messages to Responses API input items.
- L55 `convert_tools(self, tools: List[Dict[str, Any]])` (method) — Convert OpenAI tool schemas to Responses API function definitions.
- L60 `build_kwargs(self, model: str, messages: List[Dict[str, Any]], tools: Optional[List[Dict[str, Any]]]=None, **params)` (method) — Build Responses API kwargs.
- L269 `normalize_response(self, response: Any, **kwargs)` (method) — Normalize Codex Responses API response to NormalizedResponse.
- L317 `validate_response(self, response: Any)` (method) — Check Codex Responses API response has valid output structure.
- L331 `preflight_kwargs(self, api_kwargs: Any, *, allow_stream: bool=False)` (method) — Validate and sanitize Codex API kwargs before the call.
- L339 `map_finish_reason(self, raw_reason: str)` (method) — Map Codex response.status to OpenAI finish_reason.
