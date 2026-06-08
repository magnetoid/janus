---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_hermes_state_wal_fallback.py

Symbols in `tests/test_hermes_state_wal_fallback.py`.

- L34 `_make_blocking_factory(reason: str, attempt_counter: list)` (function) — Return a sqlite3.Connection subclass that raises on PRAGMA journal_mode=WAL.
- L47 `_open_blocking(path, reason='locking protocol', **kwargs)` (function) — Open a connection whose WAL pragma raises ``reason``.
- L59 `_reset_last_init_error()` (function) — Reset the module-global last-error before and after each test.
- L67 `_reset_wal_fallback_warned_paths()` (function) — Reset the WAL-fallback warned-paths set so dedup doesn't leak between tests.
- L74 `TestApplyWalWithFallback` (class)
- L75 `test_succeeds_on_local_fs(self, tmp_path)` (method) — Happy path: WAL works on a normal filesystem.
- L84 `test_falls_back_to_delete_on_locking_protocol(self, tmp_path, caplog)` (method) — NFS-style ``locking protocol`` error → DELETE mode + one WARNING.
- L104 `test_falls_back_on_not_authorized(self, tmp_path)` (method) — Some FUSE mounts block WAL pragma outright ('not authorized').
- L113 `test_reraises_on_disk_io_error(self, tmp_path)` (method) — Transient EIO from ``PRAGMA journal_mode=WAL`` must NOT silently
- L133 `test_does_not_downgrade_when_disk_says_wal(self, tmp_path)` (method) — Refuse to downgrade an already-WAL DB even if the set-pragma path
- L186 `test_reraises_unrelated_operational_error(self, tmp_path)` (method) — Non-WAL-compat errors must NOT be silently swallowed by the fallback.
- L197 `test_warning_deduplicated_per_db_label(self, tmp_path, caplog)` (method) — Repeated calls with the same db_label log exactly ONE warning.
- L226 `test_warning_fires_independently_per_db_label(self, tmp_path, caplog)` (method) — Different db_labels each get their own one warning (not globally dedup'd).
- L247 `TestGetLastInitError` (class)
- L248 `test_none_on_successful_init(self, tmp_path)` (method) — Happy-path SessionDB init does NOT clear a stale error from a prior thread.
- L265 `test_success_does_not_clear_prior_error(self, tmp_path)` (method) — Thread-safety guard: a successful init must not erase a pre-existing error.
- L280 `test_captures_cause_on_failed_init(self, tmp_path)` (method) — When SessionDB() raises, the cause is preserved for slash commands.
- L312 `TestFormatSessionDbUnavailable` (class)
- L313 `test_bare_message_when_no_cause(self)` (method) — No init error recorded → generic message.
- L318 `test_includes_cause(self)` (method) — Cause is surfaced for slash-command error strings.
- L326 `test_adds_nfs_hint_for_locking_protocol(self)` (method) — Locking-protocol cause gets an NFS/SMB pointer for the user.
- L334 `test_custom_prefix(self)` (method) — Callers can customize the prefix for context-specific messages.
- L341 `TestSessionDbUsesWalFallback` (class)
- L342 `test_sessiondb_works_when_wal_unavailable(self, tmp_path)` (method) — E2E: SessionDB initializes and performs a write on a WAL-blocked FS.
