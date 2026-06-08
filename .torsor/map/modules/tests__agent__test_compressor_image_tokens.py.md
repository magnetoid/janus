---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_compressor_image_tokens.py

Symbols in `tests/agent/test_compressor_image_tokens.py`.

- L20 `TestContentLengthForBudget` (class)
- L21 `test_plain_string(self)` (method)
- L24 `test_empty_string(self)` (method)
- L27 `test_none_coerces_to_zero(self)` (method)
- L30 `test_text_only_list(self)` (method)
- L37 `test_single_image_part_charges_fixed_budget(self)` (method)
- L45 `test_image_url_raw_base64_is_not_counted_as_chars(self)` (method) — A 1MB base64 blob inside an image_url must NOT inflate token count.
- L58 `test_multiple_image_parts(self)` (method)
- L67 `test_openai_responses_input_image_shape(self)` (method) — Responses API uses type=input_image with top-level image_url string.
- L76 `test_anthropic_native_image_shape(self)` (method) — Anthropic native shape: {type: image, source: {...}}.
- L84 `test_bare_string_part_in_list(self)` (method) — Older code paths sometimes produce mixed list-of-strings content.
- L89 `test_image_estimate_constant_is_reasonable(self)` (method) — Sanity-check the estimate aligns with real provider billing.
- L102 `TestTokenBudgetWithImages` (class) — Integration: the compressor's tail-cut decision now respects image cost.
- L105 `test_image_heavy_turns_count_toward_budget(self)` (method) — A tail with 5 image-bearing turns should blow past a 5K token budget.
