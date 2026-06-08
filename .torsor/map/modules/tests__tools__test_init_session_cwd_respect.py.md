---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_init_session_cwd_respect.py

Symbols in `tests/tools/test_init_session_cwd_respect.py`.

- L22 `_TestableEnv` (class) — Concrete subclass for testing base class methods.
- L25 `__init__(self, cwd='/tmp', timeout=10)` (method)
- L28 `_run_bash(self, cmd_string, *, login=False, timeout=120, stdin_data=None)` (method)
- L31 `cleanup(self)` (method)
- L35 `TestInitSessionCwdRespect` (class) — init_session() must preserve the configured cwd.
- L38 `test_bootstrap_contains_cd_to_configured_cwd(self)` (method) — The bootstrap script must cd to self.cwd before running pwd.
- L77 `test_configured_cwd_survives_init_session(self)` (method) — self.cwd must be the configured path after init_session completes.
- L103 `test_default_cwd_still_works(self)` (method) — When no custom cwd is configured, default /tmp behavior is preserved.
- L125 `test_bootstrap_cd_uses_shlex_quote(self)` (method) — Paths with spaces must be properly quoted in the bootstrap cd.
