---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/model_providers/test_deepseek_profile.py

Symbols in `tests/plugins/model_providers/test_deepseek_profile.py`.

- L19 `deepseek_profile()` (function) — Resolve the registered DeepSeek profile.
- L36 `TestDeepSeekThinkingWireShape` (class) — ``build_api_kwargs_extras`` produces DeepSeek's exact wire format.
- L39 `test_v4_pro_default_enables_thinking_without_effort(self, deepseek_profile)` (method) — No reasoning_config → thinking enabled, server picks default effort.
- L47 `test_v4_pro_enabled_with_high_effort(self, deepseek_profile)` (method)
- L56 `test_standard_efforts_pass_through(self, deepseek_profile, effort)` (method)
- L64 `test_xhigh_and_max_normalize_to_max(self, deepseek_profile, effort)` (method)
- L71 `test_explicitly_disabled_sends_disabled_marker(self, deepseek_profile)` (method) — ``reasoning_config.enabled=False`` → ``thinking.type=disabled``.
- L84 `test_disabled_ignores_effort_field(self, deepseek_profile)` (method) — Effort silently dropped when thinking is off.
- L92 `test_unknown_effort_omits_top_level(self, deepseek_profile)` (method) — Garbage effort → omit reasoning_effort so DeepSeek applies its default.
- L100 `test_empty_effort_omits_top_level(self, deepseek_profile)` (method)
- L108 `TestDeepSeekModelGating` (class) — V4 family + ``deepseek-reasoner`` get thinking; V3 stays untouched.
- L121 `test_thinking_capable_models_emit_thinking(self, deepseek_profile, model)` (method)
- L138 `test_non_thinking_models_emit_nothing(self, deepseek_profile, model)` (method)
- L146 `TestDeepSeekFullKwargsIntegration` (class) — End-to-end: the transport's full kwargs match DeepSeek's live wire format.
- L155 `test_full_kwargs_match_live_wire_shape(self, deepseek_profile)` (method)
- L171 `test_v3_chat_full_kwargs_omit_thinking(self, deepseek_profile)` (method)
- L187 `TestDeepSeekAuxModel` (class) — DeepSeek aux model is set on the profile so users stop seeing the
- L198 `test_profile_advertises_deepseek_chat(self, deepseek_profile)` (method)
- L201 `test_consumer_api_returns_deepseek_chat(self)` (method)
- L205 `test_consumer_api_returns_non_empty(self)` (method)
