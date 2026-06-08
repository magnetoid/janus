---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_verbose_command.py

Symbols in `tests/gateway/test_verbose_command.py`.

- L14 `_make_event(text='/verbose', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L25 `_make_runner()` (function) — Create a bare GatewayRunner without calling __init__.
- L44 `TestVerboseCommand` (class) — Tests for _handle_verbose_command in the gateway.
- L48 `test_disabled_by_default(self, tmp_path, monkeypatch)` (method) — When tool_progress_command is false, /verbose returns an info message.
- L64 `test_enabled_cycles_mode(self, tmp_path, monkeypatch)` (method) — When enabled, /verbose cycles tool_progress mode per-platform.
- L88 `test_quoted_false_keeps_command_disabled(self, tmp_path, monkeypatch)` (method) — Quoted false must not enable the /verbose gateway command.
- L107 `test_cycles_through_all_modes(self, tmp_path, monkeypatch)` (method) — Calling /verbose repeatedly cycles through all four modes.
- L130 `test_defaults_to_platform_default_when_no_tool_progress_set(self, tmp_path, monkeypatch)` (method) — When tool_progress is not in config, starts from platform default then cycles.
- L157 `test_per_platform_isolation(self, tmp_path, monkeypatch)` (method) — Cycling /verbose on Telegram doesn't change Slack's setting.
- L193 `test_no_config_file_returns_disabled(self, tmp_path, monkeypatch)` (method) — When config.yaml doesn't exist, command reports disabled.
- L205 `test_verbose_is_in_gateway_known_commands(self)` (method) — The /verbose command is recognized by the gateway dispatch.
