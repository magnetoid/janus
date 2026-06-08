---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/title_generator.py

Symbols in `agent/title_generator.py`.

- L29 `generate_title(user_message: str, assistant_response: str, timeout: float=30.0, failure_callback: Optional[FailureCallback]=None, main_runtime: dict=None)` (function) — Generate a session title from the first exchange.
- L87 `auto_title_session(session_db, session_id: str, user_message: str, assistant_response: str, failure_callback: Optional[FailureCallback]=None, main_runtime: dict=None, title_callback: Optional[TitleCallback]=None)` (function) — Generate and set a session title if one doesn't already exist.
- L133 `maybe_auto_title(session_db, session_id: str, user_message: str, assistant_response: str, conversation_history: list, failure_callback: Optional[FailureCallback]=None, main_runtime: dict=None, title_callback: Optional[TitleCallback]=None)` (function) — Fire-and-forget title generation after the first exchange.
