---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_teams.py

Symbols in `tests/gateway/test_teams.py`.

- L21 `_ensure_teams_mock()` (function) — Install a teams SDK mock in sys.modules if the real package isn't present.
- L192 `_make_config(**extra)` (function)
- L200 `TestTeamsRequirements` (class)
- L201 `test_returns_false_when_sdk_missing(self, monkeypatch)` (method)
- L205 `test_returns_false_when_aiohttp_missing(self, monkeypatch)` (method)
- L209 `test_returns_true_when_deps_available(self, monkeypatch)` (method)
- L214 `test_alias_matches(self, monkeypatch)` (method)
- L219 `test_validate_config_with_env(self, monkeypatch)` (method)
- L225 `test_validate_config_from_extra(self, monkeypatch)` (method)
- L232 `test_validate_config_missing(self, monkeypatch)` (method)
- L238 `test_validate_config_missing_tenant(self, monkeypatch)` (method)
- L249 `TestTeamsAdapterInit` (class)
- L250 `test_reads_config_from_extra(self)` (method)
- L261 `test_falls_back_to_env_vars(self, monkeypatch)` (method)
- L270 `test_default_port(self)` (method)
- L274 `test_custom_port_from_extra(self)` (method)
- L278 `test_custom_port_from_env(self, monkeypatch)` (method)
- L283 `test_invalid_port_from_extra_falls_back_to_default(self)` (method)
- L289 `test_invalid_port_from_env_falls_back_to_default(self, monkeypatch)` (method)
- L294 `test_platform_value(self)` (method)
- L303 `TestTeamsPluginRegistration` (class)
- L305 `test_register_calls_ctx(self)` (method)
- L310 `test_register_name(self)` (method)
- L316 `test_register_auth_env_vars(self)` (method)
- L323 `test_register_max_message_length(self)` (method)
- L329 `test_register_has_setup_fn(self)` (method)
- L335 `test_register_has_platform_hint(self)` (method)
- L346 `TestTeamsInteractiveSetup` (class)
- L347 `test_interactive_setup_persists_credentials(self, tmp_path, monkeypatch)` (method) — Regression for #19173: interactive_setup must import prompt helpers
- L370 `TestTeamsConnect` (class)
- L372 `test_connect_fails_without_sdk(self, monkeypatch)` (method)
- L381 `test_connect_fails_without_credentials(self)` (method)
- L390 `test_disconnect_cleans_up(self)` (method)
- L410 `TestTeamsSend` (class)
- L412 `test_send_returns_error_without_app(self)` (method)
- L422 `test_send_calls_app_send(self)` (method)
- L438 `test_send_handles_error(self)` (method)
- L451 `test_send_typing(self)` (method)
- L465 `_make_summary_payload()` (function)
- L476 `TestTeamsSummaryWriter` (class)
- L478 `test_incoming_webhook_posts_summary_text(self)` (method)
- L503 `test_graph_delivery_posts_to_channel(self)` (method)
- L529 `test_graph_delivery_falls_back_to_platform_home_channel(self)` (method)
- L548 `test_existing_record_is_reused_without_force_resend(self)` (method)
- L571 `TestTeamsMessageHandling` (class)
- L572 `_make_activity(self, *, text='Hello', from_id='user-123', from_aad_id='aad-456', from_name='Test User', conversation_id='19:abc@thread.v2', conversation_type='personal', tenant_id='tenant-789', activity_id='activity-001', attachments=None)` (method)
- L600 `_make_ctx(self, activity)` (method)
- L606 `test_personal_message_creates_dm_event(self)` (method)
- L622 `test_group_message_creates_group_event(self)` (method)
- L637 `test_channel_message_creates_channel_event(self)` (method)
- L652 `test_user_id_uses_aad_object_id(self)` (method)
- L667 `test_self_message_filtered(self)` (method)
- L681 `test_bot_mention_stripped_from_text(self)` (method)
- L699 `test_deduplication(self)` (method)
- L719 `_FakeAiohttpResponse` (class)
- L720 `__init__(self, status: int, payload, text_body: str='')` (method)
- L725 `json(self)` (method)
- L728 `text(self)` (method)
- L731 `__aenter__(self)` (method)
- L734 `__aexit__(self, exc_type, exc, tb)` (method)
- L738 `_FakeAiohttpSession` (class) — Scripted aiohttp.ClientSession with a queue of responses so tests
- L742 `__init__(self, scripts)` (method)
- L746 `__aenter__(self)` (method)
- L749 `__aexit__(self, exc_type, exc, tb)` (method)
- L752 `post(self, url, **kwargs)` (method)
- L759 `_install_fake_aiohttp(monkeypatch, session)` (function) — Replace ``aiohttp`` in ``sys.modules`` so ``import aiohttp as _aiohttp``
- L769 `TestTeamsStandaloneSend` (class)
- L772 `test_standalone_send_acquires_token_and_posts_activity(self, monkeypatch)` (method)
- L807 `test_standalone_send_returns_error_when_unconfigured(self, monkeypatch)` (method)
- L821 `test_standalone_send_propagates_token_failure(self, monkeypatch)` (method)
- L845 `test_standalone_send_rejects_off_allowlist_service_url(self, monkeypatch)` (method)
- L869 `test_standalone_send_rejects_chat_id_with_path_traversal(self, monkeypatch)` (method)
