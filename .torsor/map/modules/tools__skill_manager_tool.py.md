---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skill_manager_tool.py

Symbols in `tools/skill_manager_tool.py`.

- L59 `_guard_agent_created_enabled()` (function) — Read skills.guard_agent_created from config (default False).
- L78 `_security_scan_skill(skill_dir: Path)` (function) — Scan a skill directory after write. Returns error string if blocked, else None.
- L115 `_containing_skills_root(skill_path: Path)` (function) — Return the skills root directory (local or external_dirs entry) that
- L137 `_pinned_guard(name: str)` (function) — Return a refusal message if *name* is pinned, else None.
- L178 `_validate_name(name: str)` (function) — Validate a skill name. Returns error message or None if valid.
- L192 `_validate_category(category: Optional[str])` (function) — Validate an optional category name used as a single directory segment.
- L217 `_validate_frontmatter(content: str)` (function) — Validate that SKILL.md content has proper frontmatter with required fields.
- L256 `_validate_content_size(content: str, label: str='SKILL.md')` (function) — Check that content doesn't exceed the character limit for agent writes.
- L271 `_resolve_skill_dir(name: str, category: str=None)` (function) — Build the directory path for a new skill, optionally under a category.
- L278 `_find_skill(name: str)` (function) — Find a skill by name across all skill directories.
- L298 `_find_skill_in_other_profiles(name: str)` (function) — Look for ``name`` under SKILL.md across OTHER Hermes profiles.
- L364 `_skill_not_found_error(name: str, suffix: str='')` (function) — Build a "skill not found" error that names other profiles holding
- L401 `_validate_file_path(file_path: str)` (function) — Validate a file path for write_file/remove_file.
- L438 `_resolve_skill_target(skill_dir: Path, file_path: str)` (function) — Resolve a supporting-file path and ensure it stays within the skill directory.
- L449 `_atomic_write_text(file_path: Path, content: str, encoding: str='utf-8')` (function) — Atomically write text content to a file.
- L485 `_create_skill(name: str, content: str, category: str=None)` (function) — Create a new user skill with SKILL.md content.
- L542 `_edit_skill(name: str, content: str)` (function) — Replace the SKILL.md of any existing skill (full rewrite).
- L575 `_patch_skill(name: str, old_string: str, new_string: str, file_path: str=None, replace_all: bool=False)` (function) — Targeted find-and-replace within a skill file.
- L669 `_delete_skill(name: str, absorbed_into: Optional[str]=None)` (function) — Delete a skill.
- L726 `_write_file(name: str, file_path: str, file_content: str)` (function) — Add or overwrite a supporting file within any skill directory.
- L778 `_remove_file(name: str, file_path: str)` (function) — Remove a supporting file from any skill directory.
- L825 `skill_manage(action: str, name: str, content: str=None, category: str=None, file_path: str=None, file_content: str=None, old_string: str=None, new_string: str=None, replace_all: bool=False, absorbed_into: str=None)` (function) — Manage user-created skills. Dispatches to the appropriate action handler.
