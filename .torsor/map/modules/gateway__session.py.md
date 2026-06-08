---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/session.py

Symbols in `gateway/session.py`.

- L25 `_now()` (function) — Return the current local time.
- L34 `_hash_id(value: str)` (function) — Deterministic 12-char hex hash of an identifier.
- L39 `_hash_sender_id(value: str)` (function) — Hash a sender ID to ``user_<12hex>``.
- L44 `_hash_chat_id(value: str)` (function) — Hash the numeric portion of a chat ID, preserving platform prefix.
- L71 `SessionSource` (class) — Describes where a message originated from.
- L96 `description(self)` (method) — Human-readable description of the source.
- L116 `to_dict(self)` (method)
- L140 `from_dict(cls, data: Dict[str, Any])` (method)
- L160 `SessionContext` (class) — Full context for a session, used for dynamic system prompt injection.
- L180 `to_dict(self)` (method)
- L206 `_discord_tools_loaded()` (function) — True iff the agent will actually have Discord tools this session.
- L231 `build_session_context_prompt(context: SessionContext, *, redact_pii: bool=False)` (function) — Build the dynamic system prompt section that tells the agent about its context.
- L425 `SessionEntry` (class) — Entry in the session store.
- L494 `to_dict(self)` (method)
- L530 `from_dict(cls, data: Dict[str, Any])` (method)
- L579 `is_shared_multi_user_session(source: SessionSource, *, group_sessions_per_user: bool=True, thread_sessions_per_user: bool=False)` (function) — Return True when a non-DM session is shared across participants.
- L600 `build_session_key(source: SessionSource, group_sessions_per_user: bool=True, thread_sessions_per_user: bool=False)` (function) — Build a deterministic session key from a message source.
- L668 `SessionStore` (class) — Manages session storage and retrieval.
- L676 `__init__(self, sessions_dir: Path, config: GatewayConfig, has_active_processes_fn=None)` (method)
- L693 `_ensure_loaded(self)` (method) — Load sessions index from disk if not already loaded.
- L698 `_ensure_loaded_locked(self)` (method) — Load sessions index from disk. Must be called with self._lock held.
- L721 `_save(self)` (method) — Save sessions index to disk (kept for session key -> ID mapping).
- L744 `_generate_session_key(self, source: SessionSource)` (method) — Generate a session key from a source.
- L752 `_is_session_expired(self, entry: SessionEntry)` (method) — Check if a session has expired based on its reset policy.
- L790 `_should_reset(self, entry: SessionEntry, source: SessionSource)` (method) — Check if a session should be reset based on policy.
- L834 `has_any_sessions(self)` (method) — Check if any sessions have ever been created (across all platforms).
- L856 `get_or_create_session(self, source: SessionSource, force_new: bool=False)` (method) — Get an existing session or create a new one.
- L957 `update_session(self, session_key: str, last_prompt_tokens: int=None)` (method) — Update lightweight session metadata after an interaction.
- L973 `suspend_session(self, session_key: str)` (method) — Mark a session as suspended so it auto-resets on next access.
- L988 `mark_resume_pending(self, session_key: str, reason: str='restart_timeout')` (method) — Mark a session as resumable after a restart interruption.
- L1017 `clear_resume_pending(self, session_key: str)` (method) — Clear the resume-pending flag after a successful resumed turn.
- L1037 `prune_old_entries(self, max_age_days: int)` (method) — Drop SessionEntry records older than max_age_days.
- L1094 `suspend_recently_active(self, max_age_seconds: int=120)` (method) — Mark recently-active sessions as resumable after an unexpected exit.
- L1130 `reset_session(self, session_key: str, display_name: Optional[str]=None)` (method) — Force reset a session, creating a new session ID.
- L1182 `switch_session(self, session_key: str, target_session_id: str)` (method) — Switch a session key to point at an existing session ID.
- L1237 `list_sessions(self, active_minutes: Optional[int]=None)` (method) — List all sessions, optionally filtered by activity.
- L1251 `append_to_transcript(self, session_id: str, message: Dict[str, Any], skip_db: bool=False)` (method) — Append a message to a session's transcript (SQLite).
- L1285 `rewrite_transcript(self, session_id: str, messages: List[Dict[str, Any]])` (method) — Replace the entire transcript for a session with new messages.
- L1297 `load_transcript(self, session_id: str)` (method) — Load all messages from a session's transcript.
- L1312 `rewind_session(self, session_id: str, n: int=1)` (method) — Back up ``n`` user turns via soft-delete, keeping rows for audit.
- L1365 `build_session_context(source: SessionSource, config: GatewayConfig, session_entry: Optional[SessionEntry]=None)` (function) — Build a full session context from a source and config.
