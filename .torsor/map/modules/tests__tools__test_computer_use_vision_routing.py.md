---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_computer_use_vision_routing.py

Symbols in `tests/tools/test_computer_use_vision_routing.py`.

- L26 `TestExplicitAuxVisionOverride` (class) — Mirror agent.image_routing — config detection must agree across paths.
- L29 `test_returns_false_for_none_cfg(self)` (method)
- L33 `test_returns_false_for_non_dict_cfg(self)` (method)
- L38 `test_returns_false_when_auxiliary_block_missing(self)` (method)
- L43 `test_returns_false_when_vision_block_missing(self)` (method)
- L48 `test_returns_false_for_blank_provider_no_model_no_base_url(self)` (method)
- L53 `test_returns_false_for_provider_auto(self)` (method)
- L58 `test_returns_false_for_provider_AUTO_uppercase(self)` (method)
- L63 `test_returns_true_for_explicit_provider(self)` (method)
- L68 `test_returns_true_for_explicit_model_only(self)` (method)
- L73 `test_returns_true_for_explicit_base_url_only(self)` (method)
- L78 `test_returns_true_for_provider_auto_plus_explicit_model(self)` (method) — ``provider: auto`` + an explicit model still counts as override.
- L88 `test_handles_non_dict_vision_block(self)` (method)
- L98 `TestRouteDecision` (class) — End-to-end policy: explicit override > tool-result support > vision caps.
- L101 `test_explicit_override_routes_to_aux_even_for_vision_main(self)` (method) — Issue #24015 core repro: explicit aux config must win.
- L126 `test_non_vision_main_model_routes_to_aux(self)` (method) — The reported #24015 scenario: tencent/hy3-preview has no vision.
- L139 `test_vision_main_model_no_override_keeps_multimodal(self)` (method) — Default path: vision-capable main model + no aux override → native.
- L151 `test_provider_rejects_multimodal_tool_results_routes_to_aux(self)` (method) — Some providers' tool-result messages won't carry images at all.
- L163 `test_user_declared_vision_support_keeps_custom_provider_native(self)` (method) — Local/custom VLMs use config as their tool-result image escape hatch.
- L181 `test_user_declared_no_vision_routes_custom_provider_to_aux(self)` (method) — An explicit false override should not fall through to native routing.
- L199 `test_unknown_provider_capabilities_fail_closed(self)` (method) — When tool-result lookup returns None, route to aux (safe default).
- L211 `test_unknown_vision_capability_fails_closed(self)` (method) — When models.dev has no entry, prefer aux over a likely 404.
- L223 `test_explicit_override_wins_over_unknown_caps(self)` (method) — Explicit aux config wins regardless of unknown caps elsewhere.
- L241 `TestLookupHelpers` (class)
- L242 `test_lookup_supports_vision_returns_none_for_blank_provider(self)` (method)
- L246 `test_lookup_supports_vision_returns_none_for_blank_model(self)` (method)
- L250 `test_lookup_supports_vision_handles_lookup_exception(self)` (method) — Underlying caps lookup may raise; helper must swallow + return None.
- L260 `test_lookup_supports_vision_returns_none_when_caps_missing(self)` (method)
- L266 `test_provider_accepts_multimodal_tool_result_returns_none_for_blank_provider(self)` (method)
- L277 `TestModuleSurface` (class) — Pin the public surface so dependents stay in lockstep.
- L280 `test_should_route_capture_to_aux_vision_is_exported(self)` (method)
- L291 `test_internal_helpers_are_addressable(self, name)` (method) — Internal helpers stay importable so tests can monkeypatch them.
