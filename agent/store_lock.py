"""Cross-process exclusive locking + atomic replace for the JSON learning stores.

The learning stores (``lessons.json``, ``outcomes.json``, ``model_strengths.json``,
``lesson_recall.json``, …) are read-modify-written concurrently by auto-mine
background threads, the sleep cycle, and gateway sessions. A plain
``read → modify → write_text`` there is a lost-update race, and a mid-write
reader can see torn JSON. This module gives them the same discipline the
memory store already has (``tools/memory_tool.py::_file_lock``):

  * ``locked_store(path)`` — an exclusive advisory lock on a sibling ``.lock``
    file. Uses ``flock`` (per open-file-description, so it excludes both other
    processes AND other threads of this process) on POSIX, ``msvcrt.locking``
    on Windows. Best-effort: on platforms/filesystems without locking it
    degrades to unlocked rather than raising — these stores must never take
    the agent down.
  * ``atomic_write_text(path, text)`` — write to a same-directory temp file,
    then ``os.replace`` so readers only ever see a complete document.

The lock lives on a separate ``.lock`` file so the store itself can still be
atomically replaced while held.
"""
from __future__ import annotations

import logging
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Union

try:  # POSIX
    import fcntl
except ImportError:  # pragma: no cover - Windows
    fcntl = None  # type: ignore[assignment]

try:  # Windows
    import msvcrt
except ImportError:  # POSIX
    msvcrt = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)


@contextmanager
def locked_store(path: Union[str, Path]) -> Iterator[None]:
    """Hold an exclusive lock scoped to ``path`` for a read-modify-write."""
    lock_path = Path(f"{path}.lock")
    fd = None
    locked = False
    try:
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        if fcntl is not None or msvcrt is not None:
            fd = open(lock_path, "a+", encoding="utf-8")
            if fcntl is not None:
                fcntl.flock(fd, fcntl.LOCK_EX)
            else:
                fd.seek(0)
                msvcrt.locking(fd.fileno(), msvcrt.LK_LOCK, 1)
            locked = True
    except OSError as exc:
        logger.debug("store lock unavailable for %s: %s", lock_path, exc)
    try:
        yield
    finally:
        if fd is not None:
            if locked:
                try:
                    if fcntl is not None:
                        fcntl.flock(fd, fcntl.LOCK_UN)
                    else:
                        fd.seek(0)
                        msvcrt.locking(fd.fileno(), msvcrt.LK_UNLCK, 1)
                except OSError:
                    pass
            fd.close()


def atomic_write_text(path: Union[str, Path], text: str) -> None:
    """Write ``text`` to ``path`` via a same-directory temp file + ``os.replace``."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_fd, tmp_name = tempfile.mkstemp(
        dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp_name, str(path))
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
