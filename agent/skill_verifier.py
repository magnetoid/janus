"""Verification gate for mined / draft skills — catch broken drafts before trust.

A static self-test: confirms the SKILL.md is well-formed (name + a concise
description) and that every ``scripts/*.py`` actually parses. This catches the
common failure where the auxiliary model that mined a skill wrote broken Python
or a malformed SKILL.md — *without* executing untrusted code (running arbitrary
mined scripts is deliberately out of scope; a static gate is the safe default).

Used by procedure mining to flag drafts that wouldn't work, so low-quality
auto-mined skills don't quietly pile up.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Any, Dict, List


def _frontmatter(text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def verify_skill_dir(skill_dir: Any) -> Dict[str, Any]:
    """Return ``{"ok": bool, "issues": [str, ...]}`` for a skill directory."""
    skill_dir = Path(skill_dir)
    issues: List[str] = []

    md = skill_dir / "SKILL.md"
    if not md.is_file():
        return {"ok": False, "issues": ["missing SKILL.md"]}
    try:
        text = md.read_text(encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "issues": [f"cannot read SKILL.md: {exc}"]}

    name = _frontmatter(text, "name")
    desc = _frontmatter(text, "description")
    if not name:
        issues.append("missing 'name' in frontmatter")
    if not desc:
        issues.append("missing 'description' in frontmatter")
    elif len(desc) > 60:
        issues.append(f"description too long ({len(desc)} > 60 chars)")

    scripts = skill_dir / "scripts"
    if scripts.is_dir():
        for py in sorted(scripts.glob("*.py")):
            try:
                ast.parse(py.read_text(encoding="utf-8"))
            except SyntaxError as exc:
                issues.append(f"scripts/{py.name}: syntax error: {exc.msg} (line {exc.lineno})")
            except OSError as exc:
                issues.append(f"scripts/{py.name}: unreadable ({exc})")

    return {"ok": not issues, "issues": issues}
