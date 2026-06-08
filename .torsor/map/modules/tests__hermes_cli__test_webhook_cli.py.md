---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_webhook_cli.py

Symbols in `tests/hermes_cli/test_webhook_cli.py`.

- L18 `_isolate(tmp_path, monkeypatch)` (function)
- L26 `_make_args(**kwargs)` (function)
- L43 `TestSubscribe` (class)
- L44 `test_basic_create(self, capsys)` (method)
- L52 `test_with_options(self, capsys)` (method)
- L69 `test_custom_secret(self)` (method)
- L75 `test_auto_secret(self)` (method)
- L80 `test_update(self, capsys)` (method)
- L87 `test_invalid_name(self, capsys)` (method)
- L94 `TestList` (class)
- L95 `test_empty(self, capsys)` (method)
- L100 `test_with_entries(self, capsys)` (method)
- L111 `TestRemove` (class)
- L112 `test_remove_existing(self, capsys)` (method)
- L119 `test_remove_nonexistent(self, capsys)` (method)
- L124 `test_selective_remove(self)` (method)
- L133 `TestPersistence` (class)
- L134 `test_file_written(self)` (method)
- L141 `test_corrupted_file(self)` (method)
- L148 `test_save_creates_secret_file_owner_only_under_permissive_umask(self)` (method)
- L160 `test_save_narrows_existing_broad_secret_file_mode(self)` (method)
- L173 `TestWebhookEnabledGate` (class)
- L174 `test_blocks_when_disabled(self, capsys, monkeypatch)` (method)
- L182 `test_blocks_list_when_disabled(self, capsys, monkeypatch)` (method)
- L188 `test_allows_when_enabled(self, capsys)` (method)
- L195 `test_real_check_disabled(self, monkeypatch)` (method)
- L207 `test_real_check_enabled(self, monkeypatch)` (method)
