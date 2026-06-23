"""Standing Agreements — keep working agreements alive across a long session.

Addresses two failure modes reported on long sessions (esp. gpt-5.x):

1. **Rushing** — the agent starts a new/similar task without re-grounding on what
   was already agreed. Fixed by a *static* system-prompt directive (set once at
   session start, so it never breaks the prompt cache) telling the agent to
   restate the relevant standing agreement + plan before acting.
2. **Eviction** — in long sessions, context compression summarizes the agreement
   away. Fixed by marking agreements with a sentinel and teaching the compressor
   to keep marked messages verbatim (compression is the only sanctioned context
   mutation, so this rides it instead of fighting it).

A "standing agreement" is just a normal conversation message prefixed with
``AGREEMENT_MARKER`` — a cache-safe *append*, never a mid-conversation
system-prompt rewrite. ``pin_agreement`` / ``recall_agreements`` tools expose it
to the agent; a per-session JSON store backs listing + recall. Config-gated
(default ON — it's a core UX fix), best-effort, never raises.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

AGREEMENT_MARKER = "📌 STANDING AGREEMENT"

_DIRECTIVE = (
    'Standing agreements: messages marked "📌 STANDING AGREEMENT" are binding '
    "commitments made earlier in THIS conversation. Before starting a new or "
    "similar task, briefly restate the relevant standing agreement and your plan, "
    "and confirm the new request is consistent with it. Never rush past a prior "
    "agreement — if a request conflicts with one, flag the conflict before acting."
)


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when standing agreements are on (default ON — cheap, cache-safe)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        a = (config.get("agreements", {}) or {}) if isinstance(config, dict) else {}
        return bool(a.get("enabled", True))
    except Exception:
        return True


def directive(config: Optional[Dict[str, Any]] = None) -> str:
    """The static system-prompt directive (empty when disabled).

    Cache-safe: belongs in the stable system-prompt part, set once at session
    start and never mutated mid-conversation.
    """
    return _DIRECTIVE if enabled(config) else ""


def format_agreement(text: str) -> str:
    """Render an agreement as a marker-prefixed message body."""
    return f"{AGREEMENT_MARKER}: {' '.join(str(text).split())}"


def is_agreement_message(message: Any) -> bool:
    """True if a conversation message carries a standing agreement.

    The compressor uses this to preserve the message verbatim. Accepts dict
    messages (incl. multimodal content blocks) or raw strings.
    """
    try:
        content = message.get("content", "") if isinstance(message, dict) else message
        if isinstance(content, list):
            content = " ".join(
                str(b.get("text", "")) for b in content if isinstance(b, dict))
        return AGREEMENT_MARKER in str(content)
    except Exception:
        return False


# --- per-session store (backs /pins listing + recall) ---------------------

def _store_path(session_id: Any) -> Path:
    from janus_constants import get_janus_home
    safe = "".join(c for c in str(session_id) if c.isalnum() or c in "-_") or "default"
    return get_janus_home() / "agreements" / f"{safe}.json"


def _now() -> str:
    try:
        from janus_time import now
        return now().isoformat()
    except Exception:
        return ""


def load(session_id: Any) -> List[Dict[str, Any]]:
    p = _store_path(session_id)
    if not p.is_file():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (ValueError, OSError):
        return []


def record(session_id: Any, text: str, *, source: str = "agent") -> Optional[Dict[str, Any]]:
    """Persist an agreement for the session (deduped). Returns it or None."""
    text = " ".join(str(text).split())
    if not text:
        return None
    try:
        items = load(session_id)
        norm = text.lower()
        if any(str(i.get("text", "")).lower() == norm for i in items):
            return None
        entry = {"text": text, "source": source, "ts": _now()}
        items.append(entry)
        p = _store_path(session_id)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return entry
    except Exception as exc:
        logger.debug("agreement record failed: %s", exc)
        return None


def clear(session_id: Any) -> int:
    """Drop all agreements for the session. Returns how many were removed."""
    n = len(load(session_id))
    try:
        p = _store_path(session_id)
        if p.is_file():
            p.unlink()
    except OSError:
        pass
    return n


def render_for_prompt(session_id: Any, *, max_items: int = 10) -> str:
    """Render the session's agreements as a compact block (empty when none)."""
    items = load(session_id)
    if not items:
        return ""
    lines = ["Standing agreements in effect:"]
    lines.extend(f"- {i.get('text', '')}" for i in items[-max_items:])
    return "\n".join(lines)
