---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/service_manager.py

Symbols in `hermes_cli/service_manager.py`.

- L33 `validate_profile_name(name: str)` (function) — Raise ValueError if ``name`` is not usable as a profile name.
- L54 `ServiceManager` (class) — Abstract interface for init-system-specific service operations.
- L68 `start(self, name: str)` (method)
- L69 `stop(self, name: str)` (method)
- L70 `restart(self, name: str)` (method)
- L71 `is_running(self, name: str)` (method)
- L74 `supports_runtime_registration(self)` (method)
- L75 `register_profile_gateway(self, profile: str, *, extra_env: dict[str, str] | None=None)` (method)
- L81 `unregister_profile_gateway(self, profile: str)` (method)
- L82 `list_profile_gateways(self)` (method)
- L85 `detect_service_manager()` (function) — Detect which service manager is available in this environment.
- L121 `_s6_running()` (function) — True when s6-svscan is running as PID 1 in this container.
- L167 `_RegistrationUnsupportedMixin` (class) — Mixin for host backends that don't support runtime registration.
- L170 `supports_runtime_registration(self)` (method)
- L173 `register_profile_gateway(self, profile: str, *, extra_env: dict[str, str] | None=None)` (method)
- L184 `unregister_profile_gateway(self, profile: str)` (method)
- L190 `list_profile_gateways(self)` (method)
- L194 `SystemdServiceManager` (class) — Thin wrapper around the ``systemd_*`` functions in hermes_cli.gateway.
- L204 `start(self, name: str)` (method)
- L208 `stop(self, name: str)` (method)
- L212 `restart(self, name: str)` (method)
- L216 `is_running(self, name: str)` (method)
- L222 `LaunchdServiceManager` (class) — Thin wrapper around the ``launchd_*`` functions in hermes_cli.gateway.
- L227 `start(self, name: str)` (method)
- L231 `stop(self, name: str)` (method)
- L235 `restart(self, name: str)` (method)
- L239 `is_running(self, name: str)` (method)
- L244 `WindowsServiceManager` (class) — Thin wrapper around ``hermes_cli.gateway_windows`` (Scheduled Task /
- L258 `install(self, *, force: bool=False, start_now: bool | None=None, start_on_login: bool | None=None, elevated_handoff: bool=False)` (method)
- L274 `start(self, name: str)` (method)
- L278 `stop(self, name: str)` (method)
- L282 `restart(self, name: str)` (method)
- L286 `is_running(self, name: str)` (method)
- L294 `get_service_manager()` (function) — Return the ServiceManager instance for the current environment.
- L351 `_seed_supervise_skeleton(svc_dir: Path)` (function) — Pre-create the ``supervise/`` and top-level ``event/`` skeleton
- L482 `S6Error` (class) — Base error for S6ServiceManager lifecycle failures.
- L490 `__init__(self, message: str, *, service: str | None=None)` (method)
- L495 `GatewayNotRegisteredError` (class) — Raised when a lifecycle method targets a slot that doesn't exist.
- L504 `__init__(self, profile: str)` (method)
- L514 `S6CommandError` (class) — Raised when an s6 command fails for a reason other than a
- L522 `__init__(self, *, service: str, action: str, returncode: int, stderr: str)` (method)
- L536 `S6ServiceManager` (class) — Per-profile gateway supervision via s6-overlay.
- L546 `__init__(self, scandir: Path=S6_DYNAMIC_SCANDIR)` (method)
- L551 `_service_dir(self, profile: str)` (method)
- L555 `_service_name(self, profile: str)` (method)
- L559 `_render_run_script(profile: str, extra_env: dict[str, str])` (method) — Generate the run script for a profile-gateway s6 service.
- L628 `_render_log_run(profile: str)` (method) — Generate the log/run script for a profile-gateway service.
- L686 `_run_svc(self, action_flag: str, action_label: str, name: str)` (method) — Shared lifecycle dispatch for start / stop / restart.
- L732 `start(self, name: str)` (method) — Bring up a registered service (``s6-svc -u``).
- L742 `stop(self, name: str)` (method) — Bring down a registered service (``s6-svc -d``).
- L751 `restart(self, name: str)` (method) — Restart a registered service (``s6-svc -t`` = SIGTERM).
- L760 `is_running(self, name: str)` (method) — True iff ``s6-svstat`` reports the service as up.
- L771 `supports_runtime_registration(self)` (method)
- L774 `register_profile_gateway(self, profile: str, *, extra_env: dict[str, str] | None=None)` (method) — Create the s6 service directory for a profile gateway.
- L853 `unregister_profile_gateway(self, profile: str)` (method) — Stop the profile gateway service and remove its directory.
- L917 `list_profile_gateways(self)` (method) — Return the profile names of all currently-registered gateway services.
