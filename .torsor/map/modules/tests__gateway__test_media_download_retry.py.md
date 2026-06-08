---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_media_download_retry.py

Symbols in `tests/gateway/test_media_download_retry.py`.

- L25 `_make_http_status_error(status_code: int)` (function)
- L33 `_make_timeout_error()` (function)
- L42 `TestCacheImageFromBytes` (class) — Tests for gateway.platforms.base.cache_image_from_bytes
- L45 `test_caches_valid_jpeg(self, tmp_path, monkeypatch)` (method)
- L51 `test_caches_valid_png(self, tmp_path, monkeypatch)` (method)
- L57 `test_rejects_html_content(self, tmp_path, monkeypatch)` (method)
- L63 `test_rejects_empty_data(self, tmp_path, monkeypatch)` (method)
- L69 `test_rejects_plain_text(self, tmp_path, monkeypatch)` (method)
- L81 `TestCacheImageFromUrl` (class) — Tests for gateway.platforms.base.cache_image_from_url
- L84 `test_success_on_first_attempt(self, _mock_safe, tmp_path, monkeypatch)` (method) — A clean 200 response caches the image and returns a path.
- L108 `test_retries_on_timeout_then_succeeds(self, _mock_safe, tmp_path, monkeypatch)` (method) — A timeout on the first attempt is retried; second attempt succeeds.
- L138 `test_retries_on_429_then_succeeds(self, _mock_safe, tmp_path, monkeypatch)` (method) — A 429 response on the first attempt is retried; second attempt succeeds.
- L165 `test_raises_after_max_retries_exhausted(self, _mock_safe, tmp_path, monkeypatch)` (method) — Timeout on every attempt raises after all retries are consumed.
- L188 `test_non_retryable_4xx_raises_immediately(self, _mock_safe, tmp_path, monkeypatch)` (method) — A 404 (non-retryable) is raised immediately without any retry.
- L219 `TestCacheAudioFromUrl` (class) — Tests for gateway.platforms.base.cache_audio_from_url
- L222 `test_success_on_first_attempt(self, _mock_safe, tmp_path, monkeypatch)` (method) — A clean 200 response caches the audio and returns a path.
- L246 `test_retries_on_timeout_then_succeeds(self, _mock_safe, tmp_path, monkeypatch)` (method) — A timeout on the first attempt is retried; second attempt succeeds.
- L276 `test_retries_on_429_then_succeeds(self, _mock_safe, tmp_path, monkeypatch)` (method) — A 429 response on the first attempt is retried; second attempt succeeds.
- L303 `test_retries_on_500_then_succeeds(self, _mock_safe, tmp_path, monkeypatch)` (method) — A 500 response on the first attempt is retried; second attempt succeeds.
- L330 `test_raises_after_max_retries_exhausted(self, _mock_safe, tmp_path, monkeypatch)` (method) — Timeout on every attempt raises after all retries are consumed.
- L353 `test_non_retryable_4xx_raises_immediately(self, _mock_safe, tmp_path, monkeypatch)` (method) — A 404 (non-retryable) is raised immediately without any retry.
- L384 `TestSSRFRedirectGuard` (class) — cache_image_from_url / cache_audio_from_url must reject redirects
- L388 `_make_redirect_response(self, target_url: str)` (method) — Build a mock httpx response that looks like a redirect.
- L395 `_make_client_capturing_hooks(self)` (method) — Return (mock_client, captured_kwargs dict) where captured_kwargs
- L409 `test_image_blocks_private_redirect(self, tmp_path, monkeypatch)` (method) — cache_image_from_url rejects a redirect to a private IP.
- L439 `test_audio_blocks_private_redirect(self, tmp_path, monkeypatch)` (method) — cache_audio_from_url rejects a redirect to a private IP.
- L468 `test_safe_redirect_allowed(self, tmp_path, monkeypatch)` (method) — A redirect to a public IP is allowed through.
- L511 `_ensure_slack_mock()` (function)
- L542 `_make_slack_adapter()` (function)
- L556 `TestSlackAttachmentDiagnostics` (class)
- L557 `test_missing_scope_error_returns_actionable_notice(self)` (method) — _describe_slack_api_error translates a missing_scope response into
- L577 `test_download_failure_403_returns_permission_notice(self)` (method)
- L589 `TestSlackDownloadSlackFile` (class) — Tests for SlackAdapter._download_slack_file
- L592 `test_success_on_first_attempt(self, tmp_path, monkeypatch)` (method) — Successful download on first try returns a cached file path.
- L617 `test_rejects_html_response(self, tmp_path, monkeypatch)` (method) — An HTML sign-in page from Slack is rejected, not cached as image.
- L646 `test_retries_on_timeout_then_succeeds(self, tmp_path, monkeypatch)` (method) — Timeout on first attempt triggers retry; success on second.
- L677 `test_raises_after_max_retries(self, tmp_path, monkeypatch)` (method) — Timeout on every attempt eventually raises after 3 total tries.
- L699 `test_non_retryable_403_raises_immediately(self, tmp_path, monkeypatch)` (method) — A 403 is not retried; it raises immediately.
- L728 `TestSlackDownloadSlackFileBytes` (class) — Tests for SlackAdapter._download_slack_file_bytes
- L731 `test_success_returns_bytes(self)` (method) — Successful download returns raw bytes.
- L754 `test_rejects_html_response(self)` (method) — Slack HTML sign-in pages should not be accepted as file bytes.
- L777 `test_retries_on_429_then_succeeds(self)` (method) — 429 on first attempt is retried; raw bytes returned on second.
- L804 `test_raises_after_max_retries(self)` (method) — Persistent timeouts raise after all 3 attempts are exhausted.
- L830 `_make_mm_adapter()` (function) — Build a minimal MattermostAdapter with mocked internals.
- L845 `_make_aiohttp_resp(status: int, content: bytes=b'file bytes', content_type: str='image/jpeg')` (function) — Build a context-manager mock for an aiohttp response.
- L858 `TestMattermostSendUrlAsFile` (class) — Tests for MattermostAdapter._send_url_as_file
- L861 `test_success_on_first_attempt(self, _mock_safe)` (method) — 200 on first attempt → file uploaded and post created.
- L878 `test_retries_on_429_then_succeeds(self, _mock_safe)` (method) — 429 on first attempt is retried; 200 on second attempt succeeds.
- L899 `test_retries_on_500_then_succeeds(self, _mock_safe)` (method) — 5xx on first attempt is retried; 200 on second attempt succeeds.
- L917 `test_falls_back_to_text_after_max_retries_on_5xx(self, _mock_safe)` (method) — Three consecutive 500s exhaust retries; falls back to send() with URL text.
- L936 `test_falls_back_on_client_error(self, _mock_safe)` (method) — aiohttp.ClientError on every attempt falls back to send() with URL.
- L961 `test_non_retryable_404_falls_back_immediately(self, _mock_safe)` (method) — 404 is non-retryable (< 500, != 429); send() is called right away.
