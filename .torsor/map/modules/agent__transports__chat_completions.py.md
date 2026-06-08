---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/transports/chat_completions.py

Symbols in `agent/transports/chat_completions.py`.

- L22 `_build_gemini_thinking_config(model: str, reasoning_config: dict | None)` (function) — Translate Hermes/OpenRouter-style reasoning config to Gemini thinkingConfig.
- L78 `_snake_case_gemini_thinking_config(config: dict | None)` (function) — Convert Gemini thinking config keys to the OpenAI-compat field names.
- L93 `_is_gemini_openai_compat_base_url(base_url: Any)` (function)
- L102 `_model_consumes_thought_signature(model: Any)` (function) — True when the outgoing model is a Gemini family model that requires
- L118 `ChatCompletionsTransport` (class) — Transport for api_mode='chat_completions'.
- L125 `api_mode(self)` (method)
- L128 `convert_messages(self, messages: list[dict[str, Any]], **kwargs)` (method) — Messages are already in OpenAI format — strip internal fields
- L219 `convert_tools(self, tools: list[dict[str, Any]])` (method) — Tools are already in OpenAI format — identity.
- L223 `build_kwargs(self, model: str, messages: list[dict[str, Any]], tools: list[dict[str, Any]] | None=None, **params)` (method) — Build chat.completions.create() kwargs.
- L458 `_build_kwargs_from_profile(self, profile, model, sanitized, tools, params)` (method) — Build API kwargs using a ProviderProfile — single path, no legacy flags.
- L599 `normalize_response(self, response: Any, **kwargs)` (method) — Normalize OpenAI ChatCompletion to NormalizedResponse.
- L676 `validate_response(self, response: Any)` (method) — Check that response has valid choices.
- L686 `extract_cache_stats(self, response: Any)` (method) — Extract OpenRouter/OpenAI cache stats from prompt_tokens_details.
