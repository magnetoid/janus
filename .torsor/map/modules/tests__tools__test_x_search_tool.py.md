---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_x_search_tool.py

Symbols in `tests/tools/test_x_search_tool.py`.

- L17 `_FakeResponse` (class)
- L18 `__init__(self, payload, *, status_code=200, text=None)` (method)
- L23 `raise_for_status(self)` (method)
- L29 `json(self)` (method)
- L39 `test_x_search_posts_responses_request(monkeypatch)` (function)
- L84 `test_x_search_rejects_conflicting_handle_filters(monkeypatch)` (function)
- L100 `test_x_search_extracts_inline_url_citations(monkeypatch)` (function)
- L146 `test_x_search_returns_structured_http_error(monkeypatch)` (function)
- L176 `test_x_search_retries_read_timeout_then_succeeds(monkeypatch)` (function)
- L203 `test_x_search_retries_5xx_then_succeeds(monkeypatch)` (function)
- L232 `_no_xai_env(monkeypatch)` (function) — Strip any XAI_* env vars so the resolver doesn't see a leaked dev key.
- L238 `test_x_search_uses_xai_oauth_when_only_oauth_available(monkeypatch)` (function) — OAuth-only user: credential_source should be ``xai-oauth``.
- L274 `test_x_search_uses_api_key_when_only_xai_api_key_set(monkeypatch)` (function) — API-key-only user: credential_source should be ``xai``.
- L312 `test_x_search_prefers_oauth_when_both_available(monkeypatch)` (function) — Both credentials present: OAuth wins (matches Teknium's billing preference).
- L353 `test_x_search_returns_tool_error_when_no_credentials(monkeypatch)` (function) — No credentials anywhere: tool returns a clear error, not a 401 from xAI.
- L381 `test_x_search_check_fn_false_when_resolver_raises(monkeypatch)` (function) — Resolver exceptions (e.g. expired token + failed refresh) gate the tool out.
- L399 `test_x_search_honors_config_model_and_timeout(monkeypatch, tmp_path)` (function) — ``x_search.model`` and ``x_search.timeout_seconds`` override the defaults.
- L427 `test_x_search_registered_in_registry_with_check_fn()` (function) — The tool is registered under the x_search toolset with the gating check_fn.
- L448 `_no_post_allowed(monkeypatch)` (function) — Guard: any test that should fail before HTTP can hit this fence.
- L456 `test_x_search_rejects_malformed_from_date(monkeypatch)` (function)
- L467 `test_x_search_rejects_malformed_to_date(monkeypatch)` (function)
- L478 `test_x_search_rejects_inverted_date_range(monkeypatch)` (function)
- L495 `test_x_search_rejects_future_from_date(monkeypatch)` (function) — ``from_date`` in the future can never match any post → reject.
- L516 `test_x_search_allows_future_to_date(monkeypatch)` (function) — ``to_date`` in the future is fine — caller may want posts as they arrive.
- L550 `test_x_search_accepts_today_as_from_date(monkeypatch)` (function) — ``from_date == today UTC`` is a valid edge case (today is past + present).
- L579 `test_x_search_marks_degraded_when_handle_filter_returns_no_citations(monkeypatch)` (function) — allowed_x_handles set + zero citations → degraded=True.
- L600 `test_x_search_marks_degraded_when_excluded_handles_and_no_citations(monkeypatch)` (function)
- L617 `test_x_search_marks_degraded_when_date_range_and_no_citations(monkeypatch)` (function)
- L639 `test_x_search_not_degraded_when_filter_returns_inline_citations(monkeypatch)` (function) — A real citation from the inline annotations clears the degraded flag.
- L682 `test_x_search_not_degraded_when_filter_returns_top_level_citations(monkeypatch)` (function) — A real citation from xAI's top-level ``citations`` array also clears the flag.
- L705 `test_x_search_not_degraded_when_no_filters_active(monkeypatch)` (function) — A broad query that returns no citations isn't necessarily degraded.
