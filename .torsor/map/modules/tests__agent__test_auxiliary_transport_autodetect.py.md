---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_transport_autodetect.py

Symbols in `tests/agent/test_auxiliary_transport_autodetect.py`.

- L23 `_clean_env(monkeypatch)` (function)
- L50 `test_endpoint_speaks_anthropic_messages(url, expected, label)` (function)
- L61 `test_maybe_wrap_anthropic_rewraps_kimi_coding_url()` (function) — Plain OpenAI client pointed at api.kimi.com/coding gets rewrapped.
- L79 `test_maybe_wrap_anthropic_rewraps_slash_anthropic_url()` (function) — Plain OpenAI client pointed at any /anthropic URL gets rewrapped.
- L97 `test_maybe_wrap_anthropic_skips_openai_wire_urls()` (function) — OpenRouter / OpenAI / Moonshot-legacy stay as plain OpenAI clients.
- L112 `test_maybe_wrap_anthropic_respects_explicit_chat_completions()` (function) — api_mode=chat_completions overrides URL heuristics.
- L126 `test_maybe_wrap_anthropic_honors_explicit_anthropic_messages()` (function) — api_mode=anthropic_messages wraps even when URL wouldn't trigger.
- L145 `test_maybe_wrap_anthropic_double_wrap_safe()` (function) — Already-wrapped AnthropicAuxiliaryClient passes through unchanged.
- L157 `test_maybe_wrap_anthropic_codex_client_passes_through()` (function) — CodexAuxiliaryClient is never re-dispatched.
- L174 `test_maybe_wrap_anthropic_sdk_missing_falls_back()` (function) — ImportError on anthropic SDK returns plain client with warning.
- L213 `test_resolve_provider_client_kimi_coding_wraps_anthropic(monkeypatch, tmp_path)` (function) — End-to-end: resolve_provider_client('kimi-coding', 'kimi-for-coding')
