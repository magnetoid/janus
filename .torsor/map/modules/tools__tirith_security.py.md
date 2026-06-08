---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/tirith_security.py

Symbols in `tools/tirith_security.py`.

- L51 `_env_bool(key: str, default: bool)` (function)
- L58 `_env_int(key: str, default: int)` (function)
- L68 `_load_security_config()` (function) — Load security settings from config.yaml, with env var overrides.
- L113 `_warn_once(key: str, message: str, *args)` (function) — ``logger.warning`` but at-most-once per ``key`` for the process
- L124 `_reset_spawn_warning_state()` (function) — Clear the warn-once dedupe set. Called when tirith is freshly
- L136 `_get_hermes_home()` (function) — Return the Hermes home directory, respecting HERMES_HOME env var.
- L141 `_failure_marker_path()` (function) — Return the path to the install-failure marker file.
- L146 `_read_failure_reason()` (function) — Read the failure reason from the disk marker.
- L163 `_is_install_failed_on_disk()` (function) — Check if a recent install failure was persisted to disk.
- L180 `_mark_install_failed(reason: str='')` (function) — Persist install failure to disk to avoid retry on next process.
- L197 `_clear_install_failed()` (function) — Remove the failure marker after successful install.
- L209 `_hermes_bin_dir()` (function) — Return $HERMES_HOME/bin, creating it if needed.
- L216 `_detect_target()` (function) — Return the Rust target triple for the current platform, or None.
- L244 `is_platform_supported()` (function) — True when tirith ships a prebuilt binary for this OS+arch.
- L254 `_download_file(url: str, dest: str, timeout: int=10)` (function) — Download a URL to a local file.
- L264 `_verify_cosign(checksums_path: str, sig_path: str, cert_path: str)` (function) — Verify cosign provenance signature on checksums.txt.
- L304 `_verify_checksum(archive_path: str, checksums_path: str, archive_name: str)` (function) — Verify SHA-256 of the archive against checksums.txt.
- L329 `_extract_tirith_binary(tar: tarfile.TarFile, dest_dir: str, log)` (function) — Extract the tirith binary from a release archive into dest_dir.
- L355 `_install_tirith(*, log_failures: bool=True)` (function) — Download and install tirith to $HERMES_HOME/bin/tirith.
- L453 `_is_explicit_path(configured_path: str)` (function) — Return True if the user explicitly configured a non-default tirith path.
- L458 `_resolve_tirith_path(configured_path: str)` (function) — Resolve the tirith binary path, auto-installing if necessary.
- L566 `_background_install(*, log_failures: bool=True)` (function) — Background thread target: download and install tirith.
- L598 `ensure_installed(*, log_failures: bool=True)` (function) — Ensure tirith is available, downloading in background if needed.
- L696 `check_command_security(command: str)` (function) — Run tirith security scan on a command.
- L806 `_is_app_tld_finding(finding: dict)` (function) — Return True if this finding is a lookalike_tld warning for the .app TLD only.
