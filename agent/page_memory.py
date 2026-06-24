"""PageMem — persistent per-site page memory for the browser agent.

Each browser visit yields an accessibility-tree snapshot like ``- button "Submit"
[e2]``. The ``[e2]`` ref is ephemeral (per-snapshot); the STABLE identity is the
role + accessible-name (``button "Submit"``). PageMem keys on the stable identity,
discards the ref, and persists per-domain:

  * a profile of the site's interactive elements, and
  * task playbooks (semantic action sequences the agent recorded after success),

so a repeat visit recalls what worked instead of re-deriving structure from scratch.
Deterministic (no model in the capture path), config-gated (default ON), best-effort
— never blocks or breaks browsing. Typed secrets are never persisted.
"""
from __future__ import annotations

import hashlib
import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# a11y roles that represent an actionable affordance worth remembering.
_INTERACTIVE_ROLES = frozenset({
    "button", "link", "textbox", "searchbox", "combobox", "checkbox", "radio",
    "menuitem", "menuitemcheckbox", "menuitemradio", "tab", "switch", "option",
    "slider", "spinbutton",
})
# `- <role> "<name>" [eN]`  (ref optional; we deliberately drop it)
_ELEMENT_RE = re.compile(r'^\s*-\s+([a-z]+)\s+"([^"]*)"')
# Targets/labels whose typed value must never be persisted.
_SECRET_HINT = re.compile(r"password|passwd|secret|token|credential|otp|\bpin\b|api[_\s-]?key|cvv",
                          re.IGNORECASE)
_SECRET_VALUE = re.compile(r"^[A-Za-z0-9_\-/+=.]{24,}$")  # long opaque token-ish value
_SCRUBBED = "[scrubbed]"


def enabled(config: Optional[Dict[str, Any]] = None) -> bool:
    """True when PageMem is on (default ON — low-risk, local, prunable)."""
    try:
        if config is None:
            from janus_cli.config import load_config
            config = load_config()
        pmc = (config.get("page_memory", {}) or {}) if isinstance(config, dict) else {}
        return bool(pmc.get("enabled", True))
    except Exception:
        return True


def _cfg(config: Optional[Dict[str, Any]], key: str, default: Any) -> Any:
    try:
        pmc = (config.get("page_memory", {}) or {}) if isinstance(config, dict) else {}
        val = pmc.get(key, default)
        return val if val is not None else default
    except Exception:
        return default


def _domain(url: str) -> str:
    """Normalized domain key: lowercase host, ``www.`` and port stripped."""
    try:
        u = str(url or "").strip()
        netloc = urlparse(u).netloc or urlparse("//" + u).netloc
        host = netloc.split("@")[-1].split(":")[0].lower()
        return host[4:] if host.startswith("www.") else host
    except Exception:
        return ""


def _parse_elements(aria_snapshot: Optional[str]) -> List[Dict[str, str]]:
    """Distill interactive, named elements from an accessibility-tree snapshot.

    Deterministic. Drops the ephemeral ``[eN]`` ref, non-interactive roles, and
    unnamed elements (nothing stable to key on).
    """
    out: List[Dict[str, str]] = []
    if not aria_snapshot:
        return out
    seen = set()
    for line in str(aria_snapshot).splitlines():
        m = _ELEMENT_RE.match(line)
        if not m:
            continue
        role, name = m.group(1), m.group(2).strip()
        if role not in _INTERACTIVE_ROLES or not name:
            continue
        key = role + "|" + name
        if key in seen:
            continue
        seen.add(key)
        out.append({"role": role, "name": name})
    return out


def _store_path(domain: str) -> Path:
    from janus_constants import get_janus_home
    safe = re.sub(r"[^a-z0-9.-]+", "_", domain.lower()) or "default"
    return get_janus_home() / "page_memory" / f"{safe[:120]}.json"


def _load(domain: str) -> Dict[str, Any]:
    p = _store_path(domain)
    if not p.is_file():
        return {"domain": domain, "elements": [], "playbooks": []}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"domain": domain, "elements": [], "playbooks": []}
        data.setdefault("elements", [])
        data.setdefault("playbooks", [])
        return data
    except (ValueError, OSError):
        return {"domain": domain, "elements": [], "playbooks": []}


def _save(domain: str, data: Dict[str, Any]) -> None:
    try:
        p = _store_path(domain)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception as exc:
        logger.debug("page_memory save failed: %s", exc)


def capture(url: str, aria_snapshot: Optional[str], config: Optional[Dict[str, Any]] = None) -> Optional[int]:
    """Merge the snapshot's interactive elements into the domain profile (dedup,
    cap). Deterministic, best-effort. Returns the merged element count or None."""
    try:
        domain = _domain(url)
        if not domain:
            return None
        parsed = _parse_elements(aria_snapshot)
        if not parsed:
            return None
        data = _load(domain)
        existing = {e["role"] + "|" + e["name"]: e for e in data["elements"]
                    if isinstance(e, dict) and "role" in e and "name" in e}
        for el in parsed:
            k = el["role"] + "|" + el["name"]
            if k in existing:
                existing[k]["seen"] = int(existing[k].get("seen", 1)) + 1
            else:
                existing[k] = {"role": el["role"], "name": el["name"], "seen": 1}
        merged = sorted(existing.values(), key=lambda e: e.get("seen", 1), reverse=True)
        cap = int(_cfg(config, "max_elements", 60))
        data["elements"] = merged[:cap]
        _save(domain, data)
        return len(data["elements"])
    except Exception as exc:
        logger.debug("page_memory capture failed: %s", exc)
        return None


