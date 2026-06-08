---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_slack_approval_buttons.py

Symbols in `tests/gateway/test_slack_approval_buttons.py`.

- L21 `_ensure_slack_mock()` (function) — Wire up the minimal mocks required to import SlackAdapter.
- L49 `_make_adapter()` (function) — Create a SlackAdapter instance with mocked internals.
- L61 `_AuthRunner` (class)
- L62 `__init__(self, auth_fn=None)` (method)
- L66 `handle(self, event)` (method)
- L69 `_is_user_authorized(self, source)` (method)
- L74 `_attach_auth_runner(adapter, auth_fn=None)` (function)
- L84 `TestSlackExecApproval` (class) — Test the send_exec_approval method sends Block Kit buttons.
- L88 `test_sends_blocks_with_buttons(self)` (method)
- L125 `test_sends_in_thread(self)` (method)
- L141 `test_not_connected(self)` (method)
- L150 `test_truncates_long_command(self)` (method)
- L170 `TestSlackApprovalAction` (class) — Test the approval button click handler.
- L174 `test_resolves_approval(self)` (method)
- L211 `test_prevents_double_click(self)` (method)
- L235 `test_deny_action(self)` (method)
- L261 `test_global_allowlist_blocks_unauthorized_click(self, monkeypatch)` (method)
- L287 `TestSlackInteractiveAuth` (class)
- L288 `test_delegates_to_gateway_runner_auth(self)` (method)
- L309 `TestSlackSlashConfirmAction` (class)
- L311 `test_global_allowlist_allows_authorized_click(self, monkeypatch)` (method)
- L354 `TestSlackThreadContext` (class) — Test thread context fetching.
- L358 `test_fetches_and_formats_context(self)` (method)
- L388 `test_skips_bot_messages(self)` (method) — Self-bot child replies are skipped to avoid circular context,
- L429 `test_empty_thread(self)` (method)
- L440 `test_api_failure_returns_empty(self)` (method)
- L451 `test_fetch_thread_context_includes_bot_parent(self)` (method) — The thread parent posted by a bot (e.g. a cron summary) must be
- L483 `test_fetch_thread_context_excludes_self_bot_replies(self)` (method) — Parent (non-self bot) is kept, self-bot child replies are dropped,
- L517 `test_fetch_thread_context_multi_workspace(self)` (method) — Self-bot filtering must use the per-workspace bot user id so a
- L563 `test_fetch_thread_context_current_ts_excluded(self)` (method) — Regression guard: the message whose ts == current_ts must never
- L585 `test_fetch_thread_parent_text_from_cache(self)` (method) — _fetch_thread_parent_text should reuse the thread-context cache
- L615 `TestSessionKeyFix` (class) — Test that _has_active_session_for_thread uses build_session_key.
- L618 `test_uses_build_session_key(self)` (method) — Verify the fix uses build_session_key instead of manual key construction.
- L643 `test_no_session_returns_false(self)` (method)
- L658 `test_no_session_store(self)` (method)
- L671 `TestThreadEngagement` (class) — Test _bot_message_ts and _mentioned_threads tracking.
- L675 `test_send_tracks_bot_message_ts(self)` (method) — Bot's sent messages are tracked so thread replies work without @mention.
- L688 `test_bot_message_ts_cap(self)` (method) — Verify memory is bounded when many messages are sent.
- L700 `test_mentioned_threads_populated_on_mention(self)` (method) — When bot is @mentioned in a thread, that thread is tracked.
- L707 `test_mentioned_threads_cap(self)` (method) — Verify _mentioned_threads is bounded.
