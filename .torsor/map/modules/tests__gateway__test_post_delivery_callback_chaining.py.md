---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_post_delivery_callback_chaining.py

Symbols in `tests/gateway/test_post_delivery_callback_chaining.py`.

- L15 `_MinAdapter` (class)
- L16 `connect(self)` (method)
- L19 `disconnect(self)` (method)
- L22 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L25 `get_chat_info(self, chat_id)` (method)
- L30 `adapter()` (function)
- L34 `TestPostDeliveryCallbackChaining` (class)
- L35 `test_single_callback_fires(self, adapter)` (method)
- L42 `test_two_callbacks_chain_in_order(self, adapter)` (method)
- L50 `test_three_callbacks_chain_in_order(self, adapter)` (method) — Chain composes over an already-chained callback.
- L61 `test_exception_in_one_callback_does_not_block_next(self, adapter)` (method)
- L73 `test_same_generation_chains(self, adapter)` (method)
- L85 `test_stale_generation_registration_rejected(self, adapter)` (method) — A registration with an older generation than the existing
- L99 `test_pop_at_wrong_generation_returns_none(self, adapter)` (method)
- L107 `test_empty_session_key_is_noop(self, adapter)` (method)
- L111 `test_non_callable_is_noop(self, adapter)` (method)
