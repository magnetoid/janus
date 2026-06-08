---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_computer_use_capture_routing.py

Symbols in `tests/tools/test_computer_use_capture_routing.py`.

- L50 `tmp_cache_dir(tmp_path)` (function) — Override get_hermes_dir so cache writes land under tmp_path.
- L62 `_make_capture(*, png_b64: str=_PNG_B64, mode: str='som', elements=None, app: str='Safari', window_title: str='GitHub – Issue #24015', width: int=1280, height: int=800)` (function)
- L93 `_stub_aux_analysis(text: str)` (function) — Return a fake vision_analyze_tool coroutine result (JSON envelope).
- L102 `TestCaptureResponseDefaultPath` (class) — When routing helper says 'native', the existing multimodal envelope wins.
- L105 `test_som_capture_returns_multimodal_envelope_when_native(self)` (method)
- L123 `test_jpeg_capture_returns_image_jpeg_mime_when_native(self)` (method)
- L134 `test_ax_only_capture_returns_text_regardless_of_routing(self)` (method)
- L155 `TestCaptureResponseRoutedToAuxVision` (class) — When routing helper says 'aux', the PNG is pre-analysed and a text
- L159 `test_som_capture_returns_text_with_vision_analysis(self, tmp_cache_dir)` (method)
- L212 `test_temp_screenshot_file_is_cleaned_up_after_routing(self, tmp_cache_dir)` (method)
- L244 `test_aux_route_creates_missing_cache_dir(self, tmp_path)` (method)
- L277 `test_temp_file_cleaned_up_even_when_aux_call_raises(self, tmp_cache_dir)` (method)
- L309 `test_empty_aux_analysis_falls_back_to_multimodal(self, tmp_cache_dir)` (method)
- L331 `test_invalid_aux_response_falls_back_to_multimodal(self, tmp_cache_dir)` (method)
- L356 `TestRoutingDecisionWiring` (class) — Verify _should_route_through_aux_vision wires the right config + helper.
- L359 `test_explicit_aux_vision_in_config_routes_to_aux(self)` (method)
- L378 `test_no_explicit_aux_and_vision_capable_main_keeps_multimodal(self)` (method)
- L396 `test_config_load_failure_disables_routing_safely(self)` (method)
- L405 `test_helper_decision_exception_is_swallowed(self)` (method)
- L423 `TestBugReproductionAnchor` (class) — Without the fix, this test would assert the wrong thing.
- L434 `test_non_vision_main_model_never_returns_image_url_when_routed(self, tmp_cache_dir)` (method)
