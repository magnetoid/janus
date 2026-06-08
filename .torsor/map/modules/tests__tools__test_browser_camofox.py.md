---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_camofox.py

Symbols in `tests/tools/test_browser_camofox.py`.

- L30 `TestCamofoxMode` (class)
- L31 `test_disabled_by_default(self, monkeypatch)` (method)
- L35 `test_enabled_when_url_set(self, monkeypatch)` (method)
- L39 `test_cdp_override_takes_priority(self, monkeypatch)` (method) — When BROWSER_CDP_URL is set (via /browser connect), CDP takes priority over Camofox.
- L45 `test_cdp_override_blank_does_not_disable_camofox(self, monkeypatch)` (method) — Empty/whitespace BROWSER_CDP_URL should not suppress Camofox.
- L51 `test_health_check_unreachable(self, monkeypatch)` (method)
- L61 `_config_with_camofox(**camofox_config)` (function)
- L65 `_mock_response(status=200, json_data=None)` (function)
- L79 `TestCamofoxLoopbackRewrite` (class)
- L81 `test_rewrites_localhost_when_enabled(self, mock_config, monkeypatch)` (method)
- L97 `test_rewrite_is_opt_in(self, mock_config, monkeypatch)` (method)
- L107 `test_preserves_public_urls_when_enabled(self, mock_config, monkeypatch)` (method)
- L117 `test_env_alias_takes_precedence(self, mock_config, monkeypatch)` (method)
- L133 `TestCamofoxNavigate` (class)
- L135 `test_creates_tab_on_first_navigate(self, mock_post, monkeypatch)` (method)
- L145 `test_navigate_uses_rewritten_loopback_url(self, mock_post, mock_config, monkeypatch)` (method)
- L162 `test_navigates_existing_tab(self, mock_post, monkeypatch)` (method)
- L174 `test_connection_error_returns_helpful_message(self, monkeypatch)` (method)
- L186 `TestCamofoxSnapshot` (class)
- L187 `test_no_session_returns_error(self, monkeypatch)` (method)
- L195 `test_returns_snapshot(self, mock_get, mock_post, monkeypatch)` (method)
- L217 `TestCamofoxInteractions` (class)
- L219 `test_click(self, mock_post, monkeypatch)` (method)
- L230 `test_type(self, mock_post, monkeypatch)` (method)
- L241 `test_scroll(self, mock_post, monkeypatch)` (method)
- L252 `test_back(self, mock_post, monkeypatch)` (method)
- L262 `test_press(self, mock_post, monkeypatch)` (method)
- L278 `TestCamofoxClose` (class)
- L281 `test_close_session(self, mock_post, mock_delete, monkeypatch)` (method)
- L291 `test_close_nonexistent_session(self, monkeypatch)` (method)
- L302 `TestCamofoxConsole` (class)
- L303 `test_console_returns_empty_with_note(self, monkeypatch)` (method)
- L316 `TestCamofoxGetImages` (class)
- L319 `test_get_images(self, mock_get, mock_post, monkeypatch)` (method)
- L338 `TestCamofoxVisionConfig` (class)
- L342 `test_camofox_vision_uses_configured_temperature_and_timeout(self, mock_get_raw, mock_get, mock_post, monkeypatch)` (method)
- L374 `test_camofox_vision_defaults_temperature_when_config_omits_it(self, mock_get_raw, mock_get, mock_post, monkeypatch)` (method)
- L409 `TestBrowserToolRouting` (class) — Verify that browser_tool.py delegates to camofox when CAMOFOX_URL is set.
- L413 `test_browser_navigate_routes_to_camofox(self, mock_post, monkeypatch)` (method)
- L423 `test_check_requirements_passes_with_camofox(self, monkeypatch)` (method)
