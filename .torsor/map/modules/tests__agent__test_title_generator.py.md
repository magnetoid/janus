---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_title_generator.py

Symbols in `tests/agent/test_title_generator.py`.

- L13 `TestGenerateTitle` (class) — Unit tests for generate_title().
- L16 `test_returns_title_on_success(self)` (method)
- L25 `test_strips_quotes(self)` (method)
- L34 `test_strips_title_prefix(self)` (method)
- L43 `test_truncates_long_titles(self)` (method)
- L53 `test_returns_none_on_empty_response(self)` (method)
- L61 `test_returns_none_on_exception(self)` (method)
- L65 `test_invokes_failure_callback_on_exception(self)` (method) — failure_callback must fire so the user sees a warning (issue #15775).
- L81 `test_failure_callback_errors_are_swallowed(self)` (method) — A broken callback must not crash title generation.
- L91 `test_no_callback_matches_legacy_behavior(self)` (method) — Omitting failure_callback preserves the silent-None return.
- L96 `test_truncates_long_messages(self)` (method) — Long user/assistant messages should be truncated in the LLM request.
- L115 `TestAutoTitleSession` (class) — Tests for auto_title_session() — the sync worker function.
- L118 `test_skips_if_no_session_db(self)` (method)
- L121 `test_skips_if_title_exists(self)` (method)
- L129 `test_generates_and_sets_title(self)` (method)
- L137 `test_invokes_title_callback_after_setting_title(self)` (method)
- L152 `test_skips_if_generation_fails(self)` (method)
- L161 `TestMaybeAutoTitle` (class) — Tests for maybe_auto_title() — the fire-and-forget entry point.
- L164 `test_skips_if_not_first_exchange(self)` (method) — Should not fire for conversations with more than 2 user messages.
- L183 `test_fires_on_first_exchange(self)` (method) — Should fire a background thread for the first exchange.
- L207 `test_forwards_failure_callback_to_worker(self)` (method) — maybe_auto_title must forward failure_callback into the thread.
- L233 `test_skips_if_no_response(self)` (method)
- L237 `test_skips_if_no_session_db(self)` (method)
