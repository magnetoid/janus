---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_shutdown_memory_provider_messages.py

Symbols in `tests/gateway/test_shutdown_memory_provider_messages.py`.

- L30 `_mock_dotenv(monkeypatch)` (function) — gateway.run imports dotenv at module load; stub so tests run bare.
- L37 `_make_runner()` (function)
- L50 `_FakeAgent` (class)
- L51 `__init__(self, session_messages=None, has_shutdown=True)` (method)
- L59 `TestCleanupAgentResourcesPassesMessages` (class) — _cleanup_agent_resources forwards the agent's session messages.
- L62 `test_populated_messages_forwarded(self)` (method) — Real-world path: an agent that ran a turn has a populated
- L78 `test_empty_list_still_forwarded(self)` (method) — An agent that initialised but ran no turns has an empty list
- L91 `test_missing_attribute_falls_back_to_no_arg(self)` (method) — Test stubs built via ``object.__new__(AIAgent)`` skip
- L103 `test_non_list_attribute_falls_back_to_no_arg(self)` (method) — A MagicMock-based agent auto-synthesises ``_session_messages``
- L117 `test_provider_exception_is_swallowed(self)` (method) — Provider teardown must be best-effort — a raising
- L132 `test_none_agent_is_noop(self)` (method) — Defensive: None agent short-circuits (idle sweeps may
- L139 `test_agent_without_shutdown_method_is_tolerated(self)` (method) — An agent without ``shutdown_memory_provider`` (old test
