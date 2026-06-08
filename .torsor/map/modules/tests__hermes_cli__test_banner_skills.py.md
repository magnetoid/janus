---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_banner_skills.py

Symbols in `tests/hermes_cli/test_banner_skills.py`.

- L14 `test_get_available_skills_delegates_to_find_all_skills()` (function) — get_available_skills should call _find_all_skills (which handles filtering).
- L26 `test_get_available_skills_excludes_disabled()` (function) — Disabled skills should not appear in the banner count.
- L41 `test_get_available_skills_empty_when_no_skills()` (function) — No skills installed returns empty dict.
- L50 `test_get_available_skills_handles_import_failure()` (function) — If _find_all_skills import fails, return empty dict gracefully.
- L59 `test_get_available_skills_null_category_becomes_general()` (function) — Skills with None category should be grouped under 'general'.
