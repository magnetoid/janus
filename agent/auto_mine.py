"""Auto-fire session-end mining (memory + procedures) — opt-in, best-effort.

When a session ends (e.g. ``/new``), if the user has opted in via config
(``memory.session_mining`` / ``skills.session_mining``), distill the just-ended
transcript into memory facts and/or draft skills — in a background thread so it
never blocks the UI, swallowing all errors.

OFF by default: flip the flags on only after eyeballing a manual
``janus memory mine`` / ``janus skills mine`` run, so quality is checked before
it runs unattended. A short session is skipped (nothing worth mining).
"""
from __future__ import annotations

import logging
import threading
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_MIN_MESSAGES = 6  # don't mine trivial sessions


def _flag(section: str, key: str) -> bool:
    try:
        import yaml
        from janus_constants import get_janus_home

        cfg_path = get_janus_home() / "config.yaml"
        if not cfg_path.is_file():
            return False
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        sec = cfg.get(section, {})
        return bool(isinstance(sec, dict) and sec.get(key))
    except Exception:
        return False


def maybe_automine(
    messages: List[Dict[str, Any]], *, run_in_thread: bool = True
) -> Optional[threading.Thread]:
    """Mine the just-ended session for memory/skills if opted in.

    Returns the worker thread (or None if nothing was scheduled). Fully
    best-effort — never raises, never blocks meaningful work.
    """
    try:
        if not messages or len(messages) < _MIN_MESSAGES:
            return None
        mine_memory = _flag("memory", "session_mining")
        mine_skills = _flag("skills", "session_mining")
        if not (mine_memory or mine_skills):
            return None
        snapshot = list(messages)

        def _work():
            if mine_memory:
                try:
                    from tools.memory_tool import MemoryStore
                    from agent.memory_miner import mine_session_memory

                    store = MemoryStore()
                    store.load_from_disk()
                    mine_session_memory(snapshot, store)
                except Exception as exc:
                    logger.debug("auto memory mining failed: %s", exc)
            if mine_skills:
                try:
                    from agent.skill_miner import mine_session_skills

                    try:
                        from tools.skills_tool import _find_all_skills
                        existing = [s["name"] for s in _find_all_skills()]
                    except Exception:
                        existing = []
                    mine_session_skills(snapshot, existing_skill_names=existing)
                except Exception as exc:
                    logger.debug("auto skill mining failed: %s", exc)

        if run_in_thread:
            t = threading.Thread(target=_work, daemon=True, name="auto-mine")
            t.start()
            return t
        _work()
        return None
    except Exception as exc:  # the session boundary must never break
        logger.debug("maybe_automine failed: %s", exc)
        return None
