---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_provider_resolution.py

Symbols in `tests/cli/test_cli_provider_resolution.py`.

- L20 `_reset_modules(prefixes: tuple[str, ...])` (function)
- L27 `_restore_cli_and_tool_modules()` (function) — Save and restore tools/cli/run_agent modules around every test.
- L42 `_install_prompt_toolkit_stubs()` (function)
- L111 `_import_cli()` (function)
- L126 `test_hermes_cli_init_does_not_eagerly_resolve_runtime_provider(monkeypatch)` (function)
- L143 `test_runtime_resolution_failure_is_not_sticky(monkeypatch)` (function)
- L175 `test_runtime_resolution_rebuilds_agent_on_routing_change(monkeypatch)` (function)
- L203 `test_cli_turn_routing_uses_primary_when_disabled(monkeypatch)` (function)
- L217 `test_cli_prefers_config_provider_over_stale_env_override(monkeypatch)` (function)
- L233 `test_codex_provider_replaces_incompatible_default_model(monkeypatch)` (function) — When provider resolves to openai-codex and no model was explicitly
- L273 `test_model_flow_nous_prints_subscription_guidance_without_mutating_explicit_tts(monkeypatch, capsys)` (function)
- L311 `test_model_flow_nous_offers_tool_gateway_prompt_when_unconfigured(monkeypatch, capsys)` (function)
- L364 `test_codex_provider_uses_config_model(monkeypatch)` (function) — Model comes from config.yaml, not LLM_MODEL env var.
- L407 `test_codex_config_model_not_replaced_by_normalization(monkeypatch)` (function) — When the user sets model.default in config.yaml to a specific codex
- L450 `test_codex_provider_preserves_explicit_codex_model(monkeypatch)` (function) — If the user explicitly passes a Codex-compatible model, it must be
- L477 `test_codex_provider_strips_provider_prefix_from_model(monkeypatch)` (function) — openai/gpt-5.3-codex should become gpt-5.3-codex — the Codex
- L503 `test_cmd_model_falls_back_to_auto_on_invalid_provider(monkeypatch, capsys)` (function)
- L529 `test_model_flow_custom_saves_verified_v1_base_url(monkeypatch, capsys)` (function)
- L572 `test_model_flow_custom_persists_selected_api_mode(monkeypatch)` (function)
- L629 `test_cmd_model_forwards_nous_login_tls_options(monkeypatch)` (function)
- L685 `test_auto_provider_name_localhost()` (function)
- L691 `test_auto_provider_name_runpod()` (function)
- L696 `test_auto_provider_name_remote()` (function)
- L702 `test_save_custom_provider_uses_provided_name(monkeypatch, tmp_path)` (function) — When a display name is passed, it should appear in the saved entry.
