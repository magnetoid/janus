---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/skill_utils.py

Symbols in `agent/skill_utils.py`.

- L47 `is_excluded_skill_path(path)` (function) — True if any component of *path* is in EXCLUDED_SKILL_DIRS.
- L70 `yaml_load(content: str)` (function) — Parse YAML with lazy import and CSafeLoader preference.
- L88 `parse_frontmatter(content: str)` (function) — Parse YAML frontmatter from a markdown string.
- L128 `skill_matches_platform(frontmatter: Dict[str, Any])` (function) — Return True when the skill is compatible with the current OS.
- L187 `_detect_environment(env: str)` (function) — Return True when the named runtime environment is currently active.
- L233 `skill_matches_environment(frontmatter: Dict[str, Any])` (function) — Return True when the skill is relevant to the current runtime environment.
- L275 `get_disabled_skill_names(platform: str | None=None)` (function) — Read disabled skill names from config.yaml.
- L317 `_normalize_string_set(values)` (function)
- L336 `_external_dirs_cache_clear()` (function) — Test hook — drop the in-process cache.
- L341 `get_external_skills_dirs()` (function) — Read ``skills.external_dirs`` from config.yaml and return validated paths.
- L427 `get_all_skills_dirs()` (function) — Return all skill directories: local ``~/.hermes/skills/`` first, then external.
- L441 `extract_skill_conditions(frontmatter: Dict[str, Any])` (function) — Extract conditional activation fields from parsed frontmatter.
- L461 `extract_skill_config_vars(frontmatter: Dict[str, Any])` (function) — Extract config variable declarations from parsed frontmatter.
- L520 `discover_all_skill_config_vars()` (function) — Scan all enabled skills and collect their config variable declarations.
- L565 `_resolve_dotpath(config: Dict[str, Any], dotted_key: str)` (function) — Walk a nested dict following a dotted key.  Returns None if any part is missing.
- L577 `resolve_skill_config_values(config_vars: List[Dict[str, Any]])` (function) — Resolve current values for skill config vars from config.yaml.
- L618 `extract_skill_description(frontmatter: Dict[str, Any])` (function) — Extract a truncated description from parsed frontmatter.
- L632 `iter_skill_index_files(skills_dir: Path, filename: str)` (function) — Walk skills_dir yielding sorted paths matching *filename*.
- L652 `parse_qualified_name(name: str)` (function) — Split ``'namespace:skill-name'`` into ``(namespace, bare_name)``.
- L662 `is_valid_namespace(candidate: Optional[str])` (function) — Check whether *candidate* is a valid namespace (``[a-zA-Z0-9_-]+``).
