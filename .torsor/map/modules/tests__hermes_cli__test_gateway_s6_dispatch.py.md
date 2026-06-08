---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_gateway_s6_dispatch.py

Symbols in `tests/hermes_cli/test_gateway_s6_dispatch.py`.

- L14 `_CallRecorder` (class) — Minimal stand-in for S6ServiceManager.
- L18 `__init__(self)` (method)
- L21 `start(self, name: str)` (method)
- L24 `stop(self, name: str)` (method)
- L27 `restart(self, name: str)` (method)
- L31 `test_dispatch_returns_false_on_host(monkeypatch: pytest.MonkeyPatch)` (function) — When the environment isn't s6 (host run), the helper must
- L47 `test_dispatch_returns_true_and_calls_start_on_s6(monkeypatch: pytest.MonkeyPatch)` (function)
- L67 `test_dispatch_translates_action_to_manager_method(monkeypatch: pytest.MonkeyPatch, action: str, expected: str)` (function)
- L82 `test_dispatch_unknown_action_returns_false(monkeypatch: pytest.MonkeyPatch)` (function) — An unrecognized action (e.g. 'install') must not silently
- L99 `test_dispatch_defaults_profile_to_default(monkeypatch: pytest.MonkeyPatch)` (function) — When profile is None, the helper resolves it via _profile_arg().
- L124 `_ListingRecorder` (class) — _CallRecorder that also exposes a profile list.
- L127 `__init__(self, profiles: list[str])` (method)
- L131 `list_profile_gateways(self)` (method)
- L135 `test_dispatch_all_returns_false_on_host(monkeypatch: pytest.MonkeyPatch)` (function)
- L149 `test_dispatch_all_iterates_every_profile_on_stop(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function)
- L171 `test_dispatch_all_iterates_every_profile_on_restart(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function)
- L192 `test_dispatch_all_handles_partial_failure(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function) — A failure on one profile must not skip the others; the helper
- L224 `test_dispatch_all_empty_list_reports_and_returns_true(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function) — With no profile gateways registered the helper still claims the
- L245 `test_dispatch_all_unknown_action_returns_false(monkeypatch: pytest.MonkeyPatch)` (function) — `start --all` is not a supported CLI surface; the helper must
- L269 `test_dispatch_renders_gateway_not_registered_friendly(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function) — `hermes -p typo gateway start` should print a clear message and
- L301 `test_dispatch_renders_s6_command_error_friendly(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture)` (function) — An s6-svc failure (e.g. EACCES on the supervise FIFO) should
- L343 `_Args` (class) — Lightweight argparse-like namespace for the helper.
- L346 `__init__(self, no_supervise: bool=False)` (method)
- L350 `_stub_s6(monkeypatch: pytest.MonkeyPatch, *, on_s6: bool)` (function) — Wire up service-manager stubs so the underlying dispatcher will
- L364 `test_redirect_noop_on_host(monkeypatch: pytest.MonkeyPatch)` (function) — Host runs (non-s6) must not redirect. Returns False; caller
- L381 `test_redirect_fires_inside_s6_container(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str])` (function) — Inside an s6 container, `gateway run` should:
- L431 `test_redirect_falls_back_when_sleep_missing(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str])` (function) — Regression guard for issue #36208: when ``os.execvp("sleep", ...)``
- L468 `test_block_until_terminated_installs_sigterm_handler_and_blocks(monkeypatch: pytest.MonkeyPatch)` (function) — ``_block_until_terminated`` must register a SIGTERM handler (so
- L510 `test_redirect_short_circuits_supervised_child(monkeypatch: pytest.MonkeyPatch)` (function) — The recursion guard: when the supervised gateway s6-supervise is
- L536 `test_redirect_respects_no_supervise_flag(monkeypatch: pytest.MonkeyPatch)` (function) — `--no-supervise` (CLI flag) must skip the redirect even inside
- L558 `test_redirect_respects_no_supervise_env(monkeypatch: pytest.MonkeyPatch, value: str)` (function) — `HERMES_GATEWAY_NO_SUPERVISE=1` (env var) must skip the redirect.
- L582 `test_redirect_no_supervise_env_falsy_values_dont_opt_out(monkeypatch: pytest.MonkeyPatch)` (function) — Falsy / unrecognized values of HERMES_GATEWAY_NO_SUPERVISE must
