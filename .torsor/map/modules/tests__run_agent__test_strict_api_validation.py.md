---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_strict_api_validation.py

Symbols in `tests/run_agent/test_strict_api_validation.py`.

- L16 `_tool_defs(*names)` (function)
- L30 `_FakeOpenAI` (class)
- L31 `__init__(self, **kw)` (method)
- L35 `close(self)` (method)
- L39 `_make_agent(monkeypatch, provider, api_mode='chat_completions', base_url='https://openrouter.ai/api/v1')` (function)
- L55 `TestStrictApiValidation` (class) — Verify tool_call field sanitization prevents 400 errors on strict APIs.
- L58 `test_fireworks_compatible_messages_after_sanitization(self, monkeypatch)` (method) — Messages should be Fireworks-compatible after sanitization.
- L94 `test_codex_preserves_fields_for_replay(self, monkeypatch)` (method) — Codex mode should preserve fields for Responses API replay.
- L120 `test_sanitize_method_with_fireworks_provider(self, monkeypatch)` (method) — Simulating Fireworks provider should trigger sanitization.
- L132 `test_no_sanitize_for_codex_responses(self, monkeypatch)` (method) — Codex responses mode should NOT sanitize.
