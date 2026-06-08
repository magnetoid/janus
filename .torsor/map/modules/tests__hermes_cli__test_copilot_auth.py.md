---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_copilot_auth.py

Symbols in `tests/hermes_cli/test_copilot_auth.py`.

- L7 `TestTokenValidation` (class) — Token type validation.
- L10 `test_classic_pat_rejected(self)` (method)
- L17 `test_oauth_token_accepted(self)` (method)
- L22 `test_fine_grained_pat_accepted(self)` (method)
- L27 `test_github_app_token_accepted(self)` (method)
- L32 `test_empty_token_rejected(self)` (method)
- L39 `TestResolveToken` (class) — Token resolution with env var priority.
- L42 `test_copilot_github_token_first_priority(self, monkeypatch)` (method)
- L51 `test_gh_token_second_priority(self, monkeypatch)` (method)
- L60 `test_github_token_third_priority(self, monkeypatch)` (method)
- L69 `test_classic_pat_in_env_skipped(self, monkeypatch)` (method) — Classic PATs in env vars should be skipped, not returned.
- L80 `test_gh_cli_fallback(self, monkeypatch)` (method)
- L90 `test_gh_cli_classic_pat_raises(self, monkeypatch)` (method)
- L99 `test_no_token_returns_empty(self, monkeypatch)` (method)
- L110 `TestRequestHeaders` (class) — Copilot API header generation.
- L113 `test_default_headers_include_openai_intent(self)` (method)
- L120 `test_agent_turn_sets_initiator(self)` (method)
- L125 `test_user_turn_sets_initiator(self)` (method)
- L130 `test_vision_header(self)` (method)
- L135 `test_no_vision_header_by_default(self)` (method)
- L141 `TestCopilotDefaultHeaders` (class) — The models.py copilot_default_headers uses copilot_auth.
- L144 `test_includes_openai_intent(self)` (method)
- L150 `test_includes_x_initiator(self)` (method)
- L156 `TestApiModeSelection` (class) — API mode selection matching opencode's shouldUseCopilotResponsesApi.
- L159 `test_gpt5_uses_responses(self)` (method)
- L168 `test_gpt5_mini_excluded(self)` (method)
- L172 `test_gpt4_uses_chat(self)` (method)
- L178 `test_non_gpt_uses_chat(self)` (method)
- L186 `TestEnvVarOrder` (class) — PROVIDER_REGISTRY has correct env var order.
- L189 `test_copilot_env_vars_include_copilot_github_token(self)` (method)
- L196 `test_copilot_env_vars_order_matches_docs(self)` (method)
