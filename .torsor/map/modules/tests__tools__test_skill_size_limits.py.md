---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_size_limits.py

Symbols in `tests/tools/test_skill_size_limits.py`.

- L20 `isolate_skills(tmp_path, monkeypatch)` (function) — Redirect SKILLS_DIR to a temp directory.
- L30 `_make_skill_content(body_chars: int)` (function) — Generate valid SKILL.md content with a body of the given character count.
- L42 `TestValidateContentSize` (class) — Unit tests for _validate_content_size.
- L45 `test_within_limit(self)` (method)
- L48 `test_at_limit(self)` (method)
- L51 `test_over_limit(self)` (method)
- L57 `test_custom_label(self)` (method)
- L62 `TestCreateSkillSizeLimit` (class) — create action rejects oversized content.
- L65 `test_create_within_limit(self, isolate_skills)` (method)
- L70 `test_create_over_limit(self, isolate_skills)` (method)
- L76 `test_create_at_limit(self, isolate_skills)` (method)
- L86 `TestEditSkillSizeLimit` (class) — edit action rejects oversized content.
- L89 `test_edit_over_limit(self, isolate_skills)` (method)
- L103 `TestPatchSkillSizeLimit` (class) — patch action checks resulting size, not just the new_string.
- L106 `test_patch_that_would_exceed_limit(self, isolate_skills)` (method)
- L121 `test_patch_that_reduces_size_on_oversized_skill(self, isolate_skills, tmp_path)` (method) — Patches that shrink an already-oversized skill should succeed.
- L143 `test_patch_supporting_file_size_limit(self, isolate_skills)` (method) — Patch on a supporting file also checks size.
- L166 `TestWriteFileSizeLimit` (class) — write_file action enforces both char and byte limits.
- L169 `test_write_file_over_char_limit(self, isolate_skills)` (method)
- L182 `test_write_file_within_limit(self, isolate_skills)` (method)
- L195 `TestHandPlacedSkillsNoLimit` (class) — Skills dropped directly on disk are not constrained.
- L198 `test_oversized_handplaced_skill_loads(self, isolate_skills, tmp_path)` (method) — A hand-placed 200k skill can still be read via skill_view.
