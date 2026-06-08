---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/bedrock.py

Symbols in `agent/transports/bedrock.py`.

- L15 `BedrockTransport` (class) — Transport for api_mode='bedrock_converse'.
- L19 `api_mode(self)` (method)
- L22 `convert_messages(self, messages: List[Dict[str, Any]], **kwargs)` (method) — Convert OpenAI messages to Bedrock Converse format.
- L27 `convert_tools(self, tools: List[Dict[str, Any]])` (method) — Convert OpenAI tool schemas to Bedrock Converse toolConfig.
- L32 `build_kwargs(self, model: str, messages: List[Dict[str, Any]], tools: Optional[List[Dict[str, Any]]]=None, **params)` (method) — Build Bedrock converse() kwargs.
- L67 `normalize_response(self, response: Any, **kwargs)` (method) — Normalize Bedrock response to NormalizedResponse.
- L118 `validate_response(self, response: Any)` (method) — Check Bedrock response structure.
- L134 `map_finish_reason(self, raw_reason: str)` (method) — Map Bedrock stop reason to OpenAI finish_reason.
