---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/async_utils.py

Symbols in `agent/async_utils.py`.

- L34 `safe_schedule_threadsafe(coro: Coroutine[Any, Any, Any], loop: Optional[asyncio.AbstractEventLoop], *, logger: Optional[logging.Logger]=None, log_message: str='Failed to schedule coroutine on loop', log_level: int=logging.DEBUG)` (function) — Schedule ``coro`` on ``loop`` from a sync context, leak-safe.
