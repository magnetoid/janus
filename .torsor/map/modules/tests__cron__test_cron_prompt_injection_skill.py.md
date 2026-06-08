---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_prompt_injection_skill.py

Symbols in `tests/cron/test_cron_prompt_injection_skill.py`.

- L24 `cron_env(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with an empty skills tree.
- L65 `_plant_skill(hermes_home: Path, name: str, body: str)` (function) — Drop a SKILL.md into ~/.hermes/skills/<name>/ bypassing skills_guard.
- L75 `_plant_bundle(hermes_home: Path, name: str, skills: list[str], instruction: str='')` (function) — Drop a bundle YAML into ~/.hermes/skill-bundles/ and refresh cache.
- L94 `TestScanAssembledCronPrompt` (class)
- L95 `test_clean_prompt_passes_through(self, cron_env)` (method)
- L103 `test_injection_pattern_raises(self, cron_env)` (method)
- L112 `test_env_exfil_pattern_raises(self, cron_env)` (method)
- L120 `test_invisible_unicode_raises(self, cron_env)` (method)
- L135 `TestBuildJobPromptScansSkillContent` (class)
- L136 `test_clean_skill_builds_normally(self, cron_env)` (method)
- L151 `test_builtin_style_github_api_example_is_allowed(self, cron_env)` (method)
- L170 `test_skill_with_injection_payload_raises(self, cron_env)` (method) — The core attack: planted skill carries an injection payload.
- L197 `test_skill_with_env_exfil_command_in_prose_is_allowed(self, cron_env)` (method) — A skill that *describes* an exfil command in prose (e.g. a
- L229 `test_skill_with_invisible_unicode_sanitized_not_blocked(self, cron_env)` (method) — A stray zero-width space in a vetted skill body is stripped, not
- L251 `test_no_skills_still_scans_user_prompt(self, cron_env)` (method) — Defense-in-depth: even without skills, assembled-prompt scanning
- L266 `test_missing_skill_does_not_crash(self, cron_env)` (method)
- L279 `test_skill_bundle_in_job_skills_loads_referenced_skills(self, cron_env)` (method)
- L305 `test_bundle_name_shadows_skill_name_for_cron_jobs(self, cron_env)` (method)
