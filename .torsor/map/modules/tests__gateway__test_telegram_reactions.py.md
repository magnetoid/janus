---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_reactions.py

Symbols in `tests/gateway/test_telegram_reactions.py`.

- L13 `_make_adapter(**extra_env)` (function)
- L24 `_make_event(chat_id: str='123', message_id: str='456')` (function)
- L42 `test_reactions_disabled_by_default(monkeypatch)` (function) — Telegram reactions should be disabled by default.
- L49 `test_reactions_enabled_when_set_true(monkeypatch)` (function) — Setting TELEGRAM_REACTIONS=true enables reactions.
- L56 `test_reactions_enabled_with_1(monkeypatch)` (function) — TELEGRAM_REACTIONS=1 enables reactions.
- L63 `test_reactions_disabled_with_false(monkeypatch)` (function) — TELEGRAM_REACTIONS=false disables reactions.
- L70 `test_reactions_disabled_with_0(monkeypatch)` (function) — TELEGRAM_REACTIONS=0 disables reactions.
- L77 `test_reactions_disabled_with_no(monkeypatch)` (function) — TELEGRAM_REACTIONS=no disables reactions.
- L88 `test_set_reaction_calls_bot_api(monkeypatch)` (function) — _set_reaction should call bot.set_message_reaction with correct args.
- L104 `test_set_reaction_returns_false_without_bot(monkeypatch)` (function) — _set_reaction should return False when bot is not available.
- L115 `test_set_reaction_handles_api_error_gracefully(monkeypatch)` (function) — API errors during reaction should not propagate.
- L129 `test_on_processing_start_adds_eyes_reaction(monkeypatch)` (function) — Processing start should add eyes reaction when enabled.
- L145 `test_on_processing_start_skipped_when_disabled(monkeypatch)` (function) — Processing start should not react when reactions are disabled.
- L157 `test_on_processing_start_handles_missing_ids(monkeypatch)` (function) — Should handle events without chat_id or message_id gracefully.
- L177 `test_on_processing_complete_success(monkeypatch)` (function) — Successful processing should set thumbs-up reaction.
- L193 `test_on_processing_complete_failure(monkeypatch)` (function) — Failed processing should set thumbs-down reaction.
- L209 `test_on_processing_complete_skipped_when_disabled(monkeypatch)` (function) — Processing complete should not react when reactions are disabled.
- L221 `test_on_processing_complete_cancelled_clears_reaction(monkeypatch)` (function) — Cancelled processing should clear the in-progress reaction.
- L245 `test_on_processing_complete_cancelled_skipped_when_disabled(monkeypatch)` (function) — Cancelled processing should not call the API when reactions are off.
- L257 `test_clear_reactions_handles_api_error_gracefully(monkeypatch)` (function) — API errors during clear should not propagate.
- L268 `test_clear_reactions_returns_false_without_bot(monkeypatch)` (function) — _clear_reactions should return False when bot is not available.
- L280 `test_config_bridges_telegram_reactions(monkeypatch, tmp_path)` (function) — gateway/config.py bridges telegram.reactions to TELEGRAM_REACTIONS env var.
- L301 `test_config_reactions_env_takes_precedence(monkeypatch, tmp_path)` (function) — Env var should take precedence over config.yaml for reactions.
