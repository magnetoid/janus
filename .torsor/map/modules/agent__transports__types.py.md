---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/types.py

Symbols in `agent/transports/types.py`.

- L19 `ToolCall` (class) — A normalized tool call from any provider.
- L46 `type(self)` (method)
- L50 `function(self)` (method) — Return self so tc.function.name / tc.function.arguments work.
- L55 `call_id(self)` (method) — Codex call_id from provider_data, accessed via getattr by _build_assistant_message.
- L60 `response_item_id(self)` (method) — Codex response_item_id from provider_data.
- L65 `extra_content(self)` (method) — Gemini extra_content (thought_signature) from provider_data.
- L80 `Usage` (class) — Token usage from an API response.
- L90 `NormalizedResponse` (class) — Normalized API response from any provider.
- L115 `reasoning_content(self)` (method)
- L120 `reasoning_details(self)` (method)
- L125 `codex_reasoning_items(self)` (method)
- L130 `codex_message_items(self)` (method)
- L140 `build_tool_call(id: str | None, name: str, arguments: Any, **provider_fields: Any)` (function) — Build a ``ToolCall``, auto-serialising *arguments* if it's a dict.
- L155 `map_finish_reason(reason: str | None, mapping: dict[str, str])` (function) — Translate a provider-specific stop reason to the normalised set.
