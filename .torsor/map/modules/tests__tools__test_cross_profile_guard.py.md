---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_cross_profile_guard.py

Symbols in `tests/tools/test_cross_profile_guard.py`.

- L22 `fake_hermes(tmp_path, monkeypatch)` (function) — Build a two-profile Hermes layout and point HERMES_HOME at
- L59 `TestWriteFileCrossProfileGuard` (class)
- L60 `test_in_profile_write_allowed(self, fake_hermes)` (method)
- L70 `test_cross_profile_write_blocked_by_default(self, fake_hermes)` (method) — The May 2026 incident — security-profile session edits default
- L85 `test_cross_profile_True_bypass(self, fake_hermes)` (method) — Explicit override after user direction must succeed.
- L96 `test_non_hermes_path_unaffected(self, fake_hermes, tmp_path)` (method)
- L111 `TestPatchCrossProfileGuard` (class)
- L112 `test_cross_profile_patch_blocked(self, fake_hermes)` (method)
- L127 `test_cross_profile_patch_bypass(self, fake_hermes)` (method)
- L141 `test_v4a_patch_extracts_path_for_guard(self, fake_hermes)` (method) — V4A patches embed the target paths in the patch body, not in
- L167 `TestSkillManageCrossProfileErrorUX` (class)
- L168 `_make_skill_in_profile(self, profile_dir: Path, name: str)` (method)
- L175 `test_error_names_other_profile_when_skill_lives_there(self, fake_hermes, monkeypatch)` (method) — The original incident shape — model expects 'foo' in active
- L194 `test_error_names_multiple_profiles(self, fake_hermes, monkeypatch)` (method) — When the skill exists in TWO other profiles, both should be named.
- L210 `test_genuinely_missing_skill_keeps_helpful_hint(self, fake_hermes, monkeypatch)` (method) — When no profile has the skill, error falls back to skills_list hint.
- L229 `TestSystemPromptActiveProfile` (class)
- L230 `test_default_profile_line_in_prompt(self, tmp_path, monkeypatch)` (method) — When active profile is 'default', the prompt names it and warns
- L244 `test_named_profile_line_in_prompt_text(self, fake_hermes)` (method) — When active profile is 'hermes-security', the prompt warns
