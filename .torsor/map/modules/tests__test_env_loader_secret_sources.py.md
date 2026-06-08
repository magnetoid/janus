---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_env_loader_secret_sources.py

Symbols in `tests/test_env_loader_secret_sources.py`.

- L24 `_reset_sources()` (function) — Each test starts with a clean source map and applied-home guard.
- L33 `test_get_secret_source_returns_none_for_untracked_var()` (function)
- L37 `test_get_secret_source_returns_label_for_tracked_var()` (function)
- L42 `test_format_secret_source_suffix_empty_for_untracked()` (function)
- L48 `test_format_secret_source_suffix_bitwarden_uses_proper_name()` (function)
- L56 `test_format_secret_source_suffix_generic_label_for_future_sources()` (function)
- L66 `test_apply_external_secret_sources_records_bitwarden_origin(tmp_path, monkeypatch)` (function) — End-to-end: when ``apply_bitwarden_secrets`` returns applied keys,
- L107 `test_apply_external_secret_sources_noop_when_disabled(tmp_path, monkeypatch)` (function) — Disabled Bitwarden config must not touch the source map.
- L124 `test_apply_external_secret_sources_dedupes_within_process(tmp_path, monkeypatch)` (function) — ``load_hermes_dotenv()`` is called at module-import time from several
