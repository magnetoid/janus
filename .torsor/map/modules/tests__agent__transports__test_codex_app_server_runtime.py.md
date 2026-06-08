---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_codex_app_server_runtime.py

Symbols in `tests/agent/transports/test_codex_app_server_runtime.py`.

- L18 `TestApiModeRegistration` (class) — The new api_mode must be registered or downstream parsing rejects it.
- L21 `test_codex_app_server_is_a_valid_api_mode(self)` (method)
- L24 `test_existing_api_modes_still_present(self)` (method)
- L36 `TestMaybeApplyCodexAppServerRuntime` (class) — The opt-in helper that rewrites api_mode → codex_app_server.
- L50 `test_default_off_for_openai(self, model_cfg)` (method) — Default behavior is preserved when the flag is unset/auto.
- L57 `test_opt_in_rewrites_openai(self)` (method)
- L65 `test_opt_in_rewrites_openai_codex(self)` (method)
- L73 `test_case_insensitive(self)` (method)
- L94 `test_other_providers_never_rerouted(self, provider)` (method) — Non-OpenAI providers MUST NOT be rerouted even with the flag set —
- L107 `TestCodexAppServerModule` (class) — Module-surface tests for the JSON-RPC speaker. Don't require codex CLI.
- L110 `test_module_imports(self)` (method)
- L117 `test_parse_codex_version_valid(self)` (method)
- L124 `test_parse_codex_version_invalid(self)` (method)
- L131 `test_check_binary_handles_missing_executable(self)` (method)
- L138 `test_codex_error_class_is_runtimeerror(self)` (method)
- L147 `TestSpawnEnvIsolation` (class) — The codex spawn must NOT rewrite HOME — codex's shell tool spawns
- L160 `test_spawn_env_preserves_HOME(self, monkeypatch)` (method) — The spawn env must contain the parent process's HOME unchanged.
- L204 `test_spawn_env_sets_CODEX_HOME_when_provided(self, monkeypatch)` (method) — CODEX_HOME isolation must still work — that's the whole point
- L245 `test_kanban_worker_adds_only_kanban_writable_root(self, monkeypatch)` (method) — Codex-runtime Kanban workers need to write board state outside
