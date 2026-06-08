---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_channel_prompts.py

Symbols in `tests/gateway/test_discord_channel_prompts.py`.

- L12 `_ensure_discord_mock()` (function)
- L37 `_CapturingAgent` (class)
- L40 `__init__(self, *args, **kwargs)` (method)
- L44 `run_conversation(self, user_message, conversation_history=None, task_id=None, persist_user_message=None)` (method)
- L53 `_install_fake_agent(monkeypatch)` (function)
- L59 `_make_adapter()` (function)
- L69 `_make_runner()` (function)
- L95 `_make_source()` (function)
- L104 `TestResolveChannelPrompts` (class)
- L105 `test_no_prompt_returns_none(self)` (method)
- L109 `test_match_by_channel_id(self)` (method)
- L114 `test_numeric_yaml_keys_normalized_at_config_load(self)` (method) — Numeric YAML keys are normalized to strings by config bridging.
- L128 `test_match_by_parent_id(self)` (method)
- L133 `test_exact_channel_overrides_parent(self)` (method)
- L143 `test_build_message_event_sets_channel_prompt(self)` (method)
- L160 `test_dispatch_thread_session_inherits_parent_channel_prompt(self)` (method)
- L178 `test_blank_prompts_are_ignored(self)` (method)
- L185 `test_retry_preserves_channel_prompt(monkeypatch)` (function)
- L213 `test_run_agent_appends_channel_prompt_to_ephemeral_system_prompt(monkeypatch, tmp_path)` (function)
