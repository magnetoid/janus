---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/delivery.py

Symbols in `gateway/delivery.py`.

- L38 `_is_silence_narration(content: Optional[str])` (function) — Return True when ``content`` is *only* a silence-narration token.
- L56 `_looks_like_telegram_private_chat_id(chat_id: Optional[str])` (function)
- L65 `_looks_like_int(value: Optional[str])` (function)
- L75 `_send_result_failed(result: Any)` (function)
- L81 `_send_result_error(result: Any)` (function)
- L89 `_is_thread_not_found_delivery_error(result: Any)` (function)
- L95 `DeliveryTarget` (class) — A single delivery target.
- L112 `parse(cls, target: str, origin: Optional[SessionSource]=None)` (method) — Parse a delivery target string.
- L162 `to_string(self)` (method) — Convert back to string format.
- L175 `DeliveryRouter` (class) — Routes messages to appropriate destinations.
- L183 `__init__(self, config: GatewayConfig, adapters: Dict[Platform, Any]=None)` (method) — Initialize the delivery router.
- L195 `deliver(self, content: str, targets: List[DeliveryTarget], job_id: Optional[str]=None, job_name: Optional[str]=None, metadata: Optional[Dict[str, Any]]=None)` (method) — Deliver content to all specified targets.
- L237 `_deliver_local(self, content: str, job_id: Optional[str], job_name: Optional[str], metadata: Optional[Dict[str, Any]])` (method) — Save content to local files.
- L283 `_save_full_output(self, content: str, job_id: str)` (method) — Save full cron output to disk and return the file path.
- L292 `_filter_silence_narration_enabled(self)` (method) — Whether the outbound silence-narration filter is active.
- L304 `_deliver_to_platform(self, target: DeliveryTarget, content: str, metadata: Optional[Dict[str, Any]])` (method) — Deliver content to a messaging platform.
