"""OpenTelemetry (OTLP) observability for Janus.

Exports LLM and tool metrics over OTLP so the agent's behaviour and the
self-improvement loop can be *measured*, not asserted. A standalone plugin in
the spirit of ``observability/langfuse``: it touches **zero core files** and
only consumes the existing ``post_api_request`` (per API call) and
``pre/post_tool_call`` hooks.

Inert by default. ``register`` always installs the hooks, but they no-op until
BOTH (a) ``opentelemetry`` is installed and (b) an OTLP endpoint is configured
via ``OTEL_EXPORTER_OTLP_ENDPOINT`` (or ``JANUS_OTLP_ENDPOINT``). So enabling
the plugin without the optional deps costs nothing and never raises.

Enable:  ``janus plugins enable observability/otlp``
Deps:    ``uv pip install opentelemetry-sdk opentelemetry-exporter-otlp``
Config:  set ``OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318/v1/metrics``

Emitted instruments (all labelled by model/provider or tool):
  janus.llm.tokens      (counter, by kind=input|output|cache_read)
  janus.llm.cost_usd    (counter)
  janus.llm.latency     (histogram, seconds)
  janus.tool.calls      (counter, by status=ok|error)
  janus.tool.latency    (histogram, seconds)
"""
from __future__ import annotations

import logging
import os
import threading
import time
from typing import Any, Dict

logger = logging.getLogger(__name__)

_LOCK = threading.Lock()
_INSTRUMENTS: Dict[str, Any] = {}
_INIT_ATTEMPTED = False
_TOOL_START: Dict[str, float] = {}  # key -> monotonic start, for tool latency


def _endpoint() -> str:
    return (os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT")
            or os.environ.get("JANUS_OTLP_ENDPOINT") or "").strip()


def _get_instruments() -> Dict[str, Any]:
    """Lazily build the OTel meter + instruments. Returns ``{}`` (inert) when
    opentelemetry is missing or no OTLP endpoint is configured. Attempted once."""
    global _INIT_ATTEMPTED
    with _LOCK:
        if _INSTRUMENTS or _INIT_ATTEMPTED:
            return _INSTRUMENTS
        _INIT_ATTEMPTED = True
        if not _endpoint():
            return _INSTRUMENTS
        try:
            from opentelemetry import metrics
            from opentelemetry.sdk.metrics import MeterProvider
            from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
            from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
            from opentelemetry.sdk.resources import Resource

            reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint=_endpoint()))
            provider = MeterProvider(
                metric_readers=[reader],
                resource=Resource.create({"service.name": "janus-agent"}),
            )
            metrics.set_meter_provider(provider)
            meter = metrics.get_meter("janus")
            _INSTRUMENTS.update({
                "llm_tokens": meter.create_counter("janus.llm.tokens", unit="token"),
                "llm_cost": meter.create_counter("janus.llm.cost_usd", unit="USD"),
                "llm_latency": meter.create_histogram("janus.llm.latency", unit="s"),
                "tool_calls": meter.create_counter("janus.tool.calls", unit="call"),
                "tool_latency": meter.create_histogram("janus.tool.latency", unit="s"),
            })
            logger.info("OTLP observability active → %s", _endpoint())
        except Exception as exc:  # pragma: no cover - depends on optional dep
            logger.debug("OTLP init skipped (opentelemetry missing/misconfigured): %s", exc)
    return _INSTRUMENTS


# ── pure extractors (testable without opentelemetry) ────────────────────────

def _llm_metrics(*, model: str = "", provider: str = "", base_url: str = "",
                 api_mode: str = "", usage: Any = None, api_duration: float = 0.0) -> Dict[str, Any]:
    """Extract {model, provider, *_tokens, cost_usd, latency_s} from a
    post-api-request hook's kwargs. Best-effort; tokens/cost default to 0."""
    out: Dict[str, Any] = {
        "model": model or "unknown", "provider": provider or "unknown",
        "input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0,
        "cost_usd": 0.0, "latency_s": float(api_duration or 0.0),
    }
    if usage is None:
        return out
    try:
        from agent.usage_pricing import estimate_usage_cost, normalize_usage

        cu = normalize_usage(usage, provider=provider, api_mode=api_mode)
        out["input_tokens"] = int(getattr(cu, "input_tokens", 0) or 0)
        out["output_tokens"] = int(getattr(cu, "output_tokens", 0) or 0)
        out["cache_read_tokens"] = int(getattr(cu, "cache_read_tokens", 0) or 0)
        cr = estimate_usage_cost(model, cu, provider=provider, base_url=base_url)
        if getattr(cr, "amount_usd", None) is not None:
            out["cost_usd"] = float(cr.amount_usd)
    except Exception as exc:
        logger.debug("OTLP llm metric extraction failed: %s", exc)
    return out


def _tool_succeeded(result: Any) -> bool:
    """A tool result is a FAILURE when it is a tool_error JSON (``{"error":...}``)."""
    c = str(result or "").lstrip()
    return not (c.startswith('{"error"') or c.lower().startswith("error:"))


def _tool_key(task_id: str, session_id: str, tool_call_id: str) -> str:
    return f"{task_id}|{session_id}|{tool_call_id}"


# ── hooks ───────────────────────────────────────────────────────────────────

def on_post_api_request(*, model: str = "", provider: str = "", base_url: str = "",
                        api_mode: str = "", usage: Any = None, api_duration: float = 0.0,
                        **_: Any) -> None:
    inst = _get_instruments()
    if not inst:
        return
    try:
        m = _llm_metrics(model=model, provider=provider, base_url=base_url,
                         api_mode=api_mode, usage=usage, api_duration=api_duration)
        labels = {"model": m["model"], "provider": m["provider"]}
        for kind in ("input", "output", "cache_read"):
            n = m[f"{kind}_tokens"]
            if n:
                inst["llm_tokens"].add(n, {**labels, "kind": kind})
        if m["cost_usd"]:
            inst["llm_cost"].add(m["cost_usd"], labels)
        inst["llm_latency"].record(m["latency_s"], labels)
    except Exception as exc:
        logger.debug("OTLP post_api_request emit failed: %s", exc)


def on_pre_tool_call(*, task_id: str = "", session_id: str = "", tool_call_id: str = "",
                     **_: Any) -> None:
    if not _get_instruments():
        return
    try:
        _TOOL_START[_tool_key(task_id, session_id, tool_call_id)] = time.monotonic()
    except Exception:
        pass


def on_post_tool_call(*, tool_name: str = "", result: Any = None, task_id: str = "",
                      session_id: str = "", tool_call_id: str = "", **_: Any) -> None:
    inst = _get_instruments()
    if not inst:
        return
    try:
        start = _TOOL_START.pop(_tool_key(task_id, session_id, tool_call_id), None)
        duration = (time.monotonic() - start) if start else 0.0
        tool = tool_name or "unknown"
        inst["tool_calls"].add(1, {"tool": tool, "status": "ok" if _tool_succeeded(result) else "error"})
        inst["tool_latency"].record(duration, {"tool": tool})
    except Exception as exc:
        logger.debug("OTLP post_tool_call emit failed: %s", exc)


def register(ctx) -> None:
    # post_api_request fires once per API call and carries usage/latency — the
    # right granularity for LLM metrics (post_llm_call is per-turn → would
    # double-count, so it is intentionally NOT registered here).
    ctx.register_hook("post_api_request", on_post_api_request)
    ctx.register_hook("pre_tool_call", on_pre_tool_call)
    ctx.register_hook("post_tool_call", on_post_tool_call)
