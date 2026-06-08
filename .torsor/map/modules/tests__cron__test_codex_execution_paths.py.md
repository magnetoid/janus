---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_codex_execution_paths.py

Symbols in `tests/cron/test_codex_execution_paths.py`.

- L18 `_patch_agent_bootstrap(monkeypatch)` (function)
- L36 `_codex_message_response(text: str)` (function)
- L50 `_UnauthorizedError` (class)
- L51 `__init__(self)` (method)
- L56 `_FakeOpenAI` (class)
- L57 `__init__(self, **kwargs)` (method)
- L60 `close(self)` (method)
- L64 `_Codex401ThenSuccessAgent` (class)
- L68 `__init__(self, *args, **kwargs)` (method)
- L78 `_try_refresh_codex_client_credentials(self, *, force: bool=True)` (method)
- L82 `run_conversation(self, user_message: str, conversation_history=None, task_id=None)` (method)
- L95 `test_cron_run_job_codex_path_handles_internal_401_refresh(monkeypatch)` (function)
- L126 `test_gateway_run_agent_codex_path_handles_internal_401_refresh(monkeypatch)` (function)
