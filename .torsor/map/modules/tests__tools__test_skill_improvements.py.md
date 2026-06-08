---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_improvements.py

Symbols in `tests/tools/test_skill_improvements.py`.

- L34 `TestFuzzyPatchSkill` (class)
- L36 `setup_skills(self, tmp_path, monkeypatch)` (method)
- L43 `test_exact_match_still_works(self)` (method)
- L50 `test_whitespace_trimmed_match(self)` (method) — Patch with extra leading whitespace should still find the target.
- L70 `test_indentation_flexible_match(self)` (method) — Patch where only indentation differs should succeed.
- L95 `test_multiple_matches_blocked_without_replace_all(self)` (method) — Multiple fuzzy matches should return an error without replace_all.
- L112 `test_replace_all_with_fuzzy(self)` (method)
- L130 `test_no_match_returns_preview(self)` (method)
- L136 `test_fuzzy_patch_on_supporting_file(self)` (method) — Fuzzy matching should also work on supporting files.
- L152 `test_patch_preserves_frontmatter_validation(self)` (method) — Fuzzy matching should still run frontmatter validation on SKILL.md.
- L160 `test_skill_manage_patch_uses_fuzzy(self)` (method) — The dispatcher should route to the fuzzy-matching patch.
