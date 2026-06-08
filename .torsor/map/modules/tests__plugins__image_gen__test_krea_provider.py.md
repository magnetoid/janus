---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/image_gen/test_krea_provider.py

Symbols in `tests/plugins/image_gen/test_krea_provider.py`.

- L18 `_fake_api_key(monkeypatch)` (function) — Ensure KREA_API_KEY is set for all tests.
- L23 `_completed_job(url: str='https://krea.cdn/img.png')` (function)
- L33 `_submit_response(job_id: str='00000000-0000-0000-0000-000000000abc')` (function)
- L47 `_poll_response(body: dict)` (function)
- L60 `TestKreaImageGenProvider` (class)
- L61 `test_name(self)` (method)
- L66 `test_display_name(self)` (method)
- L71 `test_is_available_with_key(self, monkeypatch)` (method)
- L77 `test_is_available_without_key(self, monkeypatch)` (method)
- L83 `test_list_models(self)` (method)
- L96 `test_default_model_is_medium(self)` (method)
- L101 `test_get_setup_schema(self)` (method)
- L118 `TestModelResolution` (class)
- L119 `test_default(self)` (method)
- L126 `test_env_override_large(self, monkeypatch)` (method)
- L134 `test_env_override_unknown_falls_back_to_default(self, monkeypatch)` (method)
- L141 `test_creativity_default(self)` (method)
- L146 `test_creativity_valid(self)` (method)
- L152 `test_creativity_invalid(self)` (method)
- L163 `TestGenerate` (class)
- L164 `test_missing_api_key(self, monkeypatch)` (method)
- L173 `test_empty_prompt(self)` (method)
- L180 `test_successful_generation(self)` (method) — Happy path: submit → one poll → completed → URL downloaded.
- L213 `test_large_model_routes_to_large_endpoint(self, monkeypatch)` (method)
- L232 `test_aspect_ratio_mapping(self)` (method) — Hermes 'square' must map to Krea '1:1' in the wire payload.
- L252 `test_auth_header(self)` (method)
- L271 `test_passthrough_seed_styles_moodboards(self)` (method)
- L300 `test_unknown_kwargs_ignored(self)` (method) — Forward-compat: unknown kwargs must not break generate().
- L328 `TestGenerateErrors` (class)
- L329 `test_submit_http_error(self)` (method)
- L349 `test_submit_timeout(self)` (method)
- L361 `test_submit_connection_error(self)` (method)
- L374 `test_submit_missing_job_id(self)` (method)
- L389 `test_job_failed(self)` (method)
- L412 `test_job_cancelled(self)` (method)
- L433 `test_completed_but_missing_urls(self)` (method)
- L454 `test_url_download_failure_falls_back_to_bare_url(self)` (method) — Mirror of xAI behaviour — if local cache fails, return the URL.
- L475 `test_polling_picks_up_completed_at_with_unknown_status(self)` (method) — ``completed_at`` set + unrecognised pending status → still terminal.
- L504 `TestPollRetryPolicy` (class) — Polling fail-fast on permanent 4xx, retry on transient 5xx/429.
- L507 `_http_error_response(self, status: int)` (method)
- L519 `test_poll_fails_fast_on_401(self)` (method) — Auth failure mid-poll should not wait the 180s deadline.
- L536 `test_poll_fails_fast_on_404(self)` (method) — Missing job (404) should surface immediately, not retry for 180s.
- L552 `test_poll_fails_fast_on_403(self)` (method) — Billing/permission failure (403) should not retry.
- L566 `test_poll_retries_on_503_then_succeeds(self)` (method) — Transient 5xx should retry and eventually surface a completion.
- L588 `test_poll_retries_on_429(self)` (method) — Rate-limit (429) is in the retryable set.
- L616 `TestRegistration` (class)
- L617 `test_register(self)` (method)
