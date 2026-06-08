---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_hardline_blocklist.py

Symbols in `tests/tools/test_hardline_blocklist.py`.

- L140 `test_hardline_detection_blocks(command)` (function)
- L147 `test_hardline_detection_allows(command)` (function)
- L158 `clean_session(monkeypatch)` (function) — Reset session-scoped approval state around each test.
- L174 `test_check_dangerous_command_blocks_hardline(clean_session)` (function)
- L181 `test_check_all_command_guards_blocks_hardline(clean_session)` (function)
- L188 `test_yolo_env_var_cannot_bypass_hardline(clean_session, monkeypatch)` (function) — HERMES_YOLO_MODE=1 must not bypass the hardline floor.
- L202 `test_session_yolo_cannot_bypass_hardline(clean_session)` (function) — Gateway /yolo (session-scoped) must not bypass the hardline floor.
- L215 `test_approvals_mode_off_cannot_bypass_hardline(clean_session, monkeypatch, tmp_path)` (function) — config approvals.mode=off (yolo-equivalent) must not bypass hardline.
- L226 `test_cron_approve_mode_cannot_bypass_hardline(clean_session, monkeypatch)` (function) — Cron sessions with cron_mode=approve must not bypass hardline.
- L237 `test_container_backends_still_bypass(clean_session)` (function) — Containerized backends remain bypass-approved — they can't touch the host.
- L249 `test_hardline_runs_before_dangerous_detection(clean_session)` (function) — Hardline command should return hardline block, not dangerous approval prompt.
- L259 `test_recoverable_dangerous_commands_still_pass_yolo(clean_session, monkeypatch)` (function) — Yolo still bypasses the regular DANGEROUS_PATTERNS list.
- L279 `test_hardline_list_is_small()` (function) — Hardline list stays focused on unrecoverable commands only.
- L322 `test_sudo_stdin_guard_detects_without_password()` (function) — sudo -S is dangerous when SUDO_PASSWORD is not configured.
- L332 `test_sudo_stdin_guard_allows_benign_commands()` (function) — Commands without explicit sudo -S are not blocked.
- L341 `test_sudo_stdin_guard_bypassed_when_password_configured(monkeypatch)` (function) — When SUDO_PASSWORD is set, sudo -S is legitimate (injected by transform).
- L351 `test_sudo_stdin_guard_blocks_via_check_all_command_guards(clean_session)` (function) — Integration: check_all_command_guards returns block for sudo -S.
- L362 `test_sudo_stdin_guard_not_blocked_by_yolo(clean_session, monkeypatch)` (function) — yolo/approvals.mode=off must NOT bypass sudo stdin guard.
- L371 `test_sudo_stdin_guard_container_bypass(clean_session)` (function) — Containerized backends still bypass — they can't touch the host.
