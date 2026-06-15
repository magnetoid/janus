"""Read a gated boolean config flag, with an env-var override layer.

Precedence (highest first): env override > config.yaml > default. The env layer
exists so the eval A/B gate (agent/eval_trend.compare_feature) can flip a
feature ON/OFF for a single hermetic suite run without mutating config on disk.

Override var name: ``JANUS_FLAG_<SECTION>__<KEY>`` (key dots become double
underscores), e.g. ``JANUS_FLAG_EVALS__TREND__ENABLED``. Truthy = 1/true/yes/on.
Best-effort: any error falls back to ``default``.
"""
from __future__ import annotations

import logging
import os
from typing import Any

logger = logging.getLogger(__name__)

_TRUTHY = {"1", "true", "yes", "on"}
_FALSY = {"0", "false", "no", "off"}


def _env_override(section: str, key: str):
    var = "JANUS_FLAG_" + section.upper() + "__" + key.upper().replace(".", "__")
    raw = os.environ.get(var)
    if raw is None:
        return None
    low = raw.strip().lower()
    if low in _TRUTHY:
        return True
    if low in _FALSY:
        return False
    return None


def _config_value(section: str, key: str):
    try:
        import yaml
        from janus_constants import get_janus_home

        cfg_path = get_janus_home() / "config.yaml"
        if not cfg_path.is_file():
            return None
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        node: Any = cfg.get(section, {})
        for part in key.split("."):
            if not isinstance(node, dict) or part not in node:
                return None
            node = node[part]
        return node
    except Exception as exc:
        logger.debug("flag config read failed: %s", exc)
        return None


def flag_enabled(section: str, key: str, *, default: bool = False) -> bool:
    """True/False for ``section.key``: env override > config.yaml > default."""
    override = _env_override(section, key)
    if override is not None:
        return override
    value = _config_value(section, key)
    if value is None:
        return default
    return bool(value)