def _scrub_steps(steps: Any) -> List[Dict[str, Any]]:
    """Copy steps, redacting any typed value into a secret-looking field."""
    out: List[Dict[str, Any]] = []
    for s in (steps or []):
        if not isinstance(s, dict):
            continue
        step = {k: v for k, v in s.items()}
        if "value" in step and step["value"] is not None:
            target = str(step.get("target", ""))
            val = str(step["value"])
            if _SECRET_HINT.search(target) or _SECRET_VALUE.match(val):
                step["value"] = _SCRUBBED
        out.append(step)
    return out


def _playbook_id(task: str, steps: List[Dict[str, Any]]) -> str:
    raw = (str(task) + json.dumps(steps, sort_keys=True, ensure_ascii=False)).encode("utf-8")
    return "pb" + hashlib.sha1(raw).hexdigest()[:8]


def record_playbook(url: str, task: str, steps: Any,
                    config: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """Persist a named action sequence for the site (secrets scrubbed). Returns id."""
    try:
        domain = _domain(url)
        task = str(task or "").strip()
        if not domain or not task:
            return None
        clean = _scrub_steps(steps)
        if not clean:
            return None
        pid = _playbook_id(task, clean)
        data = _load(domain)
        data["playbooks"] = [p for p in data["playbooks"]
                             if isinstance(p, dict) and p.get("id") != pid]
        data["playbooks"].append({"id": pid, "task": task, "steps": clean,
                                  "ok": 0, "fail": 0, "streak": 0})
        cap = int(_cfg(config, "max_playbooks", 12))
        if len(data["playbooks"]) > cap:
            data["playbooks"] = sorted(
                data["playbooks"], key=lambda p: p.get("ok", 0) - p.get("fail", 0),
                reverse=True)[:cap]
        _save(domain, data)
        return pid
    except Exception as exc:
        logger.debug("page_memory record_playbook failed: %s", exc)
        return None


def note_outcome(url: str, playbook_id: str, ok: bool,
                 config: Optional[Dict[str, Any]] = None) -> None:
    """Bump a playbook's counters; drop it after N consecutive failures (decay)."""
    try:
        domain = _domain(url)
        data = _load(domain)
        decay = int(_cfg(config, "decay_fails", 3))
        kept: List[Dict[str, Any]] = []
        for p in data["playbooks"]:
            if not isinstance(p, dict):
                continue
            if p.get("id") == playbook_id:
                if ok:
                    p["ok"] = int(p.get("ok", 0)) + 1
                    p["streak"] = 0
                else:
                    p["fail"] = int(p.get("fail", 0)) + 1
                    p["streak"] = int(p.get("streak", 0)) + 1
                    if p["streak"] >= decay:
                        continue  # decayed away
            kept.append(p)
        data["playbooks"] = kept
        _save(domain, data)
    except Exception as exc:
        logger.debug("page_memory note_outcome failed: %s", exc)


def recall(url: str) -> Dict[str, Any]:
    """Return ``{profile_elements, playbooks}`` for the domain (best playbooks first)."""
    try:
        domain = _domain(url)
        if not domain:
            return {"profile_elements": [], "playbooks": []}
        data = _load(domain)
        playbooks = sorted(
            (p for p in data["playbooks"] if isinstance(p, dict)),
            key=lambda p: p.get("ok", 0) - p.get("fail", 0), reverse=True)
        return {"profile_elements": data["elements"], "playbooks": playbooks}
    except Exception as exc:
        logger.debug("page_memory recall failed: %s", exc)
        return {"profile_elements": [], "playbooks": []}


def format_recall(rec: Optional[Dict[str, Any]], max_elements: int = 25,
                  max_playbooks: int = 4) -> str:
    """Render a compact ``📍 PageMem`` block for injection (empty when nothing known)."""
    try:
        if not rec:
            return ""
        els = rec.get("profile_elements") or []
        pbs = rec.get("playbooks") or []
        if not els and not pbs:
            return ""
        lines = ["📍 **PageMem** (this site, from past visits — verify before relying):"]
        if els:
            shown = ", ".join(f'{e["role"]} "{e["name"]}"' for e in els[:max_elements]
                              if isinstance(e, dict))
            lines.append(f"Known interactive elements: {shown}")
        for p in pbs[:max_playbooks]:
            if not isinstance(p, dict):
                continue
            seq = " → ".join(
                f'{s.get("action", "?")} {s.get("target", "")}'.strip()
                + (f' = {s["value"]}' if s.get("value") else "")
                for s in (p.get("steps") or []) if isinstance(s, dict))
            lines.append(f'• {p.get("task", "task")}: {seq}')
        return "\n".join(lines)
    except Exception as exc:
        logger.debug("page_memory format_recall failed: %s", exc)
        return ""
