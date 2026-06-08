---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/model_providers/test_kimi_profile.py

Symbols in `tests/plugins/model_providers/test_kimi_profile.py`.

- L18 `kimi_profile()` (function) — Resolve the registered Kimi profile via the provider registry.
- L34 `TestKimiReasoningWireShape` (class) — ``build_api_kwargs_extras`` never emits thinking + reasoning_effort together.
- L37 `test_no_config_enables_thinking_without_effort(self, kimi_profile)` (method) — No reasoning_config → thinking on, server picks the depth.
- L49 `test_explicit_effort_sends_effort_only(self, kimi_profile, effort)` (method)
- L56 `test_enabled_without_effort_falls_back_to_thinking(self, kimi_profile)` (method)
- L64 `test_unrecognized_effort_falls_back_to_thinking(self, kimi_profile, effort)` (method) — Unknown/strong efforts aren't in Moonshot's low|medium|high set, so
- L73 `test_disabled_sends_thinking_disabled_only(self, kimi_profile)` (method)
- L80 `test_disabled_ignores_effort(self, kimi_profile)` (method)
- L98 `test_never_emits_both(self, kimi_profile, reasoning_config)` (method) — The core invariant: thinking and reasoning_effort are never both set.
- L106 `TestKimiFullKwargsIntegration` (class) — The transport's full kwargs carry at most one reasoning knob.
- L109 `_build(self, kimi_profile, reasoning_config)` (method)
- L122 `test_explicit_effort_omits_thinking(self, kimi_profile)` (method)
- L127 `test_no_config_omits_effort(self, kimi_profile)` (method)
