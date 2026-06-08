---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_dump_build_sha.py

Symbols in `tests/docker/test_dump_build_sha.py`.

- L33 `_run_dump(image: str)` (function) — Return the stdout of ``docker run <image> dump``.
- L53 `_read_baked_sha_from_image(image: str)` (function) — Return the ``/opt/hermes/.hermes_build_sha`` content, or None if absent.
- L67 `test_dump_reports_baked_sha_when_present(built_image: str)` (function) — When the image was built with ``HERMES_GIT_SHA``, dump must surface it.
