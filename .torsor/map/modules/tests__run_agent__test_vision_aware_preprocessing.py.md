---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_vision_aware_preprocessing.py

Symbols in `tests/run_agent/test_vision_aware_preprocessing.py`.

- L22 `_make_agent()` (function) — Build a bare-bones AIAgent instance without running __init__.
- L48 `TestPrepareAnthropicMessages` (class)
- L49 `test_no_images_passes_through(self)` (method)
- L55 `test_vision_capable_passes_images_through(self)` (method) — The Anthropic adapter handles image_url/input_image natively.
- L63 `test_non_vision_replaces_images_with_text(self)` (method)
- L84 `TestPrepareMessagesForNonVision` (class)
- L85 `test_no_images_passes_through(self)` (method)
- L91 `test_vision_capable_passes_through(self)` (method) — For vision-capable models on chat.completions path, provider handles pixels.
- L100 `test_non_vision_strips_images(self)` (method)
- L116 `test_multiple_messages_with_mixed_content(self)` (method)
- L141 `TestModelSupportsVision` (class)
- L142 `test_missing_provider_or_model_returns_false(self)` (method)
- L151 `test_uses_get_model_capabilities(self)` (method)
- L161 `test_none_caps_returns_false(self)` (method)
- L166 `test_exception_returns_false(self)` (method)
- L171 `test_top_level_model_override_wins(self)` (method)
- L179 `test_per_provider_per_model_override_wins(self)` (method)
- L188 `test_named_custom_provider_resolved_via_config_provider(self)` (method)
- L203 `test_override_false_disables_vision_for_models_dev_models(self)` (method)
