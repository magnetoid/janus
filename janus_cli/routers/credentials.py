from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/credentials/pool")
async def list_credential_pool():
    from agent.credential_pool import load_pool
    from janus_cli.auth import read_credential_pool

    providers = []
    # read_credential_pool(None) lists every provider that has pooled entries;
    # load_pool() then gives us the rich PooledCredential objects per provider.
    raw_pool = read_credential_pool()
    for provider_id in sorted(raw_pool.keys()):
        try:
            pool = load_pool(provider_id)
        except Exception:
            web_server_mod._log.exception("load_pool(%s) failed", provider_id)
            continue
        entries = pool.entries()
        if not entries:
            continue
        providers.append({
            "provider": provider_id,
            "entries": [
                web_server_mod._pool_entry_summary(e, i) for i, e in enumerate(entries, start=1)
            ],
        })
    return {"providers": providers}

@router.post("/api/credentials/pool")
async def add_credential_pool_entry(body: web_server_mod.CredentialPoolAdd):
    import uuid as _uuid
    from agent.credential_pool import (
        load_pool,
        PooledCredential,
        AUTH_TYPE_API_KEY,
        SOURCE_MANUAL,
    )

    provider = (body.provider or "").strip().lower()
    api_key = (body.api_key or "").strip()
    if not provider or not api_key:
        raise web_server_mod.HTTPException(status_code=400, detail="provider and api_key are required")

    try:
        pool = load_pool(provider)
        label = (body.label or "").strip() or f"key #{len(pool.entries()) + 1}"
        entry = PooledCredential(
            provider=provider,
            id=_uuid.uuid4().hex[:6],
            label=label,
            auth_type=AUTH_TYPE_API_KEY,
            priority=0,
            source=SOURCE_MANUAL,
            access_token=api_key,
        )
        pool.add_entry(entry)
    except Exception as exc:
        web_server_mod._log.exception("POST /api/credentials/pool failed")
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    return {"ok": True, "provider": provider, "count": len(pool.entries())}

@router.delete("/api/credentials/pool/{provider}/{index}")
async def remove_credential_pool_entry(provider: str, index: int):
    """Remove a pool entry.  ``index`` is 1-based (matches the list response)."""
    from agent.credential_pool import load_pool

    provider = (provider or "").strip().lower()
    try:
        pool = load_pool(provider)
        removed = pool.remove_index(index)
    except Exception as exc:
        web_server_mod._log.exception("DELETE /api/credentials/pool failed")
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    if removed is None:
        raise web_server_mod.HTTPException(status_code=404, detail="No pool entry at that index")
    return {"ok": True, "provider": provider, "count": len(pool.entries())}

