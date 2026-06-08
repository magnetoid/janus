---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_skills_config.py

Symbols in `tests/hermes_cli/test_skills_config.py`.

- L9 `TestGetDisabledSkills` (class)
- L10 `test_empty_config(self)` (method)
- L14 `test_reads_global_disabled(self)` (method)
- L19 `test_reads_platform_disabled(self)` (method)
- L27 `test_platform_falls_back_to_global(self)` (method)
- L33 `test_missing_skills_key(self)` (method)
- L37 `test_empty_disabled_list(self)` (method)
- L46 `TestSaveDisabledSkills` (class)
- L48 `test_saves_global_sorted(self, mock_save)` (method)
- L56 `test_saves_platform_disabled(self, mock_save)` (method)
- L63 `test_saves_empty(self, mock_save)` (method)
- L70 `test_creates_skills_key(self, mock_save)` (method)
- L82 `TestIsSkillDisabled` (class)
- L84 `test_globally_disabled(self, mock_load)` (method)
- L90 `test_globally_enabled(self, mock_load)` (method)
- L96 `test_platform_disabled(self, mock_load)` (method)
- L105 `test_platform_enabled_overrides_global(self, mock_load)` (method)
- L115 `test_platform_falls_back_to_global(self, mock_load)` (method)
- L122 `test_empty_config(self, mock_load)` (method)
- L128 `test_exception_returns_false(self, mock_load)` (method)
- L135 `test_env_var_platform(self, mock_load)` (method)
- L147 `TestGetDisabledSkillNames` (class) — Tests for agent.skill_utils.get_disabled_skill_names.
- L150 `test_explicit_platform_param(self, tmp_path, monkeypatch)` (method) — Explicit platform= parameter should resolve per-platform list.
- L169 `test_session_platform_env_var(self, tmp_path, monkeypatch)` (method) — HERMES_SESSION_PLATFORM should be used when HERMES_PLATFORM is unset.
- L188 `test_hermes_platform_takes_precedence(self, tmp_path, monkeypatch)` (method) — HERMES_PLATFORM should win over HERMES_SESSION_PLATFORM.
- L207 `test_explicit_param_overrides_env_vars(self, tmp_path, monkeypatch)` (method) — Explicit platform= param should override all env vars.
- L226 `test_no_platform_returns_global(self, tmp_path, monkeypatch)` (method) — No platform env vars or param should return global list.
- L250 `TestFindAllSkillsFiltering` (class)
- L253 `test_disabled_skill_excluded(self, mock_platform, mock_disabled, tmp_path, monkeypatch)` (method)
- L270 `test_enabled_skill_included(self, mock_platform, mock_disabled, tmp_path, monkeypatch)` (method)
- L285 `test_skip_disabled_returns_all(self, mock_platform, mock_disabled, tmp_path, monkeypatch)` (method) — skip_disabled=True ignores the disabled set (for config UI).
- L304 `TestGetCategories` (class)
- L305 `test_extracts_unique_categories(self)` (method)
- L315 `test_none_becomes_uncategorized(self)` (method)
