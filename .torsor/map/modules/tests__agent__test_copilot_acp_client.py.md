---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_copilot_acp_client.py

Symbols in `tests/agent/test_copilot_acp_client.py`.

- L16 `_FakeProcess` (class)
- L17 `__init__(self)` (method)
- L21 `CopilotACPClientSafetyTests` (class)
- L22 `setUp(self)` (method)
- L25 `_dispatch(self, message: dict, *, cwd: str)` (method)
- L39 `test_request_permission_is_not_auto_allowed(self)` (method)
- L53 `test_read_text_file_blocks_internal_hermes_hub_files(self)` (method)
- L77 `test_read_text_file_redacts_sensitive_content(self)` (method)
- L101 `test_write_text_file_reuses_write_denylist(self)` (method)
- L124 `test_write_text_file_respects_safe_root(self)` (method)
- L159 `_make_home_client(tmp_path)` (function)
- L169 `_fake_popen_capture(captured)` (function)
- L177 `test_run_prompt_prefers_profile_home_when_available(monkeypatch, tmp_path)` (function)
- L195 `test_run_prompt_passes_home_when_parent_env_is_clean(monkeypatch, tmp_path)` (function)
