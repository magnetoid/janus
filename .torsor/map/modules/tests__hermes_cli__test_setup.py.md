---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_setup.py

Symbols in `tests/hermes_cli/test_setup.py`.

- L11 `_maybe_keep_current_tts(question, choices)` (function)
- L18 `_clear_provider_env(monkeypatch)` (function)
- L29 `_stub_tts(monkeypatch)` (function) — Stub out TTS prompts so setup_model_provider doesn't block.
- L38 `_write_model_config(tmp_path, provider, base_url='', model_name='test-model')` (function) — Simulate what a _model_flow_* function writes to disk.
- L53 `test_setup_delegates_to_select_provider_and_model(tmp_path, monkeypatch)` (function) — setup_model_provider calls select_provider_and_model and syncs config.
- L76 `test_setup_syncs_openrouter_from_disk(tmp_path, monkeypatch)` (function) — When select_provider_and_model saves OpenRouter config to disk,
- L99 `test_setup_syncs_nous_from_disk(tmp_path, monkeypatch)` (function) — Nous OAuth writes config to disk; wizard config dict must pick it up.
- L121 `test_setup_custom_providers_synced(tmp_path, monkeypatch)` (function) — custom_providers written by select_provider_and_model must survive.
- L144 `test_setup_gateway_skips_service_install_when_systemctl_missing(monkeypatch, capsys)` (function)
- L182 `test_setup_gateway_in_container_shows_docker_guidance(monkeypatch, capsys)` (function) — setup_gateway() in a Docker container shows Docker-specific restart instructions.
- L225 `test_setup_syncs_custom_provider_removal_from_disk(tmp_path, monkeypatch)` (function) — Removing the last custom provider in model setup should persist.
- L250 `test_setup_cancel_preserves_existing_config(tmp_path, monkeypatch)` (function) — When the user cancels provider selection, existing config is preserved.
- L276 `test_setup_exception_in_select_gracefully_handled(tmp_path, monkeypatch)` (function) — If select_provider_and_model raises, setup continues with existing config.
- L293 `test_setup_keyboard_interrupt_gracefully_handled(tmp_path, monkeypatch)` (function) — KeyboardInterrupt during provider selection is handled.
- L309 `test_select_provider_and_model_warns_if_named_custom_provider_disappears(tmp_path, monkeypatch, capsys)` (function) — If a saved custom provider is deleted mid-selection, show a warning instead of silently doing nothing.
- L341 `test_select_provider_and_model_accepts_named_provider_from_providers_section(tmp_path, monkeypatch, capsys)` (function)
- L376 `test_codex_setup_uses_runtime_access_token_for_live_model_list(tmp_path, monkeypatch)` (function) — Codex model list fetching uses the runtime access token.
- L399 `test_modal_setup_can_use_nous_subscription_without_modal_creds(tmp_path, monkeypatch, capsys)` (function)
- L441 `test_modal_setup_persists_direct_mode_when_user_chooses_their_own_account(tmp_path, monkeypatch)` (function)
- L482 `test_setup_slack_saves_home_channel(monkeypatch)` (function) — _setup_slack() saves SLACK_HOME_CHANNEL when the user provides one.
- L498 `test_setup_slack_home_channel_empty_not_saved(monkeypatch)` (function) — _setup_slack() does not save SLACK_HOME_CHANNEL when left blank.
