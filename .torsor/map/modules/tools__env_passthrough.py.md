---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/env_passthrough.py

Symbols in `tools/env_passthrough.py`.

- L34 `_get_allowed()` (function) — Get or create the allowed env vars set for the current context/session.
- L48 `_is_hermes_provider_credential(name: str)` (function) — True if ``name`` is a Hermes-managed provider credential (API key,
- L70 `register_env_passthrough(var_names: Iterable[str])` (function) — Register environment variable names as allowed in sandboxed environments.
- L103 `_load_config_passthrough()` (function) — Load ``tools.env_passthrough`` from config.yaml (cached).
- L143 `is_env_passthrough(var_name: str)` (function) — Check whether *var_name* is allowed to pass through to sandboxes.
- L154 `get_all_passthrough()` (function) — Return the union of skill-registered and config-based passthrough vars.
- L159 `clear_env_passthrough()` (function) — Reset the skill-scoped allowlist (e.g. on session reset).
