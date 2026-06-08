---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_skill_env_passthrough.py

Symbols in `tests/tools/test_skill_env_passthrough.py`.

- L13 `_clean_passthrough()` (function)
- L21 `_create_skill(tmp_path, name, frontmatter_extra='')` (function) — Create a minimal skill directory with SKILL.md.
- L37 `TestSkillViewRegistersPassthrough` (class)
- L38 `test_available_env_vars_registered(self, tmp_path, monkeypatch)` (method) — When a skill declares required_environment_variables and the var IS set,
- L65 `test_remote_backend_persisted_env_vars_registered(self, tmp_path, monkeypatch)` (method) — Remote-backed skills still register locally available env vars.
- L94 `test_missing_env_vars_not_registered(self, tmp_path, monkeypatch)` (method) — When a skill declares required_environment_variables but the var is NOT set,
- L119 `test_no_env_vars_skill_no_registration(self, tmp_path, monkeypatch)` (method) — Skills without required_environment_variables shouldn't register anything.
