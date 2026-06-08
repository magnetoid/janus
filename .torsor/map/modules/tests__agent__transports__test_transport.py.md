---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_transport.py

Symbols in `tests/agent/transports/test_transport.py`.

- L13 `TestProviderTransportABC` (class) — Verify the ABC contract is enforceable.
- L16 `test_cannot_instantiate_abc(self)` (method)
- L20 `test_concrete_must_implement_all_abstract(self)` (method)
- L28 `test_minimal_concrete(self)` (method)
- L51 `TestTransportRegistry` (class)
- L53 `test_get_unregistered_returns_none(self)` (method)
- L56 `test_anthropic_registered_on_import(self)` (method)
- L62 `test_discovers_missing_transport_when_registry_partially_populated(self)` (method) — Importing one transport directly must not hide other valid api_modes.
- L69 `test_register_and_get(self)` (method)
- L92 `TestAnthropicTransport` (class)
- L95 `transport(self)` (method)
- L99 `test_api_mode(self, transport)` (method)
- L102 `test_convert_tools_simple(self, transport)` (method)
- L116 `test_validate_response_none(self, transport)` (method)
- L119 `test_validate_response_empty_content(self, transport)` (method)
- L123 `test_validate_response_empty_content_with_end_turn_is_valid(self, transport)` (method)
- L127 `test_validate_response_empty_content_with_tool_use_is_invalid(self, transport)` (method)
- L131 `test_validate_response_valid(self, transport)` (method)
- L135 `test_map_finish_reason(self, transport)` (method)
- L144 `test_extract_cache_stats_none_usage(self, transport)` (method)
- L148 `test_extract_cache_stats_with_cache(self, transport)` (method)
- L154 `test_extract_cache_stats_zero(self, transport)` (method)
- L159 `test_normalize_response_text(self, transport)` (method) — Test normalization of a simple text response.
- L173 `test_normalize_response_tool_calls(self, transport)` (method) — Test normalization of a tool-use response.
- L196 `test_normalize_response_thinking(self, transport)` (method) — Test normalization preserves thinking content.
- L211 `test_build_kwargs_returns_dict(self, transport)` (method) — Test build_kwargs produces a usable kwargs dict.
- L224 `test_convert_messages_extracts_system(self, transport)` (method) — Test convert_messages separates system from messages.
