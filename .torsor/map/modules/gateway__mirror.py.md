---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/mirror.py

Symbols in `gateway/mirror.py`.

- L25 `mirror_to_session(platform: str, chat_id: str, message_text: str, source_label: str='cli', thread_id: Optional[str]=None, user_id: Optional[str]=None)` (function) — Append a delivery-mirror message to the target session's transcript.
- L84 `_find_session_id(platform: str, chat_id: str, thread_id: Optional[str]=None, user_id: Optional[str]=None)` (function) — Find the active session_id for a platform + chat_id pair.
- L153 `_append_to_sqlite(session_id: str, message: dict)` (function) — Append a message to the SQLite session database.
