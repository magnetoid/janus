---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_prompt_caching.py

Symbols in `tests/agent/test_prompt_caching.py`.

- L13 `TestApplyCacheMarker` (class)
- L14 `test_tool_message_gets_top_level_marker_on_native_anthropic(self)` (method) — Native Anthropic path: cache_control injected top-level (adapter moves it inside tool_result).
- L20 `test_tool_message_skips_marker_on_openrouter(self)` (method) — OpenRouter path: top-level cache_control on role:tool is invalid and causes silent hang.
- L26 `test_none_content_gets_top_level_marker(self)` (method)
- L31 `test_empty_string_content_gets_top_level_marker(self)` (method) — Empty text blocks cannot have cache_control (Anthropic rejects them).
- L39 `test_string_content_wrapped_in_list(self)` (method)
- L48 `test_list_content_last_item_gets_marker(self)` (method)
- L60 `test_empty_list_content_no_crash(self)` (method)
- L66 `TestApplyAnthropicCacheControl` (class)
- L67 `test_empty_messages(self)` (method)
- L71 `test_returns_deep_copy(self)` (method)
- L79 `test_system_message_gets_marker(self)` (method)
- L90 `test_last_3_non_system_get_markers(self)` (method)
- L107 `test_no_system_message(self)` (method)
- L116 `test_1h_ttl(self)` (method)
- L123 `test_max_4_breakpoints(self)` (method)
