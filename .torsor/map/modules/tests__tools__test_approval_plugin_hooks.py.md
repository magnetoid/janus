---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_approval_plugin_hooks.py

Symbols in `tests/tools/test_approval_plugin_hooks.py`.

- L22 `isolated_session(monkeypatch, tmp_path)` (function) — Give each test a fresh session_key, clean approval-state, and isolated
- L49 `TestCliPathFiresHooks` (class) — CLI-interactive approval path: HERMES_INTERACTIVE is set, the
- L53 `test_pre_and_post_fire_with_expected_kwargs(self, isolated_session, monkeypatch)` (method)
- L96 `test_deny_reported_to_post_hook(self, isolated_session, monkeypatch)` (method)
- L120 `test_plugin_hook_crash_does_not_break_approval(self, isolated_session, monkeypatch)` (method) — A crashing plugin must never prevent the approval flow from
- L146 `TestGatewayPathFiresHooks` (class) — Async gateway approval path: HERMES_GATEWAY_SESSION is set and a
