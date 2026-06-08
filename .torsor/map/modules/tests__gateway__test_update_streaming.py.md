---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_update_streaming.py

Symbols in `tests/gateway/test_update_streaming.py`.

- L23 `_make_event(text='/update', platform=Platform.TELEGRAM, user_id='12345', chat_id='67890')` (function) — Build a MessageEvent for testing.
- L35 `_make_runner(hermes_home=None)` (function) — Create a bare GatewayRunner without calling __init__.
- L63 `TestGatewayPrompt` (class) — Tests for _gateway_prompt() function.
- L66 `test_writes_prompt_file_and_reads_response(self, tmp_path)` (method) — Writes .update_prompt.json, reads .update_response, returns answer.
- L90 `test_prompt_file_content(self, tmp_path)` (method) — Verifies the prompt JSON structure.
- L121 `test_timeout_returns_default(self, tmp_path)` (method) — Returns default when no response within timeout.
- L132 `test_empty_response_returns_default(self, tmp_path)` (method) — Empty response file returns default.
- L152 `TestRestoreStashWithInputFn` (class) — Tests for _restore_stashed_changes with the input_fn parameter.
- L155 `test_uses_input_fn_when_provided(self, tmp_path)` (method) — When input_fn is provided, it's called instead of input().
- L179 `test_input_fn_yes_proceeds_with_restore(self, tmp_path)` (method) — When input_fn returns 'y', stash apply is attempted.
- L209 `TestUpdateCommandGatewayFlag` (class) — Verify the gateway spawns hermes update --gateway.
- L213 `test_spawns_with_gateway_flag(self, tmp_path)` (method) — The spawned update command includes --gateway and PYTHONUNBUFFERED.
- L249 `TestWatchUpdateProgress` (class) — Tests for _watch_update_progress() streaming output.
- L253 `test_streams_output_to_adapter(self, tmp_path)` (method) — New output is sent to the adapter periodically.
- L291 `test_detects_and_forwards_prompt(self, tmp_path)` (method) — Detects .update_prompt.json and sends it to the user.
- L334 `test_prompt_forwarding_preserves_thread_metadata(self, tmp_path)` (method) — Forwarded update prompts keep the originating thread/topic metadata.
- L386 `test_cleans_up_on_completion(self, tmp_path)` (method) — All marker files are cleaned up when update finishes.
- L416 `test_failure_exit_code(self, tmp_path)` (method) — Non-zero exit code sends failure message.
- L442 `test_falls_back_and_delivers_after_reconnect(self, tmp_path)` (method) — Completion-only fallback waits for the platform to reconnect.
- L487 `test_prompt_forwarded_only_once(self, tmp_path)` (method) — Regression: prompt must not be re-sent on every poll cycle.
- L538 `test_prompt_is_recovered_after_watcher_restart(self, tmp_path)` (method) — A forwarded prompt stays on disk until answered so a new watcher can recover it.
- L612 `TestUpdatePromptInterception` (class) — Tests for update prompt response interception in _handle_message.
- L616 `test_intercepts_response_when_prompt_pending(self, tmp_path)` (method) — When _update_prompt_pending is set, the next message writes .update_response.
- L645 `test_recognized_slash_command_bypasses_pending_update_prompt(self, tmp_path)` (method) — Known slash commands must dispatch normally instead of being consumed.
- L682 `test_unrecognized_slash_command_still_consumed_as_response(self, tmp_path)` (method) — Unknown /foo is written verbatim to .update_response (legacy behavior).
- L706 `test_normal_message_when_no_prompt_pending(self, tmp_path)` (method) — Messages pass through normally when no prompt is pending.
- L728 `TestCmdUpdateGatewayMode` (class) — Tests for cmd_update with --gateway flag.
- L731 `test_gateway_flag_enables_gateway_prompt_for_stash(self, tmp_path)` (method) — With --gateway, stash restore uses _gateway_prompt instead of input().
- L753 `test_gateway_flag_parsed(self)` (method) — The --gateway flag is accepted by the update subparser.
