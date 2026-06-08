---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/conversation_loop.py

Symbols in `agent/conversation_loop.py`.

- L67 `_ollama_context_limit_error(agent: Any, request_tokens: int)` (function) — Return a user-facing error when Ollama is loaded with too little context.
- L111 `_ra()` (function) — Lazy reference to ``run_agent`` so callers can patch
- L120 `_nous_entitlement_message(capability: str)` (function)
- L137 `_print_nous_entitlement_guidance(agent, capability: str)` (function)
- L146 `_is_nous_inference_route(provider: str, base_url: str)` (function)
- L157 `_billing_or_entitlement_message(*, capability: str, provider: str, base_url: str, model: str)` (function)
- L182 `_print_billing_or_entitlement_guidance(agent, *, capability: str, provider: str, base_url: str, model: str)` (function)
- L203 `_try_refresh_nous_paid_entitlement_credentials(agent)` (function) — Refresh Nous runtime credentials after a fresh paid-entitlement check.
- L218 `_restore_or_build_system_prompt(agent, system_message, conversation_history)` (function) — Restore the cached system prompt from the session DB or build it fresh.
- L333 `_get_continuation_prompt(is_partial_stub: bool, dropped_tools: Optional[List[str]]=None)` (function)
- L364 `run_conversation(agent, user_message: str, system_message: str=None, conversation_history: List[Dict[str, Any]]=None, task_id: str=None, stream_callback: Optional[callable]=None, persist_user_message: Optional[str]=None)` (function) — Run a complete conversation with tool calling until completion.
