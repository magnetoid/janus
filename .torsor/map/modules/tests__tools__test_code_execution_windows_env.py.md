---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_code_execution_windows_env.py

Symbols in `tests/tools/test_code_execution_windows_env.py`.

- L37 `_no_passthrough(_name)` (function)
- L41 `TestWindowsEssentialAllowlist` (class) — The allowlist itself — contents, shape, and invariants.
- L44 `test_contains_winsock_required_vars(self)` (method)
- L48 `test_contains_subprocess_required_vars(self)` (method)
- L52 `test_contains_user_profile_vars(self)` (method)
- L58 `test_contains_only_uppercase_names(self)` (method)
- L64 `test_no_overlap_with_secret_substrings(self)` (method)
- L75 `TestScrubChildEnvWindows` (class) — Verify _scrub_child_env passes Windows essentials through when
- L80 `_sample_windows_env(self)` (method) — A realistic subset of what os.environ looks like on Windows.
- L102 `test_windows_essentials_passed_through_when_is_windows_true(self)` (method)
- L123 `test_secrets_still_blocked_on_windows(self)` (method) — The Windows allowlist must NOT defeat the secret-substring block.
- L139 `test_unknown_vars_still_dropped_on_windows(self)` (method)
- L146 `test_essentials_blocked_when_is_windows_false(self)` (method) — On POSIX hosts, Windows-specific vars should not pass — they
- L163 `test_case_insensitive_essential_match(self)` (method) — Windows env var names are case-insensitive at the OS level but
- L180 `TestScrubChildEnvPassthroughInteraction` (class) — The passthrough hook runs *before* the secret block, so a skill
- L185 `test_passthrough_wins_over_secret_block(self)` (method)
- L193 `test_passthrough_still_works_on_windows(self)` (method)
- L213 `TestWindowsSocketSmokeTest` (class) — Integration-ish smoke test: spawn a child Python with a scrubbed
- L219 `test_child_can_create_socket_with_scrubbed_env(self)` (method)
- L255 `_legacy_posix_scrubber(source_env, is_passthrough)` (function) — Independent oracle for TestPosixEquivalence — a from-scratch reimpl of
- L289 `TestPosixEquivalence` (class) — Lock in the invariant that _scrub_child_env(env, is_windows=False)
- L368 `test_posix_behavior_unchanged(self, env_name, env, pt_name, pt)` (method) — For every combination of (env shape × passthrough rule), the
- L386 `test_posix_behavior_unchanged_on_real_os_environ(self)` (method) — Bonus check against the actual os.environ of the host running
- L399 `test_windows_mode_is_strict_superset_of_posix_mode(self)` (method) — Correctness check on the NEW behavior: is_windows=True must
- L446 `TestSandboxWritesUtf8` (class) — Verify the file-write call sites use UTF-8 explicitly, not the
- L452 `test_stub_and_script_writes_specify_utf8(self)` (method) — Both ``hermes_tools.py`` and ``script.py`` writes in
- L472 `test_file_rpc_stub_uses_utf8(self)` (method) — The file-based RPC transport stub (used by remote backends)
- L484 `test_stub_source_roundtrips_through_utf8(self)` (method) — Concrete regression: write the generated stub to a temp file
- L524 `test_windows_default_encoding_would_have_failed(self)` (method) — Negative control: prove that on Windows, writing the stub
- L600 `TestChildStdioIsUtf8` (class) — Verify the sandbox child is spawned with UTF-8 stdio encoding,
- L604 `test_popen_env_sets_pythonioencoding_utf8(self)` (method) — Source-level check: the Popen call site must set
- L615 `test_popen_env_sets_pythonutf8_mode(self)` (method) — Source-level check: PYTHONUTF8=1 must be set too — it makes
- L626 `test_live_child_can_print_non_ascii(self)` (method) — Live regression: spawn a Python child with the same env
- L671 `test_windows_child_without_utf8_env_would_fail(self)` (method) — Negative control: spawn a Python child *without* our env
