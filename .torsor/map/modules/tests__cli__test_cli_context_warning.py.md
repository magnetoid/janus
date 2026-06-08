---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_context_warning.py

Symbols in `tests/cli/test_cli_context_warning.py`.

- L13 `_isolate(tmp_path, monkeypatch)` (function) — Isolate HERMES_HOME so tests don't touch real config.
- L21 `cli_obj(_isolate)` (function) — Create a minimal HermesCLI instance for banner testing.
- L46 `TestLowContextWarning` (class) — Tests that the CLI warns about low context lengths.
- L49 `test_warning_for_below_minimum_context(self, cli_obj)` (method) — Warning shown when context is below Hermes' minimum.
- L62 `test_warning_for_low_context(self, cli_obj)` (method) — Warning shown when context is 4096 (Ollama default).
- L74 `test_warning_for_2048_context(self, cli_obj)` (method) — Warning shown for 2048 tokens (common LM Studio default).
- L85 `test_no_warning_at_boundary(self, cli_obj)` (method) — No warning at exactly Hermes' minimum context length.
- L96 `test_no_warning_above_boundary(self, cli_obj)` (method) — No warning above Hermes' minimum context length.
- L107 `test_ollama_specific_hint(self, cli_obj)` (method) — Ollama-specific fix shown when port 11434 detected.
- L120 `test_lm_studio_specific_hint(self, cli_obj)` (method) — LM Studio-specific fix shown when port 1234 detected.
- L132 `test_generic_hint_for_other_servers(self, cli_obj)` (method) — Generic fix shown for unknown servers.
- L144 `test_no_warning_when_no_context_length(self, cli_obj)` (method) — No warning when context length is not yet known.
- L155 `test_compact_banner_does_not_crash_on_narrow_terminal(self, cli_obj)` (method) — Compact mode should still have ctx_len defined for warning logic.
