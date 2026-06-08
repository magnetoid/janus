---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_run_agent_multimodal_prologue.py

Symbols in `tests/run_agent/test_run_agent_multimodal_prologue.py`.

- L20 `TestSummarizeUserMessageForLog` (class)
- L21 `test_plain_string_passthrough(self)` (method)
- L24 `test_none_returns_empty_string(self)` (method)
- L27 `test_text_only_list(self)` (method)
- L31 `test_list_with_image_only(self)` (method)
- L36 `test_list_with_text_and_image(self)` (method)
- L45 `test_list_with_multiple_images(self)` (method)
- L54 `test_scalar_fallback(self)` (method)
- L57 `test_list_supports_slice_and_replace(self)` (method) — The whole point of this helper: its output must be a plain str.
- L66 `TestChatContentToResponsesParts` (class)
- L67 `test_non_list_returns_empty(self)` (method)
- L71 `test_text_parts_become_input_text(self)` (method)
- L75 `test_image_url_object_becomes_input_image(self)` (method)
- L81 `test_bare_string_image_url(self)` (method)
- L85 `test_responses_format_passthrough(self)` (method) — Input already in Responses format should round-trip cleanly.
- L96 `test_unknown_parts_skipped(self)` (method) — Unknown types shouldn't crash — filtered silently at this level
- L102 `test_empty_url_image_skipped(self)` (method)
