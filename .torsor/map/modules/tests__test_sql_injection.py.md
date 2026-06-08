---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_sql_injection.py

Symbols in `tests/test_sql_injection.py`.

- L8 `test_session_cols_no_injection_chars()` (function) — _SESSION_COLS must not contain SQL injection vectors.
- L17 `test_get_sessions_all_query_is_parameterized()` (function) — _GET_SESSIONS_ALL must use a ? placeholder for the cutoff value.
- L26 `test_get_sessions_with_source_query_is_parameterized()` (function) — _GET_SESSIONS_WITH_SOURCE must use ? placeholders for both parameters.
- L35 `test_session_col_names_are_safe_identifiers()` (function) — Every column name listed in _SESSION_COLS must be a simple identifier.
