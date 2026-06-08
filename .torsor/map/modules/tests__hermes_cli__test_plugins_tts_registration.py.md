---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_plugins_tts_registration.py

Symbols in `tests/hermes_cli/test_plugins_tts_registration.py`.

- L20 `_write_plugin(root: Path, name: str, *, manifest_extra: Dict[str, Any] | None=None, register_body: str='pass')` (function)
- L43 `_enable(hermes_home: Path, name: str)` (function)
- L58 `TestRegisterTTSProvider` (class) — End-to-end: a fake plugin registers via the hook, ends up in the registry.
- L61 `test_accepts_valid_provider(self)` (method)
- L93 `test_rejects_non_provider(self, caplog)` (method) — A plugin that passes a non-TTSProvider gets a warning, no exception.
- L120 `test_rejects_builtin_shadow(self, caplog)` (method) — A plugin trying to register a name colliding with a built-in is silently
