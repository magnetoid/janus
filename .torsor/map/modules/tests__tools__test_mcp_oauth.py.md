---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_oauth.py

Symbols in `tests/tools/test_mcp_oauth.py`.

- L33 `TestHermesTokenStorage` (class)
- L34 `test_roundtrip_tokens(self, tmp_path, monkeypatch)` (method)
- L59 `test_token_file_created_with_0o600(self, tmp_path, monkeypatch)` (method) — Tokens must land on disk at 0o600 with no umask-default exposure window.
- L89 `test_roundtrip_client_info(self, tmp_path, monkeypatch)` (method)
- L106 `test_remove_cleans_up(self, tmp_path, monkeypatch)` (method)
- L120 `test_has_cached_tokens(self, tmp_path, monkeypatch)` (method)
- L132 `test_corrupt_tokens_returns_none(self, tmp_path, monkeypatch)` (method)
- L143 `test_corrupt_client_info_returns_none(self, tmp_path, monkeypatch)` (method)
- L159 `TestBuildOAuthAuth` (class)
- L160 `test_returns_oauth_provider(self, tmp_path, monkeypatch)` (method)
- L170 `test_returns_none_without_sdk(self, monkeypatch)` (method)
- L176 `test_pre_registered_client_id_stored(self, tmp_path, monkeypatch)` (method)
- L195 `test_scope_passed_through(self, tmp_path, monkeypatch)` (method)
- L213 `TestUtilities` (class)
- L214 `test_find_free_port_returns_int(self)` (method)
- L219 `test_find_free_port_unique(self)` (method) — Two consecutive calls should return different ports (usually).
- L225 `test_can_open_browser_false_in_ssh(self, monkeypatch)` (method)
- L229 `test_can_open_browser_false_without_display(self, monkeypatch)` (method)
- L239 `test_can_open_browser_true_with_display(self, monkeypatch)` (method)
- L247 `TestRedirectHandlerSshHint` (class) — _redirect_handler must print an SSH tunnel hint on remote sessions.
- L250 `_run(self, coro)` (method)
- L253 `test_ssh_hint_shown_on_ssh_session(self, monkeypatch, capsys)` (method)
- L267 `test_ssh_hint_shown_via_ssh_tty(self, monkeypatch, capsys)` (method)
- L280 `test_no_ssh_hint_on_local_session(self, monkeypatch, capsys)` (method)
- L293 `test_no_ssh_hint_when_port_not_set(self, monkeypatch, capsys)` (method)
- L309 `TestPathTraversal` (class) — Verify server_name is sanitized to prevent path traversal.
- L312 `test_path_traversal_blocked(self, tmp_path, monkeypatch)` (method)
- L320 `test_dots_and_slashes_sanitized(self, tmp_path, monkeypatch)` (method)
- L327 `test_normal_name_unchanged(self, tmp_path, monkeypatch)` (method)
- L332 `test_special_chars_sanitized(self, tmp_path, monkeypatch)` (method)
- L345 `TestCallbackHandlerIsolation` (class) — Verify concurrent OAuth flows don't share state.
- L348 `test_independent_result_dicts(self)` (method)
- L358 `test_handler_writes_to_own_result(self)` (method)
- L374 `test_handler_captures_error(self)` (method)
- L393 `TestOAuthPortSharing` (class) — Verify build_oauth_auth and _wait_for_callback use the same port.
- L396 `test_port_stored_globally(self, tmp_path, monkeypatch)` (method)
- L416 `TestRemoveOAuthTokens` (class)
- L417 `test_removes_files(self, tmp_path, monkeypatch)` (method)
- L429 `test_no_error_when_files_missing(self, tmp_path, monkeypatch)` (method)
- L438 `TestIsInteractive` (class) — _is_interactive() detects headless/daemon/container environments.
- L441 `test_false_when_stdin_not_tty(self, monkeypatch)` (method)
- L447 `test_true_when_stdin_is_tty(self, monkeypatch)` (method)
- L453 `test_false_when_stdin_has_no_isatty(self, monkeypatch)` (method) — Some environments replace stdin with an object without isatty().
- L460 `TestWaitForCallbackNoBlocking` (class) — _wait_for_callback() must never call input() — it raises instead.
- L463 `test_raises_on_timeout_instead_of_input(self)` (method) — When no auth code arrives, raises OAuthNonInteractiveError.
- L479 `TestBuildOAuthAuthNonInteractive` (class) — build_oauth_auth() in non-interactive mode.
- L482 `test_noninteractive_without_cached_tokens_warns(self, tmp_path, monkeypatch, caplog)` (method) — Without cached tokens, non-interactive mode logs a clear warning.
- L502 `test_noninteractive_with_cached_tokens_no_warning(self, tmp_path, monkeypatch, caplog)` (method) — With cached tokens, non-interactive mode logs no 'no cached tokens' warning.
- L535 `test_build_client_metadata_basic()` (function) — _build_client_metadata returns metadata with expected defaults.
- L549 `test_build_client_metadata_without_secret_is_public()` (function) — Without client_secret, token endpoint auth is 'none' (public client).
- L560 `test_build_client_metadata_with_secret_is_confidential()` (function) — With client_secret, token endpoint auth is 'client_secret_post'.
- L571 `test_configure_callback_port_picks_free_port()` (function) — _configure_callback_port(0) picks a free port in the ephemeral range.
- L581 `test_configure_callback_port_uses_explicit_port()` (function) — An explicit redirect_port is preserved.
- L591 `test_build_oauth_auth_preserves_server_url_path()` (function) — server_url with path is forwarded to OAuthClientProvider unmodified.
- L625 `TestPasteCallbackReader` (class) — _paste_callback_reader parses redirect URLs / query strings from stdin.
- L628 `_empty_result(self)` (method)
- L631 `test_parses_full_local_redirect_url(self, monkeypatch)` (method)
- L642 `test_parses_remote_provider_url(self, monkeypatch)` (method) — User pastes the URL their browser ended up on, including a real host.
- L651 `test_parses_bare_query_string(self, monkeypatch)` (method)
- L661 `test_parses_leading_question_mark(self, monkeypatch)` (method)
- L671 `test_captures_error_param(self, monkeypatch)` (method)
- L681 `test_empty_input_noop(self, monkeypatch)` (method)
- L688 `test_garbage_input_noop(self, monkeypatch, capsys)` (method)
- L699 `test_skips_when_http_listener_already_won(self, monkeypatch)` (method) — If HTTP listener filled the result first, paste must not overwrite.
- L710 `test_swallows_stdin_errors(self, monkeypatch)` (method) — OSError / interrupt on readline must not propagate.
- L720 `TestWaitForCallbackPasteIntegration` (class) — _wait_for_callback offers the paste prompt only when interactive.
- L723 `test_paste_prompt_shown_on_tty(self, monkeypatch, capsys)` (method)
- L742 `test_paste_prompt_NOT_shown_when_noninteractive(self, monkeypatch, capsys)` (method) — Preserves existing invariant: no input() / paste prompt in headless runs.
- L758 `TestPasteCallbackSkipToken` (class) — User can type `skip` (or similar) at the paste prompt to bail out.
- L761 `_empty_result(self)` (method)
- L765 `test_skip_tokens_set_sentinel(self, monkeypatch, token)` (method)
- L773 `test_skip_message_printed(self, monkeypatch, capsys)` (method)
- L781 `test_skip_does_not_overwrite_http_winner(self, monkeypatch)` (method) — If HTTP listener already wrote a code, `skip` must not stomp it.
- L789 `test_skip_token_not_parsed_as_url(self, monkeypatch, capsys)` (method) — `skip` must NOT fall through to URL parsing (which would silently no-op).
- L801 `TestWaitForCallbackSkipIntegration` (class) — _wait_for_callback maps the skip sentinel to OAuthNonInteractiveError.
- L804 `test_skip_raises_non_interactive_error(self, monkeypatch)` (method) — Skip token must raise OAuthNonInteractiveError (mcp_tool handles as non-fatal).
- L817 `test_paste_prompt_mentions_skip(self, monkeypatch, capsys)` (method) — The interactive prompt must tell users about the skip option.
