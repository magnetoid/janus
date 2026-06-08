---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_list_allowed_sources.py

Symbols in `tests/gateway/test_session_list_allowed_sources.py`.

- L21 `_StubDB` (class)
- L22 `__init__(self, rows)` (method)
- L26 `list_sessions_rich(self, **kwargs)` (method)
- L31 `_call(limit: int | None=None)` (function)
- L42 `test_session_list_surfaces_all_user_facing_sources(monkeypatch)` (function) — acp / webhook / custom sources should all appear; only ``tool`` is hidden.
- L72 `test_session_list_default_limit_is_200(monkeypatch)` (function) — Default limit should be wide enough for long-running users.
- L82 `test_session_list_respects_explicit_limit(monkeypatch)` (function)
- L91 `test_session_list_preserves_ordering_after_filter(monkeypatch)` (function)
