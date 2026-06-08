---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_config_env_bridge_authority.py

Symbols in `tests/gateway/test_config_env_bridge_authority.py`.

- L24 `_run_gateway_import(hermes_home: Path, initial_env: dict[str, str])` (function) — Import gateway.run in a clean subprocess and return the post-import env.
- L83 `_write_config(home: Path, agent_cfg: dict | None=None, display_cfg: dict | None=None, timezone: str | None=None)` (function)
- L96 `_write_env(home: Path, entries: dict[str, str])` (function)
- L102 `hermes_home(tmp_path: Path)` (function)
- L108 `test_config_max_turns_wins_over_stale_env(hermes_home: Path)` (function) — Regression: config.yaml:agent.max_turns=500 must beat .env=60.
- L121 `test_config_gateway_timeout_wins_over_stale_env(hermes_home: Path)` (function) — Every agent.* bridge key must be config-authoritative, not .env-authoritative.
- L138 `test_config_display_busy_input_mode_wins_over_stale_env(hermes_home: Path)` (function)
- L147 `test_config_display_busy_text_mode_wins_over_stale_env(hermes_home: Path)` (function)
- L156 `test_config_timezone_wins_over_stale_env(hermes_home: Path)` (function)
- L165 `test_env_value_survives_when_config_omits_key(hermes_home: Path)` (function) — If config.yaml doesn't set max_turns, .env value must still pass through.
