---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_view_traversal.py

Symbols in `tests/tools/test_skill_view_traversal.py`.

- L15 `fake_skills(tmp_path)` (function) — Create a fake skills directory with one skill and a sensitive file outside.
- L36 `TestPathTraversalBlocked` (class)
- L37 `test_dotdot_in_skill_name_blocked(self, fake_skills)` (method) — A traversal skill name must not escape the skills search root.
- L56 `test_absolute_skill_name_blocked(self, fake_skills)` (method) — An absolute skill name must not bypass the trusted search root.
- L70 `test_legit_skill_name_still_works(self, fake_skills)` (method) — A normal skill name must still resolve after the name guard.
- L75 `test_dotdot_in_file_path(self, fake_skills)` (method) — Direct .. traversal should be rejected.
- L81 `test_dotdot_nested(self, fake_skills)` (method) — Nested .. traversal should also be rejected.
- L87 `test_legitimate_file_still_works(self, fake_skills)` (method) — Valid paths within the skill directory should work normally.
- L93 `test_no_file_path_shows_skill(self, fake_skills)` (method) — Calling skill_view without file_path should return the SKILL.md.
- L98 `test_symlink_escape_blocked(self, fake_skills)` (method) — Symlinks pointing outside the skill directory should be blocked.
- L115 `test_sensitive_file_not_leaked(self, fake_skills)` (method) — Even if traversal somehow passes, sensitive content must not leak.
