---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_providers_xai.py

Symbols in `tests/tools/test_web_providers_xai.py`.

- L19 `_creds(api_key: str='xai-test-key', base_url: str='https://api.x.ai/v1')` (function)
- L23 `_mock_resp(json_data, status_code: int=200)` (function)
- L31 `_responses_payload(text: str, annotations=None, citations=None)` (function) — Build a minimal Responses-API reply with one message + output_text block.
- L54 `TestXAIProviderIdentity` (class)
- L55 `test_provider_name(self)` (method)
- L59 `test_implements_web_search_provider(self)` (method)
- L64 `test_supports_search_only(self)` (method)
- L70 `test_display_name(self)` (method)
- L75 `TestXAIProviderIsAvailable` (class) — ``is_available()`` MUST be cheap — no network, no token refresh, no
- L82 `test_available_via_env_var(self, monkeypatch)` (method)
- L87 `test_available_via_auth_store(self, monkeypatch, tmp_path)` (method) — Cheap probe should detect xai-oauth tokens in ~/.hermes/auth.json
- L103 `test_unavailable_when_no_env_and_no_auth_store(self, monkeypatch, tmp_path)` (method)
- L110 `test_unavailable_when_auth_store_has_empty_token(self, monkeypatch, tmp_path)` (method)
- L122 `test_unavailable_when_auth_store_corrupted(self, monkeypatch, tmp_path)` (method) — A malformed auth.json must not crash availability scans.
- L131 `test_is_available_does_not_call_resolver(self, monkeypatch)` (method) — Regression guard: ``is_available()`` must NEVER touch the resolver,
- L149 `TestXAIProviderSearchJSONPath` (class)
- L158 `test_happy_path_normalizes_results(self)` (method)
- L177 `test_limit_truncates_json_results(self)` (method)
- L188 `test_parses_json_with_leading_prose(self)` (method) — Reasoning models sometimes narrate before the JSON block; we tolerate it.
- L201 `test_drops_rows_without_url(self)` (method)
- L222 `TestXAIProviderSearchFallbacks` (class)
- L223 `test_falls_back_to_annotations_when_json_missing(self)` (method) — If Grok ignores the JSON instruction, derive results from url_citation annotations.
- L255 `test_falls_back_to_citations_list(self)` (method) — If no JSON and no annotations, derive from top-level citations list.
- L269 `test_annotations_without_url_citations_fall_through_to_citations(self)` (method) — When annotations exist but none are url_citation type (e.g. future
- L297 `test_empty_response_returns_empty_success(self)` (method)
- L315 `TestXAIProviderRequestShape` (class)
- L316 `test_posts_to_responses_endpoint_with_bearer_token(self)` (method)
- L344 `test_honors_configured_model(self)` (method)
- L360 `test_allowed_domains_passes_through_as_filters(self)` (method)
- L381 `test_excluded_domains_passes_through_as_filters(self)` (method)
- L402 `test_allowed_domains_capped_at_five(self)` (method) — xAI caps domain filters at 5; we trim silently to avoid 400s.
- L427 `TestXAIProviderSearchErrors` (class)
- L428 `test_missing_creds_returns_failure(self)` (method)
- L437 `test_mutually_exclusive_domain_filters_rejected_locally(self)` (method)
- L450 `test_http_error_returns_failure(self)` (method)
- L467 `test_request_error_returns_failure(self)` (method)
- L479 `test_bad_json_response_returns_failure(self)` (method)
- L495 `test_401_on_oauth_path_triggers_force_refresh_and_retry(self)` (method) — OAuth credentials → 401 must force-refresh and retry once.
- L541 `test_401_on_env_var_path_does_not_retry(self)` (method) — Env-var (XAI_API_KEY) creds can't be refreshed — must not retry.
- L573 `test_401_retry_gives_up_when_refresh_returns_same_token(self)` (method) — If the force-refresh returns the same token (refresh-token also
- L610 `test_non_401_http_error_is_not_retried(self)` (method) — Only 401 is retryable — 429 / 500 / 503 must fail fast so the
- L642 `test_http_200_with_error_envelope_surfaces_failure(self)` (method) — xAI sometimes returns 200 with ``{"error": {...}}`` (model
- L664 `TestXAIBackendWiring` (class)
- L665 `test_is_backend_available_true_via_env_var(self, monkeypatch)` (method)
- L671 `test_is_backend_available_false_when_no_creds(self, monkeypatch, tmp_path)` (method)
- L678 `test_is_backend_available_does_not_call_resolver(self, monkeypatch)` (method) — Regression guard — `_is_backend_available` runs on every web_search
- L691 `test_configured_backend_xai_accepted(self, monkeypatch)` (method)
- L696 `test_xai_not_in_legacy_backend_candidate_chain(self, monkeypatch)` (method) — The hardcoded ``backend_candidates`` tuple in ``_get_backend()``
- L728 `TestXAIProviderOAuthPath` (class) — Verifies the provider works when credentials come from the OAuth
- L736 `test_search_uses_oauth_bearer_token_and_base_url(self, monkeypatch)` (method)
