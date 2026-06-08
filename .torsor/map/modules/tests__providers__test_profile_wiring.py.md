---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/providers/test_profile_wiring.py

Symbols in `tests/providers/test_profile_wiring.py`.

- L13 `transport()` (function)
- L17 `_msgs()` (function)
- L21 `_max_tokens_fn(n)` (function)
- L25 `TestNvidiaProfileParity` (class)
- L26 `test_max_tokens_match(self, transport)` (method) — NVIDIA profile sets max_tokens=16384; legacy flag is removed.
- L36 `TestKimiProfileParity` (class)
- L37 `test_temperature_omitted(self, transport)` (method)
- L49 `test_max_tokens(self, transport)` (method)
- L61 `test_thinking_enabled(self, transport)` (method)
- L77 `test_thinking_disabled(self, transport)` (method)
- L93 `test_reasoning_effort_default(self, transport)` (method)
- L110 `TestOpenRouterProfileParity` (class)
- L111 `test_provider_preferences(self, transport)` (method)
- L124 `test_reasoning_full_config(self, transport)` (method)
- L137 `test_default_reasoning(self, transport)` (method)
- L150 `TestNousProfileParity` (class)
- L151 `test_tags(self, transport)` (method)
- L161 `test_reasoning_omitted_when_disabled(self, transport)` (method)
- L176 `TestQwenProfileParity` (class)
- L177 `test_max_tokens(self, transport)` (method)
- L189 `test_vl_high_resolution(self, transport)` (method)
- L199 `test_metadata_top_level(self, transport)` (method)
- L213 `test_message_preprocessing(self, transport)` (method) — Qwen profile normalizes string content to list-of-parts.
- L233 `TestDeveloperRoleParity` (class) — Developer role swap must work on BOTH legacy and profile paths.
- L236 `test_legacy_path_swaps_for_gpt5(self, transport)` (method)
- L243 `test_profile_path_swaps_for_gpt5(self, transport)` (method)
- L251 `test_profile_path_no_swap_for_claude(self, transport)` (method)
- L260 `TestRequestOverridesParity` (class) — request_overrides with extra_body must merge identically on both paths.
- L263 `test_extra_body_override_legacy(self, transport)` (method)
- L271 `test_extra_body_override_profile(self, transport)` (method)
- L279 `test_extra_body_override_merges_with_provider_body(self, transport)` (method) — Override extra_body merges WITH provider extra_body, not replaces.
- L290 `test_top_level_override(self, transport)` (method)
