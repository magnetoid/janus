---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_run_cleanup_progress.py

Symbols in `tests/gateway/test_run_cleanup_progress.py`.

- L33 `CleanupCaptureAdapter` (class) — Adapter that records every delete_message call for inspection.
- L38 `__init__(self, platform=Platform.TELEGRAM)` (method)
- L44 `connect(self)` (method)
- L47 `disconnect(self)` (method)
- L50 `_mint_id(self)` (method)
- L54 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L61 `edit_message(self, chat_id, message_id, content)` (method)
- L65 `delete_message(self, chat_id, message_id)` (method)
- L69 `send_typing(self, chat_id, metadata=None)` (method)
- L72 `stop_typing(self, chat_id)` (method)
- L75 `get_chat_info(self, chat_id: str)` (method)
- L79 `NoDeleteAdapter` (class) — Adapter that inherits the base no-op delete_message (used to prove
- L83 `delete_message(self, chat_id, message_id)` (method)
- L95 `ProgressAgent` (class) — Emits two tool-progress events and returns a normal final response.
- L98 `__init__(self, **kwargs)` (method)
- L102 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L112 `FailingAgent` (class)
- L113 `__init__(self, **kwargs)` (method)
- L117 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L134 `_make_runner(adapter)` (function)
- L157 `_install_fakes(monkeypatch, agent_cls, *, cleanup_on: bool)` (function) — Wire up the module stubs every _run_agent test needs.
- L192 `test_cleanup_off_by_default_leaves_bubbles(monkeypatch, tmp_path)` (function) — Without ``cleanup_progress: true``, firing whatever callback is
- L225 `test_cleanup_registers_callback_and_deletes_on_success(monkeypatch, tmp_path)` (function) — With the flag on, the cleanup callback deletes the progress bubble.
- L266 `test_cleanup_skipped_on_failed_run(monkeypatch, tmp_path)` (function) — Failed runs skip cleanup registration — breadcrumbs stay.
- L297 `test_cleanup_noop_on_adapter_without_delete_support(monkeypatch, tmp_path)` (function) — Adapters that inherit the base-class delete_message no-op are
- L326 `test_cleanup_chains_with_existing_callback(monkeypatch, tmp_path)` (function) — When a bg-review-style callback is already registered, the cleanup
