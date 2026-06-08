---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/helpers.py

Symbols in `gateway/platforms/helpers.py`.

- L27 `MessageDeduplicator` (class) — TTL-based message deduplication cache.
- L43 `__init__(self, max_size: int=2000, ttl_seconds: float=300)` (method)
- L48 `is_duplicate(self, msg_id: str)` (method) — Return True if *msg_id* was already seen within the TTL window.
- L73 `clear(self)` (method) — Clear all tracked messages.
- L81 `TextBatchAggregator` (class) — Aggregates rapid-fire text events into single messages.
- L101 `__init__(self, handler, *, batch_delay: float=0.6, split_delay: float=2.0, split_threshold: int=4000)` (method)
- L116 `is_enabled(self)` (method) — Return True if batching is active (delay > 0).
- L120 `enqueue(self, event: 'MessageEvent', key: str)` (method) — Add *event* to the pending batch for *key*.
- L137 `_flush(self, key: str)` (method) — Wait then dispatch the batched event for *key*.
- L157 `cancel_all(self)` (method) — Cancel all pending flush tasks.
- L180 `strip_markdown(text: str)` (function) — Strip markdown formatting for plain-text platforms (SMS, iMessage, etc.).
- L201 `ThreadParticipationTracker` (class) — Persistent tracking of threads the bot has participated in.
- L222 `__init__(self, platform_name: str, max_tracked: int=500)` (method)
- L229 `_state_path(self)` (method)
- L233 `_load(self)` (method)
- L244 `_save(self)` (method)
- L252 `mark(self, thread_id: str)` (method) — Mark *thread_id* as participated and persist.
- L258 `__contains__(self, thread_id: str)` (method)
- L261 `clear(self)` (method)
- L268 `redact_phone(phone: str)` (function) — Redact a phone number for logging, preserving country code and last 4.
