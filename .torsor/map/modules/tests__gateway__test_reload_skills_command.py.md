---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_reload_skills_command.py

Symbols in `tests/gateway/test_reload_skills_command.py`.

- L27 `_make_source()` (function)
- L37 `_make_event(text: str)` (function)
- L41 `_make_runner()` (function)
- L92 `test_reload_skills_handler_queues_note_on_diff(monkeypatch)` (function) — Diff non-empty → handler queues a one-shot note and does NOT touch transcript.
- L142 `test_reload_skills_handler_reports_no_changes(monkeypatch)` (function) — No diff → no queued note, no transcript write.
- L170 `test_dispatcher_routes_reload_skills(monkeypatch)` (function) — ``/reload-skills`` must reach ``_handle_reload_skills_command``.
- L187 `test_underscored_alias_not_flagged_unknown(monkeypatch)` (function) — Telegram autocomplete sends ``/reload_skills`` for ``/reload-skills``.
