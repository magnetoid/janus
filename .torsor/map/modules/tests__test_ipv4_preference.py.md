---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_ipv4_preference.py

Symbols in `tests/test_ipv4_preference.py`.

- L8 `_reload_constants()` (function) — Reload hermes_constants to get a fresh apply_ipv4_preference.
- L15 `TestApplyIPv4Preference` (class) — Tests for apply_ipv4_preference().
- L18 `setup_method(self)` (method) — Save the original getaddrinfo before each test.
- L22 `teardown_method(self)` (method) — Restore the original getaddrinfo after each test.
- L26 `test_noop_when_force_false(self)` (method) — No patch when force=False.
- L33 `test_patches_getaddrinfo_when_forced(self)` (method) — Patches socket.getaddrinfo when force=True.
- L41 `test_double_patch_is_safe(self)` (method) — Calling apply twice doesn't double-wrap.
- L49 `test_af_unspec_becomes_af_inet(self)` (method) — AF_UNSPEC (default) calls get rewritten to AF_INET.
- L67 `test_explicit_family_preserved(self)` (method) — Explicit AF_INET6 requests are not intercepted.
- L84 `test_fallback_on_gaierror(self)` (method) — Falls back to AF_UNSPEC if AF_INET resolution fails.
- L106 `TestConfigDefault` (class) — Verify network section exists in DEFAULT_CONFIG.
- L109 `test_network_section_in_default_config(self)` (method)
