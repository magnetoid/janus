---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/shutdown_forensics.py

Symbols in `gateway/shutdown_forensics.py`.

- L37 `_signal_name(sig: Any)` (function) — Return a human-readable signal name (or ``str(sig)`` as fallback).
- L48 `_read_proc_field(pid: int, key: str)` (function) — Read a single field from /proc/<pid>/status.  Linux only; None elsewhere.
- L60 `_read_proc_cmdline(pid: int)` (function) — Read /proc/<pid>/cmdline as a printable string.  Linux only; None elsewhere.
- L73 `_proc_summary(pid: int)` (function) — Compact /proc/<pid> snapshot: pid, ppid, state, uid, cmdline.
- L104 `snapshot_shutdown_context(received_signal: Any=None)` (function) — Fast (<10ms) snapshot of who/what is asking us to shut down.
- L197 `spawn_async_diagnostic(log_path: Path, signal_name: str, *, timeout_seconds: float=5.0)` (function) — Fire-and-forget ``ps``-style snapshot written to ``log_path``.
- L281 `format_context_for_log(ctx: Dict[str, Any])` (function) — Render a shutdown context dict as a single, scannable log line.
- L314 `context_as_json(ctx: Dict[str, Any])` (function) — JSON-serialise a context dict for structured ingestion.  Never raises.
- L322 `check_systemd_timing_alignment(drain_timeout: float)` (function) — At startup, sanity-check that systemd's TimeoutStopSec >= drain_timeout.
- L409 `_parse_systemd_duration_to_us(raw: str)` (function) — Parse 'TimeoutStopUSec=1min 30s' / '90s' style values to microseconds.
