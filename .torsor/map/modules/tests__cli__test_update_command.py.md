---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_update_command.py

Symbols in `tests/cli/test_update_command.py`.

- L28 `_bound(fn, instance)` (function) — Bind an unbound method to a stand-in instance.
- L33 `_make_self(modal_response)` (function) — Build a minimal stand-in 'self' for ``_handle_update_command``.
- L53 `_call(self_)` (function) — Invoke the real ``_handle_update_command`` on the stub.
- L63 `test_managed_install_refuses_and_does_not_set_pending_relaunch(capsys)` (function) — Under a managed install (brew/docker), /update prints a hint and
- L96 `test_affirmative_answer_sets_pending_relaunch_and_returns_true(answer, capsys)` (function) — Recognised affirmative answers ("y", "yes", "1", "ok") set
- L115 `test_negative_answer_cancels(answer, capsys)` (function) — Any "no"-shaped answer cancels without setting ``_pending_relaunch``.
- L126 `test_none_response_cancels(capsys)` (function) — ``None`` from the modal (timeout or dismiss) cancels cleanly.
- L137 `test_unrecognized_or_cancel_input_cancels(answer, capsys)` (function) — Unrecognised input and explicit "cancel" do not proceed.
