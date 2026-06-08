---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_discord_skill_clamp_warning.py

Symbols in `tests/hermes_cli/test_discord_skill_clamp_warning.py`.

- L22 `test_clamp_collision_emits_warning_naming_both_skills(tmp_path: Path, caplog)` (function) — Two skills with identical first 32 chars — warning names both.
- L84 `test_clamp_collision_with_reserved_name_emits_distinct_warning(tmp_path: Path, caplog)` (function) — A skill clashing with a reserved gateway command gets its own phrasing.
- L136 `test_no_collision_no_warning(tmp_path: Path, caplog)` (function) — Sanity: two distinct-prefix skills produce zero warnings.
- L174 `test_long_skill_name_preserves_cmd_key_through_by_category(tmp_path: Path)` (function) — Skills with names > 32 chars must keep their original cmd_key.
