---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_destructive_slash_inline_skip_e2e.py

Symbols in `tests/cli/test_destructive_slash_inline_skip_e2e.py`.

- L20 `_make_cli_stub()` (function) — Build a minimal HermesCLI-shaped object that can run ``process_command``
- L54 `test_reset_now_invokes_new_session_without_modal()` (function) — ``/reset now`` runs ``new_session`` and never touches the modal.
- L69 `test_new_yes_with_title_preserves_title()` (function) — ``/new --yes My Session`` runs ``new_session(title='My Session')``.
- L83 `test_new_without_skip_token_still_consults_modal()` (function) — ``/new My Session`` (no skip token) must reach the modal.
