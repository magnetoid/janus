---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/session_search_tool.py

Symbols in `tools/session_search_tool.py`.

- L42 `_format_timestamp(ts: Union[int, float, str, None])` (function) — Convert a Unix timestamp (float/int) or ISO string to a human-readable date.
- L67 `_resolve_to_parent(db, session_id: str)` (function) — Walk parent_session_id chain to the lineage root. Falls back to input on errors.
- L89 `_shape_message(m: Dict[str, Any], anchor_id: Optional[int]=None)` (function) — Slim a message row for the tool response. Keeps content even if empty.
- L110 `_resolve_profile_db(profile: str)` (function) — Open another profile's ``state.db`` read-only, or None for the current one.
- L133 `_locate_session_db(session_id: str)` (function) — Scan every profile's ``state.db`` (read-only) for a session id.
- L177 `_read_session(db, session_id: str, head: int=20, tail: int=10)` (function) — Read shape: dump a whole session by id (head + tail when large).
- L226 `_list_recent_sessions(db, limit: int, current_session_id: str=None)` (function) — Return metadata for the most recent sessions (no LLM calls, no FTS5).
- L269 `_scroll(db, session_id: str, around_message_id: int, window: int=5, current_session_id: str=None)` (function) — Scroll shape: return a window of messages centered on an anchor.
- L393 `_discover(db, query: str, role_filter: Optional[List[str]], limit: int, sort: Optional[str], current_session_id: str=None)` (function) — Discovery shape: FTS5 + anchored window + bookends per hit. Single call.
- L494 `session_search(query: str='', role_filter: str=None, limit: int=3, db=None, current_session_id: str=None, session_id: str=None, around_message_id: int=None, window: int=5, sort: str=None, profile: str=None)` (function) — Single-shape tool. Mode inferred from which args are set.
- L618 `check_session_search_requirements()` (function) — Requires the SQLite state database.
