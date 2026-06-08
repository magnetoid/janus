---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/prompt_builder.py

Symbols in `agent/prompt_builder.py`.

- L45 `_scan_context_content(content: str, filename: str)` (function) — Scan context file content for injection. Returns sanitized content.
- L64 `_find_git_root(start: Path)` (function) — Walk *start* and its parents looking for a ``.git`` directory.
- L80 `_find_hermes_md(cwd: Path)` (function) — Discover the nearest ``.hermes.md`` or ``HERMES.md``.
- L101 `_strip_yaml_frontmatter(content: str)` (function) — Remove optional YAML frontmatter (``---`` delimited) from *content*.
- L456 `format_steer_marker(steer_text: str)` (function) — Wrap a mid-turn steer for appending to a tool result (see module note).
- L724 `_probe_remote_backend(env_type: str)` (function) — Run a tiny introspection command inside the active terminal backend.
- L800 `_clear_backend_probe_cache()` (function) — Test helper — drop the backend probe cache so monkeypatched backends take effect.
- L805 `build_environment_hints()` (function) — Return environment-specific guidance for the system prompt.
- L929 `_skills_prompt_snapshot_path()` (function)
- L933 `clear_skills_system_prompt_cache(*, clear_snapshot: bool=False)` (function) — Drop the in-process skills prompt cache (and optionally the disk snapshot).
- L944 `_build_skills_manifest(skills_dir: Path)` (function) — Build an mtime/size manifest of all SKILL.md and DESCRIPTION.md files.
- L957 `_load_skills_snapshot(skills_dir: Path)` (function) — Load the disk snapshot if it exists and its manifest still matches.
- L975 `_write_skills_snapshot(skills_dir: Path, manifest: dict[str, list[int]], skill_entries: list[dict], category_descriptions: dict[str, str])` (function) — Persist skill metadata to disk for fast cold-start reuse.
- L994 `_build_snapshot_entry(skill_file: Path, skills_dir: Path, frontmatter: dict, description: str)` (function) — Build a serialisable metadata dict for one skill.
- L1028 `_parse_skill_file(skill_file: Path)` (function) — Read a SKILL.md once and return platform compatibility, frontmatter, and description.
- L1054 `_skill_should_show(conditions: dict, available_tools: 'set[str] | None', available_toolsets: 'set[str] | None')` (function) — Return False if the skill's conditional activation rules exclude it.
- L1085 `build_skills_system_prompt(available_tools: 'set[str] | None'=None, available_toolsets: 'set[str] | None'=None)` (function) — Build a compact skill index for the system prompt.
- L1319 `build_nous_subscription_prompt(valid_tool_names: 'set[str] | None'=None)` (function) — Build a compact Nous subscription capability block for the system prompt.
- L1389 `_truncate_content(content: str, filename: str, max_chars: int=CONTEXT_FILE_MAX_CHARS)` (function) — Head/tail truncation with a marker in the middle.
- L1401 `load_soul_md()` (function) — Load SOUL.md from HERMES_HOME and return its content, or None.
- L1429 `_load_hermes_md(cwd_path: Path)` (function) — .hermes.md / HERMES.md — walk to git root.
- L1452 `_load_agents_md(cwd_path: Path)` (function) — AGENTS.md — top-level only (no recursive walk).
- L1468 `_load_claude_md(cwd_path: Path)` (function) — CLAUDE.md / claude.md — cwd only.
- L1484 `_load_cursorrules(cwd_path: Path)` (function) — .cursorrules + .cursor/rules/*.mdc — cwd only.
- L1514 `build_context_files_prompt(cwd: Optional[str]=None, skip_soul: bool=False)` (function) — Discover and load context files for the system prompt.
