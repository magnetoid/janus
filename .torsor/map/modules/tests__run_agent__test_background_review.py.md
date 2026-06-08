---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_background_review.py

Symbols in `tests/run_agent/test_background_review.py`.

- L9 `_bare_agent()` (function)
- L35 `ImmediateThread` (class)
- L36 `__init__(self, *, target, daemon=None, name=None)` (method)
- L39 `start(self)` (method)
- L43 `test_background_review_shuts_down_memory_provider_before_close(monkeypatch)` (function)
- L79 `test_background_review_summarizer_receives_captured_messages_after_close(monkeypatch)` (function) — The action summarizer must see review messages even after close cleanup.
- L151 `test_background_review_installs_auto_deny_approval_callback(monkeypatch)` (function) — Regression guard for #15216.
- L207 `test_background_review_summary_is_attributed_to_self_improvement_loop(monkeypatch)` (function) — The CLI/gateway emission must identify the self-improvement loop.
- L270 `test_background_review_fork_skips_external_memory_plugins(monkeypatch)` (function) — The background review fork must NOT touch external memory plugins.
