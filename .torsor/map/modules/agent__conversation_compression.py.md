---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/conversation_compression.py

Symbols in `agent/conversation_compression.py`.

- L44 `_compression_lock_holder(agent: Any)` (function) — Build a unique holder id for the lock: pid:tid:agent-instance:uuid.
- L64 `check_compression_model_feasibility(agent: Any)` (function) — Warn at session start if the auxiliary compression model's context
- L253 `replay_compression_warning(agent: Any)` (function) — Re-send the compression warning through ``status_callback``.
- L271 `compress_context(agent: Any, messages: list, system_message: str, *, approx_tokens: Optional[int]=None, task_id: str='default', focus_topic: Optional[str]=None, force: bool=False)` (function) — Compress conversation context and split the session in SQLite.
- L617 `try_shrink_image_parts_in_messages(api_messages: list)` (function) — Re-encode all native image parts at a smaller size to recover from
