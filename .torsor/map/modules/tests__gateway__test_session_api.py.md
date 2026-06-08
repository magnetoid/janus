---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_api.py

Symbols in `tests/gateway/test_session_api.py`.

- L15 `session_db(tmp_path)` (function)
- L26 `adapter(session_db)` (function)
- L33 `auth_adapter(session_db)` (function)
- L39 `_create_session_app(adapter: APIServerAdapter)` (function)
- L55 `test_capabilities_advertises_session_control_surface(adapter)` (function)
- L79 `test_session_crud_and_message_history(adapter, session_db)` (function)
- L125 `test_session_fork_uses_current_sessiondb_branch_primitives(adapter, session_db)` (function)
- L147 `test_session_chat_loads_history_and_preserves_session_headers(auth_adapter, session_db)` (function)
- L183 `test_session_chat_accepts_multimodal_message(auth_adapter, session_db)` (function)
- L210 `test_session_chat_stream_accepts_multimodal_message(adapter, session_db)` (function)
- L243 `test_session_chat_stream_emits_lifecycle_events_and_keepalive_safe_shape(adapter, session_db)` (function)
- L272 `test_session_chat_stream_run_completed_carries_turn_transcript(adapter, session_db)` (function) — run.completed must include the full interleaved turn transcript so a
- L341 `test_session_endpoints_require_auth_when_key_configured(auth_adapter)` (function)
- L357 `test_session_header_rejected_without_api_key(adapter, session_db)` (function)
