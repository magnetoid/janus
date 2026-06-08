---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_command_bypass_active_session.py

Symbols in `tests/gateway/test_command_bypass_active_session.py`.

- L29 `_StubAdapter` (class) — Concrete adapter with abstract methods stubbed out.
- L32 `connect(self)` (method)
- L35 `disconnect(self)` (method)
- L38 `send(self, chat_id, text, **kwargs)` (method)
- L41 `get_chat_info(self, chat_id)` (method)
- L45 `_make_adapter()` (function) — Create a minimal adapter for testing the active-session guard.
- L65 `_make_event(text='/stop', chat_id='12345')` (function)
- L72 `_session_key(chat_id='12345')` (function)
- L84 `TestCommandBypassActiveSession` (class) — Commands that must bypass the active-session guard.
- L88 `test_stop_bypasses_guard(self)` (method) — /stop must be dispatched directly, not queued.
- L104 `test_new_bypasses_guard(self)` (method) — /new must be dispatched directly, not queued.
- L116 `test_reset_bypasses_guard(self)` (method) — /reset (alias for /new) must be dispatched directly.
- L128 `test_approve_bypasses_guard(self)` (method) — /approve must bypass (deadlock prevention).
- L140 `test_deny_bypasses_guard(self)` (method) — /deny must bypass (deadlock prevention).
- L152 `test_status_bypasses_guard(self)` (method) — /status must bypass so it returns a system response.
- L164 `test_agents_bypasses_guard(self)` (method) — /agents must bypass so active-task queries don't interrupt runs.
- L176 `test_tasks_alias_bypasses_guard(self)` (method) — /tasks alias must bypass active-session guard too.
- L188 `test_background_bypasses_guard(self)` (method) — /background must bypass so it spawns a parallel task, not an interrupt.
- L204 `test_steer_bypasses_guard(self)` (method) — /steer must bypass the Level-1 active-session guard so it reaches
- L223 `test_help_bypasses_guard(self)` (method) — /help must bypass so it is not silently dropped as pending slash text.
- L239 `test_update_bypasses_guard(self)` (method) — /update must bypass so it is not discarded by the pending-command safety net.
- L255 `test_queue_bypasses_guard(self)` (method) — /queue must bypass so it can queue without interrupting.
- L280 `TestAllResolvableCommandsBypassGuard` (class) — Every recognized slash command must bypass the Level-1 active-session
- L306 `test_command_bypasses_guard(self, command_text, canonical)` (method) — Any resolvable slash command bypasses instead of being queued.
- L322 `test_should_bypass_returns_true_for_every_registered_command(self)` (method) — Spot-check: the commands previously-broken on Discord all bypass.
- L335 `test_should_bypass_returns_false_for_unknown(self)` (method) — Unknown words don't bypass — they get queued as user text.
- L351 `TestNonBypassStillQueued` (class) — Regular messages and unknown commands must be queued, not dispatched.
- L355 `test_regular_text_queued(self)` (method) — Plain text while agent is running must be queued as pending.
- L371 `test_unknown_command_queued(self)` (method) — Unknown /commands must be queued, not dispatched.
- L383 `test_file_path_not_treated_as_command(self)` (method) — A message like '/path/to/file' must not bypass the guard.
- L400 `TestNoActiveSessionNormalDispatch` (class) — When no agent is running, messages spawn a background task normally.
- L404 `test_stop_when_no_session_active(self)` (method) — /stop without an active session spawns a background task
- L425 `TestPendingCommandSafetyNet` (class) — The safety net in gateway/run.py _run_agent must discard command text
- L429 `test_stop_command_detected(self)` (method) — resolve_command must recognize /stop so the safety net can
- L437 `test_new_command_detected(self)` (method)
- L443 `test_reset_alias_detected(self)` (method)
- L449 `test_unknown_command_not_detected(self)` (method)
- L454 `test_file_path_not_detected_as_command(self)` (method) — '/path/to/file' should not resolve as a command.
- L468 `TestBypassWithBotnameSuffix` (class) — Telegram appends @botname to commands. The bypass must still work.
- L472 `test_stop_with_botname(self)` (method) — /stop@MyHermesBot must bypass the guard.
- L486 `test_new_with_botname(self)` (method) — /new@MyHermesBot must bypass the guard.
