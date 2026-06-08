---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/debug.py

Symbols in `hermes_cli/debug.py`.

- L64 `_pending_file()` (function) — Path to ``~/.hermes/pastes/pending.json``.
- L81 `_load_pending()` (function)
- L98 `_save_pending(entries: list[dict])` (function)
- L111 `_record_pending(urls: list[str], delay_seconds: int=_AUTO_DELETE_SECONDS)` (function) — Record *urls* for deletion at ``now + delay_seconds``.
- L131 `_sweep_expired_pastes(now: Optional[float]=None)` (function) — Synchronously DELETE any pending pastes whose ``expire_at`` has passed.
- L178 `_best_effort_sweep_expired_pastes()` (function) — Attempt pending-paste cleanup without letting /debug fail offline.
- L211 `_extract_paste_id(url: str)` (function) — Extract the paste ID from a paste.rs or dpaste.com URL.
- L223 `delete_paste(url: str)` (function) — Delete a paste from paste.rs.  Returns True on success.
- L244 `_schedule_auto_delete(urls: list[str], delay_seconds: int=_AUTO_DELETE_SECONDS)` (function) — Record *urls* for deletion ``delay_seconds`` from now.
- L261 `_upload_paste_rs(content: str)` (function) — Upload to paste.rs.  Returns the paste URL.
- L281 `_upload_dpaste_com(content: str, expiry_days: int=7)` (function) — Upload to dpaste.com.  Returns the paste URL.
- L317 `upload_to_pastebin(content: str, expiry_days: int=7)` (function) — Upload *content* to a paste service, trying paste.rs then dpaste.com.
- L347 `LogSnapshot` (class) — Single-read snapshot of a log file used by debug-share.
- L355 `_primary_log_path(log_name: str)` (function) — Where *log_name* would live if present. Doesn't check existence.
- L363 `_resolve_log_path(log_name: str)` (function) — Find the log file for *log_name*, falling back to the .1 rotation.
- L384 `_redact_log_text(text: str)` (function) — Run ``redact_sensitive_text`` with ``force=True`` over upload-bound text.
- L401 `_capture_log_snapshot(log_name: str, *, tail_lines: int, max_bytes: int=_MAX_LOG_BYTES, redact: bool=True)` (function) — Capture a log once and derive summary/full-log views from it.
- L487 `_capture_default_log_snapshots(log_lines: int, *, redact: bool=True)` (function) — Capture all logs used by debug-share exactly once.
- L516 `_capture_dump()` (function) — Run ``hermes dump`` and return its stdout as a string.
- L535 `collect_debug_report(*, log_lines: int=200, dump_text: str='', log_snapshots: Optional[dict[str, LogSnapshot]]=None)` (function) — Build the summary debug report: system dump + log tails.
- L589 `DebugShareResult` (class) — Structured outcome of a ``debug share`` upload.
- L604 `build_debug_share(*, log_lines: int=200, expiry: int=7, redact: bool=True)` (function) — Collect the debug report + full logs, upload each, return the URLs.
- L694 `run_debug_share(args)` (function) — Collect debug report + full logs, upload each, print URLs.
- L776 `run_debug_delete(args)` (function) — Delete one or more paste URLs uploaded by /debug.
- L797 `run_debug(args)` (function) — Route debug subcommands.
