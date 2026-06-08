---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/chat_completion_helpers.py

Symbols in `agent/chat_completion_helpers.py`.

- L42 `_ra()` (function) — Lazy ``run_agent`` reference.
- L53 `estimate_request_context_tokens(api_payload: Any)` (function) — Estimate context/load tokens from an API payload, dict or messages list.
- L106 `_is_openai_codex_backend(agent)` (function)
- L118 `_env_float(name: str, default: float)` (function)
- L125 `interruptible_api_call(agent, api_kwargs: dict)` (function) — Run the API call in a background thread so the main conversation loop
- L527 `build_api_kwargs(agent, api_messages: list)` (function) — Build the keyword arguments dict for the active API mode.
- L787 `build_assistant_message(agent, assistant_message, finish_reason: str)` (function) — Build a normalized assistant message dict from an API response message.
- L1005 `try_activate_fallback(agent, reason: 'FailoverReason | None'=None)` (function) — Switch to the next fallback model/provider in the chain.
- L1265 `handle_max_iterations(agent, messages: list, api_call_count: int)` (function) — Request a summary when max iterations are reached. Returns the final response text.
- L1495 `cleanup_task_resources(agent, task_id: str)` (function) — Clean up VM and browser resources for a given task.
- L1527 `interruptible_streaming_api_call(agent, api_kwargs: dict, *, on_first_delta=None)` (function) — Streaming variant of _interruptible_api_call for real-time token delivery.
