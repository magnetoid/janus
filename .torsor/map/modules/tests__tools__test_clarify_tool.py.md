---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_clarify_tool.py

Symbols in `tests/tools/test_clarify_tool.py`.

- L15 `TestClarifyToolBasics` (class) — Basic functionality tests for clarify_tool.
- L18 `test_simple_question_with_callback(self)` (method) — Should return user response for simple question.
- L30 `test_question_with_choices(self)` (method) — Should pass choices to callback and return response.
- L46 `test_empty_question_returns_error(self)` (method) — Should return error for empty question.
- L52 `test_whitespace_only_question_returns_error(self)` (method) — Should return error for whitespace-only question.
- L57 `test_no_callback_returns_error(self)` (method) — Should return error when no callback is provided.
- L64 `TestClarifyToolChoicesValidation` (class) — Tests for choices parameter validation.
- L67 `test_choices_trimmed_to_max(self)` (method) — Should trim choices to MAX_CHOICES.
- L80 `test_empty_choices_become_none(self)` (method) — Empty choices list should become None (open-ended).
- L93 `test_choices_with_only_whitespace_stripped(self)` (method) — Whitespace-only choices should be stripped out.
- L104 `test_invalid_choices_type_returns_error(self)` (method) — Non-list choices should return error.
- L114 `test_choices_converted_to_strings(self)` (method) — Non-string choices should be converted to strings.
- L126 `TestClarifyToolCallbackHandling` (class) — Tests for callback error handling.
- L129 `test_callback_exception_returns_error(self)` (method) — Should return error if callback raises exception.
- L139 `test_callback_receives_stripped_question(self)` (method) — Callback should receive trimmed question.
- L150 `test_user_response_stripped(self)` (method) — User response should be stripped of whitespace.
- L159 `TestCheckClarifyRequirements` (class) — Tests for the requirements check function.
- L162 `test_always_returns_true(self)` (method) — clarify tool has no external requirements.
- L167 `TestClarifySchema` (class) — Tests for the OpenAI function-calling schema.
- L170 `test_schema_name(self)` (method) — Schema should have correct name.
- L174 `test_schema_has_description(self)` (method) — Schema should have a description.
- L179 `test_schema_question_required(self)` (method) — Question parameter should be required.
- L183 `test_schema_choices_optional(self)` (method) — Choices parameter should be optional.
- L187 `test_schema_choices_max_items(self)` (method) — Schema should specify max items for choices.
- L192 `test_max_choices_is_four(self)` (method) — MAX_CHOICES constant should be 4.
