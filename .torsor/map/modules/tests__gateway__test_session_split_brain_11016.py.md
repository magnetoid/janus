---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_split_brain_11016.py

Symbols in `tests/gateway/test_session_split_brain_11016.py`.

- L39 `_StubAdapter` (class)
- L40 `connect(self)` (method)
- L43 `disconnect(self)` (method)
- L46 `send(self, chat_id, text, **kwargs)` (method)
- L49 `get_chat_info(self, chat_id)` (method)
- L53 `_make_adapter()` (function)
- L66 `_make_event(text='hello', chat_id='12345')` (function)
- L73 `_session_key(chat_id='12345')` (function)
- L85 `_make_runner()` (function)
- L105 `TestAdapterSessionCancellation` (class)
- L108 `test_command_cancels_active_task_and_unblocks_follow_up(self, command_text)` (method) — /stop /new /reset must cancel the adapter task and let follow-ups through.
- L167 `test_new_keeps_guard_until_command_finishes_then_runs_follow_up(self)` (method) — /new must finish runner logic before cancelling old work or releasing the guard.
- L234 `TestStaleSessionLockSelfHeal` (class)
- L236 `test_stale_lock_with_done_task_is_healed_on_next_message(self)` (method) — A split-brain guard (owner task done but entry still live) heals on next inbound.
- L271 `test_no_owner_task_is_not_treated_as_stale(self)` (method) — If _session_tasks has no entry at all, the guard isn't stale.
- L286 `test_live_owner_task_is_not_stale(self)` (method) — When the owner task is alive, do NOT heal — agent is really busy.
- L308 `TestRunnerSessionGenerationGuard` (class)
- L309 `test_release_without_generation_behaves_as_before(self)` (method)
- L318 `test_release_with_current_generation_clears_slot(self)` (method)
- L328 `test_release_with_stale_generation_blocks(self)` (method)
- L345 `test_is_session_run_current_tracks_bumps(self)` (method)
- L364 `TestOldTaskCannotClobberNewerGuard` (class) — Direct regression for the unconditional-delete bug.
- L373 `test_release_session_guard_matches_on_event_identity(self)` (method)
- L392 `test_release_session_guard_without_guard_releases_unconditionally(self)` (method)
