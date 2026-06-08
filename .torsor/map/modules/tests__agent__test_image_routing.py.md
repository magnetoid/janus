---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_image_routing.py

Symbols in `tests/agent/test_image_routing.py`.

- L25 `TestCoerceMode` (class)
- L26 `test_valid_modes_pass_through(self)` (method)
- L31 `test_case_insensitive(self)` (method)
- L35 `test_invalid_falls_back_to_auto(self)` (method)
- L41 `test_strips_whitespace(self)` (method)
- L48 `TestExplicitAuxVisionOverride` (class)
- L49 `test_none_config(self)` (method)
- L52 `test_empty_config(self)` (method)
- L55 `test_default_auto_is_not_explicit(self)` (method)
- L59 `test_provider_set_is_explicit(self)` (method)
- L63 `test_model_set_is_explicit(self)` (method)
- L67 `test_base_url_set_is_explicit(self)` (method)
- L75 `TestDecideImageInputMode` (class)
- L76 `test_explicit_native_overrides_everything(self)` (method)
- L83 `test_explicit_text_overrides_everything(self)` (method)
- L88 `test_auto_with_vision_capable_model(self)` (method)
- L92 `test_auto_with_non_vision_model(self)` (method)
- L96 `test_auto_with_unknown_model(self)` (method)
- L100 `test_auto_respects_aux_vision_override_even_for_vision_model(self)` (method) — If the user configured a dedicated vision backend, don't bypass it.
- L106 `test_none_config_is_auto(self)` (method)
- L110 `test_invalid_mode_coerces_to_auto(self)` (method)
- L115 `test_auto_uses_text_for_text_only_modalities_even_with_attachment_flag(self)` (method)
- L134 `TestCoerceCapabilityBool` (class)
- L135 `test_real_bool_passes_through(self)` (method)
- L139 `test_int_0_and_1(self)` (method)
- L143 `test_other_ints_return_none(self)` (method)
- L147 `test_yaml_true_tokens(self)` (method)
- L151 `test_yaml_false_tokens(self)` (method)
- L155 `test_quoted_false_does_not_silently_become_true(self)` (method)
- L160 `test_unrecognised_strings_return_none(self)` (method)
- L166 `test_other_types_return_none(self)` (method)
- L176 `TestSupportsVisionOverride` (class)
- L177 `test_no_cfg_returns_none(self)` (method)
- L181 `test_top_level_shortcut_wins(self)` (method)
- L185 `test_top_level_false_propagates(self)` (method)
- L189 `test_per_provider_per_model_via_runtime_name(self)` (method)
- L197 `test_per_provider_per_model_via_config_name(self)` (method)
- L208 `test_quoted_false_string_in_yaml_does_not_enable(self)` (method)
- L213 `test_unrecognised_value_falls_through(self)` (method)
- L217 `test_no_override_returns_none(self)` (method)
- L221 `test_malformed_sections_are_ignored(self)` (method)
- L231 `TestLookupSupportsVisionOverride` (class)
- L232 `test_config_override_short_circuits_models_dev(self)` (method)
- L238 `test_config_override_false_beats_vision_capable_models_dev(self)` (method)
- L245 `test_no_override_falls_back_to_models_dev(self)` (method)
- L250 `test_no_override_no_models_dev_entry_returns_none(self)` (method)
- L254 `test_cfg_none_falls_back_to_models_dev(self)` (method)
- L263 `TestAutoModeRespectsOverride` (class)
- L264 `test_auto_native_for_custom_with_supports_vision_true(self)` (method)
- L272 `test_auto_text_for_custom_with_supports_vision_false(self)` (method)
- L277 `test_auto_text_for_custom_with_no_override(self)` (method)
- L282 `test_explicit_aux_vision_override_still_wins(self)` (method)
- L296 `_png_bytes()` (function) — Return a tiny valid 1x1 transparent PNG.
- L303 `TestBuildNativeContentParts` (class)
- L304 `test_text_then_image(self, tmp_path: Path)` (method)
- L318 `test_empty_text_inserts_default_prompt(self, tmp_path: Path)` (method)
- L331 `test_missing_file_is_skipped(self, tmp_path: Path)` (method)
- L338 `test_path_hint_appended(self, tmp_path: Path)` (method) — The local path of each attached image is appended to the user
- L353 `test_path_hint_one_per_attached_image(self, tmp_path: Path)` (method) — Each successfully attached image gets its own path hint line;
- L369 `test_multiple_images(self, tmp_path: Path)` (method)
- L384 `test_mime_inference_jpg(self, tmp_path: Path)` (method)
- L392 `test_mime_inference_webp(self, tmp_path: Path)` (method)
- L400 `test_mime_sniff_overrides_misleading_extension(self, tmp_path: Path)` (method) — Discord-style bug: file is named .webp but contains PNG bytes.
- L417 `TestLargeImageHandling` (class) — Large images attach at native size; shrink is handled reactively at
- L423 `test_large_image_passes_through_unchanged(self, tmp_path: Path)` (method) — A multi-MB image is attached as-is — no resize, no skip.
- L436 `test_missing_file_returns_none(self, tmp_path: Path)` (method)
- L441 `test_build_native_parts_no_provider_kwarg(self, tmp_path: Path)` (method) — build_native_content_parts takes text + paths, no provider kwarg.
- L457 `TestExtractImageRefs` (class) — Scan task body / inbound text for image paths and URLs (kanban worker
- L461 `test_empty_or_none_returns_empty(self)` (method)
- L465 `test_finds_absolute_path(self, tmp_path: Path)` (method)
- L473 `test_finds_home_relative_path(self, tmp_path: Path, monkeypatch)` (method)
- L482 `test_skips_nonexistent_paths(self, tmp_path: Path)` (method)
- L489 `test_finds_http_image_url(self)` (method)
- L495 `test_finds_https_url_with_query_string(self)` (method)
- L500 `test_url_trailing_punctuation_stripped(self)` (method)
- L506 `test_ignores_non_image_urls(self)` (method)
- L511 `test_dedupes_paths_and_urls(self, tmp_path: Path)` (method)
- L522 `test_ignores_paths_in_fenced_code_block(self, tmp_path: Path)` (method)
- L538 `test_ignores_paths_in_inline_code(self, tmp_path: Path)` (method)
- L549 `test_does_not_match_paths_inside_urls(self, tmp_path: Path)` (method)
- L557 `test_mixed_paths_and_urls(self, tmp_path: Path)` (method)
- L568 `test_case_insensitive_extension(self, tmp_path: Path)` (method)
- L579 `TestBuildNativeContentPartsURLs` (class) — URL pass-through support added so kanban task bodies (and other
- L583 `test_url_only_no_local_paths(self)` (method)
- L599 `test_mixed_path_and_url(self, tmp_path: Path)` (method)
- L617 `test_empty_url_list_is_no_op(self, tmp_path: Path)` (method)
- L625 `test_blank_url_strings_are_dropped(self)` (method)
- L633 `test_url_only_inserts_default_prompt_when_text_empty(self)` (method)
