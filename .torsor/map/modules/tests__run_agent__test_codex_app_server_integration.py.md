---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_codex_app_server_integration.py

Symbols in `tests/run_agent/test_codex_app_server_integration.py`.

- L24 `fake_session(monkeypatch)` (function) — Replace CodexAppServerSession with a stub that returns a fixed
- L52 `_make_codex_agent()` (function) — Construct an AIAgent in codex_app_server mode without contacting any
- L67 `TestApiModeAccepted` (class)
- L68 `test_api_mode_is_codex_app_server(self)` (method)
- L73 `TestRunConversationCodexPath` (class)
- L74 `test_run_conversation_returns_codex_shape(self, fake_session)` (method)
- L87 `test_projected_messages_are_spliced(self, fake_session)` (method)
- L101 `test_nudge_counters_tick(self, fake_session)` (method) — The skill nudge counter must accumulate tool_iterations across
- L120 `test_user_message_not_duplicated(self, fake_session)` (method) — Regression guard: the user message must appear exactly once in
- L133 `test_background_review_NOT_invoked_below_threshold(self, fake_session)` (method) — A single turn shouldn't trigger background review — counters
- L148 `test_background_review_skill_trigger_fires_above_threshold(self, monkeypatch)` (method) — When tool iterations cross the skill nudge interval, the
- L195 `test_background_review_signature_never_breaks(self, fake_session)` (method) — Even when no trigger fires, the helper must never call
- L223 `test_chat_completions_loop_is_not_entered(self, fake_session)` (method) — The early-return must bypass the regular API call loop entirely.
- L236 `TestReviewForkApiModeDowngrade` (class) — When the parent agent runs on codex_app_server, the background
- L242 `test_codex_app_server_parent_downgrades_review_fork(self)` (method) — Live test against the real _spawn_background_review code path:
- L307 `TestErrorHandling` (class)
- L308 `test_session_exception_returns_partial_with_error(self, monkeypatch)` (method)
- L324 `test_interrupted_turn_marked_partial(self, monkeypatch)` (method)
- L347 `TestSessionRetirementOnRunAgent` (class) — run_agent.py side: when run_turn returns should_retire=True, the
- L351 `test_should_retire_drops_session(self, monkeypatch)` (method)
- L385 `test_normal_turn_keeps_session(self, fake_session)` (method) — fake_session fixture returns should_retire=False (default).
- L394 `test_exception_path_also_drops_session(self, monkeypatch)` (method) — Even if run_turn raises (not just sets should_retire), we must
