---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_external_skills.py

Symbols in `tests/agent/test_external_skills.py`.

- L11 `external_skills_dir(tmp_path)` (function) — Create a temp dir with a sample external skill.
- L23 `hermes_home(tmp_path)` (function) — Create a minimal HERMES_HOME with config.
- L31 `TestGetExternalSkillsDirs` (class)
- L32 `test_empty_config(self, hermes_home)` (method)
- L39 `test_nonexistent_dir_skipped(self, hermes_home)` (method)
- L48 `test_valid_dir_returned(self, hermes_home, external_skills_dir)` (method)
- L58 `test_duplicate_dirs_deduplicated(self, hermes_home, external_skills_dir)` (method)
- L67 `test_local_skills_dir_excluded(self, hermes_home)` (method)
- L77 `test_no_config_file(self, hermes_home)` (method)
- L84 `test_string_value_converted_to_list(self, hermes_home, external_skills_dir)` (method)
- L94 `TestGetAllSkillsDirs` (class)
- L95 `test_local_always_first(self, hermes_home, external_skills_dir)` (method)
- L106 `TestExternalSkillsInFindAll` (class)
- L107 `test_external_skills_found(self, hermes_home, external_skills_dir)` (method)
- L121 `test_local_takes_precedence(self, hermes_home, external_skills_dir)` (method) — If the same skill name exists locally and externally, local wins.
- L143 `TestExternalSkillView` (class)
- L144 `test_skill_view_finds_external(self, hermes_home, external_skills_dir)` (method)
