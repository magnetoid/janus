---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_mention_boundaries.py

Symbols in `tests/gateway/test_telegram_mention_boundaries.py`.

- L20 `_make_adapter()` (function)
- L28 `_mention_entity(text, mention='@hermes_bot')` (function) — Build a MENTION entity pointing at a literal `@username` in `text`.
- L34 `_text_mention_entity(offset, length, user_id)` (function) — Build a TEXT_MENTION entity (used when the target user has no public @handle).
- L44 `_message(text=None, caption=None, entities=None, caption_entities=None)` (function)
- L56 `TestRealMentionsAreDetected` (class) — A real Telegram mention always comes with a MENTION entity — detect those.
- L59 `test_mention_at_start_of_message(self)` (method)
- L65 `test_mention_mid_sentence(self)` (method)
- L71 `test_mention_at_end_of_message(self)` (method)
- L77 `test_mention_in_caption(self)` (method)
- L83 `test_text_mention_entity_targets_bot(self)` (method) — TEXT_MENTION is Telegram's entity type for @FirstName -> user without a public handle.
- L90 `TestSubstringFalsePositivesAreRejected` (class) — Bare `@bot_username` substrings without a MENTION entity must NOT match.
- L99 `test_email_like_substring(self)` (method) — bug #12545 exact repro: 'foo@hermes_bot.example'.
- L105 `test_hostname_substring(self)` (method)
- L110 `test_superstring_username(self)` (method) — `@hermes_botx` is a different username; Telegram would emit a mention
- L117 `test_underscore_suffix_substring(self)` (method)
- L122 `test_substring_inside_url_without_entity(self)` (method) — @handle inside a URL produces a URL entity, not a MENTION entity.
- L128 `test_substring_inside_code_block_without_entity(self)` (method) — Telegram doesn't emit mention entities inside code/pre entities.
- L134 `test_plain_text_with_no_at_sign(self)` (method)
- L139 `test_email_substring_in_caption(self)` (method)
- L145 `TestEntityEdgeCases` (class) — Malformed or mismatched entities should not crash or over-match.
- L148 `test_mention_entity_for_different_username(self)` (method)
- L154 `test_text_mention_entity_for_different_user(self)` (method)
- L159 `test_malformed_entity_with_negative_offset(self)` (method)
- L165 `test_malformed_entity_with_zero_length(self)` (method)
- L172 `TestCaseInsensitivity` (class) — Telegram usernames are case-insensitive; the slice-compare normalizes both sides.
- L175 `test_uppercase_mention(self)` (method)
- L181 `test_mixed_case_mention(self)` (method)
