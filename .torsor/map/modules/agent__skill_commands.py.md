---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/skill_commands.py

Symbols in `agent/skill_commands.py`.

- L30 `_resolve_skill_commands_platform()` (function) — Return the current platform scope used for disabled-skill filtering.
- L53 `_load_skill_payload(skill_identifier: str, task_id: str | None=None)` (function) — Load a skill by name/path and return (loaded_payload, skill_dir, display_name).
- L121 `_inject_skill_config(loaded_skill: dict[str, Any], parts: list[str])` (function) — Resolve and inject skill-declared config values into the message parts.
- L160 `_build_skill_message(loaded_skill: dict[str, Any], skill_dir: Path | None, activation_note: str, user_instruction: str='', runtime_note: str='', session_id: str | None=None)` (function) — Format a loaded skill into a user/system message payload.
- L263 `scan_skill_commands()` (function) — Scan ~/.hermes/skills/ and return a mapping of /command -> skill info.
- L333 `get_skill_commands()` (function) — Return the current skill commands mapping (scan first if empty).
- L348 `reload_skills()` (function) — Re-scan the skills directory and return a diff of what changed.
- L413 `resolve_skill_command_key(command: str)` (function) — Resolve a user-typed /command to its canonical skill_cmds key.
- L432 `build_skill_invocation_message(cmd_key: str, user_instruction: str='', task_id: str | None=None, runtime_note: str='')` (function) — Build the user message content for a skill slash command invocation.
- L479 `build_preloaded_skills_prompt(skill_identifiers: list[str], task_id: str | None=None)` (function) — Load one or more skills for session-wide CLI preloading.
