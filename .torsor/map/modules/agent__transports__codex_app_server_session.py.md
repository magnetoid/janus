---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/codex_app_server_session.py

Symbols in `agent/transports/codex_app_server_session.py`.

- L65 `TurnResult` (class) — Result of one user→assistant→tool turn through the codex app-server.
- L91 `_coerce_turn_input_text(user_input: Any)` (function) — Collapse Hermes/OpenAI rich content into app-server text input.
- L154 `_classify_oauth_failure(*parts: str)` (function) — Return a user-friendly re-auth hint if any of the provided strings
- L178 `_ServerRequestRouting` (class) — Default policies for codex-side approval requests when no interactive
- L188 `CodexAppServerSession` (class) — One Codex thread per Hermes session, lifetime owned by AIAgent.
- L197 `__init__(self, *, cwd: Optional[str]=None, codex_bin: str='codex', codex_home: Optional[str]=None, permission_profile: Optional[str]=None, approval_callback: Optional[Callable[..., str]]=None, on_event: Optional[Callable[[dict], None]]=None, request_routing: Optional[_ServerRequestRouting]=None, client_factory: Optional[Callable[..., CodexAppServerClient]]=None)` (method)
- L236 `ensure_started(self)` (method) — Spawn the subprocess, do the initialize handshake, and start a
- L296 `close(self)` (method)
- L308 `__enter__(self)` (method)
- L311 `__exit__(self, *exc: Any)` (method)
- L316 `request_interrupt(self)` (method) — Idempotent: signal the active turn loop to issue turn/interrupt
- L323 `_format_error_with_stderr(self, prefix: str, exc: Any='', *, tail_lines: int=_STDERR_TAIL_LINES)` (method) — Build a user-facing error string for codex failures.
- L362 `run_turn(self, user_input: Any, *, turn_timeout: float=600.0, notification_poll_timeout: float=0.25, post_tool_quiet_timeout: float=90.0)` (method) — Send a user message and block until turn/completed, while
- L618 `_issue_interrupt(self, turn_id: Optional[str])` (method)
- L633 `_handle_server_request(self, req: dict)` (method) — Translate a codex server request (approval) into Hermes' approval
- L691 `_decide_exec_approval(self, params: dict)` (method)
- L714 `_decide_apply_patch_approval(self, params: dict)` (method)
- L755 `_track_pending_file_change(self, note: dict)` (method) — Maintain self._pending_file_changes from item/started + item/completed
- L792 `_lookup_pending_file_change(self, item_id: str)` (method) — Look up an in-progress fileChange item by id and summarize its
- L805 `_approval_choice_to_codex_decision(choice: str)` (function) — Map Hermes approval choices onto codex's CommandExecutionApprovalDecision
- L821 `_has_turn_aborted_marker(text: str)` (function) — Return True if `text` contains any of the raw markers codex uses
- L839 `_get_hermes_version()` (function) — Best-effort Hermes version string for codex's userAgent line.
