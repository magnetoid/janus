"""Live provider-credential verification — shared by setup and doctor.

A freshly-pasted API key that is wrong should fail at paste time, not on the
user's first real conversation. ``live_check_provider()`` makes one cheap
authenticated request (a models-list GET — no tokens spent) against the
provider the user just configured and reports plainly: verified, rejected,
or unreachable.

The check is deliberately best-effort: providers without a checkable
endpoint (OAuth flows that already validated during auth, SigV4 providers
like Bedrock, local endpoints) return ``skip`` and setup proceeds — a
missing health check must never block onboarding.
"""

from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)

# status values
OK = "ok"                  # authenticated request succeeded
INVALID = "invalid"        # provider rejected the credential (401/403)
UNREACHABLE = "unreachable"  # network trouble — do not block on this
SKIP = "skip"              # no checkable endpoint for this provider


@dataclass
class CheckResult:
    status: str
    detail: str = ""
    latency_ms: Optional[int] = None


def _first_env(*names: str) -> Optional[str]:
    for name in names:
        value = os.getenv(name)
        if value and value.strip():
            return value.strip()
    return None


def _get(url: str, headers: dict, timeout: float = 10.0) -> CheckResult:
    import httpx

    started = time.monotonic()
    try:
        r = httpx.get(url, headers=headers, timeout=timeout)
    except Exception as exc:
        logger.debug("provider check unreachable (%s): %s", url, exc)
        return CheckResult(UNREACHABLE, "could not reach the provider API")
    latency = int((time.monotonic() - started) * 1000)
    if r.status_code == 200:
        return CheckResult(OK, latency_ms=latency)
    if r.status_code in (401, 403):
        return CheckResult(INVALID, "the provider rejected this credential", latency)
    if r.status_code == 402:
        return CheckResult(INVALID, "credential accepted but the account is out of credits", latency)
    if r.status_code == 429:
        # Rate-limited means the key authenticated — that's a pass for setup.
        return CheckResult(OK, "rate-limited but authenticated", latency)
    return CheckResult(UNREACHABLE, f"unexpected HTTP {r.status_code}", latency)


def _check_anthropic() -> CheckResult:
    try:
        from janus_cli.auth import get_anthropic_key
        key = get_anthropic_key()
    except Exception:
        key = _first_env("ANTHROPIC_API_KEY")
    if not key:
        return CheckResult(SKIP, "no Anthropic credential found")
    headers = {"anthropic-version": "2023-06-01"}
    if key.startswith("sk-ant-oat"):
        headers["Authorization"] = f"Bearer {key}"
    else:
        headers["x-api-key"] = key
    return _get("https://api.anthropic.com/v1/models", headers)


def _check_openrouter() -> CheckResult:
    key = _first_env("OPENROUTER_API_KEY")
    if not key:
        return CheckResult(SKIP, "no OPENROUTER_API_KEY found")
    return _get(
        "https://openrouter.ai/api/v1/models",
        {"Authorization": f"Bearer {key}"},
    )


def _check_openai() -> CheckResult:
    key = _first_env("OPENAI_API_KEY")
    if not key:
        return CheckResult(SKIP, "no OPENAI_API_KEY found")
    base = (_first_env("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
    return _get(f"{base}/models", {"Authorization": f"Bearer {key}"})


def _check_via_profile(provider: str) -> CheckResult:
    """Generic Bearer-auth check using the provider plugin's profile."""
    try:
        from providers import get_provider_profile
        profile = get_provider_profile(provider)
    except Exception:
        profile = None
    if profile is None:
        return CheckResult(SKIP, "no provider profile")
    if getattr(profile, "auth_type", None) != "api_key":
        return CheckResult(SKIP, f"auth type {getattr(profile, 'auth_type', '?')!r} verifies during auth")
    if not getattr(profile, "supports_health_check", True):
        return CheckResult(SKIP, "provider has no models endpoint")

    key_vars = tuple(
        v for v in (profile.env_vars or ())
        if not v.endswith("_BASE_URL") and not v.endswith("_URL")
    )
    key = _first_env(*key_vars) if key_vars else None
    if not key:
        return CheckResult(SKIP, "no credential found in environment")

    models_url = getattr(profile, "models_url", None)
    if not models_url:
        base = getattr(profile, "base_url", None)
        if not base:
            return CheckResult(SKIP, "provider profile has no base URL")
        models_url = base.rstrip("/") + "/models"
    return _get(models_url, {"Authorization": f"Bearer {key}"})


_DEDICATED = {
    "anthropic": _check_anthropic,
    "openrouter": _check_openrouter,
    "openai": _check_openai,
}


def live_check_provider(provider: Optional[str]) -> CheckResult:
    """Verify the configured credential for *provider* with one live request.

    Never raises. Returns a :class:`CheckResult` whose ``status`` is one of
    ``ok`` / ``invalid`` / ``unreachable`` / ``skip``. Callers should treat
    only ``invalid`` as actionable — ``unreachable`` and ``skip`` must not
    block setup.
    """
    name = (provider or "").strip().lower()
    if not name:
        return CheckResult(SKIP, "no provider selected")
    try:
        checker = _DEDICATED.get(name)
        if checker is not None:
            return checker()
        return _check_via_profile(name)
    except Exception as exc:  # verification must never break setup
        logger.debug("provider check failed for %s: %s", name, exc)
        return CheckResult(UNREACHABLE, str(exc))


def verify_telegram_token(token: str) -> tuple[str, dict]:
    """Live-check a Telegram bot token via the getMe API.

    Returns ``(status, bot_info)`` — status is ``ok`` (bot_info has
    ``username`` etc.), ``invalid`` (Telegram rejected the token), or
    ``unreachable`` (network trouble; callers should save and move on).
    Never raises.
    """
    if not token:
        return INVALID, {}
    try:
        import httpx
        r = httpx.get(f"https://api.telegram.org/bot{token}/getMe", timeout=10)
        try:
            data = r.json()
        except ValueError:
            data = {}
        if r.status_code == 200 and data.get("ok"):
            return OK, data.get("result") or {}
        if r.status_code in (401, 404):
            return INVALID, {}
        return UNREACHABLE, {}
    except Exception as exc:
        logger.debug("telegram getMe unreachable: %s", exc)
        return UNREACHABLE, {}
