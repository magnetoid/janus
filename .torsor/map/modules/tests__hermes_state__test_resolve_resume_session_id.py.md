---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_state/test_resolve_resume_session_id.py

Symbols in `tests/hermes_state/test_resolve_resume_session_id.py`.

- L21 `db(tmp_path)` (function)
- L25 `_make_chain(db: SessionDB, ids_with_parent)` (function) — Create sessions in order, forcing started_at so ordering is deterministic.
- L37 `test_redirects_from_empty_head_to_descendant_with_messages(db)` (function)
- L53 `test_returns_self_when_session_has_messages(db)` (function)
- L59 `test_returns_self_when_no_descendant_has_messages(db)` (function)
- L64 `test_returns_self_for_isolated_session(db)` (function)
- L69 `test_returns_self_for_nonexistent_session(db)` (function)
- L73 `test_empty_session_id_passthrough(db)` (function)
- L78 `test_walks_from_middle_of_chain(db)` (function)
- L86 `test_prefers_most_recent_child_when_fork_exists(db)` (function)
