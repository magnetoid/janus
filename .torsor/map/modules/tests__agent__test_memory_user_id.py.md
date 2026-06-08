---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_memory_user_id.py

Symbols in `tests/agent/test_memory_user_id.py`.

- L20 `RecordingProvider` (class) — Minimal provider that records what initialize() receives.
- L23 `__init__(self, name='recording')` (method)
- L29 `name(self)` (method)
- L32 `is_available(self)` (method)
- L35 `initialize(self, session_id: str, **kwargs)` (method)
- L39 `system_prompt_block(self)` (method)
- L42 `prefetch(self, query: str, *, session_id: str='')` (method)
- L45 `sync_turn(self, user_content, assistant_content, *, session_id='')` (method)
- L48 `get_tool_schemas(self)` (method)
- L51 `handle_tool_call(self, tool_name, args, **kwargs)` (method)
- L54 `shutdown(self)` (method)
- L63 `TestMemoryManagerUserIdThreading` (class) — Verify user_id reaches providers via initialize_all.
- L66 `test_user_id_forwarded_to_provider(self)` (method)
- L81 `test_chat_context_forwarded_to_provider(self)` (method)
- L103 `test_no_user_id_when_cli(self)` (method) — CLI sessions should not have user_id in kwargs.
- L117 `test_user_id_none_not_forwarded(self)` (method) — Explicit None user_id should not appear in kwargs.
- L132 `test_multiple_providers_all_receive_user_id(self)` (method)
- L157 `TestMem0UserIdScoping` (class) — Verify Mem0 plugin uses gateway user_id when provided.
- L160 `test_gateway_user_id_overrides_default(self)` (method) — When user_id is passed via kwargs, it should override the config default.
- L176 `test_no_user_id_falls_back_to_config(self)` (method) — Without user_id in kwargs, should use config default.
- L191 `test_no_user_id_no_config_uses_hermes_user(self)` (method) — Without user_id or config override, should default to 'hermes-user'.
- L205 `test_different_users_get_different_ids(self)` (method) — Two providers initialized with different user_ids should be scoped differently.
- L231 `TestHonchoUserIdScoping` (class) — Verify Honcho plugin keeps runtime user scoping separate from config peer_name.
- L234 `test_gateway_user_id_is_passed_as_runtime_peer(self)` (method) — Gateway user_id should scope Honcho sessions without mutating config peer_name.
- L276 `test_session_manager_prefers_runtime_user_id_over_config_peer_name(self)` (method) — Session manager should isolate gateway users even when config peer_name is static.
- L308 `test_no_user_id_preserves_config_peer_name(self)` (method) — Without user_id, the config peer_name should be preserved.
- L339 `TestAIAgentUserIdPropagation` (class) — Verify AIAgent stores user_id and passes it to memory init kwargs.
- L342 `test_user_id_stored_on_agent(self)` (method) — AIAgent should store user_id as instance attribute.
- L351 `test_user_id_none_by_default(self)` (method) — AIAgent should have None user_id when not provided (CLI mode).
