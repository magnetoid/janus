---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_session_info.py

Symbols in `tests/gateway/test_session_info.py`.

- L10 `runner()` (function) — Create a bare GatewayRunner without __init__.
- L15 `_patch_info(tmp_path, config_yaml, model, runtime)` (function) — Return a context-manager stack that patches _format_session_info deps.
- L27 `TestFormatSessionInfo` (class)
- L29 `test_includes_model_name(self, runner, tmp_path)` (method)
- L37 `test_includes_provider(self, runner, tmp_path)` (method)
- L45 `test_config_context_length(self, runner, tmp_path)` (method)
- L54 `test_default_fallback_hint(self, runner, tmp_path)` (method)
- L63 `test_local_endpoint_shown(self, runner, tmp_path)` (method)
- L74 `test_cloud_endpoint_hidden(self, runner, tmp_path)` (method)
- L82 `test_million_context_format(self, runner, tmp_path)` (method)
- L90 `test_missing_config(self, runner, tmp_path)` (method) — No config.yaml should not crash.
- L100 `test_runtime_resolution_failure_doesnt_crash(self, runner, tmp_path)` (method) — If runtime resolution raises, should still produce output.
