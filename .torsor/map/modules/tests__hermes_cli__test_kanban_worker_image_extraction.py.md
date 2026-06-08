---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_worker_image_extraction.py

Symbols in `tests/hermes_cli/test_kanban_worker_image_extraction.py`.

- L38 `kanban_home(tmp_path: Path, monkeypatch)` (function) — Isolated HERMES_HOME with a fresh kanban DB for each test.
- L48 `_add_task_with_body(body: str, *, title: str='Look at this')` (function)
- L63 `_read_body(task_id: str)` (function)
- L72 `TestExtractFromTaskBody` (class) — Read a real kanban task body and run it through extract_image_refs.
- L75 `test_local_path_in_body_round_trips(self, kanban_home, tmp_path)` (method)
- L88 `test_url_in_body_round_trips(self, kanban_home)` (method)
- L99 `test_mixed_path_and_url_in_body(self, kanban_home, tmp_path)` (method)
- L112 `test_body_without_images_yields_nothing(self, kanban_home)` (method)
- L122 `test_empty_body_is_safe(self, kanban_home)` (method)
- L131 `TestBuildPartsFromTaskBody` (class) — Verify the full pipeline produces a multimodal user turn.
- L134 `test_local_path_becomes_native_image_part(self, kanban_home, tmp_path)` (method)
- L159 `test_url_becomes_image_url_part(self, kanban_home)` (method)
- L181 `test_body_with_both_yields_two_image_parts(self, kanban_home, tmp_path)` (method)
- L203 `test_body_with_no_images_leaves_query_untouched(self, kanban_home)` (method)
- L222 `test_code_block_example_is_not_attached(self, kanban_home, tmp_path)` (method)
