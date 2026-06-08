---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_profiles_s6_hooks.py

Symbols in `tests/hermes_cli/test_profiles_s6_hooks.py`.

- L27 `_HostManager` (class) — Mimics a host backend that doesn't support runtime registration.
- L31 `supports_runtime_registration(self)` (method)
- L34 `register_profile_gateway(self, *args: Any, **kwargs: Any)` (method)
- L37 `unregister_profile_gateway(self, *args: Any, **kwargs: Any)` (method)
- L41 `_S6Manager` (class) — Mimics S6ServiceManager just enough for the hooks.
- L45 `__init__(self)` (method)
- L51 `supports_runtime_registration(self)` (method)
- L54 `register_profile_gateway(self, profile: str, *, extra_env: dict[str, str] | None=None)` (method)
- L62 `unregister_profile_gateway(self, profile: str)` (method)
- L68 `_patch_detect_s6(monkeypatch: pytest.MonkeyPatch)` (function) — Pretend we're inside an s6 container so the host short-circuit
- L86 `test_register_noop_on_host(monkeypatch: pytest.MonkeyPatch)` (function)
- L100 `test_register_calls_through_on_s6(monkeypatch: pytest.MonkeyPatch)` (function)
- L110 `test_register_swallows_duplicate_value_error(monkeypatch: pytest.MonkeyPatch)` (function) — A pre-existing s6 registration (from container-boot reconcile)
- L125 `test_register_swallows_arbitrary_error(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str])` (function) — Even an unexpected exception from the manager must not bring
- L141 `test_register_swallows_no_backend_runtime_error(monkeypatch: pytest.MonkeyPatch)` (function) — When `get_service_manager()` raises RuntimeError (no backend
- L156 `test_register_silent_when_detect_throws(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str])` (function) — If detect_service_manager itself raises (e.g. a partial s6
- L180 `test_unregister_noop_on_host(monkeypatch: pytest.MonkeyPatch)` (function)
- L189 `test_unregister_calls_through_on_s6(monkeypatch: pytest.MonkeyPatch)` (function)
- L199 `test_unregister_swallows_errors(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str])` (function)
