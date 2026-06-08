# Langfuse Observability Plugin

This plugin ships bundled with Janus but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

Pick one:

```bash
# Interactive: walks you through credentials + SDK install + enable
janus tools  # → Langfuse Observability

# Manual
pip install langfuse
janus plugins enable observability/langfuse
```

## Required credentials

Set these in `~/.janus/.env` (or via `janus tools`):

```bash
JANUS_LANGFUSE_PUBLIC_KEY=pk-lf-...
JANUS_LANGFUSE_SECRET_KEY=sk-lf-...
JANUS_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
janus plugins list                 # observability/langfuse should show "enabled"
janus chat -q "hello"              # then check Langfuse for a "Janus turn" trace
```

## Optional tuning

```bash
JANUS_LANGFUSE_ENV=production       # environment tag
JANUS_LANGFUSE_RELEASE=v1.0.0       # release tag
JANUS_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
JANUS_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
JANUS_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
janus plugins disable observability/langfuse
```
