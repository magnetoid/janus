---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/onboarding.py

Symbols in `agent/onboarding.py`.

- L36 `busy_input_hint_gateway(mode: str)` (function) — Hint shown the first time a user messages while the agent is busy.
- L63 `busy_input_hint_cli(mode: str)` (function) — CLI version of the busy-input hint (plain text, no markdown).
- L84 `tool_progress_hint_gateway()` (function)
- L92 `tool_progress_hint_cli()` (function)
- L99 `openclaw_residue_hint_cli()` (function) — Banner shown the first time Hermes starts and finds ``~/.openclaw/``.
- L118 `detect_openclaw_residue(home: Optional[Path]=None)` (function) — Return True if an OpenClaw workspace directory is present in ``$HOME``.
- L134 `profile_build_mode(config: Mapping[str, Any])` (function) — Resolve the onboarding profile-build mode from config.
- L157 `profile_build_directive()` (function) — System-note directive appended to the very first message ever.
- L190 `_get_seen_dict(config: Mapping[str, Any])` (function)
- L198 `is_seen(config: Mapping[str, Any], flag: str)` (function) — Return True if the user has already been shown this first-touch hint.
- L203 `mark_seen(config_path: Path, flag: str)` (function) — Persist ``onboarding.seen.<flag> = True`` to ``config_path``.
