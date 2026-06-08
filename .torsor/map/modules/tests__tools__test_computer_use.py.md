---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_computer_use.py

Symbols in `tests/tools/test_computer_use.py`.

- L20 `_reset_backend()` (function) — Tear down the cached backend between tests.
- L31 `noop_backend()` (function) — Return the active noop backend instance so tests can inspect calls.
- L41 `TestSchema` (class)
- L42 `test_schema_is_universal_openai_function_format(self)` (method)
- L51 `test_schema_does_not_use_anthropic_native_types(self)` (method) — Generic OpenAI schema — no `type: computer_20251124`.
- L59 `test_schema_supports_element_and_coordinate_targeting(self)` (method)
- L67 `test_schema_lists_all_expected_actions(self)` (method)
- L75 `test_capture_mode_enum_has_som_vision_ax(self)` (method)
- L80 `test_schema_exposes_max_elements_cap_for_capture(self)` (method)
- L87 `test_schema_max_elements_documents_default_and_upper_bound(self)` (method) — Schema description must agree with the runtime. The original PR
- L102 `TestRegistration` (class)
- L103 `test_tool_registers_with_registry(self)` (method)
- L112 `test_check_fn_is_false_on_linux(self)` (method)
- L124 `TestDispatch` (class)
- L125 `test_missing_action_returns_error(self)` (method)
- L131 `test_unknown_action_returns_error(self)` (method)
- L137 `test_list_apps_returns_json(self, noop_backend)` (method)
- L144 `test_wait_clamps_long_waits(self, noop_backend)` (method)
- L152 `test_click_without_target_returns_error(self, noop_backend)` (method)
- L160 `test_click_by_element_routes_to_backend(self, noop_backend)` (method)
- L168 `test_double_click_sets_click_count(self, noop_backend)` (method)
- L174 `test_right_click_sets_button(self, noop_backend)` (method)
- L180 `test_type_action_routes_to_type_text_backend(self, noop_backend)` (method) — type action must call backend.type_text, not type_text_chars (issue #24170, bug 3).
- L191 `test_drag_action_routes_to_backend_by_coordinate(self, noop_backend)` (method) — drag action must dispatch to backend.drag with coordinates (issue #24170, bug 4).
- L207 `test_drag_action_routes_to_backend_by_element(self, noop_backend)` (method) — drag action must dispatch to backend.drag with element indices (issue #24170, bug 4).
- L223 `test_drag_action_requires_coordinates_or_elements(self, noop_backend)` (method) — drag without from/to must return an error.
- L230 `test_set_value_routes_to_backend(self, noop_backend)` (method) — set_value must reach the backend — regression for missing _NoopBackend stub.
- L239 `test_set_value_missing_value_returns_error(self, noop_backend)` (method)
- L244 `test_capture_after_skipped_when_action_failed(self, noop_backend)` (method) — capture_after must not fire when res.ok=False (regression guard).
- L269 `test_capture_after_fires_when_action_succeeds(self, noop_backend)` (method) — capture_after must trigger for successful actions.
- L283 `TestSafetyGuards` (class)
- L291 `test_blocked_type_patterns(self, text, noop_backend)` (method)
- L304 `test_blocked_key_combos(self, keys, noop_backend)` (method)
- L311 `test_safe_key_combos_pass(self, noop_backend)` (method)
- L317 `test_type_with_empty_string_is_allowed(self, noop_backend)` (method)
- L328 `TestCaptureResponse` (class)
- L329 `test_capture_ax_mode_returns_text_json(self, noop_backend)` (method)
- L336 `test_capture_vision_mode_with_image_returns_multimodal_envelope(self)` (method) — Inject a fake backend that returns a PNG to exercise the envelope path.
- L375 `test_capture_som_with_elements_formats_index(self)` (method)
- L414 `_ax_backend_with(self, count: int)` (method) — Construct a fake backend that yields ``count`` AX elements.
- L445 `test_capture_ax_caps_elements_at_default_for_dense_trees(self)` (method) — Regression for #22865: an Electron-style 600-element AX tree must
- L465 `test_capture_ax_honors_explicit_max_elements_override(self)` (method)
- L479 `test_capture_ax_below_cap_is_unchanged(self)` (method) — Backwards-compat: small captures keep the full elements array and
- L496 `test_capture_ax_invalid_max_elements_falls_back_to_default(self)` (method) — Malformed `max_elements` (string, negative, zero) must not silently
- L514 `test_capture_ax_clamps_oversized_max_elements_to_hard_cap(self)` (method) — A caller passing a very large `max_elements` must not be able to
- L532 `test_capture_ax_summary_indices_match_returned_elements(self)` (method) — When `max_elements` is below the human-summary's own line cap, the
- L558 `test_capture_multimodal_summary_omits_truncation_note(self)` (method) — The som/vision multimodal envelope returns a screenshot, not an
- L605 `TestCuaCaptureImageDimensions` (class)
- L606 `test_png_dimensions_are_sniffed_from_image_bytes(self)` (method)
- L616 `test_jpeg_dimensions_are_sniffed_from_sof_segment(self)` (method)
- L635 `TestAnthropicAdapterMultimodal` (class)
- L636 `test_multimodal_envelope_becomes_tool_result_with_image_block(self)` (method)
- L675 `test_old_screenshots_are_evicted_beyond_max_keep(self)` (method) — Image blocks in old tool_results get replaced with placeholders.
- L740 `test_content_parts_helper_filters_to_text_and_image(self)` (method)
- L759 `TestCompressorScreenshotPruning` (class)
- L760 `_make_compressor(self)` (method)
- L766 `test_prunes_openai_content_parts_image(self)` (method)
- L797 `test_prunes_multimodal_envelope_dict(self)` (method)
- L822 `TestImageAwareTokenEstimator` (class)
- L823 `test_image_block_counts_as_flat_1500_tokens(self)` (method)
- L838 `test_multimodal_envelope_counts_images(self)` (method)
- L859 `TestPromptGuidance` (class)
- L860 `test_computer_use_guidance_constant_exists(self)` (method)
- L872 `TestRunAgentMultimodalHelpers` (class)
- L873 `test_is_multimodal_tool_result(self)` (method)
- L882 `test_multimodal_text_summary_prefers_summary(self)` (method)
- L891 `test_multimodal_text_summary_falls_back_to_parts(self)` (method)
- L899 `test_append_subdir_hint_to_multimodal_appends_to_text_part(self)` (method)
- L915 `test_trajectory_normalize_strips_images(self)` (method)
- L934 `test_computer_use_image_result_becomes_error_for_text_only_model(self)` (method)
- L957 `test_computer_use_image_result_preserved_for_vision_model(self)` (method)
- L975 `test_other_multimodal_tool_uses_text_summary_for_text_only_model(self)` (method)
- L1000 `TestUniversality` (class)
- L1001 `test_schema_is_valid_openai_function_schema(self)` (method) — The schema must be round-trippable as a standard OpenAI tool definition.
- L1011 `test_no_provider_gating_in_tool_registration(self)` (method) — Anthropic-only gating was a #4562 artefact — must not recur.
- L1028 `TestElementLabelParsing` (class) — Bug 5: element labels stripped in capture results (cua-driver v0.1.6 format).
- L1035 `test_classic_quoted_label_format(self)` (method)
- L1050 `test_new_id_eq_format(self)` (method) — cua-driver v0.1.6 format: [N] AXRole (order) id=Label
- L1066 `test_mixed_formats_in_single_tree(self)` (method) — Gracefully handles trees that mix old and new line formats.
- L1082 `TestCaptureAfterAppContext` (class) — Bug 2: capture_after=True loses app context after actions.
- L1089 `test_capture_after_uses_last_app(self)` (method) — capture_after=True should pass _last_app to the follow-up capture.
- L1155 `test_capture_after_without_prior_app_uses_none(self)` (method) — When no app context is set, follow-up capture uses app=None (frontmost).
- L1225 `_make_cua_backend_with_windows(windows: List[Dict[str, Any]])` (function) — Construct a CuaDriverBackend with a mocked MCP session that returns
- L1241 `TestCuaDriverSessionReconnect` (class)
- L1242 `test_call_tool_reconnects_once_after_closed_resource(self)` (method) — A daemon restart closes the cached MCP stdio channel; recover once.
- L1281 `test_call_tool_does_not_retry_on_unrelated_error(self)` (method) — Non-transport errors must propagate without a reconnect attempt.
- L1313 `TestCaptureAppFilterNoMatch` (class) — capture(app=X) must not silently fall back to the frontmost window
- L1322 `test_app_filter_no_match_returns_empty_capture_with_diagnostic(self)` (method)
- L1345 `test_app_filter_match_still_works(self)` (method)
- L1366 `test_no_app_filter_still_picks_frontmost(self)` (method) — When no app= is given, capture continues to pick the frontmost
- L1386 `TestFocusAppFilterNoMatch` (class) — focus_app(app=X) must return ok=False when X matches nothing —
- L1392 `test_focus_app_no_match_returns_not_ok(self)` (method)
- L1409 `test_focus_app_match_still_works(self)` (method)
