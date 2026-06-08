---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_platform_reconnect.py

Symbols in `tests/gateway/test_platform_reconnect.py`.

- L14 `StubAdapter` (class) — Adapter whose connect() result can be controlled.
- L17 `__init__(self, *, platform=Platform.TELEGRAM, succeed=True, fatal_error=None, fatal_retryable=True)` (method)
- L30 `connect(self)` (method)
- L36 `disconnect(self)` (method)
- L39 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L42 `send_typing(self, chat_id, metadata=None)` (method)
- L45 `get_chat_info(self, chat_id)` (method)
- L49 `_make_runner()` (function) — Create a minimal GatewayRunner via object.__new__ to skip __init__.
- L75 `TestStartupPlatformIsolation` (class) — Verify one blocked platform cannot prevent later platforms from starting.
- L79 `test_start_continues_after_platform_connect_timeout(self, tmp_path)` (method) — A timeout on Telegram should queue it and still connect Feishu.
- L138 `test_connect_adapter_timeout_raises_retryable_exception(self, monkeypatch)` (method) — The timeout helper turns a hanging connect into a caught startup error.
- L154 `TestStartupFailureQueuing` (class) — Verify that failed platforms are queued during startup.
- L157 `test_failed_platform_queued_on_connect_failure(self)` (method) — When adapter.connect() returns False without fatal error, queue for retry.
- L169 `test_failed_platform_not_queued_for_nonretryable(self)` (method) — Non-retryable errors should not be in the retry queue.
- L178 `TestPlatformReconnectWatcher` (class) — Test the _platform_reconnect_watcher background task.
- L182 `test_reconnect_succeeds_on_retry(self)` (method) — Watcher should reconnect a failed platform when connect() succeeds.
- L221 `test_reconnect_retries_resume_pending_for_platform(self)` (method) — A successful reconnect retries the startup auto-resume scoped to
- L269 `test_reconnect_nonretryable_removed_from_queue(self)` (method) — Non-retryable errors should remove the platform from the retry queue.
- L307 `test_reconnect_retryable_stays_in_queue(self)` (method) — Retryable failures should remain in the queue with incremented attempts.
- L345 `test_reconnect_never_auto_pauses_retryable_failures(self)` (method) — Retryable failures (network/DNS) must keep retrying indefinitely —
- L395 `test_reconnect_skips_paused_platforms(self)` (method) — A paused platform should not be retried by the watcher tick.
- L433 `test_reconnect_skips_when_not_time_yet(self)` (method) — Watcher should skip platforms whose next_retry is in the future.
- L467 `test_no_failed_platforms_watcher_idles(self)` (method) — When no platforms are failed, watcher should just idle.
- L494 `test_adapter_create_returns_none(self)` (method) — If _create_adapter returns None, remove from queue (missing deps).
- L529 `TestRuntimeDisconnectQueuing` (class) — Test that _handle_adapter_fatal_error queues retryable disconnections.
- L533 `test_retryable_runtime_error_queued_for_reconnect(self)` (method) — Retryable runtime errors should add the platform to _failed_platforms.
- L548 `test_nonretryable_runtime_error_not_queued(self)` (method) — Non-retryable runtime errors should not be queued for reconnection.
- L564 `test_retryable_error_keeps_gateway_alive_when_all_down(self)` (method) — When all adapters fail at runtime with retryable errors, the
- L586 `test_retryable_error_no_exit_when_other_adapters_still_connected(self)` (method) — Gateway should NOT exit if some adapters are still connected.
- L606 `test_nonretryable_error_triggers_shutdown(self)` (method) — Gateway should shut down when no adapters remain and nothing is queued.
- L623 `TestPauseResume` (class) — Test the per-platform pause/resume helpers and slash command.
- L626 `test_pause_marks_platform_paused(self)` (method)
- L639 `test_pause_is_idempotent(self)` (method)
- L655 `test_pause_no_op_when_platform_not_queued(self)` (method)
- L661 `test_resume_clears_paused_and_resets_attempts(self)` (method)
- L677 `test_resume_returns_false_when_not_paused(self)` (method)
- L686 `test_resume_returns_false_when_not_queued(self)` (method)
- L691 `TestPlatformSlashCommand` (class) — Test the /platform list|pause|resume slash command handler.
- L694 `_make_event(self, content: str)` (method)
- L700 `test_list_shows_connected_and_paused(self)` (method)
- L717 `test_pause_command_pauses_queued_platform(self)` (method)
- L731 `test_pause_rejects_unqueued_platform(self)` (method)
- L739 `test_resume_command_resumes_paused_platform(self)` (method)
- L755 `test_unknown_platform_name(self)` (method)
- L763 `test_bare_platform_shows_usage_with_list(self)` (method)
