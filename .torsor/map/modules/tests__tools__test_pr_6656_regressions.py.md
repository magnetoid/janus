---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_pr_6656_regressions.py

Symbols in `tests/tools/test_pr_6656_regressions.py`.

- L42 `TestUninstallPathTraversal` (class) — The ``install_path`` field in ``lock.json`` is attacker-controllable
- L50 `hub_setup(self, tmp_path, monkeypatch)` (method) — Build a hub directory tree with a malicious lock.json entry.
- L84 `_write_lock(self, hub_dir: Path, entries: dict)` (method)
- L88 `test_traversal_via_parent_segments_rejected(self, hub_setup)` (method) — install_path: "../do-not-delete" must NOT escape SKILLS_DIR.
- L112 `test_absolute_path_rejected(self, hub_setup)` (method) — install_path that's an absolute path outside SKILLS_DIR must be refused.
- L130 `test_symlink_escape_rejected(self, tmp_path, hub_setup)` (method) — Symlinks inside SKILLS_DIR that point outside must be refused
- L153 `test_legitimate_skill_uninstall_still_works(self, hub_setup)` (method) — The guard must NOT block a normal skill directory inside SKILLS_DIR.
- L180 `TestBundleHashFilenameSensitivity` (class) — Hashes must change when filenames are swapped, even if combined
- L187 `_make_bundle(self, files: dict)` (method)
- L196 `test_filename_swap_changes_hash(self)` (method) — Swapping content between SKILL.md and scripts/run.sh must
- L204 `test_identical_bundles_same_hash(self)` (method) — Sanity: equal content + paths = equal hash.
- L210 `test_disk_hash_changes_on_filename_swap(self, tmp_path)` (method) — ``content_hash`` on disk must also be filename-sensitive,
- L226 `test_bundle_and_disk_hash_match(self, tmp_path)` (method) — Symmetry contract: the same skill, expressed as a SkillBundle
- L250 `TestListPendingLock` (class) — list_pending writes via _cleanup_expired. Without the lock,
- L255 `test_list_pending_acquires_lock(self, tmp_path)` (method) — Source-grep contract: ``list_pending`` body must be wrapped
- L284 `test_list_pending_returns_correct_data(self, tmp_path)` (method) — End-to-end smoke: even with the lock held, basic operation works.
