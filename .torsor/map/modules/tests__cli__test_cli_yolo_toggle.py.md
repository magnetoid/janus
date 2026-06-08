---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_yolo_toggle.py

Symbols in `tests/cli/test_cli_yolo_toggle.py`.

- L40 `_clear_approval_state(monkeypatch)` (function) — Clear the YOLO bypass + env var around every test so cases are independent.
- L50 `_make_stand_in(session_id: str=SESSION_KEY)` (function) — Minimal stand-in exposing only ``session_id``.
- L63 `TestToggleYoloIsSessionScoped` (class) — The CLI /yolo handler must mutate the session-yolo set, not the env var.
- L71 `test_toggle_yolo_enables_session_bypass(self)` (method)
- L81 `test_toggle_yolo_disables_session_bypass_on_second_call(self)` (method)
- L89 `test_toggle_yolo_does_not_mutate_env_var(self)` (method) — Toggling /yolo must not write ``HERMES_YOLO_MODE`` — that path is
- L99 `test_toggle_yolo_falls_back_to_default_when_session_id_missing(self)` (method) — An edge case during CLI bootstrap: a ``/yolo`` triggered before the
- L110 `test_two_independent_sessions_are_isolated(self)` (method) — ``/yolo`` toggled in one session must not bypass approvals in
- L127 `TestIsSessionYoloActiveHelper` (class) — The status-bar helper must read the live session-yolo state, not the
- L131 `test_helper_reflects_toggle(self)` (method)
- L146 `test_helper_honors_frozen_yolo_mode(self)` (method) — ``hermes --yolo`` sets ``HERMES_YOLO_MODE`` before tool imports, so
- L156 `TestToggleYoloEndToEnd` (class) — End-to-end: a dangerous command must auto-approve through the same
- L160 `test_toggle_yolo_bypasses_dangerous_command_check(self)` (method)
- L178 `TestIsSessionYoloActiveAttrSafety` (class) — The status-bar helper runs against partially-constructed CLI fixtures
- L186 `test_helper_survives_missing_session_id_attr(self)` (method)
- L194 `TestSessionRotationTransfersYolo` (class) — When the CLI's ``session_id`` rotates mid-run (``/branch``, auto
- L201 `test_transfer_moves_yolo_to_new_session(self)` (method)
- L215 `test_transfer_is_noop_when_yolo_was_off(self)` (method)
- L225 `test_transfer_is_noop_when_ids_match(self)` (method)
- L236 `test_transfer_handles_empty_inputs_safely(self)` (method)
