---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/skill_preprocessing.py

Symbols in `agent/skill_preprocessing.py`.

- L23 `load_skills_config()` (function) — Load the ``skills`` section of config.yaml (best-effort).
- L37 `substitute_template_vars(content: str, skill_dir: Path | None, session_id: str | None)` (function) — Replace ${HERMES_SKILL_DIR} / ${HERMES_SESSION_ID} in skill content.
- L63 `run_inline_shell(command: str, cwd: Path | None, timeout: int)` (function) — Execute a single inline-shell snippet and return its stdout (trimmed).
- L101 `expand_inline_shell(content: str, skill_dir: Path | None, timeout: int)` (function) — Replace every !`cmd` snippet in ``content`` with its stdout.
- L123 `preprocess_skill_content(content: str, skill_dir: Path | None, session_id: str | None=None, skills_cfg: dict | None=None)` (function) — Apply configured SKILL.md template and inline-shell preprocessing.
