---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_non_stream_stale_timeout.py

Symbols in `tests/agent/test_non_stream_stale_timeout.py`.

- L18 `_write_config(tmp_path: Path, body: str)` (function)
- L23 `_make_agent(tmp_path: Path, **overrides)` (function)
- L42 `test_estimator_chat_completions_messages()` (function)
- L55 `test_estimator_responses_api_input()` (function)
- L68 `test_estimator_responses_api_long_session_triggers_tier()` (function) — A real long Codex session (large ``input``) should clear the 50k boundary.
- L79 `test_estimator_bare_list_back_compat()` (function)
- L87 `test_estimator_empty_inputs()` (function)
- L94 `test_estimator_unknown_dict_fallback()` (function)
- L103 `test_default_base_is_90s(monkeypatch, tmp_path)` (function) — Default base stale timeout dropped from 300s to 90s (May 2026).
- L116 `test_short_codex_request_uses_base_only(monkeypatch, tmp_path)` (function) — Codex payload below 50k tokens -> default 90s base.
- L128 `test_long_codex_request_bumps_to_50k_tier(monkeypatch, tmp_path)` (function) — Codex payload > 50k tokens -> at least 150s.
- L142 `test_very_long_codex_request_bumps_to_100k_tier(monkeypatch, tmp_path)` (function) — Codex payload > 100k tokens -> at least 240s.
- L154 `test_chat_completions_long_messages_bumps_tier(monkeypatch, tmp_path)` (function) — Chat Completions estimator still works for the legacy messages path.
- L174 `test_explicit_user_config_overrides_default(monkeypatch, tmp_path)` (function) — If the user explicitly sets a stale_timeout, the new defaults don't apply.
