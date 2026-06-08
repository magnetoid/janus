---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_memento_cards.py

Symbols in `tests/skills/test_memento_cards.py`.

- L21 `isolated_data(tmp_path, monkeypatch)` (function) — Redirect card storage to a temp directory for every test.
- L30 `_run(capsys, argv: list[str])` (function) — Run main() with given argv and return parsed JSON output.
- L40 `TestCardCRUD` (class)
- L41 `test_add_creates_card(self, capsys)` (method)
- L52 `test_add_default_collection(self, capsys)` (method)
- L56 `test_list_all(self, capsys)` (method)
- L62 `test_list_by_collection(self, capsys)` (method)
- L69 `test_list_by_status(self, capsys)` (method)
- L76 `test_delete_card(self, capsys)` (method)
- L86 `test_delete_nonexistent(self, capsys)` (method)
- L90 `test_delete_collection(self, capsys)` (method)
- L104 `TestDueFiltering` (class)
- L105 `test_new_card_is_due(self, capsys)` (method)
- L110 `test_future_card_not_due(self, capsys, monkeypatch)` (method)
- L118 `test_retired_card_not_due(self, capsys)` (method)
- L125 `test_due_with_collection_filter(self, capsys)` (method)
- L135 `TestRating` (class)
- L136 `test_hard_adds_1_day(self, capsys)` (method)
- L146 `test_good_adds_3_days(self, capsys)` (method)
- L155 `test_easy_adds_7_days_and_increments_streak(self, capsys)` (method)
- L162 `test_retire_sets_retired(self, capsys)` (method)
- L169 `test_auto_retire_after_3_easys(self, capsys)` (method)
- L187 `test_hard_resets_ease_streak(self, capsys)` (method)
- L214 `test_rate_nonexistent_card(self, capsys)` (method)
- L221 `TestCSV` (class)
- L222 `test_export_import_roundtrip(self, capsys, tmp_path)` (method)
- L253 `test_import_without_collection_column(self, capsys, tmp_path)` (method)
- L266 `test_import_skips_empty_rows(self, capsys, tmp_path)` (method)
- L278 `test_import_nonexistent_file(self, capsys, tmp_path)` (method)
- L285 `TestQuizBatchAdd` (class)
- L286 `test_add_quiz_creates_cards(self, capsys)` (method)
- L298 `test_add_quiz_deduplicates_by_video_id(self, capsys)` (method)
- L309 `test_add_quiz_invalid_json(self, capsys)` (method)
- L316 `TestStats` (class)
- L317 `test_stats_empty(self, capsys)` (method)
- L324 `test_stats_counts(self, capsys)` (method)
- L343 `TestEdgeCases` (class)
- L344 `test_empty_deck_operations(self, capsys)` (method) — Operations on empty deck shouldn't crash.
- L353 `test_corrupt_json_recovery(self, capsys)` (method) — Corrupt JSON file should be treated as empty.
- L364 `test_missing_cards_key_recovery(self, capsys)` (method) — JSON without 'cards' key should be treated as empty.
- L372 `test_atomic_write_creates_dir(self, capsys)` (method) — Data dir is created automatically if missing.
- L381 `test_delete_collection_empty(self, capsys)` (method) — Deleting a nonexistent collection succeeds with 0 deleted.
- L390 `TestUserAnswer` (class)
- L391 `test_rate_stores_user_answer(self, capsys)` (method)
- L398 `test_rate_without_user_answer_keeps_null(self, capsys)` (method)
- L404 `test_new_card_has_last_user_answer_null(self, capsys)` (method)
- L408 `test_user_answer_persists_in_list(self, capsys)` (method)
- L416 `test_export_excludes_user_answer(self, capsys, tmp_path)` (method)
