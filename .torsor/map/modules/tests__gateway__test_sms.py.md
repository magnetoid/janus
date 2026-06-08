---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_sms.py

Symbols in `tests/gateway/test_sms.py`.

- L20 `TestSmsConfigLoading` (class) — Verify _apply_env_overrides wires SMS correctly.
- L23 `test_env_overrides_create_sms_config(self)` (method)
- L38 `test_env_overrides_set_home_channel(self)` (method)
- L58 `TestSmsFormatAndTruncate` (class) — Test SmsAdapter.format_message strips markdown.
- L61 `_make_adapter(self)` (method)
- L79 `test_strips_bold(self)` (method)
- L83 `test_strips_italic(self)` (method)
- L87 `test_strips_code_blocks(self)` (method)
- L93 `test_strips_inline_code(self)` (method)
- L97 `test_strips_headers(self)` (method)
- L101 `test_strips_links(self)` (method)
- L105 `test_collapses_newlines(self)` (method)
- L113 `TestSmsEchoPrevention` (class) — Adapter should ignore messages from its own number.
- L116 `test_own_number_detection(self)` (method) — The adapter stores _from_number for echo prevention.
- L133 `TestSmsRequirements` (class)
- L134 `test_check_sms_requirements_missing_sid(self)` (method)
- L141 `test_check_sms_requirements_missing_token(self)` (method)
- L148 `test_check_sms_requirements_both_set(self)` (method)
- L169 `TestWebhookHostConfig` (class) — Verify SMS_WEBHOOK_HOST env var and default.
- L172 `test_default_host_is_localhost(self)` (method)
- L176 `test_host_from_env(self)` (method)
- L190 `test_webhook_url_from_env(self)` (method)
- L204 `test_webhook_url_stripped(self)` (method)
- L221 `TestStartupGuard` (class) — Adapter must refuse to start without SMS_WEBHOOK_URL.
- L224 `_make_adapter(self, extra_env=None)` (method)
- L240 `test_refuses_start_without_webhook_url(self)` (method)
- L246 `test_missing_webhook_url_is_non_retryable(self)` (method)
- L254 `test_missing_phone_number_is_non_retryable(self)` (method)
- L272 `test_insecure_flag_does_not_set_fatal_error(self)` (method)
- L288 `test_insecure_flag_allows_start_without_url(self)` (method)
- L303 `test_webhook_url_allows_start(self)` (method)
- L321 `_compute_twilio_signature(auth_token, url, params)` (function) — Reference implementation of Twilio's signature algorithm.
- L334 `TestTwilioSignatureValidation` (class) — Unit tests for SmsAdapter._validate_twilio_signature.
- L337 `_make_adapter(self, auth_token='test_token_secret')` (method)
- L350 `test_valid_signature_accepted(self)` (method)
- L357 `test_invalid_signature_rejected(self)` (method)
- L363 `test_wrong_token_rejected(self)` (method)
- L370 `test_params_sorted_by_key(self)` (method) — Signature must be computed with params sorted alphabetically.
- L378 `test_empty_param_values_included(self)` (method) — Blank values must be included in signature computation.
- L386 `test_url_matters(self)` (method) — Different URLs produce different signatures.
- L397 `test_port_variant_443_matches_without_port(self)` (method) — Signature for https URL with :443 validates against URL without port.
- L408 `test_port_variant_without_port_matches_443(self)` (method) — Signature for https URL without port validates against URL with :443.
- L419 `test_non_standard_port_no_variant(self)` (method) — Non-standard port must NOT match URL without port.
- L430 `test_port_variant_http_80(self)` (method) — Port variant also works for http with port 80.
- L444 `TestWebhookSignatureEnforcement` (class) — Integration tests for signature validation in _handle_webhook.
- L447 `_make_adapter(self, webhook_url='')` (method)
- L462 `_mock_request(self, body, headers=None)` (method)
- L469 `test_insecure_flag_skips_validation(self)` (method) — With SMS_INSECURE_NO_SIGNATURE=true and no URL, requests are accepted.
- L480 `test_insecure_flag_with_url_still_validates(self)` (method) — When both SMS_WEBHOOK_URL and SMS_INSECURE_NO_SIGNATURE are set,
- L490 `test_missing_signature_returns_403(self)` (method)
- L498 `test_invalid_signature_returns_403(self)` (method)
- L506 `test_valid_signature_returns_200(self)` (method)
- L522 `test_port_variant_signature_returns_200(self)` (method) — Signature computed with :443 should pass when URL configured without port.
