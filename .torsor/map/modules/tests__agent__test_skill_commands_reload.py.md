---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_skill_commands_reload.py

Symbols in `tests/agent/test_skill_commands_reload.py`.

- L21 `_write_skill(skills_dir: Path, name: str, description: str='')` (function)
- L39 `hermes_home(monkeypatch)` (function) — Isolate HERMES_HOME for ``reload_skills`` tests.
- L67 `TestReloadSkillsHelper` (class) — ``agent.skill_commands.reload_skills``.
- L70 `test_returns_expected_keys(self, hermes_home)` (method)
- L79 `test_detects_newly_added_skill_with_description(self, hermes_home)` (method)
- L93 `test_detects_removed_skill_carries_description(self, hermes_home)` (method)
- L111 `test_description_passes_through_verbatim(self, hermes_home)` (method) — ``description`` must be the full SKILL.md frontmatter string — no
- L127 `test_unchanged_skills_appear_in_unchanged_list(self, hermes_home)` (method)
- L140 `test_does_not_invalidate_prompt_cache_snapshot(self, hermes_home)` (method) — reload_skills must NOT delete the skills prompt-cache snapshot.
