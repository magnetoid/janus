---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_resolve_last_session.py

Symbols in `tests/hermes_cli/test_resolve_last_session.py`.

- L8 `_FakeDB` (class)
- L9 `__init__(self, rows)` (method)
- L13 `search_sessions(self, source=None, limit=20, **_kw)` (method)
- L21 `close(self)` (method)
- L25 `test_resolve_last_session_prefers_last_active_over_started_at(monkeypatch)` (function)
- L49 `test_search_sessions_exposes_last_active_column(tmp_path, monkeypatch)` (function)
- L87 `test_resolve_last_session_returns_none_when_empty(monkeypatch)` (function)
- L92 `test_resolve_last_session_closes_db_on_search_error(monkeypatch)` (function)
- L110 `test_resolve_last_session_falls_back_to_started_at(monkeypatch)` (function)
- L121 `test_resolve_last_session_not_limited_to_newest_started_20(tmp_path, monkeypatch)` (function)
