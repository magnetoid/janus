---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_codex_silent_hang_hint.py

Symbols in `tests/run_agent/test_codex_silent_hang_hint.py`.

- L17 `_make_agent(tmp_path: Path, **overrides)` (function)
- L34 `_isolate_hermes_home(monkeypatch, tmp_path)` (function)
- L42 `test_hint_fires_for_bare_gpt_5_5_on_codex(tmp_path)` (function)
- L53 `test_hint_fires_for_vendor_prefixed_gpt_5_5(tmp_path)` (function)
- L60 `test_hint_fires_for_gpt_5_5_codex_suffix(tmp_path)` (function)
- L67 `test_hint_fires_when_model_arg_omitted(tmp_path)` (function) — The helper falls back to ``self.model`` when ``model=`` not passed.
- L78 `test_hint_skipped_for_gpt_5_4(tmp_path)` (function) — gpt-5.4 is the recommended workaround — must not trigger.
- L85 `test_hint_skipped_for_gpt_5_50_false_positive(tmp_path)` (function) — ``gpt-5.50`` (hypothetical future SKU) must not regex-match gpt-5.5.
- L92 `test_hint_skipped_for_non_codex_api_mode(tmp_path)` (function) — Hint only fires on the Codex Responses path.
- L99 `test_hint_skipped_for_non_codex_provider(tmp_path)` (function) — Same model on a non-Codex provider does not trigger.
- L111 `test_hint_skipped_for_empty_model(tmp_path)` (function) — Explicit empty string ``model`` short-circuits the regex.
- L121 `test_hint_skipped_for_unrelated_model_on_codex(tmp_path)` (function)
