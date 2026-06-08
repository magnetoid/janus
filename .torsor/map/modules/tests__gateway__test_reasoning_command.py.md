---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_reasoning_command.py

Symbols in `tests/gateway/test_reasoning_command.py`.

- L18 `_make_event(text='/reasoning', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L29 `_make_runner()` (function) — Create a bare GatewayRunner without calling __init__.
- L49 `_CapturingAgent` (class) — Fake agent that records init kwargs for assertions.
- L54 `__init__(self, *args, **kwargs)` (method)
- L58 `run_conversation(self, user_message: str, conversation_history=None, task_id=None)` (method)
- L66 `TestReasoningCommand` (class)
- L68 `test_reasoning_in_help_output(self)` (method)
- L76 `test_reasoning_is_known_command(self)` (method)
- L80 `test_parse_reasoning_command_args_accepts_ascii_and_smart_global_flags(self)` (method)
- L85 `test_reasoning_command_reloads_current_state_from_config(self, tmp_path, monkeypatch)` (method)
- L108 `test_handle_reasoning_command_updates_config_and_cache(self, tmp_path, monkeypatch)` (method)
- L127 `test_handle_reasoning_command_defaults_to_session_only(self, tmp_path, monkeypatch)` (method)
- L148 `test_reasoning_global_clears_existing_session_override(self, tmp_path, monkeypatch)` (method)
- L169 `test_reasoning_reset_clears_session_override_without_config_write(self, tmp_path, monkeypatch)` (method)
- L189 `test_resolve_session_reasoning_prefers_session_override(self, tmp_path, monkeypatch)` (method)
- L203 `test_run_agent_reloads_reasoning_config_per_message(self, tmp_path, monkeypatch)` (method)
- L252 `test_run_agent_prefers_session_reasoning_override(self, tmp_path, monkeypatch)` (method)
- L302 `test_run_agent_includes_enabled_mcp_servers_in_gateway_toolsets(self, tmp_path, monkeypatch)` (method)
- L363 `test_run_agent_homeassistant_uses_default_platform_toolset(self, tmp_path, monkeypatch)` (method)
- L412 `TestLoadShowReasoningCoercion` (class) — Regression: display.show_reasoning must be coerced, not bool()'d.
- L415 `_load_with_config(self, tmp_path, monkeypatch, yaml_body: str)` (method)
- L422 `test_quoted_false_is_false(self, tmp_path, monkeypatch)` (method)
- L428 `test_quoted_off_is_false(self, tmp_path, monkeypatch)` (method)
- L434 `test_quoted_true_is_true(self, tmp_path, monkeypatch)` (method)
- L440 `test_bare_true_is_true(self, tmp_path, monkeypatch)` (method)
- L446 `test_missing_is_false(self, tmp_path, monkeypatch)` (method)
