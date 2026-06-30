# OTLP observability

Exports Janus LLM + tool metrics over OpenTelemetry (OTLP) so spend, latency,
and tool reliability can be graphed in Prometheus/Grafana/Honeycomb/etc. — the
measurement spine the self-improvement loop is judged against.

**Standalone & inert by default.** Touches no core files; consumes the existing
`post_api_request` / `pre_tool_call` / `post_tool_call` hooks. Does nothing
until both the optional deps are installed *and* an endpoint is set.

## Enable

```bash
uv pip install opentelemetry-sdk opentelemetry-exporter-otlp
janus plugins enable observability/otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318/v1/metrics   # or JANUS_OTLP_ENDPOINT
```

## Instruments

| Instrument | Type | Labels |
|---|---|---|
| `janus.llm.tokens` | counter | `model`, `provider`, `kind` (input/output/cache_read) |
| `janus.llm.cost_usd` | counter | `model`, `provider` |
| `janus.llm.latency` | histogram (s) | `model`, `provider` |
| `janus.tool.calls` | counter | `tool`, `status` (ok/error) |
| `janus.tool.latency` | histogram (s) | `tool` |

LLM metrics come from `post_api_request` (per API call); tool latency is
measured between `pre_tool_call` and `post_tool_call`; tool failure is detected
from `tool_error()`-shaped results (`{"error": ...}`).
