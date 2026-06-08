---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pairing.py

Symbols in `tests/gateway/test_pairing.py`.

- L23 `_make_store(tmp_path)` (function) — Create a PairingStore with PAIRING_DIR pointed to tmp_path.
- L34 `TestSecureWrite` (class)
- L35 `test_creates_parent_dirs(self, tmp_path)` (method)
- L45 `test_sets_file_permissions(self, tmp_path)` (method)
- L57 `TestCodeGeneration` (class)
- L58 `test_code_format(self, tmp_path)` (method)
- L66 `test_code_uniqueness(self, tmp_path)` (method) — Multiple codes for different users should be distinct.
- L77 `test_stores_pending_entry(self, tmp_path)` (method)
- L96 `TestHashedStorage` (class)
- L97 `test_pending_file_contains_hash_and_salt(self, tmp_path)` (method) — Stored entries must have 'hash' and 'salt', never the plaintext code.
- L125 `test_plaintext_code_not_stored(self, tmp_path)` (method) — The raw JSON file must not contain the plaintext code anywhere.
- L133 `test_valid_code_verifies_against_hash(self, tmp_path)` (method) — approve_code with the correct code should succeed.
- L143 `test_invalid_code_rejected(self, tmp_path)` (method) — approve_code with a wrong code should fail.
- L151 `test_different_salts_per_entry(self, tmp_path)` (method) — Each pending entry should have a unique salt.
- L164 `test_hash_code_static_method(self, tmp_path)` (method) — _hash_code should be deterministic for the same code+salt.
- L176 `TestLegacyPendingFileCompat` (class) — Defensive coverage for pre-hash pending.json on upgraded installs.
- L186 `_write_legacy(tmp_path, code='ABCD1234', created_at=None)` (method) — Write a pre-hash pending.json with plaintext code as the key.
- L202 `test_approve_code_ignores_legacy_entries(self, tmp_path)` (method) — A valid old-format code must NOT silently approve under the new schema.
- L216 `test_list_pending_handles_legacy_entries(self, tmp_path)` (method) — list_pending must not KeyError on a missing 'hash' field.
- L226 `test_cleanup_expired_removes_legacy_at_ttl(self, tmp_path)` (method) — Legacy entries past CODE_TTL must still get pruned.
- L242 `test_cleanup_expired_handles_malformed_entries(self, tmp_path)` (method) — Non-dict / missing-created_at entries get evicted, not crashed on.
- L260 `test_approve_code_skips_malformed_entries(self, tmp_path)` (method) — Malformed entries must not crash approve_code's hash loop.
- L281 `TestRateLimiting` (class)
- L282 `test_same_user_rate_limited(self, tmp_path)` (method)
- L290 `test_different_users_not_rate_limited(self, tmp_path)` (method)
- L298 `test_rate_limit_expires(self, tmp_path)` (method)
- L313 `test_whatsapp_alias_flip_hits_same_rate_limit(self, tmp_path, monkeypatch)` (method)
- L336 `TestMaxPending` (class)
- L337 `test_max_pending_per_platform(self, tmp_path)` (method)
- L350 `test_different_platforms_independent(self, tmp_path)` (method)
- L365 `TestApprovalFlow` (class)
- L366 `test_approve_valid_code(self, tmp_path)` (method)
- L378 `test_approved_user_is_approved(self, tmp_path)` (method)
- L385 `test_unapproved_user_not_approved(self, tmp_path)` (method)
- L390 `test_approve_removes_from_pending(self, tmp_path)` (method)
- L398 `test_approve_case_insensitive(self, tmp_path)` (method)
- L407 `test_approve_strips_whitespace(self, tmp_path)` (method)
- L416 `test_invalid_code_returns_none(self, tmp_path)` (method)
- L422 `test_whatsapp_approved_user_survives_alias_flip(self, tmp_path, monkeypatch)` (method)
- L444 `test_whatsapp_legacy_raw_jid_approval_survives_alias_flip(self, tmp_path, monkeypatch)` (method)
- L477 `TestLockout` (class)
- L478 `test_lockout_after_max_failures(self, tmp_path)` (method)
- L491 `test_lockout_blocks_code_generation(self, tmp_path)` (method)
- L500 `test_lockout_blocks_code_approval(self, tmp_path)` (method) — Regression guard for #10195: lockout must also gate approve_code.
- L536 `test_lockout_expires(self, tmp_path)` (method)
- L556 `TestCodeExpiry` (class)
- L557 `test_expired_codes_cleaned_up(self, tmp_path)` (method)
- L572 `test_expired_code_cannot_be_approved(self, tmp_path)` (method)
- L592 `TestRevoke` (class)
- L593 `test_revoke_approved_user(self, tmp_path)` (method)
- L605 `test_revoke_nonexistent_returns_false(self, tmp_path)` (method)
- L616 `TestListAndClear` (class)
- L617 `test_list_approved(self, tmp_path)` (method)
- L627 `test_list_approved_all_platforms(self, tmp_path)` (method)
- L637 `test_clear_pending(self, tmp_path)` (method)
- L647 `test_clear_pending_all_platforms(self, tmp_path)` (method)
