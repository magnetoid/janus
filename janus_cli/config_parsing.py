from typing import Any, Dict, List, Optional, Set, Tuple
import os
import logging
import copy
from pathlib import Path
from janus_cli.config import DEFAULT_CONFIG, get_config_path, get_env_path, _set_nested
from janus_cli.config_validation import validate_config_structure, ConfigIssue

logger = logging.getLogger(__name__)

def _preserve_env_ref_templates(current, raw, loaded_expanded=None):
    """Restore raw ``${VAR}`` templates when a value is otherwise unchanged.

    ``load_config()`` expands env refs for runtime use. When a caller later
    persists that config after modifying some unrelated setting, keep the
    original on-disk template instead of writing the expanded plaintext
    secret back to ``config.yaml``.

    Prefer preserving the raw template when ``current`` still matches either
    the value previously returned by ``load_config()`` for this config path or
    the current environment expansion of ``raw``. This handles env-var
    rotation between load and save while still treating mixed literal/template
    string edits as caller-owned once their rendered value diverges.
    """
    if isinstance(current, str) and isinstance(raw, str) and re.search(r"\${[^}]+}", raw):
        if current == raw:
            return raw
        if isinstance(loaded_expanded, str) and current == loaded_expanded:
            return raw
        if _expand_env_vars(raw) == current:
            return raw
        return current

    if isinstance(current, dict) and isinstance(raw, dict):
        return {
            key: _preserve_env_ref_templates(
                value,
                raw.get(key),
                loaded_expanded.get(key) if isinstance(loaded_expanded, dict) else None,
            )
            for key, value in current.items()
        }

    if isinstance(current, list) and isinstance(raw, list):
        # Prefer matching named config objects (e.g. custom_providers) by name
        # so harmless reordering doesn't drop the original template. If names
        # are duplicated, fall back to positional matching instead of silently
        # shadowing one entry.
        current_by_name = _items_by_unique_name(current)
        raw_by_name = _items_by_unique_name(raw)
        loaded_by_name = _items_by_unique_name(loaded_expanded)
        if current_by_name is not None and raw_by_name is not None:
            return [
                _preserve_env_ref_templates(
                    item,
                    raw_by_name.get(item.get("name")),
                    loaded_by_name.get(item.get("name")) if loaded_by_name is not None else None,
                )
                for item in current
            ]
        return [
            _preserve_env_ref_templates(
                item,
                raw[index] if index < len(raw) else None,
                loaded_expanded[index]
                if isinstance(loaded_expanded, list) and index < len(loaded_expanded)
                else None,
            )
            for index, item in enumerate(current)
        ]

    return current


def _normalize_root_model_keys(config: Dict[str, Any]) -> Dict[str, Any]:
    """Move stale root-level provider/base_url/context_length into model section.

    Some users (or older code) placed ``provider:``, ``base_url:``, or
    ``context_length:`` at the config root instead of inside ``model:``.
    These root-level keys are only used as a fallback when the corresponding
    ``model.*`` key is empty — they never override an existing value.
    After migration the root-level keys are removed so they can't cause
    confusion on subsequent loads.
    """
    # Only act if there are root-level keys to migrate
    has_root = any(config.get(k) for k in ("provider", "base_url", "context_length"))
    if not has_root:
        return config

    config = dict(config)
    model = config.get("model")
    if not isinstance(model, dict):
        model = {"default": model} if model else {}
        config["model"] = model

    for key in ("provider", "base_url", "context_length"):
        root_val = config.get(key)
        if root_val and not model.get(key):
            model[key] = root_val
        config.pop(key, None)

    return config


