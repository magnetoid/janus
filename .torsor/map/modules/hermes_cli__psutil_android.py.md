---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/psutil_android.py

Symbols in `hermes_cli/psutil_android.py`.

- L21 `PsutilAndroidInstallError` (class) — Raised when the pinned psutil sdist is missing or unsafe.
- L25 `_normalize_member_parts(member_name: str)` (function)
- L35 `_safe_extract_tar_gz(archive: Path, destination: Path)` (function) — Extract a tar.gz without allowing traversal or link members.
- L67 `prepare_patched_psutil_sdist(archive: Path, destination: Path)` (function) — Safely extract the pinned psutil sdist and patch it for Android.
