---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_reload_skills_discord_resync.py

Symbols in `tests/gateway/test_reload_skills_discord_resync.py`.

- L28 `_make_adapter()` (function) — Construct a DiscordAdapter without going through __init__ / token checks.
- L42 `TestRefreshSkillGroup` (class)
- L43 `test_refresh_repopulates_entries_after_catalog_change(self, monkeypatch)` (method) — The initial catalog is replaced wholesale on refresh.
- L86 `test_refresh_sorts_entries_alphabetically(self, monkeypatch)` (method) — Autocomplete order must be stable and predictable across refreshes.
- L112 `test_refresh_handles_collector_exception_gracefully(self, monkeypatch)` (method) — A broken collector must not take down /reload-skills.
- L138 `TestRegisterSkillGroupUsesInstanceState` (class) — The closure-based ``entries`` / ``skill_lookup`` must be gone.
- L154 `test_refresh_catalog_state_populates_instance_attrs(self, monkeypatch)` (method)
- L185 `TestHandleReloadSkillsCallsRefreshSkillGroup` (class) — Gateway-side integration: /reload-skills must call refresh on adapters.
- L188 `test_orchestrator_calls_refresh_skill_group_on_every_adapter(self)` (method) — Sync + async refresh_skill_group implementations both get awaited/called.
