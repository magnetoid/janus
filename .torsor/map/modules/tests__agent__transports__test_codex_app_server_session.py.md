---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_codex_app_server_session.py

Symbols in `tests/agent/transports/test_codex_app_server_session.py`.

- L25 `FakeClient` (class) — Stand-in for CodexAppServerClient that records calls and lets the test
- L29 `__init__(self, *, codex_bin: str='codex', codex_home=None)` (method)
- L43 `initialize(self, **kwargs)` (method)
- L48 `request(self, method: str, params: Optional[dict]=None, timeout: float=30.0)` (method)
- L62 `notify(self, method: str, params=None)` (method)
- L65 `respond(self, request_id, result)` (method)
- L68 `respond_error(self, request_id, code, message, data=None)` (method)
- L71 `take_notification(self, timeout: float=0.0)` (method)
- L80 `take_server_request(self, timeout: float=0.0)` (method)
- L85 `close(self)` (method)
- L88 `is_alive(self)` (method)
- L93 `stderr_tail(self, n: int=20)` (method)
- L97 `queue_notification(self, method: str, **params)` (method)
- L100 `queue_server_request(self, method: str, request_id: Any='srv-1', **params)` (method)
- L103 `set_stderr_tail(self, lines)` (method) — Test helper: seed stderr_tail() output for OAuth-refresh classifier tests.
- L108 `make_session(client: FakeClient, **kwargs)` (function)
- L118 `TestApprovalChoiceMapping` (class)
- L126 `test_mapping(self, choice, expected)` (method)
- L130 `TestTurnInputCoercion` (class)
- L131 `test_list_content_keeps_text_and_marks_images(self)` (method)
- L141 `TestLifecycle` (class)
- L142 `test_ensure_started_is_idempotent(self)` (method)
- L152 `test_thread_start_passes_cwd_only(self)` (method) — thread/start carries cwd. We intentionally do NOT pass `permissions`
- L164 `test_close_idempotent(self)` (method)
- L175 `TestRunTurn` (class)
- L176 `test_simple_text_turn_returns_final_message(self)` (method)
- L199 `test_rich_content_turn_is_collapsed_to_text_payload(self)` (method)
- L228 `test_tool_iteration_counter_ticks(self)` (method)
- L257 `test_turn_start_failure_returns_error(self)` (method)
- L273 `test_turn_start_failure_attaches_redacted_stderr_tail(self)` (method) — When codex stderr has content (non-OAuth), the tail gets attached
- L306 `test_turn_start_timeout_attaches_redacted_stderr_tail(self)` (method) — A non-OAuth TimeoutError on turn/start surfaces with codex stderr
- L329 `test_startup_failure_returns_error_with_stderr(self)` (method) — Codex thread/start failures during ensure_started() used to bubble
- L353 `test_interrupt_during_turn_issues_turn_interrupt(self)` (method)
- L377 `test_deadline_exceeded_records_error(self)` (method)
- L386 `test_deadline_uses_monotonic_clock(self)` (method)
- L403 `test_failed_turn_records_error_from_turn_completed(self)` (method)
- L417 `TestServerRequestRouting` (class)
- L418 `test_exec_approval_with_callback_approves_once(self)` (method)
- L442 `test_exec_approval_no_callback_denies(self)` (method)
- L454 `test_apply_patch_approval_session_maps_to_session_decision(self)` (method)
- L476 `test_unknown_server_request_replied_with_error(self)` (method)
- L490 `test_mcp_elicitation_for_hermes_tools_auto_accepts(self)` (method) — When codex elicits on behalf of hermes-tools (our own callback),
- L511 `test_mcp_elicitation_for_other_servers_declines(self)` (method) — For third-party MCP servers we decline by default so users
- L531 `test_routing_auto_approve_bypass(self)` (method)
- L545 `test_callback_raises_falls_back_to_decline(self)` (method)
- L565 `TestApprovalPromptEnrichment` (class) — Quirk #4: apply_patch prompt should show what's changing.
- L569 `test_exec_falls_back_to_session_cwd(self)` (method) — When codex omits cwd from the approval params, the prompt shows
- L591 `test_apply_patch_prompt_summarizes_pending_changes(self)` (method) — When the projector has cached the fileChange item from item/started,
- L629 `test_apply_patch_prompt_works_without_cached_summary(self)` (method) — When approval arrives before item/started (or without changes
- L655 `TestSessionRetirement` (class) — Mirrors openclaw beta.8's resilience fixes:
- L667 `test_deadline_marks_session_for_retirement(self)` (method)
- L682 `test_completed_turn_does_not_retire(self)` (method)
- L697 `test_post_tool_quiet_watchdog_trips_and_retires(self)` (method)
- L725 `test_post_tool_watchdog_uses_monotonic_clock(self)` (method)
- L754 `test_post_tool_watchdog_resets_on_further_activity(self)` (method) — A tool completion followed by an agent message should NOT trip
- L791 `test_turn_aborted_marker_in_text_is_terminal(self)` (method) — If codex emits `<turn_aborted>` in agent text and never sends
- L817 `test_turn_aborted_self_closing_marker_also_terminal(self)` (method)
- L831 `test_oauth_refresh_failure_on_turn_start_suggests_login(self)` (method)
- L852 `test_oauth_failure_from_stderr_on_turn_start_failure(self)` (method) — If the RPC error itself is opaque but stderr shows an auth
- L876 `test_oauth_failure_in_turn_completed_error(self)` (method) — A failed turn/completed whose error mentions auth/refresh
- L894 `test_generic_turn_failure_does_not_trigger_oauth_hint(self)` (method) — A boring model error must NOT rewrite the message into a fake
- L914 `test_dead_subprocess_detected_between_iterations(self)` (method) — If codex dies (segfault, OOM, killed by its auth refresh
- L936 `TestThreadStartCrossFill` (class) — Mirrors openclaw beta.8's tolerance for thread.id/sessionId aliasing.
- L939 `test_thread_id_under_thread_key(self)` (method)
- L945 `test_thread_session_id_alias_under_thread_key(self)` (method)
- L957 `test_top_level_session_id_fallback(self)` (method)
- L967 `test_missing_thread_id_raises(self)` (method)
- L981 `TestHasTurnAbortedMarker` (class) — Unit coverage for the marker matcher itself.
- L984 `test_empty_string(self)` (method)
- L991 `test_plain_text_no_marker(self)` (method)
- L997 `test_open_marker(self)` (method)
- L1003 `test_self_closing_marker(self)` (method)
- L1010 `TestClassifyOAuthFailure` (class) — Unit coverage for the OAuth classifier; conservative on purpose.
- L1013 `test_invalid_grant_classified(self)` (method)
- L1021 `test_token_refresh_classified(self)` (method)
- L1029 `test_401_classified(self)` (method)
- L1036 `test_generic_error_not_classified(self)` (method)
- L1044 `test_empty_inputs(self)` (method)
- L1052 `test_multi_string_search(self)` (method) — Hint can come from any of the provided strings.
