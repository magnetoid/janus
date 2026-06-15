"""
Gateway runner - entry point for messaging platform integrations.

This module provides:
- start_gateway(): Start all configured platform adapters
- GatewayRunner: Main class managing the gateway lifecycle

Usage:
    # Start the gateway
    python -m gateway.run
    
    # Or from CLI
    python cli.py --gateway
"""

from gateway.core import *
from gateway.runner import *

# Back-compat shim: ``gateway.run`` is the historical import path. The wildcard
# imports above do NOT re-export underscore-prefixed names, so private helpers
# that callers still import from here (e.g. gateway.platforms.api_server /
# feishu_comment import _resolve_gateway_model, _load_gateway_config,
# _resolve_runtime_agent_kwargs) would be missing. Re-export every private name
# from core and runner so the legacy path keeps working.
import gateway.core as _core
import gateway.runner as _runner
for _src in (_core, _runner):
    for _n in dir(_src):
        if _n.startswith("_") and not _n.startswith("__") and _n not in globals():
            globals()[_n] = getattr(_src, _n)
del _core, _runner, _src, _n

if __name__ == "__main__":
    import sys
    sys.exit(main())
