---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_image_shrink_recovery.py

Symbols in `tests/run_agent/test_image_shrink_recovery.py`.

- L26 `_FakeApiError` (class) — Stand-in for an openai.BadRequestError with status_code + body.
- L29 `__init__(self, status_code: int, message: str, body: dict | None=None)` (method)
- L39 `TestImageTooLargeClassification` (class)
- L40 `test_anthropic_400_image_exceeds_message(self)` (method) — Anthropic's exact wording must classify as image_too_large, not context.
- L53 `test_generic_image_too_large_no_status(self)` (method) — No status_code path: message text alone triggers classification.
- L60 `test_image_too_large_not_confused_with_context_overflow(self)` (method) — 'image exceeds' must NOT be mis-classified as context_overflow.
- L73 `test_regular_context_overflow_unaffected(self)` (method) — Context-overflow errors without image keywords still classify correctly.
- L86 `_big_png_data_url(size_kb: int)` (function) — Build a data URL with a plausible large base64 payload.
- L93 `_make_agent()` (function) — Build a bare AIAgent for method-level testing, no provider setup.
- L102 `TestShrinkImagePartsHelper` (class)
- L103 `test_no_messages_returns_false(self)` (method)
- L108 `test_no_image_parts_returns_false(self)` (method)
- L116 `test_small_image_part_not_shrunk(self, monkeypatch)` (method) — An image under 4 MB is left alone — shrink helper only touches oversized ones.
- L140 `test_oversized_image_url_dict_shape_rewritten(self, monkeypatch)` (method) — OpenAI chat.completions shape: {image_url: {url: data:...}}.
- L166 `test_oversized_input_image_string_shape_rewritten(self, monkeypatch)` (method) — OpenAI Responses shape: {type: input_image, image_url: "data:..."}.
- L189 `test_multiple_images_all_shrunk(self, monkeypatch)` (method)
- L214 `test_http_url_images_not_touched(self, monkeypatch)` (method) — Only data: URLs are candidates — http URLs are server-fetched.
- L235 `test_shrink_failure_returns_false_and_leaves_url_intact(self, monkeypatch)` (method) — If re-encode fails, leave the URL alone so the caller surfaces the original error.
- L255 `test_shrink_that_makes_it_bigger_rejected(self, monkeypatch)` (method) — If the 'shrink' somehow produces a larger payload, skip it.
- L277 `test_mixed_one_shrinkable_one_not_returns_false(self, monkeypatch)` (method) — Regression for the wedged-session incident (May 2026).
