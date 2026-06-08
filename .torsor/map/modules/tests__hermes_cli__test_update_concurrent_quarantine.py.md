---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_concurrent_quarantine.py

Symbols in `tests/hermes_cli/test_update_concurrent_quarantine.py`.

- L34 `_make_proc(pid: int, exe: str, name: str='hermes.exe')` (function) — Build a duck-typed psutil Process stand-in with the .info dict.
- L42 `test_detect_concurrent_returns_empty_when_no_other_processes(_winp, tmp_path)` (function)
- L55 `test_detect_concurrent_excludes_self_pid(_winp, tmp_path)` (function)
- L70 `test_detect_concurrent_finds_other_hermes_process(_winp, tmp_path)` (function)
- L88 `test_detect_concurrent_matches_case_insensitively(_winp, tmp_path)` (function)
- L104 `test_detect_concurrent_no_psutil_returns_empty(_winp, tmp_path)` (function)
- L116 `test_detect_concurrent_is_noop_off_windows(_winp, tmp_path)` (function) — No process enumeration off-Windows; the file-lock issue is Windows-only.
- L128 `_fake_psutil_with_parent_chain(parent_chain: list[int], proc_iter_rows: list, *, ancestor_exe: str | None=None)` (function) — Build a psutil stand-in that has Process()/parents()/exe() AND process_iter().
- L175 `test_detect_concurrent_excludes_parent_chain(_winp, tmp_path)` (function) — The .exe launcher (parent of os.getpid()) must NOT be flagged.
- L205 `test_detect_concurrent_still_finds_unrelated_other_hermes(_winp, tmp_path)` (function) — A sibling hermes.exe outside our ancestor chain must still be reported.
- L231 `test_detect_concurrent_parent_chain_walks_deep(_winp, tmp_path)` (function) — Multi-level ancestry (shell → launcher → python) is fully excluded.
- L259 `test_detect_concurrent_parents_call_robust_to_one_bad_hop(_winp, tmp_path)` (function) — The launcher shim is still excluded even when an ancestor exe is unreadable.
- L294 `test_detect_concurrent_parent_walk_handles_stub_without_process(_winp, tmp_path)` (function) — Partially-stubbed psutil (no Process attr) must NOT crash the helper.
- L325 `test_format_message_mentions_pids_and_remediation(tmp_path)` (function)
- L349 `test_quarantine_succeeds_first_attempt(_winp, tmp_path)` (function) — When the rename works immediately, no warning, single rename pair returned.
- L365 `test_quarantine_retries_then_succeeds(_winp, tmp_path, monkeypatch)` (function) — A transient OSError on the first attempt should not be fatal.
- L392 `test_quarantine_falls_back_to_reboot_schedule(_winp, tmp_path, capsys, monkeypatch)` (function) — When every retry fails, we schedule via MoveFileEx and warn helpfully.
- L425 `test_quarantine_actionable_warning_when_everything_fails(_winp, tmp_path, capsys, monkeypatch)` (function) — When even MoveFileEx fails we should print remediation hints, not a bare error.
- L455 `test_cmd_update_aborts_on_concurrent_instance(_winp, tmp_path, capsys)` (function) — If another hermes.exe is running, the update bails out before
- L497 `test_cmd_update_force_bypasses_concurrent_check(_winp, tmp_path)` (function) — --force lets the update proceed past the concurrent-instance gate
