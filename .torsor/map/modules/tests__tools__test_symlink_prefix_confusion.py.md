---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_symlink_prefix_confusion.py

Symbols in `tests/tools/test_symlink_prefix_confusion.py`.

- L13 `_old_check_escapes(resolved: Path, skill_dir_resolved: Path)` (function) — The BROKEN check that used startswith without separator.
- L24 `_new_check_escapes(resolved: Path, skill_dir_resolved: Path)` (function) — The FIXED check using is_relative_to().
- L32 `TestPrefixConfusionRegression` (class) — The core bug: startswith() can't distinguish directory boundaries.
- L35 `test_old_check_misses_sibling_with_shared_prefix(self, tmp_path)` (method) — Old startswith check fails on sibling dirs that share a prefix.
- L49 `test_new_check_catches_sibling_with_shared_prefix(self, tmp_path)` (method) — is_relative_to() correctly rejects sibling dirs.
- L63 `test_both_agree_on_real_subpath(self, tmp_path)` (method) — Both checks allow a genuine subpath.
- L77 `test_both_agree_on_completely_outside_path(self, tmp_path)` (method) — Both checks block a path that's completely outside.
- L91 `test_skill_dir_itself_allowed(self, tmp_path)` (method) — Requesting the skill directory itself is fine.
- L104 `_can_symlink()` (function) — Check if we can create symlinks (needs admin/dev-mode on Windows).
- L119 `TestSymlinkEscapeWithActualSymlinks` (class) — Test the full symlink scenario with real filesystem symlinks.
- L122 `test_symlink_to_sibling_prefix_dir_detected(self, tmp_path)` (method) — A symlink from axolotl/ to axolotl-backdoor/ must be caught.
- L144 `test_symlink_within_skill_dir_allowed(self, tmp_path)` (method) — A symlink that stays within the skill directory is fine.
- L158 `test_symlink_to_parent_dir_blocked(self, tmp_path)` (method) — A symlink pointing outside (to parent) is blocked.
