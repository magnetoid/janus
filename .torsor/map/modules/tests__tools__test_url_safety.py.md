---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_url_safety.py

Symbols in `tests/tools/test_url_safety.py`.

- L20 `TestNormalizeUrlForRequest` (class)
- L21 `test_percent_encodes_non_ascii_path(self)` (method)
- L27 `test_preserves_existing_percent_escapes(self)` (method)
- L33 `test_preserves_reserved_query_syntax(self)` (method)
- L39 `test_idna_encodes_hostname(self)` (method)
- L46 `TestIsSafeUrl` (class)
- L47 `test_public_url_allowed(self)` (method)
- L53 `test_ftp_scheme_blocked(self)` (method) — Only http/https should be allowed for fetch tools.
- L57 `test_missing_scheme_blocked(self)` (method) — Bare host/path should be rejected to avoid ambiguous handling.
- L61 `test_localhost_blocked(self)` (method)
- L67 `test_loopback_ip_blocked(self)` (method)
- L73 `test_private_10_blocked(self)` (method)
- L79 `test_private_172_blocked(self)` (method)
- L85 `test_private_192_blocked(self)` (method)
- L91 `test_link_local_169_254_blocked(self)` (method)
- L97 `test_metadata_google_internal_blocked(self)` (method)
- L100 `test_ipv6_loopback_blocked(self)` (method)
- L106 `test_dns_failure_blocked(self)` (method) — DNS failures now fail closed — block the request.
- L111 `test_empty_url_blocked(self)` (method)
- L114 `test_no_hostname_blocked(self)` (method)
- L117 `test_public_ip_allowed(self)` (method)
- L125 `test_cgnat_100_64_blocked(self)` (method) — 100.64.0.0/10 (CGNAT/Shared Address Space) is NOT covered by
- L133 `test_cgnat_100_127_blocked(self)` (method) — Upper end of CGNAT range (100.127.255.255).
- L140 `test_multicast_blocked(self)` (method) — Multicast addresses (224.0.0.0/4) not caught by is_private.
- L147 `test_multicast_ipv6_blocked(self)` (method)
- L153 `test_ipv4_mapped_ipv6_loopback_blocked(self)` (method) — ::ffff:127.0.0.1 — IPv4-mapped IPv6 loopback.
- L160 `test_ipv4_mapped_ipv6_metadata_blocked(self)` (method) — ::ffff:169.254.169.254 — IPv4-mapped IPv6 cloud metadata.
- L167 `test_unspecified_address_blocked(self)` (method) — 0.0.0.0 — unspecified address, can bind to all interfaces.
- L174 `test_unexpected_error_fails_closed(self)` (method) — Unexpected exceptions should block, not allow.
- L179 `test_metadata_goog_blocked(self)` (method)
- L182 `test_ipv6_unique_local_blocked(self)` (method) — fc00::/7 — IPv6 unique local addresses.
- L189 `test_non_cgnat_100_allowed(self)` (method) — 100.0.0.1 is NOT in CGNAT range (100.64.0.0/10), should be allowed.
- L197 `test_benchmark_ip_blocked_for_non_allowlisted_host(self)` (method)
- L203 `test_qq_multimedia_hostname_allowed_with_benchmark_ip(self)` (method)
- L209 `test_qq_multimedia_hostname_exception_is_exact_match(self)` (method)
- L215 `test_qq_multimedia_hostname_exception_requires_https(self)` (method)
- L221 `test_qq_multimedia_hostname_dns_failure_still_blocked(self)` (method)
- L226 `TestAsyncIsSafeUrl` (class) — async_is_safe_url must match is_safe_url (runs DNS in a thread pool).
- L230 `test_public_url_allowed(self)` (method)
- L237 `test_localhost_blocked(self)` (method)
- L244 `TestIsBlockedIp` (class) — Direct tests for the _is_blocked_ip helper.
- L254 `test_blocked_ips(self, ip_str)` (method)
- L262 `test_allowed_ips(self, ip_str)` (method)
- L267 `TestGlobalAllowPrivateUrls` (class) — Tests for the security.allow_private_urls config toggle.
- L271 `_reset_cache(self)` (method) — Reset the module-level toggle cache before and after each test.
- L277 `test_default_is_false(self, monkeypatch)` (method) — Toggle defaults to False when no env var or config is set.
- L283 `test_env_var_true(self, monkeypatch)` (method) — HERMES_ALLOW_PRIVATE_URLS=true enables the toggle.
- L288 `test_env_var_1(self, monkeypatch)` (method) — HERMES_ALLOW_PRIVATE_URLS=1 enables the toggle.
- L293 `test_env_var_yes(self, monkeypatch)` (method) — HERMES_ALLOW_PRIVATE_URLS=yes enables the toggle.
- L298 `test_env_var_false(self, monkeypatch)` (method) — HERMES_ALLOW_PRIVATE_URLS=false keeps it disabled.
- L303 `test_config_security_section(self, monkeypatch)` (method) — security.allow_private_urls in config enables the toggle.
- L310 `test_config_browser_fallback(self, monkeypatch)` (method) — browser.allow_private_urls works as legacy fallback.
- L317 `test_config_security_string_false_stays_disabled(self, monkeypatch)` (method) — Quoted false must not opt out of SSRF protection.
- L324 `test_config_browser_string_false_stays_disabled(self, monkeypatch)` (method) — Legacy browser.allow_private_urls also normalises quoted false.
- L331 `test_config_security_takes_precedence_over_browser(self, monkeypatch)` (method) — security section is checked before browser section.
- L338 `test_env_var_overrides_config(self, monkeypatch)` (method) — Env var takes priority over config.
- L345 `test_result_is_cached(self, monkeypatch)` (method) — Second call uses cached result, doesn't re-read config.
- L354 `TestAllowPrivateUrlsIntegration` (class) — Integration tests: is_safe_url respects the global toggle.
- L358 `_reset_cache(self)` (method)
- L363 `test_private_ip_allowed_when_toggle_on(self, monkeypatch)` (method) — Private IPs pass is_safe_url when toggle is enabled.
- L371 `test_benchmark_ip_allowed_when_toggle_on(self, monkeypatch)` (method) — 198.18.x.x (benchmark/OpenWrt proxy range) passes when toggle is on.
- L379 `test_cgnat_allowed_when_toggle_on(self, monkeypatch)` (method) — CGNAT range (100.64.0.0/10) passes when toggle is on.
- L387 `test_localhost_allowed_when_toggle_on(self, monkeypatch)` (method) — Even localhost passes when toggle is on.
- L397 `test_metadata_hostname_blocked_even_with_toggle(self, monkeypatch)` (method) — metadata.google.internal is ALWAYS blocked.
- L402 `test_metadata_goog_blocked_even_with_toggle(self, monkeypatch)` (method) — metadata.goog is ALWAYS blocked.
- L407 `test_metadata_ip_blocked_even_with_toggle(self, monkeypatch)` (method) — 169.254.169.254 (AWS/GCP metadata IP) is ALWAYS blocked.
- L415 `test_metadata_ipv6_blocked_even_with_toggle(self, monkeypatch)` (method) — fd00:ec2::254 (AWS IPv6 metadata) is ALWAYS blocked.
- L423 `test_ecs_metadata_blocked_even_with_toggle(self, monkeypatch)` (method) — 169.254.170.2 (AWS ECS task metadata) is ALWAYS blocked.
- L431 `test_alibaba_metadata_blocked_even_with_toggle(self, monkeypatch)` (method) — 100.100.100.200 (Alibaba Cloud metadata) is ALWAYS blocked.
- L439 `test_azure_wire_server_blocked_even_with_toggle(self, monkeypatch)` (method) — 169.254.169.253 (Azure IMDS wire server) is ALWAYS blocked.
- L447 `test_entire_link_local_blocked_even_with_toggle(self, monkeypatch)` (method) — Any 169.254.x.x address is ALWAYS blocked (entire link-local range).
- L455 `test_dns_failure_still_blocked_with_toggle(self, monkeypatch)` (method) — DNS failures are still blocked even with toggle on.
- L461 `test_empty_url_still_blocked_with_toggle(self, monkeypatch)` (method) — Empty URLs are still blocked.
- L467 `TestIsAlwaysBlockedUrl` (class) — The always-blocked floor — cloud metadata only, narrower than is_safe_url.
- L479 `test_literal_imds_ips_always_blocked(self, url)` (method) — Literal IMDS IPs and the /16 link-local range always block.
- L483 `test_gcp_metadata_hostname_always_blocked_even_without_dns(self)` (method) — metadata.google.internal blocks by hostname, no DNS needed.
- L488 `test_hostname_resolving_to_imds_always_blocked(self)` (method) — Attacker-controlled hostname resolving to IMDS still blocks.
- L497 `test_public_url_not_blocked(self)` (method)
- L507 `test_ordinary_private_urls_not_in_floor(self, url)` (method) — Floor is narrower than is_safe_url — ordinary private URLs pass.
- L511 `test_dns_failure_not_in_floor(self)` (method) — DNS failure on a non-sentinel hostname = not always-blocked.
- L519 `test_empty_url_not_in_floor(self)` (method) — Empty URL falls through — caller decides what to do with a malformed URL.
- L523 `test_malformed_url_not_in_floor(self)` (method) — Parse errors don't claim always-blocked status.
- L527 `test_floor_ignores_allow_private_urls_toggle(self, monkeypatch)` (method) — security.allow_private_urls can NOT unblock cloud metadata.
- L533 `TestIPv4MappedIPv6SSRF` (class) — Regression tests for SSRF bypass via IPv4-mapped IPv6 addresses.
- L554 `test_ipv4_mapped_blocked_ips(self, ip_str)` (method) — IPv4-mapped IPv6 addresses that should be blocked.
- L564 `test_ipv4_mapped_allowed_ips(self, ip_str)` (method) — IPv4-mapped IPv6 addresses that should be allowed.
- L571 `test_ipv4_mapped_aws_metadata_blocked(self)` (method) — ::ffff:169.254.169.254 (AWS metadata) must always be blocked.
- L578 `test_ipv4_mapped_ecs_metadata_blocked(self)` (method) — ::ffff:169.254.170.2 (AWS ECS task metadata) must always be blocked.
- L585 `test_ipv4_mapped_azure_wire_server_blocked(self)` (method) — ::ffff:169.254.169.253 (Azure IMDS wire server) must always be blocked.
- L592 `test_ipv4_mapped_alibaba_metadata_blocked(self)` (method) — ::ffff:100.100.100.200 (Alibaba Cloud metadata) must always be blocked.
