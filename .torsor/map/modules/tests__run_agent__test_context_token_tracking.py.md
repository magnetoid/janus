---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_context_token_tracking.py

Symbols in `tests/run_agent/test_context_token_tracking.py`.

- L20 `_patch_bootstrap(monkeypatch)` (function)
- L28 `_FakeAnthropicClient` (class)
- L29 `close(self)` (method)
- L33 `_FakeOpenAIClient` (class) — Fake OpenAI client returned by mocked resolve_provider_client.
- L40 `_make_agent(monkeypatch, api_mode, provider, response_fn)` (function)
- L65 `_anthropic_resp(input_tok, output_tok, cache_read=0, cache_creation=0)` (function)
- L81 `test_anthropic_cache_read_and_creation_added(monkeypatch)` (function)
- L89 `test_anthropic_no_cache_fields(monkeypatch)` (function)
- L96 `test_anthropic_cache_read_only(monkeypatch)` (function)
- L105 `test_openai_prompt_tokens_unchanged(monkeypatch)` (function)
- L120 `test_codex_no_cache_fields(monkeypatch)` (function)
