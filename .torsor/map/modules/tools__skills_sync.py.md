---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/skills_sync.py

Symbols in `tools/skills_sync.py`.

- L53 `_get_bundled_dir()` (function) — Locate the bundled skills/ directory.
- L63 `_get_optional_dir()` (function) — Locate the official optional-skills/ directory.
- L68 `_read_manifest()` (function) — Read the manifest as a dict of {skill_name: origin_hash}.
- L95 `_read_suppressed_names()` (function) — Built-in skills the curator pruned — must NOT be re-seeded on sync.
- L121 `_write_manifest(entries: Dict[str, str])` (function) — Write the manifest file atomically in v2 format (name:hash).
- L154 `_read_skill_name(skill_md: Path, fallback: str)` (function) — Read the name field from SKILL.md YAML frontmatter, falling back to *fallback*.
- L175 `_discover_bundled_skills(bundled_dir: Path)` (function) — Find all SKILL.md files in the bundled directory.
- L194 `_compute_relative_dest(skill_dir: Path, bundled_dir: Path)` (function) — Compute the destination path in SKILLS_DIR preserving the category structure.
- L203 `_dir_hash(directory: Path)` (function) — Compute a hash of all file contents in a directory for change detection.
- L217 `_safe_rel_install_path(path: Path, base: Path)` (function) — Return a normalized relative POSIX path, rejecting traversal/absolute paths.
- L228 `_skill_file_list(skill_dir: Path)` (function) — List files inside a skill directory in lock-file format.
- L237 `_content_hash(directory: Path)` (function) — Return the same hash style the skills hub lock uses, falling back locally.
- L249 `_optional_skill_index()` (function) — Return official optional skills keyed by folder name and frontmatter name.
- L276 `_move_to_restore_backup(path: Path, backup_root: Path)` (function) — Move an existing skill directory into a restore backup, preserving rel path.
- L290 `restore_official_optional_skill(name: str, *, restore: bool=False)` (function) — Restore one or all official optional skills from repo source.
- L361 `_backfill_optional_provenance(quiet: bool=False)` (function) — Mark already-present official optional skills as hub-installed.
- L454 `sync_skills(quiet: bool=False)` (function) — Sync bundled skills into ~/.hermes/skills/ using the manifest.
- L630 `_rmtree_writable(path: Path)` (function) — Remove a directory tree, making read-only entries writable first.
- L654 `reset_bundled_skill(name: str, restore: bool=False)` (function) — Reset a bundled skill's manifest tracking so future syncs work normally.
- L753 `set_bundled_skills_opt_out(enabled: bool)` (function) — Toggle the .no-bundled-skills opt-out marker for the active profile.
- L803 `is_bundled_skills_opt_out()` (function) — Return True if the active profile carries the opt-out marker.
- L808 `remove_pristine_bundled_skills(dry_run: bool=False)` (function) — Delete bundled skills that are present, manifest-tracked, AND unmodified.
