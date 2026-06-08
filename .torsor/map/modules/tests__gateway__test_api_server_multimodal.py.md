---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_multimodal.py

Symbols in `tests/gateway/test_api_server_multimodal.py`.

- L31 `TestNormalizeMultimodalContent` (class)
- L32 `test_string_passthrough(self)` (method)
- L35 `test_none_returns_empty_string(self)` (method)
- L38 `test_text_only_list_collapses_to_string(self)` (method)
- L42 `test_responses_input_text_canonicalized(self)` (method)
- L46 `test_image_url_preserved_with_text(self)` (method)
- L58 `test_input_image_converted_to_canonical_shape(self)` (method)
- L69 `test_data_image_url_accepted(self)` (method)
- L74 `test_non_image_data_url_rejected(self)` (method)
- L80 `test_file_part_rejected(self)` (method)
- L85 `test_input_file_part_rejected(self)` (method)
- L90 `test_missing_url_rejected(self)` (method)
- L95 `test_bad_scheme_rejected(self)` (method)
- L100 `test_unknown_part_type_rejected(self)` (method)
- L106 `TestContentHasVisiblePayload` (class)
- L107 `test_non_empty_string(self)` (method)
- L110 `test_whitespace_only_string(self)` (method)
- L113 `test_list_with_image_only(self)` (method)
- L116 `test_list_with_only_empty_text(self)` (method)
- L125 `_make_adapter()` (function)
- L129 `_create_app(adapter: APIServerAdapter)` (function)
- L140 `adapter()` (function)
- L144 `TestChatCompletionsMultimodalHTTP` (class)
- L146 `test_inline_image_preserved_to_run_agent(self, adapter)` (method) — Multimodal user content reaches _run_agent as a list of parts.
- L180 `test_text_only_array_collapses_to_string(self, adapter)` (method) — Text-only array becomes a plain string so logging stays unchanged.
- L207 `test_file_part_returns_400(self, adapter)` (method)
- L225 `test_non_image_data_url_returns_400(self, adapter)` (method)
- L250 `TestResponsesMultimodalHTTP` (class)
- L252 `test_input_image_canonicalized_and_forwarded(self, adapter)` (method)
- L291 `test_input_file_returns_400(self, adapter)` (method)
