---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_pre_gateway_dispatch.py

Symbols in `tests/gateway/test_pre_gateway_dispatch.py`.

- L18 `_clear_auth_env(monkeypatch)` (function)
- L30 `_make_event(text: str='hello', platform: Platform=Platform.WHATSAPP)` (function)
- L44 `_make_runner(platform: Platform)` (function)
- L64 `test_hook_skip_short_circuits_dispatch(monkeypatch)` (function) — A plugin returning {'action': 'skip'} drops the message before auth.
- L85 `test_hook_rewrite_replaces_event_text(monkeypatch)` (function) — A plugin returning {'action': 'rewrite', 'text': ...} mutates event.text.
- L112 `test_hook_allow_falls_through_to_auth(monkeypatch)` (function) — A plugin returning {'action': 'allow'} continues to normal dispatch.
- L136 `test_hook_exception_does_not_break_dispatch(monkeypatch)` (function) — A raising plugin hook does not break the gateway.
- L155 `test_internal_events_bypass_hook(monkeypatch)` (function) — Internal events (event.internal=True) skip the plugin hook entirely.
