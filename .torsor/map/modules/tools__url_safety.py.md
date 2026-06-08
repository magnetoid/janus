---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/url_safety.py

Symbols in `tools/url_safety.py`.

- L38 `normalize_url_for_request(url: str)` (function) — Return an ASCII-safe HTTP URL for Hermes-owned URL tools.
- L133 `_global_allow_private_urls()` (function) — Return True when the user has opted out of private-IP blocking.
- L184 `_reset_allow_private_cache()` (function) — Reset the cached toggle — only for tests.
- L191 `_is_blocked_ip(ip: ipaddress.IPv4Address | ipaddress.IPv6Address)` (function) — Return True if the IP should be blocked for SSRF protection.
- L213 `is_always_blocked_url(url: str)` (function) — Return True when the URL targets an always-blocked endpoint.
- L309 `_allows_private_ip_resolution(hostname: str, scheme: str)` (function) — Return True when a trusted HTTPS hostname may bypass IP-class blocking.
- L314 `is_safe_url(url: str)` (function) — Return True if the URL target is not a private/internal address.
- L396 `async_is_safe_url(url: str)` (function) — Same rules as :func:`is_safe_url`, but run the DNS work off the event loop.
