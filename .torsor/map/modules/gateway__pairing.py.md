---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/pairing.py

Symbols in `gateway/pairing.py`.

- L55 `_secure_write(path: Path, data: str)` (function) — Write data to file with restrictive permissions (owner read/write only).
- L81 `PairingStore` (class) — Manages pairing codes and approved user lists.
- L91 `__init__(self)` (method)
- L97 `_pending_path(self, platform: str)` (method)
- L100 `_approved_path(self, platform: str)` (method)
- L103 `_rate_limit_path(self)` (method)
- L106 `_load_json(self, path: Path)` (method)
- L114 `_save_json(self, path: Path, data: dict)` (method)
- L117 `_normalize_user_id(self, platform: str, user_id: str)` (method) — Normalize platform-specific user IDs before persisting them.
- L124 `_user_id_aliases(self, platform: str, user_id: str)` (method) — Return all known equivalent user IDs for auth/rate-limit checks.
- L136 `_user_ids_match(self, platform: str, left: str, right: str)` (method) — Return True when two user IDs represent the same principal.
- L144 `is_approved(self, platform: str, user_id: str)` (method) — Check if a user is approved (paired) on a platform.
- L152 `list_approved(self, platform: str=None)` (method) — List approved users, optionally filtered by platform.
- L162 `_approve_user(self, platform: str, user_id: str, user_name: str='')` (method) — Add a user to the approved list. Must be called under self._lock.
- L180 `revoke(self, platform: str, user_id: str)` (method) — Remove a user from the approved list. Returns True if found.
- L200 `_hash_code(code: str, salt: bytes)` (method) — Hash a pairing code with the given salt using SHA-256.
- L204 `generate_code(self, platform: str, user_id: str, user_name: str='')` (method) — Generate a pairing code for a new user.
- L260 `approve_code(self, platform: str, code: str)` (method) — Approve a pairing code. Adds the user to the approved list.
- L328 `list_pending(self, platform: str=None)` (method) — List pending pairing requests, optionally filtered by platform.
- L361 `clear_pending(self, platform: str=None)` (method) — Clear all pending requests. Returns count removed.
- L374 `_is_rate_limited(self, platform: str, user_id: str)` (method) — Check if a user has requested a code too recently.
- L384 `_record_rate_limit(self, platform: str, user_id: str)` (method) — Record the time of a pairing request for rate limiting.
- L393 `_is_locked_out(self, platform: str)` (method) — Check if a platform is in lockout due to failed approval attempts.
- L400 `_record_failed_attempt(self, platform: str)` (method) — Record a failed approval attempt. Triggers lockout after MAX_FAILED_ATTEMPTS.
- L416 `_cleanup_expired(self, platform: str)` (method) — Remove expired pending codes.
- L442 `_all_platforms(self, suffix: str)` (method) — List all platforms that have data files of a given suffix.
