---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tui_gateway/test_make_agent_provider.py

Symbols in `tests/tui_gateway/test_make_agent_provider.py`.

- L12 `test_make_agent_passes_resolved_provider()` (function) — _make_agent forwards provider/base_url/api_key/api_mode from
- L63 `test_make_agent_ignores_display_personality_without_system_prompt()` (function) — The TUI matches the classic CLI: personality only becomes active once
- L101 `test_make_agent_honors_tui_launch_env_flags()` (function)
- L143 `test_probe_config_health_flags_null_sections()` (function) — Bare YAML keys (`agent:` with no value) parse as None and silently
- L156 `test_probe_config_health_flags_null_personalities_with_active_personality()` (function)
- L170 `test_make_agent_tolerates_null_config_sections()` (function) — Bare `agent:` / `display:` keys in ~/.hermes/config.yaml parse as
- L204 `test_make_agent_tolerates_null_personalities_with_active_personality()` (function)
- L238 `test_make_agent_honors_per_session_model_override()` (function) — Regression for cross-session model contamination: a per-session
- L308 `test_apply_model_switch_does_not_leak_process_env()` (function) — Core fix for cross-session contamination: an in-session /model switch
