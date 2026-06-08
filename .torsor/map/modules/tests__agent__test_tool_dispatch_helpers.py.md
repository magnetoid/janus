---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_tool_dispatch_helpers.py

Symbols in `tests/agent/test_tool_dispatch_helpers.py`.

- L25 `TestUntrustedToolClassification` (class)
- L30 `test_named_high_risk_tools(self, name)` (method)
- L37 `test_browser_prefix_matches(self, name)` (method)
- L44 `test_mcp_prefix_matches(self, name)` (method)
- L51 `test_low_risk_tools_not_marked(self, name)` (method)
- L57 `test_empty_name_is_not_untrusted(self)` (method)
- L72 `TestUntrustedWrapping` (class)
- L73 `test_wraps_string_content_from_high_risk_tool(self)` (method)
- L82 `test_does_not_wrap_low_risk_tool(self)` (method)
- L87 `test_does_not_wrap_short_content(self)` (method)
- L92 `test_does_not_wrap_non_string_content(self)` (method)
- L102 `test_does_not_double_wrap(self)` (method)
- L113 `test_mcp_tool_result_wrapped(self)` (method)
- L119 `test_browser_tool_result_wrapped(self)` (method)
- L130 `TestMakeToolResultMessage` (class)
- L131 `test_low_risk_message_built_unchanged(self)` (method)
- L141 `test_high_risk_message_content_wrapped(self)` (method)
- L153 `test_high_risk_message_with_multimodal_content_unwrapped(self)` (method)
- L159 `test_brainworm_payload_in_web_extract_gets_data_framing(self)` (method) — The whole point: even if a webpage embeds the Brainworm payload,
