---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_media_extraction.py

Symbols in `tests/gateway/test_media_extraction.py`.

- L18 `extract_media_tags_fixed(result_messages, history_len)` (function) — Extract MEDIA tags from tool results, but ONLY from new messages
- L50 `extract_media_tags_production(result_messages, history_len, history_media_paths)` (function) — Mirror of the production scan in gateway/run.py after the #34608 fix.
- L81 `extract_media_tags_broken(result_messages)` (function) — The BROKEN behavior: extract MEDIA tags from ALL messages including history.
- L103 `TestMediaExtraction` (class) — Tests for MEDIA tag extraction from tool results.
- L106 `test_gateway_auto_append_ignores_media_examples_in_skill_docs(self)` (method) — Skill/documentation examples must not be appended as real attachments.
- L139 `test_gateway_auto_append_keeps_real_tts_media_tag(self)` (method) — TTS tool media tags are still auto-appended when the model omits them.
- L163 `test_media_tags_not_extracted_from_history(self)` (method) — MEDIA tags from previous turns should NOT be extracted again.
- L192 `test_media_tags_extracted_from_current_turn(self)` (method) — MEDIA tags from the current turn SHOULD be extracted.
- L217 `test_multiple_tts_calls_in_history_not_accumulated(self)` (method) — Multiple TTS calls in history should NOT accumulate in new responses.
- L249 `test_deduplication_within_current_turn(self)` (method) — Multiple MEDIA tags in current turn should be deduplicated.
- L275 `TestStaleToolMediaLeak` (class) — Regression tests for #34608.
- L290 `test_stale_execute_code_media_not_attached_to_text_only_reply(self)` (method) — The exact #34608 scenario: make_image cover from an earlier turn.
- L330 `test_current_turn_media_still_attached_when_dedup_set_empty(self)` (method) — Turn-scoping must not suppress genuinely new media.
- L350 `test_compression_shrink_falls_back_to_path_dedup(self)` (method) — When the list is shorter than history_len (mid-run compression),
