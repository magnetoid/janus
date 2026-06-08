---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/session_context.py

Symbols in `gateway/session_context.py`.

- L86 `set_current_session_id(session_id: str)` (function) — Synchronize ``HERMES_SESSION_ID`` across ContextVar and ``os.environ``.
- L101 `set_session_vars(platform: str='', chat_id: str='', chat_name: str='', thread_id: str='', user_id: str='', user_name: str='', session_key: str='', message_id: str='', cwd: str='')` (function) — Set all session context variables and return reset tokens.
- L141 `clear_session_vars(tokens: list)` (function) — Mark session context variables as explicitly cleared.
- L171 `get_session_env(name: str, default: str='')` (function) — Read a session context variable by its legacy ``HERMES_SESSION_*`` name.
