---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_lightpanda.py

Symbols in `tests/tools/test_browser_lightpanda.py`.

- L14 `_reset_engine_cache()` (function) — Reset the module-level engine cache so tests start clean.
- L22 `_clean_engine_cache()` (function) — Reset engine cache before and after each test.
- L33 `TestGetBrowserEngine` (class) — Test engine resolution from config and env vars.
- L36 `test_default_is_auto(self)` (method) — With no config or env var, engine defaults to 'auto'.
- L44 `test_config_lightpanda(self)` (method) — Config browser.engine = 'lightpanda' is respected.
- L51 `test_config_chrome(self)` (method) — Config browser.engine = 'chrome' is respected.
- L58 `test_env_var_fallback(self)` (method) — AGENT_BROWSER_ENGINE env var is used when config has no engine key.
- L65 `test_config_takes_priority_over_env(self)` (method) — Config value wins over env var.
- L73 `test_value_is_lowercased(self)` (method) — Engine value is normalized to lowercase.
- L80 `test_invalid_engine_falls_back_to_auto(self)` (method) — Unknown engine values are rejected and fall back to 'auto'.
- L87 `test_caching(self)` (method) — Result is cached — second call doesn't re-read config.
- L101 `TestShouldInjectEngine` (class) — Test whether --engine flag is injected based on mode.
- L104 `test_auto_never_injects(self)` (method)
- L108 `test_lightpanda_injects_in_local_mode(self)` (method)
- L115 `test_chrome_injects_in_local_mode(self)` (method)
- L122 `test_no_inject_in_camofox_mode(self)` (method)
- L127 `test_no_inject_with_cdp_override(self)` (method)
- L133 `test_no_inject_with_cloud_provider(self)` (method)
- L146 `TestNeedsLightpandaFallback` (class) — Test fallback detection for Lightpanda results.
- L149 `test_non_lightpanda_never_falls_back(self)` (method)
- L155 `test_failed_command_triggers_fallback(self)` (method)
- L160 `test_failed_command_reason_is_user_visible(self)` (method)
- L168 `test_empty_snapshot_triggers_fallback(self)` (method)
- L173 `test_short_snapshot_triggers_fallback(self)` (method)
- L178 `test_normal_snapshot_does_not_trigger(self)` (method)
- L185 `test_small_screenshot_triggers_fallback(self, tmp_path)` (method)
- L193 `test_actual_placeholder_size_triggers_fallback(self, tmp_path)` (method)
- L201 `test_normal_screenshot_does_not_trigger(self, tmp_path)` (method)
- L209 `test_successful_open_does_not_trigger(self)` (method)
- L214 `test_close_command_never_triggers_fallback(self)` (method) — Session-management commands like 'close' are not fallback-eligible.
- L220 `test_record_command_never_triggers_fallback(self)` (method) — The 'record' command is tied to the engine daemon — not retryable.
- L226 `test_unknown_command_does_not_trigger_fallback(self)` (method) — Commands not in the whitelist should not trigger fallback.
- L237 `TestConfigIntegration` (class) — Verify engine config is in DEFAULT_CONFIG.
- L240 `test_engine_in_default_config(self)` (method)
- L245 `test_env_var_registered(self)` (method)
- L255 `TestLightpandaRequirements` (class) — Lightpanda should expose browser tools without local Chromium.
- L258 `test_lightpanda_local_mode_does_not_require_chromium(self)` (method)
- L270 `test_chrome_local_mode_still_requires_chromium(self)` (method)
- L287 `TestCleanupResetsEngineCache` (class) — Verify cleanup_all_browsers resets engine-related globals.
- L290 `test_engine_cache_reset(self)` (method)
- L307 `TestLightpandaFallbackWarning` (class) — Verify Chrome fallback results are annotated for users.
- L310 `test_fallback_result_gets_user_visible_warning(self)` (method)
- L330 `test_browser_navigate_surfaces_fallback_warning(self)` (method)
- L357 `test_browser_navigate_surfaces_auto_snapshot_fallback_warning(self)` (method)
- L383 `test_failed_fallback_warning_is_preserved_on_click_error(self)` (method)
- L401 `test_browser_vision_lightpanda_uses_chrome_capture_and_normal_call_llm_shape(self, tmp_path)` (method)
- L441 `test_browser_get_images_preserves_fallback_warning(self)` (method)
- L458 `test_browser_vision_lightpanda_response_has_structured_fallback(self, tmp_path)` (method)
- L495 `TestEngineOverride` (class) — Verify _engine_override bypasses the cached engine.
- L505 `test_override_prevents_engine_injection(self, _camofox, _cdp, _cloud, _chromium, _local, _find, _session)` (method) — When _engine_override='auto', --engine flag is NOT injected.
- L552 `test_no_override_uses_cached_engine(self, _camofox, _cdp, _cloud, _chromium, _local, _find, _session)` (method) — Without _engine_override, the cached engine is used.
- L593 `test_hybrid_local_sidecar_injects_engine_even_with_cloud_provider(self)` (method) — A task::local sidecar is local even when global cloud config exists.
