---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_message_deduplicator.py

Symbols in `tests/gateway/test_message_deduplicator.py`.

- L17 `TestMessageDeduplicatorTTL` (class) — TTL-based expiration must work regardless of cache size.
- L20 `test_duplicate_within_ttl(self)` (method) — Same message within TTL window is duplicate.
- L26 `test_not_duplicate_after_ttl_expires(self)` (method) — Same message AFTER TTL expires should NOT be duplicate.
- L36 `test_expired_entry_gets_refreshed(self)` (method) — After an expired entry is allowed through, it should be re-tracked.
- L49 `test_different_messages_not_confused(self)` (method) — Different message IDs are independent.
- L57 `test_empty_id_never_duplicate(self)` (method) — Empty/None message IDs are never treated as duplicate.
- L63 `test_max_size_eviction_prunes_expired(self)` (method) — Cache pruning on overflow removes expired entries.
- L79 `test_max_size_eviction_caps_fresh_entries(self)` (method) — Fresh entries must still be capped to max_size on overflow.
- L92 `test_ttl_zero_means_no_dedup(self)` (method) — With TTL=0, all entries expire immediately.
