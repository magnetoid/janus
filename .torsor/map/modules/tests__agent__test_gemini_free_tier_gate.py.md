---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_gemini_free_tier_gate.py

Symbols in `tests/agent/test_gemini_free_tier_gate.py`.

- L14 `_mock_response(status: int, headers: dict | None=None, text: str='')` (function)
- L22 `_run_probe(resp: MagicMock)` (function)
- L30 `TestProbeGeminiTier` (class) — Verify the tier probe classifies keys correctly.
- L33 `test_free_tier_via_rpd_header_flash(self)` (method)
- L38 `test_free_tier_via_rpd_header_pro(self)` (method)
- L43 `test_free_tier_via_rpd_header_flash_lite(self)` (method)
- L48 `test_paid_tier_via_rpd_header(self)` (method)
- L53 `test_free_tier_via_429_body(self)` (method)
- L62 `test_paid_429_has_no_free_tier_marker(self)` (method)
- L67 `test_successful_200_without_rpd_header_is_paid(self)` (method)
- L71 `test_401_returns_unknown(self)` (method)
- L75 `test_404_returns_unknown(self)` (method)
- L79 `test_network_error_returns_unknown(self)` (method)
- L86 `test_empty_key_returns_unknown(self)` (method)
- L91 `test_malformed_rpd_header_falls_through(self)` (method)
- L96 `test_openai_compat_suffix_stripped(self)` (method) — Base URLs ending in /openai get normalized to the native endpoint.
- L113 `TestIsFreeTierQuotaError` (class)
- L114 `test_detects_free_tier_marker(self)` (method)
- L119 `test_case_insensitive(self)` (method)
- L122 `test_no_free_tier_marker(self)` (method)
- L125 `test_empty_string(self)` (method)
- L128 `test_none(self)` (method)
- L132 `TestGeminiHttpErrorFreeTierGuidance` (class) — gemini_http_error should append free-tier guidance for free-tier 429s.
- L141 `test_free_tier_429_appends_guidance(self)` (method)
- L152 `test_paid_429_has_no_billing_url(self)` (method)
- L157 `test_non_429_has_no_billing_url(self)` (method)
- L162 `test_401_has_no_billing_url(self)` (method)
