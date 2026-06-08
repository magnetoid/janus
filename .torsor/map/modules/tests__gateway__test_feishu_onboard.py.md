---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_onboard.py

Symbols in `tests/gateway/test_feishu_onboard.py`.

- L8 `_mock_urlopen(response_data, status=200)` (function) — Create a mock for urllib.request.urlopen that returns JSON response_data.
- L18 `TestPostRegistration` (class) — Tests for the low-level HTTP helper.
- L22 `test_post_registration_returns_parsed_json(self, mock_urlopen_fn)` (method)
- L31 `test_post_registration_sends_form_encoded_body(self, mock_urlopen_fn)` (method)
- L44 `TestInitRegistration` (class) — Tests for the init step.
- L48 `test_init_succeeds_when_client_secret_supported(self, mock_urlopen_fn)` (method)
- L58 `test_init_raises_when_client_secret_not_supported(self, mock_urlopen_fn)` (method)
- L69 `test_init_uses_lark_url_for_lark_domain(self, mock_urlopen_fn)` (method)
- L82 `TestBeginRegistration` (class) — Tests for the begin step.
- L86 `test_begin_returns_device_code_and_qr_url(self, mock_urlopen_fn)` (method)
- L105 `test_begin_sends_correct_archetype(self, mock_urlopen_fn)` (method)
- L122 `TestPollRegistration` (class) — Tests for the poll step.
- L127 `test_poll_returns_credentials_on_success(self, mock_urlopen_fn, mock_time)` (method)
- L149 `test_poll_switches_domain_on_lark_tenant_brand(self, mock_urlopen_fn, mock_time)` (method)
- L174 `test_poll_success_with_lark_brand_in_same_response(self, mock_urlopen_fn, mock_time)` (method) — Credentials and lark tenant_brand in one response must not be discarded.
- L196 `test_poll_returns_none_on_access_denied(self, mock_urlopen_fn, mock_time)` (method)
- L212 `test_poll_returns_none_on_timeout(self, mock_urlopen_fn, mock_time)` (method)
- L228 `test_poll_timeout_uses_monotonic_clock(self, mock_urlopen_fn, mock_time)` (method)
- L246 `TestRenderQr` (class) — Tests for QR code terminal rendering.
- L250 `test_render_qr_returns_true_on_success(self, mock_qrcode_mod)` (method)
- L260 `test_render_qr_returns_false_when_qrcode_missing(self)` (method)
- L267 `TestProbeBot` (class) — Tests for bot connectivity verification.
- L271 `test_probe_returns_bot_info_on_success(self)` (method)
- L283 `test_probe_returns_none_on_failure(self)` (method)
- L294 `test_http_fallback_when_sdk_unavailable(self, mock_urlopen_fn)` (method) — Without lark_oapi, probe falls back to raw HTTP.
- L308 `test_http_fallback_returns_none_on_network_error(self, mock_urlopen_fn)` (method)
- L317 `TestQrRegister` (class) — Tests for the public qr_register entry point.
- L325 `test_qr_register_success_flow(self, mock_init, mock_begin, mock_poll, mock_render, mock_probe)` (method)
- L354 `test_qr_register_returns_none_on_init_failure(self, mock_init)` (method)
- L365 `test_qr_register_returns_none_on_poll_failure(self, mock_init, mock_begin, mock_poll, mock_render)` (method)
- L385 `test_qr_register_returns_none_on_network_error(self, mock_init)` (method) — URLError (network down) is an expected failure → None.
- L395 `test_qr_register_returns_none_on_json_error(self, mock_init)` (method) — Malformed server response is an expected failure → None.
- L404 `test_qr_register_propagates_unexpected_errors(self, mock_init)` (method) — Bugs (e.g. AttributeError) must not be swallowed — they propagate.
- L417 `test_qr_register_returns_none_when_begin_missing_device_code(self, mock_init, mock_begin, mock_render)` (method) — Server returns begin response without device_code → RuntimeError → None.
- L432 `test_qr_register_succeeds_even_when_probe_fails(self, mock_init, mock_begin, mock_poll, mock_render, mock_probe)` (method) — Registration succeeds but probe fails → result with bot_name=None.
