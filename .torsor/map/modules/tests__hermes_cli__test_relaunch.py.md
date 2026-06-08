---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_relaunch.py

Symbols in `tests/hermes_cli/test_relaunch.py`.

- L10 `TestResolveHermesBin` (class)
- L11 `test_prefers_absolute_argv0_when_executable(self, monkeypatch)` (method)
- L18 `test_resolves_relative_argv0(self, monkeypatch, tmp_path)` (method)
- L28 `test_falls_back_to_path_which(self, monkeypatch)` (method)
- L35 `test_returns_none_when_unresolvable(self, monkeypatch)` (method)
- L41 `TestExtractInheritedFlags` (class)
- L42 `test_extracts_tui_and_dev(self)` (method)
- L46 `test_extracts_profile_with_value(self)` (method)
- L50 `test_extracts_short_p_with_value(self)` (method)
- L54 `test_extracts_equals_form(self)` (method)
- L61 `test_skips_unknown_flags(self)` (method)
- L65 `test_does_not_consume_flag_like_value(self)` (method)
- L69 `test_preserves_multiple_skills(self)` (method)
- L74 `TestInheritedFlagTable` (class) — Sanity-check the argparse-introspected table that drives extraction.
- L77 `test_short_and_long_aliases_are_paired(self)` (method)
- L87 `test_store_true_flags_do_not_take_value(self)` (method)
- L92 `test_value_flags_take_value(self)` (method)
- L97 `test_excluded_flags_are_not_inherited(self)` (method)
- L106 `TestBuildRelaunchArgv` (class)
- L107 `test_uses_bin_when_available(self, monkeypatch)` (method)
- L112 `test_falls_back_to_python_module(self, monkeypatch)` (method)
- L117 `test_preserves_inherited_flags(self, monkeypatch)` (method)
- L131 `test_can_disable_preserve(self, monkeypatch)` (method)
- L141 `TestRelaunch` (class)
- L142 `test_calls_execvp(self, monkeypatch)` (method)
- L157 `test_windows_uses_subprocess_not_execvp(self, monkeypatch)` (method) — On Windows, os.execvp raises OSError "Exec format error" when the
- L193 `test_windows_propagates_child_exit_code(self, monkeypatch)` (method) — A non-zero exit from the child should flow through to sys.exit.
- L212 `test_windows_surfaces_oserror_with_help(self, monkeypatch, capsys)` (method) — When subprocess itself raises OSError (file-not-found / bad format),
- L235 `TestResolveHermesBinWindowsPyGuard` (class) — On Windows, resolve_hermes_bin MUST NOT return a .py path.
- L243 `test_windows_rejects_py_argv0_falls_through_to_path(self, monkeypatch, tmp_path)` (method) — On Windows, if sys.argv[0] is a .py file, we must skip the
- L263 `test_posix_still_accepts_py_argv0(self, monkeypatch, tmp_path)` (method) — POSIX behaviour unchanged: argv[0] pointing at an executable
- L275 `test_windows_py_argv0_with_no_hermes_on_path_returns_none(self, monkeypatch, tmp_path)` (method) — Bulletproof fallback: if argv0 is .py on Windows AND hermes.exe
