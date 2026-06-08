---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_debug.py

Symbols in `tests/hermes_cli/test_debug.py`.

- L14 `hermes_home(tmp_path, monkeypatch)` (function) — Set up an isolated HERMES_HOME with minimal logs.
- L45 `TestUploadPasteRs` (class) — Test paste.rs upload path.
- L48 `test_upload_paste_rs_success(self)` (method)
- L61 `test_upload_paste_rs_bad_response(self)` (method)
- L73 `test_upload_paste_rs_network_error(self)` (method)
- L84 `TestUploadDpasteCom` (class) — Test dpaste.com fallback upload path.
- L87 `test_upload_dpaste_com_success(self)` (method)
- L101 `TestUploadToPastebin` (class) — Test the combined upload with fallback.
- L104 `test_tries_paste_rs_first(self)` (method)
- L114 `test_falls_back_to_dpaste_com(self)` (method)
- L126 `test_raises_when_both_fail(self)` (method)
- L141 `TestCaptureLogSnapshot` (class) — Test _capture_log_snapshot for log reading and truncation.
- L144 `test_reads_small_file(self, hermes_home)` (method)
- L152 `test_returns_none_for_missing(self, tmp_path, monkeypatch)` (method)
- L162 `test_empty_primary_reports_file_empty(self, hermes_home)` (method) — Empty primary (no .1 fallback) surfaces as '(file empty)', not missing.
- L171 `test_race_truncate_after_resolve_reports_empty(self, hermes_home, monkeypatch)` (method) — If the log is truncated between resolve and stat, say 'empty', not 'missing'.
- L184 `test_truncates_large_file(self, hermes_home)` (method) — Files larger than max_bytes get tail-truncated.
- L196 `test_keeps_first_line_when_truncation_on_boundary(self, hermes_home)` (method) — When truncation lands on a line boundary, keep the first full line.
- L215 `test_drops_partial_when_truncation_mid_line(self, hermes_home)` (method) — When truncation lands mid-line, drop the partial fragment.
- L232 `test_unknown_log_returns_none(self, hermes_home)` (method)
- L237 `test_falls_back_to_rotated_file(self, hermes_home)` (method) — When gateway.log doesn't exist, falls back to gateway.log.1.
- L252 `test_prefers_primary_over_rotated(self, hermes_home)` (method) — Primary log is used when it exists, even if .1 also exists.
- L264 `test_falls_back_when_primary_empty(self, hermes_home)` (method) — Empty primary log falls back to .1 rotation.
- L286 `TestCaptureLogSnapshotRedaction` (class) — Pin upload-time redaction at the _capture_log_snapshot boundary.
- L290 `hermes_home_with_secret(self, tmp_path, monkeypatch)` (method) — Isolated HERMES_HOME whose agent.log contains a vendor-prefixed token.
- L311 `test_default_redacts_tail_and_full_text(self, hermes_home_with_secret)` (method)
- L321 `test_redact_false_passes_through(self, hermes_home_with_secret)` (method)
- L330 `test_force_true_works_when_redaction_disabled(self, hermes_home_with_secret, monkeypatch)` (method) — Regression test: redact_sensitive_text short-circuits without force=True.
- L356 `test_default_redacts_email_addresses_for_public_share(self, hermes_home_with_secret)` (method)
- L375 `test_no_redact_preserves_email_addresses(self, hermes_home_with_secret)` (method)
- L390 `test_capture_default_log_snapshots_threads_redact(self, hermes_home_with_secret)` (method)
- L401 `test_capture_default_log_snapshots_no_redact_passes_through(self, hermes_home_with_secret)` (method)
- L416 `TestCollectDebugReport` (class) — Test the debug report builder.
- L419 `test_report_includes_dump_output(self, hermes_home)` (method)
- L431 `test_report_includes_agent_log(self, hermes_home)` (method)
- L440 `test_report_includes_errors_log(self, hermes_home)` (method)
- L449 `test_report_includes_gateway_log(self, hermes_home)` (method)
- L457 `test_report_includes_desktop_log(self, hermes_home)` (method)
- L466 `test_missing_logs_handled(self, tmp_path, monkeypatch)` (method)
- L483 `TestRunDebugShare` (class) — Test the run_debug_share CLI handler.
- L486 `test_share_sweeps_expired_pastes(self, hermes_home, capsys)` (method) — Slash-command path should sweep old pending deletes before uploading.
- L504 `test_share_survives_sweep_failure(self, hermes_home, capsys)` (method) — Expired-paste cleanup is best-effort and must not block sharing.
- L524 `test_local_flag_prints_full_logs(self, hermes_home, capsys)` (method) — --local prints the report plus full log contents.
- L541 `test_share_uploads_four_pastes(self, hermes_home, capsys)` (method) — Successful share uploads report + agent.log + gateway.log + desktop.log.
- L586 `test_share_keeps_report_and_full_log_on_same_snapshot(self, hermes_home, capsys)` (method) — A mid-run rotation must not make full agent.log older than the report.
- L635 `test_share_skips_missing_logs(self, tmp_path, monkeypatch, capsys)` (method) — Only uploads logs that exist.
- L663 `test_share_continues_on_log_upload_failure(self, hermes_home, capsys)` (method) — Log upload failure doesn't stop the report from being shared.
- L689 `test_share_exits_on_report_upload_failure(self, hermes_home, capsys)` (method) — If the main report fails to upload, exit with code 1.
- L713 `TestRunDebugShareRedaction` (class) — End-to-end: --no-redact flag, banner injection, default behavior.
- L717 `hermes_home_with_secret(self, tmp_path, monkeypatch)` (method) — Isolated HERMES_HOME whose agent.log contains a vendor-prefixed token.
- L735 `test_default_share_redacts_uploaded_content(self, hermes_home_with_secret, capsys)` (method) — The uploaded report and full-log pastes do not contain the raw token.
- L765 `test_default_share_includes_redaction_banner(self, hermes_home_with_secret, capsys)` (method) — Each upload-bound paste carries the visible redaction banner.
- L793 `test_no_redact_flag_disables_redaction_and_banner(self, hermes_home_with_secret, capsys)` (method) — --no-redact preserves original log content and omits the banner.
- L831 `TestRunDebug` (class)
- L832 `test_no_subcommand_shows_usage(self, capsys)` (method)
- L845 `test_share_subcommand_routes(self, hermes_home)` (method)
- L866 `TestExtractPasteId` (class)
- L867 `test_paste_rs_url(self)` (method)
- L871 `test_paste_rs_trailing_slash(self)` (method)
- L875 `test_http_variant(self)` (method)
- L879 `test_non_paste_rs_returns_none(self)` (method)
- L883 `test_empty_returns_none(self)` (method)
- L888 `TestDeletePaste` (class)
- L889 `test_delete_sends_delete_request(self)` (method)
- L906 `test_delete_rejects_non_paste_rs(self)` (method)
- L913 `TestScheduleAutoDelete` (class) — ``_schedule_auto_delete`` used to spawn a detached Python subprocess
- L925 `test_does_not_spawn_subprocess(self, hermes_home)` (method) — Regression guard: _schedule_auto_delete must NEVER spawn subprocesses.
- L987 `test_records_pending_to_json(self, hermes_home)` (method) — Scheduled URLs are persisted to pending.json with expiration.
- L1011 `test_skips_non_paste_rs_urls(self, hermes_home)` (method) — dpaste.com URLs auto-expire — don't track them.
- L1020 `test_merges_with_existing_pending(self, hermes_home)` (method) — Subsequent calls merge into existing pending.json.
- L1031 `test_dedupes_same_url(self, hermes_home)` (method) — Same URL recorded twice → one entry with the later expire_at.
- L1043 `TestSweepExpiredPastes` (class) — Test the opportunistic sweep that replaces the sleeping subprocess.
- L1046 `test_sweep_empty_is_noop(self, hermes_home)` (method)
- L1053 `test_sweep_deletes_expired_entries(self, hermes_home)` (method)
- L1084 `test_sweep_leaves_future_entries_alone(self, hermes_home)` (method)
- L1100 `test_sweep_survives_network_failure(self, hermes_home)` (method) — Failed DELETEs stay in pending.json until the 24h grace window.
- L1124 `test_sweep_drops_entries_past_grace_window(self, hermes_home)` (method) — After 24h past expiration, give up even on network failures.
- L1150 `TestRunDebugSweepsOnInvocation` (class) — ``run_debug`` must sweep expired pastes on every invocation.
- L1153 `test_run_debug_calls_sweep(self, hermes_home)` (method)
- L1164 `test_run_debug_survives_sweep_failure(self, hermes_home, capsys)` (method) — If the sweep throws, the subcommand still runs.
- L1182 `TestRunDebugDelete` (class)
- L1183 `test_deletes_valid_url(self, capsys)` (method)
- L1196 `test_handles_delete_failure(self, capsys)` (method)
- L1209 `test_no_urls_shows_usage(self, capsys)` (method)
- L1221 `TestShareIncludesAutoDelete` (class) — Verify that run_debug_share schedules auto-deletion and prints TTL.
- L1224 `test_share_schedules_auto_delete(self, hermes_home, capsys)` (method)
- L1246 `test_share_shows_privacy_notice(self, hermes_home, capsys)` (method)
- L1263 `test_local_no_privacy_notice(self, hermes_home, capsys)` (method)
- L1283 `TestBuildDebugShare` (class) — The shared core that returns structured paste URLs (not printed text).
- L1291 `test_returns_structured_urls(self, hermes_home)` (method)
- L1315 `test_skips_missing_logs_without_failure(self, hermes_home)` (method)
- L1330 `test_redaction_keeps_secrets_out_of_payload(self, hermes_home)` (method)
- L1353 `test_optional_log_failure_is_collected_not_raised(self, hermes_home)` (method)
- L1374 `test_required_report_failure_raises(self, hermes_home)` (method)
