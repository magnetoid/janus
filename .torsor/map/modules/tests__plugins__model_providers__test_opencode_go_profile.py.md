---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/model_providers/test_opencode_go_profile.py

Symbols in `tests/plugins/model_providers/test_opencode_go_profile.py`.

- L9 `opencode_go_profile()` (function) — Resolve the registered OpenCode Go provider profile.
- L19 `TestOpenCodeGoKimiReasoning` (class) — Kimi K2 models use Moonshot's thinking + reasoning_effort shape on OpenCode Go.
- L22 `test_high_effort_emits_thinking_and_effort(self, opencode_go_profile)` (method)
- L30 `test_disabled_emits_thinking_disabled_without_effort(self, opencode_go_profile)` (method)
- L38 `test_minimal_effort_enables_thinking_without_effort(self, opencode_go_profile)` (method)
- L54 `test_strong_efforts_clamp_to_high(self, opencode_go_profile, effort)` (method)
- L62 `test_low_and_medium_pass_through(self, opencode_go_profile)` (method)
- L71 `test_no_config_preserves_server_default(self, opencode_go_profile)` (method)
- L80 `TestOpenCodeGoDeepSeekThinking` (class) — DeepSeek V4 models use DeepSeek-style thinking controls on OpenCode Go.
- L83 `test_high_effort_emits_thinking_and_effort(self, opencode_go_profile)` (method)
- L91 `test_disabled_emits_thinking_disabled_without_effort(self, opencode_go_profile)` (method)
- L99 `test_no_config_emits_thinking_enabled_without_effort(self, opencode_go_profile)` (method)
- L107 `test_minimal_effort_enables_thinking_without_effort(self, opencode_go_profile)` (method)
- L115 `test_xhigh_and_max_normalize_to_max(self, opencode_go_profile)` (method)
- L125 `TestOpenCodeGoModelGating` (class) — Other OpenCode Go models must not receive Kimi/DeepSeek controls.
- L140 `test_non_target_models_emit_nothing(self, opencode_go_profile, model)` (method)
- L149 `TestOpenCodeGoFullKwargsIntegration` (class) — End-to-end transport kwargs include the profile-provided controls.
- L152 `test_kimi_reasoning_reaches_extra_body_and_top_level(self, opencode_go_profile)` (method)
- L166 `test_deepseek_thinking_reaches_extra_body_and_top_level(self, opencode_go_profile)` (method)