def _normalize_max_turns_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize legacy root-level max_turns into agent.max_turns."""
    config = dict(config)
    agent_config = dict(config.get("agent") or {})

    if "max_turns" in config and "max_turns" not in agent_config:
        agent_config["max_turns"] = config["max_turns"]

    if "max_turns" not in agent_config:
        agent_config["max_turns"] = DEFAULT_CONFIG["agent"]["max_turns"]

    config["agent"] = agent_config
    config.pop("max_turns", None)
    return config


def cfg_get(cfg: Optional[Dict[str, Any]], *keys: str, default: Any = None) -> Any:
    """Traverse nested dict keys safely, returning ``default`` on any miss.

    Canonical helper for the ``cfg.get("X", {}).get("Y", default)`` pattern
    that appears 50+ times across the codebase. Handles three common gotchas
    in one place:

      1. Missing intermediate keys (returns ``default``, no KeyError).
      2. An intermediate value that's not a dict (e.g. a user wrote a string
         where a section was expected). Returns ``default`` instead of
         AttributeError on ``.get()``.
      3. ``cfg is None`` (callers sometimes pass ``load_config() or None``).

    Named ``cfg_get`` rather than ``cfg_path`` to avoid shadowing the
    ubiquitous ``cfg_path = _janus_home / "config.yaml"`` local variable
    that appears in gateway/run.py, cron/scheduler.py, main.py, etc.

    Explicit ``None`` values are returned as-is (matches ``dict.get(key,
    default)`` semantics — ``default`` is only returned when the key is
    *absent*, not when it's present but set to ``None``).

    Examples:
        >>> cfg_get({"agent": {"reasoning_effort": "high"}}, "agent", "reasoning_effort")
        'high'
        >>> cfg_get({}, "agent", "reasoning_effort", default="medium")
        'medium'
        >>> cfg_get({"agent": "oops_a_string"}, "agent", "reasoning_effort", default="low")
        'low'
        >>> cfg_get(None, "anything", default=42)
        42
        >>> cfg_get({"a": {"b": None}}, "a", "b", default="def")  # explicit None preserved
        >>> cfg_get({"a": {"b": False}}, "a", "b", default=True)  # falsy values preserved
        False
    """
    if not isinstance(cfg, dict):
        return default
    node: Any = cfg
    for key in keys:
        if not isinstance(node, dict):
            return default
        if key not in node:
            return default
        node = node[key]
    return node



def read_raw_config() -> Dict[str, Any]:
    """Read ~/.janus/config.yaml as-is, without merging defaults or migrating.

    Returns the raw YAML dict, or ``{}`` if the file doesn't exist or can't
    be parsed.  Use this for lightweight config reads where you just need a
    single value and don't want the overhead of ``load_config()``'s deep-merge
    + migration pipeline.

    Cached on the config file's (mtime_ns, size) — same strategy as
    ``load_config()``. Returns a deepcopy on every call since some callers
    mutate the result before passing to ``save_config()``.
    """
    with _CONFIG_LOCK:
        try:
            config_path = get_config_path()
            st = config_path.stat()
            cache_key = (st.st_mtime_ns, st.st_size)
        except (FileNotFoundError, OSError):
            return {}

        path_key = str(config_path)
        cached = _RAW_CONFIG_CACHE.get(path_key)
        if cached is not None and cached[:2] == cache_key:
            return copy.deepcopy(cached[2])

        try:
            with open(config_path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            _warn_config_parse_failure(config_path, e)
            return {}

        if not isinstance(data, dict):
            data = {}
        _RAW_CONFIG_CACHE[path_key] = (cache_key[0], cache_key[1], copy.deepcopy(data))
        return data


def load_config() -> Dict[str, Any]:
    """Load configuration from ~/.janus/config.yaml.

    Cached on the config file's (mtime_ns, size). Returns a deepcopy of
    the cached value when unchanged, since most call sites mutate the
    result (e.g. ``cfg["model"]["default"] = ...`` before ``save_config``).
    The cache is keyed on ``str(config_path)`` so profile switches
    (which change ``JANUS_HOME`` and therefore ``get_config_path()``)
    don't collide.

    Read-only callers should use ``load_config_readonly()`` to skip the
    defensive deepcopy — that path matters in agent-loop hot spots like
    ``get_provider_request_timeout`` which is called once per API turn.
    """
    return _load_config_impl(want_deepcopy=True)


def load_config_readonly() -> Dict[str, Any]:
    """Fast-path variant of ``load_config()`` for callers that ONLY READ.

    Returns the cached config dict directly without the defensive deepcopy
    that ``load_config()`` applies. **Mutating the returned dict (or any
    nested structure) corrupts the in-process cache for every subsequent
    caller** — only use this when you are absolutely sure your code path
    will not write to the result. If you need to mutate or pass to
    ``save_config``, call ``load_config()`` instead.

    Why this exists: ``load_config()`` cache-hit cost is ~265us per call,
    half of which (~135us) is the defensive deepcopy. The agent loop calls
    into config reads (timeouts, thresholds, feature flags) ~20-50x per
    conversation; skipping deepcopy here removes a measurable allocation
    source and the GC pressure that comes with it.

    Note: this returns a plain ``dict`` (not ``MappingProxyType``) so
    existing ``isinstance(x, dict)`` guards downstream keep working. The
    safety guarantee is purely documented, not enforced — be careful.
    """
    return _load_config_impl(want_deepcopy=False)


def _load_config_impl(*, want_deepcopy: bool) -> Dict[str, Any]:
    with _CONFIG_LOCK:
        ensure_janus_home()
        config_path = get_config_path()
        path_key = str(config_path)

        try:
            st = config_path.stat()
            cache_key: Optional[Tuple[int, int]] = (st.st_mtime_ns, st.st_size)
        except FileNotFoundError:
            cache_key = None

        cached = _LOAD_CONFIG_CACHE.get(path_key)
        if cached is not None and cache_key is not None and cached[:2] == cache_key:
            return copy.deepcopy(cached[2]) if want_deepcopy else cached[2]

        config = copy.deepcopy(DEFAULT_CONFIG)

        if cache_key is not None:
            try:
                with open(config_path, encoding="utf-8") as f:
                    user_config = yaml.safe_load(f) or {}

                if "max_turns" in user_config:
                    agent_user_config = dict(user_config.get("agent") or {})
                    if agent_user_config.get("max_turns") is None:
                        agent_user_config["max_turns"] = user_config["max_turns"]
                    user_config["agent"] = agent_user_config
                    user_config.pop("max_turns", None)

                config = _deep_merge(config, user_config)
            except Exception as e:
                _warn_config_parse_failure(config_path, e)

        normalized = _normalize_root_model_keys(_normalize_max_turns_config(config))
        expanded = _expand_env_vars(normalized)
        _LAST_EXPANDED_CONFIG_BY_PATH[path_key] = copy.deepcopy(expanded)
        if cache_key is not None:
            # Cache stores a separate deepcopy so subsequent ``load_config()``
            # (deepcopy=True) callers can mutate freely without affecting the
            # cached value, and ``load_config_readonly()`` (deepcopy=False)
            # callers all see the same stable cached object.
            cached_copy = copy.deepcopy(expanded)
            _LOAD_CONFIG_CACHE[path_key] = (cache_key[0], cache_key[1], cached_copy)
            # On the readonly path return the same cached object subsequent
            # calls will see — keeps "two readonly calls return the same
            # object" invariant that callers may rely on for identity checks.
            if not want_deepcopy:
                return cached_copy
        else:
            _LOAD_CONFIG_CACHE.pop(path_key, None)
        # First-load result is a fresh dict (not aliased to the cache); safe
        # to return directly. For the deepcopy=True path this is the
        # canonical "freshly-built mutable result" the function has always
        # returned. For the deepcopy=False path with no cache (e.g. config
        # file missing), it's also fine — callers get an isolated object.
        return expanded


_SECURITY_COMMENT = """
# ── Security ──────────────────────────────────────────────────────────
# Secret redaction is ON by default — strings that look like API keys,
# tokens, and passwords are masked in tool output, logs, and chat
# responses before the model or user ever sees them. Set redact_secrets
# to false to disable (e.g. when developing the redactor itself).
# tirith pre-exec scanning is enabled by default when the tirith binary
# is available. Configure via security.tirith_* keys or env vars
# (TIRITH_ENABLED, TIRITH_BIN, TIRITH_TIMEOUT, TIRITH_FAIL_OPEN).
#
# security:
#   redact_secrets: true
#   tirith_enabled: true
#   tirith_path: "tirith"
#   tirith_timeout: 5
#   tirith_fail_open: true
"""

_FALLBACK_COMMENT = """
# ── Fallback Model ────────────────────────────────────────────────────
# Automatic provider failover when primary is unavailable.
# Uncomment and configure to enable. Triggers on rate limits (429),
# overload (529), service errors (503), or connection failures.
#
# Supported providers:
#   openrouter   (OPENROUTER_API_KEY)  — routes to any model
#   openai-codex (OAuth — janus auth) — OpenAI Codex
#   nous         (OAuth — janus auth) — Cloud Industry Portal
#   zai          (ZAI_API_KEY)         — Z.AI / GLM
#   kimi-coding  (KIMI_API_KEY)        — Kimi / Moonshot
#   kimi-coding-cn (KIMI_CN_API_KEY)   — Kimi / Moonshot (China)
#   minimax      (MINIMAX_API_KEY)     — MiniMax
#   minimax-cn   (MINIMAX_CN_API_KEY)  — MiniMax (China)
#   bedrock      (AWS IAM / boto3)     — AWS Bedrock (Converse API)
#
# For custom OpenAI-compatible endpoints, add base_url and key_env.
#
# fallback_model:
#   provider: openrouter
#   model: anthropic/claude-sonnet-4
"""


_COMMENTED_SECTIONS = """
# ── Security ──────────────────────────────────────────────────────────
# Secret redaction is ON by default. Set to false to pass tool output,
# logs, and chat responses through unmodified (e.g. for redactor dev).
#
# security:
#   redact_secrets: true

# ── Fallback Model ────────────────────────────────────────────────────
# Automatic provider failover when primary is unavailable.
# Uncomment and configure to enable. Triggers on rate limits (429),
# overload (529), service errors (503), or connection failures.
#
# Supported providers:
#   openrouter   (OPENROUTER_API_KEY)  — routes to any model
#   openai-codex (OAuth — janus auth) — OpenAI Codex
#   nous         (OAuth — janus auth) — Cloud Industry Portal
#   zai          (ZAI_API_KEY)         — Z.AI / GLM
#   kimi-coding  (KIMI_API_KEY)        — Kimi / Moonshot
#   kimi-coding-cn (KIMI_CN_API_KEY)   — Kimi / Moonshot (China)
#   minimax      (MINIMAX_API_KEY)     — MiniMax
#   minimax-cn   (MINIMAX_CN_API_KEY)  — MiniMax (China)
#   bedrock      (AWS IAM / boto3)     — AWS Bedrock (Converse API)
#
# For custom OpenAI-compatible endpoints, add base_url and key_env.
#
# fallback_model:
#   provider: openrouter
#   model: anthropic/claude-sonnet-4
"""


def save_config(config: Dict[str, Any]):
    """Save configuration to ~/.janus/config.yaml."""
    with _CONFIG_LOCK:
        if is_managed():
            managed_error("save configuration")
            return
        from utils import atomic_yaml_write

        ensure_janus_home()
        config_path = get_config_path()
        current_normalized = _normalize_root_model_keys(_normalize_max_turns_config(config))
        normalized = current_normalized
        raw_existing = _normalize_root_model_keys(_normalize_max_turns_config(read_raw_config()))
        if raw_existing:
            normalized = _preserve_env_ref_templates(
                normalized,
                raw_existing,
                _LAST_EXPANDED_CONFIG_BY_PATH.get(str(config_path)),
            )

        # Build optional commented-out sections for features that are off by
        # default or only relevant when explicitly configured.
        parts = []
        sec = normalized.get("security", {})
        if not sec or sec.get("redact_secrets") is None:
            parts.append(_SECURITY_COMMENT)
        fb = normalized.get("fallback_model", {})
        fb_is_valid = False
        if isinstance(fb, list):
            fb_is_valid = any(isinstance(e, dict) and e.get("provider") and e.get("model") for e in fb)
        elif isinstance(fb, dict):
            fb_is_valid = bool(fb.get("provider") and fb.get("model"))
        if not fb_is_valid:
            parts.append(_FALLBACK_COMMENT)

        atomic_yaml_write(
            config_path,
            normalized,
            extra_content="".join(parts) if parts else None,
        )
        _secure_file(config_path)
        _LAST_EXPANDED_CONFIG_BY_PATH[str(config_path)] = copy.deepcopy(current_normalized)


