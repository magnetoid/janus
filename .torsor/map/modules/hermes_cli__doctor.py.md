---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/doctor.py

Symbols in `hermes_cli/doctor.py`.

- L60 `_python_install_cmd()` (function)
- L64 `_system_package_install_cmd(pkg: str)` (function)
- L72 `_safe_which(cmd: str)` (function) — shutil.which wrapper resilient to platform monkeypatching in tests.
- L80 `_termux_browser_setup_steps(node_installed: bool)` (function)
- L91 `_termux_install_all_fallback_notes()` (function)
- L100 `_has_provider_env_config(content: str)` (function) — Return True when ~/.hermes/.env contains provider auth/base URL settings.
- L105 `_honcho_is_configured_for_doctor()` (function) — Return True when Honcho is configured, even if this process has no active session.
- L116 `_is_kanban_worker_env_gate(item: dict)` (function) — Return True when Kanban is unavailable only because this is not a worker process.
- L127 `_doctor_tool_availability_detail(toolset: str)` (function) — Optional explanatory suffix for toolsets whose doctor status needs context.
- L134 `_apply_doctor_tool_availability_overrides(available: list[str], unavailable: list[dict])` (function) — Adjust runtime-gated tool availability for doctor diagnostics.
- L152 `_has_healthy_oauth_fallback_for_apikey_provider(provider_label: str)` (function) — Return True when a direct API-key probe failure is non-blocking.
- L182 `check_ok(text: str, detail: str='')` (function)
- L185 `check_warn(text: str, detail: str='')` (function)
- L188 `check_fail(text: str, detail: str='')` (function)
- L191 `check_info(text: str)` (function)
- L195 `_section(title: str)` (function) — Print a doctor section banner: blank line + bold cyan ◆ title.
- L201 `_fail_and_issue(text: str, detail: str, fix: str, issues: list[str])` (function) — Emit a check_fail and append the corresponding fix instruction.
- L207 `_read_pyproject_version()` (function) — Read the ``version = "..."`` from ``pyproject.toml`` at the project root.
- L233 `_check_version_consistency(issues: list[str])` (function) — Verify pyproject.toml version matches hermes_cli.__version__.
- L261 `_check_s6_supervision(issues: list[str])` (function) — Inside a container under our s6 /init, surface what s6 sees.
- L309 `_check_gateway_service_linger(issues: list[str])` (function) — Warn when a systemd user gateway service will stop after logout.
- L356 `_build_apikey_providers_list()` (function) — Build the API-key provider health-check list once and cache it.
- L448 `run_doctor(args)` (function) — Run diagnostic checks.
