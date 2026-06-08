---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# acp_adapter/session.py

Symbols in `acp_adapter/session.py`.

- L29 `_win_path_to_wsl(path: str)` (function) — Convert a Windows drive path to its WSL /mnt/<drive>/... equivalent.
- L39 `_translate_acp_cwd(cwd: str)` (function) — Translate Windows ACP cwd values when Hermes itself is running in WSL.
- L56 `_normalize_cwd_for_compare(cwd: str | None)` (function)
- L73 `_build_session_title(title: Any, preview: Any, cwd: str | None)` (function)
- L84 `_format_updated_at(value: Any)` (function)
- L95 `_updated_at_sort_key(value: Any)` (function)
- L112 `_acp_stderr_print(*args, **kwargs)` (function) — Best-effort human-readable output sink for ACP stdio sessions.
- L123 `_register_task_cwd(task_id: str, cwd: str)` (function) — Bind a task/session id to the editor's working directory for tools.
- L140 `_expand_acp_enabled_toolsets(toolsets: List[str] | None=None, mcp_server_names: List[str] | None=None)` (function) — Return ACP toolsets plus explicit MCP server toolsets for this session.
- L158 `_clear_task_cwd(task_id: str)` (function) — Remove task-specific cwd overrides for an ACP session.
- L170 `SessionState` (class) — Tracks per-session state for an ACP-managed Hermes agent.
- L186 `SessionManager` (class) — Thread-safe manager for ACP sessions backed by Hermes AIAgent instances.
- L194 `__init__(self, agent_factory=None, db=None)` (method) — Args:
- L210 `create_session(self, cwd: str='.')` (method) — Create a new session with a unique ID and a fresh AIAgent.
- L231 `get_session(self, session_id: str)` (method) — Return the session for *session_id*, or ``None``.
- L244 `remove_session(self, session_id: str)` (method) — Remove a session from memory and database. Returns True if it existed.
- L253 `fork_session(self, session_id: str, cwd: str='.')` (method) — Deep-copy a session's history into a new session.
- L283 `list_sessions(self, cwd: str | None=None)` (method) — Return lightweight info dicts for all sessions (memory + database).
- L357 `update_cwd(self, session_id: str, cwd: str)` (method) — Update the working directory for a session and its tool overrides.
- L368 `cleanup(self)` (method) — Remove all sessions (memory and database) and clear task-specific cwd overrides.
- L388 `save_session(self, session_id: str)` (method) — Persist the current state of a session to the database.
- L401 `_get_db(self)` (method) — Lazily initialise and return the SessionDB instance.
- L423 `_persist(self, state: SessionState)` (method) — Write session state to the database.
- L471 `_restore(self, session_id: str)` (method) — Load a session from the database into memory, recreating the AIAgent.
- L545 `_delete_persisted(self, session_id: str)` (method) — Delete a session from the database. Returns True if it existed.
- L558 `_make_agent(self, *, session_id: str, cwd: str, model: str | None=None, requested_provider: str | None=None, base_url: str | None=None, api_mode: str | None=None)` (method)
