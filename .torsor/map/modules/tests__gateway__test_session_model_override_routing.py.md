---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_model_override_routing.py

Symbols in `tests/gateway/test_session_model_override_routing.py`.

- L22 `_CapturingAgent` (class) — Fake agent that records init kwargs for assertions.
- L27 `__init__(self, *args, **kwargs)` (method)
- L31 `run_conversation(self, user_message: str, conversation_history=None, task_id=None)` (method)
- L39 `_make_runner()` (function)
- L69 `_codex_override()` (function)
- L79 `_explode_runtime_resolution()` (function)
- L85 `test_run_agent_prefers_session_override_over_global_runtime(monkeypatch)` (function)
- L130 `test_background_task_prefers_session_override_over_global_runtime(monkeypatch)` (function)
- L167 `test_gateway_auth_fallback_uses_fallback_model_from_config(tmp_path, monkeypatch)` (function) — Regression: fallback provider must not inherit the primary model.
- L222 `test_gateway_auth_fallback_resolves_key_env_for_custom_provider(tmp_path, monkeypatch)` (function) — Auth-failure fallback should honor key_env/api_key_env custom-endpoint hints.
