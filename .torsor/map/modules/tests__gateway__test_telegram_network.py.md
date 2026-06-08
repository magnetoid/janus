---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_network.py

Symbols in `tests/gateway/test_telegram_network.py`.

- L28 `FakeTransport` (class) — Records calls and raises / returns based on a host→action mapping.
- L31 `__init__(self, calls, behavior)` (method)
- L36 `handle_async_request(self, request: httpx.Request)` (method)
- L54 `aclose(self)` (method)
- L58 `_fake_transport_factory(calls, behavior)` (function) — Returns a factory that creates FakeTransport instances.
- L71 `_telegram_request(path='/botTOKEN/getMe')` (function)
- L79 `TestParseFallbackIpEnv` (class)
- L80 `test_filters_invalid_and_ipv6(self, caplog)` (method)
- L86 `test_none_returns_empty(self)` (method)
- L89 `test_empty_string_returns_empty(self)` (method)
- L92 `test_whitespace_only_returns_empty(self)` (method)
- L95 `test_single_valid_ip(self)` (method)
- L98 `test_multiple_valid_ips(self)` (method)
- L102 `test_rejects_leading_zeros(self, caplog)` (method) — Leading zeros are ambiguous (octal?) so ipaddress rejects them.
- L109 `TestNormalizeFallbackIps` (class)
- L110 `test_deduplication_happens_at_transport_level(self)` (method) — _normalize does not dedup; TelegramFallbackTransport.__init__ does.
- L115 `test_empty_strings_skipped(self)` (method)
- L123 `TestRewriteRequestForIp` (class)
- L124 `test_preserves_host_and_sni(self)` (method)
- L133 `test_preserves_method_and_path(self)` (method)
- L145 `TestFallbackTransport` (class) — Primary path fails → try fallback IPs → stick to whichever works.
- L149 `test_falls_back_on_connect_timeout_and_becomes_sticky(self, monkeypatch)` (method)
- L172 `test_falls_back_on_connect_error(self, monkeypatch)` (method)
- L184 `test_does_not_fallback_on_non_connect_error(self, monkeypatch)` (method) — Errors like ReadTimeout are not connection issues — don't retry.
- L198 `test_all_ips_fail_raises_last_error(self, monkeypatch)` (method)
- L212 `test_multiple_fallback_ips_tried_in_order(self, monkeypatch)` (method)
- L233 `test_sticky_ip_tried_first_but_falls_through_if_stale(self, monkeypatch)` (method) — If the sticky IP stops working, the transport retries others.
- L262 `TestFallbackTransportPassthrough` (class) — Requests that don't need fallback behavior.
- L266 `test_non_telegram_host_bypasses_fallback(self, monkeypatch)` (method)
- L280 `test_empty_fallback_list_uses_primary_only(self, monkeypatch)` (method)
- L292 `test_primary_succeeds_no_fallback_needed(self, monkeypatch)` (method)
- L305 `TestFallbackTransportInit` (class)
- L306 `test_deduplicates_fallback_ips(self, monkeypatch)` (method)
- L313 `test_filters_invalid_ips_at_init(self, monkeypatch)` (method)
- L320 `test_uses_proxy_env_for_primary_and_fallback_transports(self, monkeypatch)` (method)
- L338 `test_no_proxy_bypasses_fallback_ip_cidr(self, monkeypatch)` (method)
- L358 `TestFallbackTransportClose` (class)
- L360 `test_aclose_closes_all_transports(self, monkeypatch)` (method)
- L376 `TestConfigFallbackIps` (class)
- L377 `test_env_var_populates_config_extra(self, monkeypatch)` (method)
- L388 `test_env_var_creates_platform_if_missing(self, monkeypatch)` (method)
- L398 `test_env_var_strips_whitespace(self, monkeypatch)` (method)
- L409 `test_empty_env_var_does_not_populate(self, monkeypatch)` (method)
- L423 `TestAdapterFallbackIps` (class)
- L424 `_make_adapter(self, extra=None)` (method)
- L448 `test_list_in_extra(self)` (method)
- L452 `test_csv_string_in_extra(self)` (method)
- L456 `test_empty_extra(self)` (method)
- L460 `test_no_extra_attr(self)` (method)
- L465 `test_invalid_ips_filtered(self)` (method)
- L474 `_doh_answer(*ips: str)` (function) — Build a minimal DoH JSON response with A records.
- L479 `FakeDoHClient` (class) — Mock httpx.AsyncClient for DoH queries.
- L482 `__init__(self, responses: dict)` (method)
- L488 `_make_response(status, body, url)` (method) — Build an httpx.Response with a request attached (needed for raise_for_status).
- L493 `get(self, url, *, params=None, headers=None, **kwargs)` (method)
- L503 `__aenter__(self)` (method)
- L506 `__aexit__(self, *args)` (method)
- L510 `TestDiscoverFallbackIps` (class) — Tests for discover_fallback_ips() — DoH-based auto-discovery.
- L513 `_patch_doh(self, monkeypatch, responses, system_dns_ips=None)` (method) — Wire up fake DoH client and system DNS.
- L528 `test_google_and_cloudflare_ips_collected(self, monkeypatch)` (method)
- L539 `test_system_dns_ip_kept_when_doh_confirms(self, monkeypatch)` (method) — DoH-confirmed IPs are kept even when they match system DNS (#14520).
- L555 `test_doh_results_deduplicated(self, monkeypatch)` (method)
- L565 `test_doh_timeout_falls_back_to_seed(self, monkeypatch)` (method)
- L575 `test_doh_connect_error_falls_back_to_seed(self, monkeypatch)` (method)
- L585 `test_doh_malformed_json_falls_back_to_seed(self, monkeypatch)` (method)
- L595 `test_one_provider_fails_other_succeeds(self, monkeypatch)` (method)
- L605 `test_system_dns_failure_keeps_all_doh_ips(self, monkeypatch)` (method) — If system DNS fails, nothing gets excluded — all DoH IPs kept.
- L617 `test_all_doh_ips_same_as_system_dns_kept(self, monkeypatch)` (method) — DoH agrees with system DNS — keep that IP instead of seed list (#14520).
- L634 `test_cloudflare_gets_accept_header(self, monkeypatch)` (method)
- L647 `test_non_a_records_ignored(self, monkeypatch)` (method) — AAAA records (type 28) and CNAME (type 5) should be skipped.
- L665 `test_invalid_ip_in_doh_response_skipped(self, monkeypatch)` (method)
