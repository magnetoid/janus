---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_bind_guard.py

Symbols in `tests/gateway/test_api_server_bind_guard.py`.

- L22 `TestIsNetworkAccessible` (class) — Direct tests for the address classification helper.
- L27 `test_ipv4_loopback(self)` (method)
- L30 `test_ipv6_loopback(self)` (method)
- L33 `test_ipv4_mapped_loopback(self)` (method)
- L40 `test_ipv4_wildcard(self)` (method)
- L43 `test_ipv6_wildcard(self)` (method)
- L47 `test_ipv4_mapped_unspecified(self)` (method)
- L50 `test_private_ipv4(self)` (method)
- L53 `test_private_ipv4_class_c(self)` (method)
- L56 `test_public_ipv4(self)` (method)
- L61 `test_localhost_resolves_to_loopback(self)` (method)
- L68 `test_hostname_resolving_to_non_loopback(self)` (method)
- L75 `test_hostname_mixed_resolution(self)` (method) — If a hostname resolves to both loopback and non-loopback, it's
- L85 `test_dns_failure_fails_closed(self)` (method) — Unresolvable hostnames should require an API key (fail closed).
- L99 `TestConnectBindGuard` (class) — Verify that connect() refuses dangerous configurations.
- L103 `test_refuses_ipv4_wildcard_without_key(self)` (method)
- L109 `test_refuses_ipv6_wildcard_without_key(self)` (method)
- L115 `test_refuses_loopback_without_key(self)` (method) — Loopback binds are still an auth boundary and require API_SERVER_KEY.
- L124 `test_allows_wildcard_with_key(self)` (method) — Non-loopback with a key should pass the guard.
