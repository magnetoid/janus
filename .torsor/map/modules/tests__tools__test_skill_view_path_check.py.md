---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_view_path_check.py

Symbols in `tests/tools/test_skill_view_path_check.py`.

- L13 `_path_escapes_skill_dir(resolved: Path, skill_dir_resolved: Path)` (function) — Reproduce the boundary check from tools/skills_tool.py.
- L21 `TestSkillViewPathBoundaryCheck` (class) — Verify the path boundary check works on all platforms.
- L24 `test_valid_subpath_allowed(self, tmp_path)` (method) — A file inside the skill directory must NOT be flagged.
- L37 `test_deeply_nested_subpath_allowed(self, tmp_path)` (method) — Deeply nested valid paths must also pass.
- L50 `test_outside_path_blocked(self, tmp_path)` (method) — A file outside the skill directory must be flagged.
- L62 `test_sibling_skill_dir_blocked(self, tmp_path)` (method) — A file in a sibling skill directory must be flagged.
- L80 `test_skill_dir_itself_allowed(self, tmp_path)` (method) — Requesting the skill directory itself must be allowed.
- L91 `TestOldCheckWouldFail` (class) — Demonstrate the bug: the old hardcoded '/' check fails on Windows.
- L94 `_old_path_escapes(self, resolved: Path, skill_dir_resolved: Path)` (method) — The BROKEN check that used hardcoded '/'.
- L102 `test_old_check_false_positive_on_windows(self, tmp_path)` (method) — On Windows, the old check incorrectly blocks valid subpaths.
