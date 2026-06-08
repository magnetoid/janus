---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cwd_env_respect.py

Symbols in `tests/cli/test_cwd_env_respect.py`.

- L13 `_resolve_cwd(terminal_config: dict, defaults: dict, env: dict)` (function) — Mirror the CWD resolution logic from cli.py load_cli_config().
- L34 `TestLocalBackendCli` (class) — Local backend always uses os.getcwd().
- L37 `test_explicit_config_ignored(self)` (method)
- L43 `test_inherited_env_overwritten(self)` (method)
- L49 `test_placeholder_resolved(self)` (method)
- L55 `test_env_and_no_config_file(self)` (method)
- L62 `TestNonLocalBackends` (class) — Non-local backends use config or per-backend defaults.
- L65 `test_placeholder_popped(self)` (method)
- L71 `test_explicit_path_kept(self)` (method)
- L77 `test_auto_placeholder_popped(self)` (method)
- L84 `TestGatewayLazyImport` (class) — Gateway lazy import of cli.py must not clobber TERMINAL_CWD.
- L87 `test_gateway_cwd_preserved(self)` (method)
- L94 `test_cli_overwrites_stale_env(self)` (method)
