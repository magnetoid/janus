---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_dashboard.py

Symbols in `tests/docker/test_dashboard.py`.

- L22 `_poll(container: str, probe: str, *, deadline_s: float=30.0, interval_s: float=0.5)` (function) — Repeatedly run ``probe`` inside the container until it exits 0 or
- L37 `test_dashboard_not_running_by_default(built_image: str, container_name: str)` (function) — Without HERMES_DASHBOARD, no dashboard process should be running.
- L56 `test_dashboard_slot_reports_down_when_disabled(built_image: str, container_name: str)` (function) — Without HERMES_DASHBOARD, s6-svstat should report the dashboard
- L85 `test_dashboard_slot_reports_up_when_enabled(built_image: str, container_name: str)` (function) — Symmetry: with HERMES_DASHBOARD=1, s6-svstat reports the slot as up.
- L118 `test_dashboard_opt_in_starts(built_image: str, container_name: str)` (function) — With HERMES_DASHBOARD=1, a dashboard process should be visible.
- L141 `test_dashboard_port_override(built_image: str, container_name: str)` (function) — HERMES_DASHBOARD_PORT changes the dashboard's listen port.
- L168 `test_dashboard_restarts_after_crash(built_image: str, container_name: str)` (function) — Phase 2 invariant: under s6 supervision, killing the dashboard
- L240 `_http_probe(container: str, path: str, *, deadline_s: float=60.0)` (function) — Poll ``http://127.0.0.1:9119<path>`` from inside the container.
- L305 `test_dashboard_oauth_gate_engages_on_non_loopback_bind(built_image: str, container_name: str)` (function) — The s6 dashboard run script must NOT auto-add ``--insecure`` when the
- L386 `test_dashboard_insecure_env_var_opts_out_of_gate(built_image: str, container_name: str)` (function) — ``HERMES_DASHBOARD_INSECURE=1`` re-enables the legacy no-gate mode
