---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_homeassistant.py

Symbols in `tests/gateway/test_homeassistant.py`.

- L28 `TestCheckRequirements` (class)
- L29 `test_returns_false_without_token(self, monkeypatch)` (method)
- L33 `test_returns_true_with_token(self, monkeypatch)` (method)
- L38 `test_returns_false_without_aiohttp(self, monkeypatch)` (method)
- L48 `TestFormatStateChange` (class)
- L50 `fmt(entity_id, old_state, new_state)` (method)
- L53 `test_climate_includes_temperatures(self)` (method)
- L67 `test_sensor_includes_unit(self)` (method)
- L79 `test_sensor_without_unit(self)` (method)
- L87 `test_binary_sensor_on(self)` (method)
- L96 `test_binary_sensor_off(self)` (method)
- L104 `test_light_turned_on(self)` (method)
- L112 `test_switch_turned_off(self)` (method)
- L120 `test_fan_domain_uses_light_switch_branch(self)` (method)
- L128 `test_alarm_panel(self)` (method)
- L137 `test_generic_domain_includes_entity_id(self)` (method)
- L146 `test_same_state_returns_none(self)` (method)
- L153 `test_empty_new_state_returns_none(self)` (method)
- L156 `test_no_old_state_uses_unknown(self)` (method)
- L165 `test_uses_entity_id_when_no_friendly_name(self)` (method)
- L179 `TestAdapterInit` (class)
- L180 `test_url_and_token_from_config_extra(self, monkeypatch)` (method)
- L193 `test_url_fallback_to_env(self, monkeypatch)` (method)
- L201 `test_trailing_slash_stripped(self)` (method)
- L209 `test_watch_filters_parsed(self)` (method)
- L226 `test_watch_all_parsed(self)` (method)
- L234 `test_defaults_when_no_extra(self, monkeypatch)` (method)
- L253 `_make_adapter(**extra)` (function)
- L260 `_make_event(entity_id, old_state, new_state, old_attrs=None, new_attrs=None)` (function)
- L270 `TestEventFilteringPipeline` (class)
- L272 `test_ignored_entity_not_forwarded(self)` (method)
- L278 `test_unwatched_domain_not_forwarded(self)` (method)
- L284 `test_watched_domain_forwarded(self)` (method)
- L300 `test_watched_entity_forwarded(self)` (method)
- L311 `test_no_filters_blocks_everything(self)` (method) — Without watch_domains, watch_entities, or watch_all, events are dropped.
- L318 `test_watch_all_passes_everything(self)` (method) — With watch_all=True and no specific filters, all events pass through.
- L325 `test_same_state_not_forwarded(self)` (method)
- L331 `test_empty_entity_id_skipped(self)` (method)
- L337 `test_message_event_has_correct_source(self)` (method)
- L354 `TestCooldown` (class)
- L356 `test_cooldown_blocks_rapid_events(self)` (method)
- L371 `test_cooldown_expires(self)` (method)
- L388 `test_different_entities_independent_cooldowns(self)` (method)
- L407 `test_zero_cooldown_passes_all(self)` (method)
- L423 `TestConfigIntegration` (class)
- L424 `test_env_override_creates_ha_platform(self, monkeypatch)` (method)
- L440 `test_no_env_no_platform(self, monkeypatch)` (method)
- L449 `test_config_roundtrip_preserves_extra(self)` (method)
- L477 `TestSendViaRestApi` (class) — send() uses REST API (not WebSocket) to avoid race conditions.
- L481 `_mock_aiohttp_session(response_status=200, response_text='OK')` (method) — Build a mock aiohttp session + response for async-with patterns.
- L503 `test_send_success(self)` (method)
- L522 `test_send_http_error(self)` (method)
- L536 `test_send_truncates_long_message(self)` (method)
- L551 `test_send_does_not_use_websocket(self)` (method) — send() must use REST API, not the WS connection (race condition fix).
- L578 `TestWsUrlConstruction` (class)
- L579 `test_http_to_ws(self)` (method)
- L585 `test_https_to_wss(self)` (method)
