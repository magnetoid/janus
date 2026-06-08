---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skills_tool.py

Symbols in `tools/skills_tool.py`.

- L111 `_skill_lookup_path_error(name: str)` (function) — Return an error if a local skill lookup *name* can escape search roots.
- L138 `load_env()` (function) — Load profile-scoped environment variables from HERMES_HOME/.env.
- L154 `SkillReadinessStatus` (class)
- L174 `set_secret_capture_callback(callback)` (function)
- L179 `skill_matches_platform(frontmatter: Dict[str, Any])` (function) — Check if a skill is compatible with the current OS platform.
- L189 `skill_matches_environment(frontmatter: Dict[str, Any])` (function) — Check if a skill is relevant to the current runtime environment.
- L201 `_normalize_prerequisite_values(value: Any)` (function)
- L209 `_collect_prerequisite_values(frontmatter: Dict[str, Any])` (function)
- L221 `_normalize_setup_metadata(frontmatter: Dict[str, Any])` (function)
- L266 `_get_required_environment_variables(frontmatter: Dict[str, Any], legacy_env_vars: List[str] | None=None)` (function)
- L335 `_capture_required_environment_variables(skill_name: str, missing_entries: List[Dict[str, Any]])` (function)
- L413 `_is_gateway_surface()` (function)
- L420 `_get_terminal_backend_name()` (function)
- L424 `_is_env_var_persisted(var_name: str, env_snapshot: Dict[str, str] | None=None)` (function)
- L434 `_remaining_required_environment_names(required_env_vars: List[Dict[str, Any]], capture_result: Dict[str, Any], *, env_snapshot: Dict[str, str] | None=None)` (function)
- L454 `_gateway_setup_hint()` (function)
- L463 `_build_setup_note(readiness_status: SkillReadinessStatus, missing: List[str], setup_help: str | None=None)` (function)
- L477 `check_skills_requirements()` (function) — Skills are always available -- the directory is created on first use if needed.
- L482 `_parse_frontmatter(content: str)` (function) — Parse YAML frontmatter from markdown content.
- L492 `_get_category_from_path(skill_path: Path)` (function) — Extract category from skill path based on directory structure.
- L518 `_parse_tags(tags_value)` (function) — Parse tags from frontmatter value.
- L549 `_get_disabled_skill_names()` (function) — Load disabled skill names from config.
- L559 `_get_session_platform()` (function) — Resolve the current platform from gateway session context.
- L573 `_is_skill_disabled(name: str, platform: str=None)` (function) — Check if a skill is disabled in config.
- L595 `_find_all_skills(*, skip_disabled: bool=False)` (function) — Recursively find all skills in ~/.hermes/skills/ and external dirs.
- L675 `_sort_skills(skills: List[Dict[str, Any]])` (function) — Keep every skill listing path ordered the same way.
- L680 `skills_list(category: str=None, task_id: str=None)` (function) — List all available skills (progressive disclosure tier 1 - minimal metadata).
- L751 `_serve_plugin_skill(skill_md: Path, namespace: str, bare: str, *, preprocess: bool=True, session_id: str | None=None)` (function) — Read a plugin-provided skill, apply guards, return JSON.
- L855 `skill_view(name: str, file_path: str=None, task_id: str=None, preprocess: bool=True)` (function) — View the content of a skill or a specific file within a skill directory.
- L1569 `_skill_view_with_bump(args, **kw)` (function) — Invoke skill_view, then bump view_count on success. Best-effort: a
