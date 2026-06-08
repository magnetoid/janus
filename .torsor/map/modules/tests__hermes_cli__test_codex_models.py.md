---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_codex_models.py

Symbols in `tests/hermes_cli/test_codex_models.py`.

- L7 `test_get_codex_model_ids_prioritizes_default_and_cache(tmp_path, monkeypatch)` (function)
- L40 `test_setup_wizard_codex_import_resolves()` (function) — Regression test for #712: setup.py must import the correct function name.
- L48 `test_get_codex_model_ids_falls_back_to_curated_defaults(tmp_path, monkeypatch)` (function)
- L60 `test_get_codex_model_ids_adds_forward_compat_models_from_templates(monkeypatch)` (function)
- L80 `test_fetch_from_api_keeps_supported_in_api_false_models(monkeypatch)` (function) — Regression: gpt-5.3-codex-spark is returned by the live Codex backend
- L116 `test_model_command_uses_runtime_access_token_for_codex_list(monkeypatch)` (function)
- L157 `test_model_command_prompts_to_reuse_or_reauthenticate_codex_session(monkeypatch, capsys)` (function)
- L196 `test_model_command_uses_existing_codex_session_without_relogin(monkeypatch)` (function)
- L237 `_make_cli(model='anthropic/claude-opus-4.6', **kwargs)` (function) — Create a HermesCLI with minimal mocking.
- L262 `TestNormalizeModelForProvider` (class) — _normalize_model_for_provider() trusts user-selected models.
- L271 `test_non_codex_provider_is_noop(self)` (method)
- L277 `test_native_provider_prefix_is_stripped_before_agent_startup(self)` (method)
- L283 `test_bare_codex_model_passes_through(self)` (method)
- L289 `test_bare_non_codex_model_passes_through(self)` (method) — gpt-5.4 (no 'codex' suffix) passes through — user chose it.
- L296 `test_any_bare_model_trusted(self)` (method) — Even a non-OpenAI bare model passes through — user explicitly set it.
- L304 `test_provider_prefix_stripped(self)` (method) — openai/gpt-5.4 → gpt-5.4 (strip prefix, keep model).
- L311 `test_any_provider_prefix_stripped(self)` (method) — anthropic/claude-opus-4.6 → claude-opus-4.6 (strip prefix only).
- L319 `test_opencode_go_prefix_stripped(self)` (method)
- L327 `test_opencode_zen_claude_sets_messages_mode(self)` (method)
- L335 `test_default_model_replaced(self)` (method) — No model configured (empty default) gets swapped for codex.
- L367 `test_default_fallback_when_api_fails(self)` (method) — No model configured falls back to gpt-5.3-codex when API unreachable.
