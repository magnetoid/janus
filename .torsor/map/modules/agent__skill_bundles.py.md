---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/skill_bundles.py

Symbols in `agent/skill_bundles.py`.

- L66 `_bundles_dir()` (function) — Return the canonical bundles directory under HERMES_HOME.
- L78 `_slugify(name: str)` (function)
- L85 `_iter_bundle_files()` (function)
- L95 `_max_mtime(files: List[Path])` (function) — Highest mtime across the bundle files plus the dir itself.
- L116 `_load_bundle_file(path: Path)` (function) — Parse a single bundle YAML file. Returns ``None`` on any error.
- L168 `scan_bundles()` (function) — Scan the bundles directory and rebuild the cache.
- L195 `get_skill_bundles()` (function) — Return the current bundle mapping, rescanning when disk changed.
- L208 `resolve_bundle_command_key(command: str)` (function) — Resolve a user-typed command to its canonical bundle slash key.
- L221 `reload_bundles()` (function) — Re-scan the bundles directory and return a diff.
- L247 `list_bundles()` (function) — Return a sorted list of bundle info dicts for display.
- L253 `build_bundle_invocation_message(cmd_key: str, user_instruction: str='', task_id: str | None=None)` (function) — Build the user message content for a bundle slash command invocation.
- L348 `bundle_path_for(name: str)` (function) — Return the canonical filesystem path for a bundle name.
- L356 `save_bundle(name: str, skills: List[str], description: str='', instruction: str='', overwrite: bool=False)` (function) — Write a bundle to disk and invalidate the cache.
- L394 `delete_bundle(name: str)` (function) — Delete a bundle by name. Returns the deleted path.
- L407 `get_bundle(name: str)` (function) — Look up a bundle by name (slug-normalized).
