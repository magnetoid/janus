---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/honcho/client.py

Symbols in `plugins/memory/honcho/client.py`.

- L35 `profile_host_key(profile: str | None)` (function) — Return the safe Honcho host key for a Hermes profile.
- L43 `_host_block(raw: dict, host: str)` (function) — Return host config, accepting legacy dot-form profile host keys.
- L53 `resolve_active_host()` (function) — Derive the Honcho host key from the active Hermes profile.
- L74 `resolve_global_config_path()` (function) — Return the shared Honcho config path for the current HOME.
- L79 `resolve_config_path()` (function) — Return the active Honcho config path.
- L105 `_normalize_recall_mode(val: str)` (function) — Normalize legacy recall mode values (e.g. 'auto' → 'hybrid').
- L111 `_resolve_bool(*vals, default: bool)` (function) — Resolve a bool config field: first non-None wins, else default.
- L125 `_parse_context_tokens(host_val, root_val)` (function) — Parse contextTokens: host wins, then root, then None (uncapped).
- L136 `_parse_int_config(host_val, root_val, default: int)` (function) — Parse an integer config: host wins, then root, then default.
- L147 `_parse_string_map(host_obj: dict, root_obj: dict, key: str)` (function) — Parse a string-to-string map with host-level whole-map override.
- L162 `_parse_optional_string(host_obj: dict, root_obj: dict, key: str, default: str='')` (function) — Parse a string field where host-level empty string can override root.
- L175 `_parse_dialectic_depth(host_val, root_val)` (function) — Parse dialecticDepth: host wins, then root, then 1. Clamped to 1-3.
- L189 `_parse_dialectic_depth_levels(host_val, root_val, depth: int)` (function) — Parse dialecticDepthLevels: optional array of reasoning levels per pass.
- L217 `_resolve_optional_float(*values: Any)` (function) — Return the first non-empty value coerced to a positive float.
- L239 `_normalize_observation_mode(val: str)` (function) — Normalize observation mode values.
- L259 `_resolve_observation(mode: str, observation_obj: dict | None)` (function) — Resolve per-peer observation booleans.
- L291 `HonchoClientConfig` (class) — Configuration for Honcho client, resolved for a specific host.
- L382 `from_env(cls, workspace_id: str='hermes', host: str | None=None)` (method) — Create config from environment variables (fallback).
- L404 `from_global_config(cls, host: str | None=None, config_path: Path | None=None)` (method) — Create config from the resolved Honcho config path.
- L622 `_git_repo_name(cwd: str)` (method) — Return the git repo root directory name, or None if not in a repo.
- L646 `_enforce_session_id_limit(cls, sanitized: str, original: str)` (method) — Truncate a sanitized session ID to Honcho's 100-char limit.
- L670 `resolve_session_name(self, cwd: str | None=None, session_title: str | None=None, session_id: str | None=None, gateway_session_key: str | None=None)` (method) — Resolve Honcho session name.
- L743 `get_honcho_client(config: HonchoClientConfig | None=None)` (function) — Get or create the Honcho client singleton.
- L869 `reset_honcho_client()` (function) — Reset the Honcho client singleton (useful for testing).
