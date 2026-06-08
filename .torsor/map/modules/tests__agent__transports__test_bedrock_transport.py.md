---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_bedrock_transport.py

Symbols in `tests/agent/transports/test_bedrock_transport.py`.

- L11 `transport()` (function)
- L16 `TestBedrockBasic` (class)
- L18 `test_api_mode(self, transport)` (method)
- L21 `test_registered(self, transport)` (method)
- L25 `TestBedrockBuildKwargs` (class)
- L27 `test_basic_kwargs(self, transport)` (method)
- L35 `test_custom_region(self, transport)` (method)
- L44 `test_max_tokens(self, transport)` (method)
- L54 `TestBedrockConvertTools` (class)
- L56 `test_convert_tools(self, transport)` (method)
- L70 `TestBedrockValidate` (class)
- L72 `test_none(self, transport)` (method)
- L75 `test_raw_dict_valid(self, transport)` (method)
- L78 `test_raw_dict_invalid(self, transport)` (method)
- L81 `test_normalized_valid(self, transport)` (method)
- L86 `TestBedrockMapFinishReason` (class)
- L88 `test_end_turn(self, transport)` (method)
- L91 `test_tool_use(self, transport)` (method)
- L94 `test_max_tokens(self, transport)` (method)
- L97 `test_guardrail(self, transport)` (method)
- L100 `test_unknown(self, transport)` (method)
- L104 `TestBedrockNormalize` (class)
- L106 `_make_bedrock_response(self, text='Hello', tool_calls=None, stop_reason='end_turn')` (method) — Build a raw Bedrock converse response dict.
- L126 `test_text_response(self, transport)` (method)
- L133 `test_tool_call_response(self, transport)` (method)
- L144 `test_raw_reasoning_content_response(self, transport)` (method)
- L162 `test_already_normalized_response(self, transport)` (method) — Test normalize_response handles already-normalized SimpleNamespace (from dispatch site).
