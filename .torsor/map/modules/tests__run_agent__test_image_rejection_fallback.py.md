---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_image_rejection_fallback.py

Symbols in `tests/run_agent/test_image_rejection_fallback.py`.

- L12 `TestStripImagesPreservesAlternation` (class) — _strip_images_from_messages must not break message role alternation.
- L15 `test_noop_when_no_images(self)` (method)
- L27 `test_string_content_untouched(self)` (method) — String content passes through — only list content is inspected.
- L34 `test_strips_image_url_part_preserves_text(self)` (method)
- L46 `test_strips_all_recognized_image_types(self)` (method)
- L60 `test_tool_message_with_all_images_replaced_not_deleted(self)` (method) — CRITICAL: tool messages must NEVER be deleted — their tool_call_id
- L93 `test_tool_message_with_mixed_content_keeps_text_parts(self)` (method)
- L116 `test_image_only_user_message_dropped(self)` (method) — Synthetic image-only user messages (gateway injection pattern) are
- L133 `test_multiple_tool_messages_all_preserved(self)` (method) — Parallel tool calls: each tool_call_id must retain a paired message.
- L161 `test_returns_false_when_nothing_changed(self)` (method)
- L168 `test_handles_non_dict_entries_gracefully(self)` (method)
- L175 `TestImageRejectionPhraseIsolation` (class) — The image-rejection phrase list must NOT false-match on other
- L200 `_matches(self, body: str)` (method)
- L204 `test_anthropic_image_too_large_does_not_trip(self)` (method)
- L217 `test_context_overflow_does_not_trip(self)` (method)
- L226 `test_rate_limit_does_not_trip(self)` (method)
- L234 `test_real_image_rejection_bodies_trip(self)` (method) — Positive cases — real-world error wordings that should trigger.
- L251 `test_codex_data_url_rejection_does_not_false_match_other_url_errors(self)` (method) — The narrow 'image_url'. expected' phrase (keyed on the
