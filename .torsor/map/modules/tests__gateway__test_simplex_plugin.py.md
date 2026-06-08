---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_simplex_plugin.py

Symbols in `tests/gateway/test_simplex_plugin.py`.

- L37 `test_platform_enum_resolves_via_plugin_scan()` (function) — The plugin filesystem scan should expose Platform("simplex").
- L50 `test_check_requirements_needs_url(monkeypatch)` (function)
- L55 `test_check_requirements_true_when_configured(monkeypatch)` (function)
- L67 `test_validate_config_uses_env_or_extra()` (function)
- L77 `test_is_connected_mirrors_validate(monkeypatch)` (function)
- L89 `test_env_enablement_none_when_unset(monkeypatch)` (function)
- L94 `test_env_enablement_seeds_ws_url(monkeypatch)` (function)
- L101 `test_env_enablement_seeds_home_channel(monkeypatch)` (function)
- L109 `test_env_enablement_home_channel_defaults_name_to_id(monkeypatch)` (function)
- L121 `test_adapter_init_custom_url()` (function)
- L130 `test_adapter_init_default_url()` (function)
- L137 `test_adapter_platform_identity()` (function) — Adapter should expose Platform("simplex") identity.
- L149 `test_guess_extension_png()` (function)
- L153 `test_guess_extension_jpg()` (function)
- L157 `test_guess_extension_ogg()` (function)
- L161 `test_guess_extension_unknown()` (function)
- L165 `test_is_image_ext()` (function)
- L171 `test_is_audio_ext()` (function)
- L181 `test_corr_id_starts_with_prefix_and_tracks_pending()` (function)
- L190 `test_corr_id_pending_set_self_trims()` (function)
- L207 `test_send_dm()` (function)
- L224 `test_send_group()` (function)
- L239 `test_send_when_ws_not_connected_does_not_crash()` (function)
- L253 `test_handle_event_filters_own_corr_id()` (function)
- L272 `test_standalone_send_missing_websockets(monkeypatch)` (function) — When websockets is unimportable, return a clean error dict.
- L305 `test_standalone_send_defaults_to_local_daemon(monkeypatch)` (function)
- L337 `test_health_monitor_does_not_reconnect_quiet_healthy_ws(monkeypatch)` (function)
- L360 `test_register_calls_register_platform()` (function)
