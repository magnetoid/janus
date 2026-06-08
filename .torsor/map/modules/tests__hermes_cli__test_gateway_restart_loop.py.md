---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_restart_loop.py

Symbols in `tests/hermes_cli/test_gateway_restart_loop.py`.

- L24 `TestGatewayLifecyclePattern` (class) — Verify the regex catches gateway lifecycle commands.
- L35 `test_hermes_gateway_commands(self, text)` (method)
- L46 `test_service_manager_commands(self, text)` (method)
- L53 `test_kill_commands(self, text)` (method)
- L70 `test_safe_commands(self, text)` (method)
- L74 `TestCronCreateLifecycleBlock` (class) — Verify cron create rejects gateway lifecycle prompts.
- L78 `_setup_cron_dir(self, tmp_path, monkeypatch)` (method)
- L83 `test_block_hermes_gateway_restart(self, capsys)` (method)
- L104 `test_block_launchctl_kickstart(self, capsys)` (method)
- L124 `test_block_script_with_lifecycle_command(self, tmp_path, capsys)` (method)
- L146 `test_allow_safe_prompt(self, capsys)` (method)
- L166 `test_allow_empty_prompt(self, capsys)` (method) — Empty prompt (no lifecycle content) should pass the filter — the
- L196 `TestGatewaySelfTargetingGuard` (class) — Verify hermes gateway stop/restart refuse when _HERMES_GATEWAY=1.
- L199 `test_stop_refuses_inside_gateway(self, monkeypatch)` (method)
- L207 `test_restart_refuses_inside_gateway(self, monkeypatch)` (method)
- L215 `test_stop_allows_outside_gateway(self, monkeypatch)` (method)
- L235 `test_restart_allows_outside_gateway(self, monkeypatch)` (method)
