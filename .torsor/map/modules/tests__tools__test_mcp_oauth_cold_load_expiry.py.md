---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_oauth_cold_load_expiry.py

Symbols in `tests/tools/test_mcp_oauth_cold_load_expiry.py`.

- L51 `TestSetTokensAbsoluteExpiry` (class)
- L52 `test_set_tokens_persists_absolute_expires_at(self, tmp_path, monkeypatch)` (method) — Tokens round-tripped through disk must encode absolute expiry.
- L83 `test_set_tokens_without_expires_in_omits_expires_at(self, tmp_path, monkeypatch)` (method) — Tokens without a TTL must not gain a fabricated expires_at.
- L109 `TestGetTokensReconstructsExpiresIn` (class)
- L110 `test_get_tokens_uses_expires_at_for_remaining_ttl(self, tmp_path, monkeypatch)` (method) — Round-trip: expires_in on read must reflect time remaining.
- L140 `test_get_tokens_returns_zero_ttl_for_expired_token(self, tmp_path, monkeypatch)` (method) — An already-expired token reloaded from disk must report expires_in=0.
- L170 `test_get_tokens_legacy_file_without_expires_at_is_loadable(self, tmp_path, monkeypatch)` (method) — Existing on-disk files (pre-Fix-A) must still load without crashing.
- L219 `test_initialize_seeds_token_expiry_time_from_stored_tokens(tmp_path, monkeypatch)` (function) — Cold-load must populate context.token_expiry_time.
- L284 `test_initialize_flags_expired_token_as_invalid(tmp_path, monkeypatch)` (function) — After _initialize, an expired-on-disk token must report is_token_valid=False.
- L355 `_noop_redirect(_url: str)` (function)
- L359 `_noop_callback()` (function)
- L369 `test_initialize_prefetches_oauth_metadata_when_missing(tmp_path, monkeypatch)` (function) — Cold-load must pre-flight PRM + ASM discovery so ``_refresh_token``
- L493 `test_initialize_skips_prefetch_when_no_tokens(tmp_path, monkeypatch)` (function) — Pre-flight must not run when there are no stored tokens yet.
