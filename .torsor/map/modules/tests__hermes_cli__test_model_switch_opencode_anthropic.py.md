---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_switch_opencode_anthropic.py

Symbols in `tests/hermes_cli/test_model_switch_opencode_anthropic.py`.

- L33 `_run_opencode_switch(raw_input: str, current_provider: str, current_model: str, current_base_url: str, explicit_provider: str='', runtime_base_url: str='')` (function) — Run switch_model with OpenCode mocks and return the result.
- L77 `TestOpenCodeGoV1Strip` (class) — OpenCode Go: ``/model minimax-*`` must strip /v1.
- L80 `test_switch_to_minimax_m27_strips_v1(self)` (method) — GLM-5 → MiniMax-M2.7: base_url loses trailing /v1.
- L95 `test_switch_to_minimax_m25_strips_v1(self)` (method) — Same behavior for M2.5.
- L108 `test_switch_to_glm_leaves_v1_intact(self)` (method) — OpenAI-compatible models (GLM, Kimi, MiMo) keep /v1.
- L124 `test_switch_to_kimi_leaves_v1_intact(self)` (method)
- L136 `test_trailing_slash_also_stripped(self)` (method) — ``/v1/`` with trailing slash is also stripped cleanly.
- L150 `TestOpenCodeZenV1Strip` (class) — OpenCode Zen: ``/model claude-*`` must strip /v1.
- L153 `test_switch_to_claude_sonnet_strips_v1(self)` (method) — Gemini → Claude on opencode-zen: /v1 stripped.
- L166 `test_switch_to_gemini_leaves_v1_intact(self)` (method) — Gemini on opencode-zen stays on chat_completions with /v1.
- L180 `test_switch_to_gpt_uses_codex_responses_keeps_v1(self)` (method) — GPT on opencode-zen uses codex_responses api_mode — /v1 kept.
- L195 `TestAgentSwitchModelDefenseInDepth` (class) — run_agent.AIAgent.switch_model() also strips /v1 as defense-in-depth.
- L198 `test_agent_switch_model_strips_v1_for_anthropic_messages(self)` (method) — Even if a caller hands in a /v1 URL, the agent strips it.
- L256 `TestStaleConfigDefaultDoesNotWedgeResolver` (class) — Regression for the real bug Quentin hit.
- L273 `test_kimi_switch_keeps_v1_despite_claude_config_default(self, tmp_path, monkeypatch)` (method)
- L309 `test_go_glm_switch_keeps_v1_despite_minimax_config_default(self, tmp_path, monkeypatch)` (method)
- L341 `test_claude_switch_still_strips_v1_with_kimi_config_default(self, tmp_path, monkeypatch)` (method) — Inverse case: config default is chat_completions, switch TO anthropic_messages.
