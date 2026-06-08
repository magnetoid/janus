---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dump.py

Symbols in `hermes_cli/dump.py`.

- L22 `_get_git_commit(project_root: Path)` (function) — Return short git commit hash, or '(unknown)'.
- L59 `_redact(value: str)` (function) — Redact all but first 4 and last 4 chars.
- L70 `_gateway_status()` (function) — Return a short gateway status string.
- L88 `_count_skills(hermes_home: Path)` (function) — Count installed skills.
- L101 `_count_mcp_servers(config: dict)` (function) — Count configured MCP servers.
- L108 `_cron_summary(hermes_home: Path)` (function) — Return cron jobs summary.
- L123 `_configured_platforms()` (function) — Return list of configured messaging platform names.
- L146 `_memory_provider(config: dict)` (function) — Return the active memory provider name.
- L153 `_get_model_and_provider(config: dict)` (function) — Extract model and provider from config.
- L168 `_config_overrides(config: dict)` (function) — Find non-default config values worth reporting.
- L219 `run_dump(args)` (function) — Output a compact, copy-pasteable setup summary.
