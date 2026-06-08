---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_compressor_historical_media.py

Symbols in `tests/agent/test_compressor_historical_media.py`.

- L41 `TestIsImagePart` (class)
- L42 `test_openai_chat_shape(self)` (method)
- L45 `test_openai_responses_shape(self)` (method)
- L48 `test_anthropic_native_shape(self)` (method)
- L51 `test_text_part_is_not_image(self)` (method)
- L55 `test_non_dict_rejected(self)` (method)
- L61 `TestContentHasImages` (class)
- L62 `test_string_content(self)` (method)
- L65 `test_empty_list(self)` (method)
- L68 `test_text_only_list(self)` (method)
- L71 `test_list_with_image(self)` (method)
- L74 `test_none(self)` (method)
- L78 `TestStripImagesFromContent` (class)
- L79 `test_string_passthrough(self)` (method)
- L82 `test_none_passthrough(self)` (method)
- L85 `test_text_only_passthrough(self)` (method)
- L89 `test_replaces_image_with_placeholder(self)` (method)
- L99 `test_does_not_mutate_input(self)` (method)
- L105 `test_handles_all_three_shapes(self)` (method)
- L112 `TestStripHistoricalMedia` (class)
- L113 `test_empty_passthrough(self)` (method)
- L116 `test_no_images_anywhere(self)` (method)
- L124 `test_single_image_user_only_first_message(self)` (method)
- L135 `test_strips_older_user_image_keeps_newest(self)` (method)
- L148 `test_strips_assistant_and_tool_images_before_anchor(self)` (method)
- L160 `test_text_only_newest_user_still_strips_older_images(self)` (method)
- L177 `test_no_image_bearing_user_is_noop(self)` (method)
- L188 `test_does_not_mutate_input_messages(self)` (method)
- L197 `test_idempotent(self)` (method)
- L208 `test_non_dict_messages_pass_through(self)` (method)
- L221 `TestCompressIntegration` (class) — Verify the stripping runs inside ContextCompressor.compress().
- L225 `compressor(self)` (method)
- L236 `test_compress_strips_historical_images(self, compressor)` (method)
