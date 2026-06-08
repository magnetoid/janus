---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/platforms/signal_rate_limit.py

Symbols in `gateway/platforms/signal_rate_limit.py`.

- L43 `SignalRateLimitError` (class) — Raised by ``SignalAdapter._rpc`` for rate-limit responses when the
- L53 `__init__(self, message: str, retry_after: Optional[float]=None)` (method)
- L58 `SignalSchedulerError` (class)
- L74 `_extract_retry_after_seconds(err: Any)` (function) — Pull the per-token Retry-After window from a signal-cli rate-limit error.
- L106 `_is_signal_rate_limit_error(err: Any)` (function) — True if a signal-cli RPC error reflects a rate-limit failure.
- L139 `_format_wait(seconds: float)` (function) — Human-friendly wait label for user-facing pacing notices.
- L147 `_signal_send_timeout(num_attachments: int)` (function) — HTTP timeout for a Signal ``send`` RPC.
- L165 `SignalAttachmentScheduler` (class) — Process-wide token-bucket simulator for Signal attachment sends.
- L180 `__init__(self, capacity: float=float(SIGNAL_RATE_LIMIT_BUCKET_CAPACITY), default_retry_after: float=float(SIGNAL_RATE_LIMIT_DEFAULT_RETRY_AFTER))` (method)
- L195 `_refill(self)` (method)
- L206 `estimate_wait(self, n: int)` (method) — Best-effort estimate of the seconds until ``n`` tokens would
- L223 `acquire(self, n: int)` (method) — Block until at least ``n`` tokens are available, return the
- L274 `report_rpc_duration(self, rpc_duration: float, n_attachments: int)` (method) — Record an attachment-send RPC that just completed.
- L303 `feedback(self, retry_after: Optional[float], n_attempted: int)` (method) — Apply server feedback after a 429.
- L325 `state(self)` (method) — Return current scheduler state for diagnostic logging (read-only).
- L351 `get_scheduler()` (function) — Return the process-wide scheduler, creating it on first access.
- L365 `_reset_scheduler()` (function) — Drop the cached scheduler so the next ``get_scheduler`` call
