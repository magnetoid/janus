from fastapi import APIRouter, HTTPException, Request, Response, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Tuple, Union
import janus_cli.web_server as web_server_mod

router = APIRouter()

@router.get("/api/cron/jobs")
async def list_cron_jobs(profile: str = "all"):
    requested = (profile or "all").strip()
    if requested.lower() != "all":
        return web_server_mod._call_cron_for_profile(requested, "list_jobs", True)

    jobs: web_server_mod.List[web_server_mod.Dict[str, web_server_mod.Any]] = []
    for item in web_server_mod._cron_profile_dicts():
        name = str(item.get("name") or "")
        if not name:
            continue
        try:
            jobs.extend(web_server_mod._call_cron_for_profile(name, "list_jobs", True))
        except Exception:
            web_server_mod._log.exception("Failed to list cron jobs for profile %s", name)
    return jobs

@router.get("/api/cron/jobs/{job_id}")
async def get_cron_job(job_id: str, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    job = web_server_mod._call_cron_for_profile(selected, "get_job", job_id)
    if not job:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return job

@router.get("/api/cron/jobs/{job_id}/runs")
async def list_cron_job_runs(job_id: str, profile: web_server_mod.Optional[str] = None, limit: int = 20):
    """Run sessions produced by a cron job, newest first.

    Cron runs are stored as ordinary sessions whose id is
    ``cron_{job_id}_{timestamp}`` (see cron/scheduler.run_job). A job's history
    is therefore every session whose id carries that prefix; ``source='cron'``
    narrows it and the id prefix binds it to this job. Powers the run-history
    list under each job in the desktop cron detail. Same row shape as
    ``/api/sessions`` so the frontend can reuse SessionInfo.

    Backed by ``SessionDB.list_cron_job_runs`` — a bounded ``[prefix, hi)``
    id-range scan, not the compression-chain CTE used for the recents list,
    so the cost scales with the requested window and not the (unbounded) total
    cron history.
    """
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    # job_id may be a human name; resolve to the canonical id used in run-session ids.
    canonical = job_id
    if selected:
        job = web_server_mod._call_cron_for_profile(selected, "get_job", job_id)
        if job and job.get("id"):
            canonical = str(job["id"])

    try:
        limit_n = max(1, min(int(limit), 100))
    except (TypeError, ValueError):
        limit_n = 20

    db = web_server_mod._open_session_db_for_profile(selected)
    try:
        runs = db.list_cron_job_runs(canonical, limit=limit_n, offset=0)
        now = web_server_mod.time.time()
        for s in runs:
            s["is_active"] = (
                s.get("ended_at") is None
                and (now - s.get("last_active", s.get("started_at", 0))) < 300
            )
            s["archived"] = bool(s.get("archived"))
            if selected:
                s["profile"] = selected
        return {"runs": runs, "limit": limit_n}
    finally:
        db.close()

@router.post("/api/cron/jobs")
async def create_cron_job(body: web_server_mod.CronJobCreate, profile: str = "default"):
    try:
        return web_server_mod._call_cron_for_profile(
            profile,
            "create_job",
            prompt=body.prompt,
            schedule=body.schedule,
            name=body.name,
            deliver=body.deliver,
        )
    except Exception as e:
        web_server_mod._log.exception("POST /api/cron/jobs failed")
        raise web_server_mod.HTTPException(status_code=400, detail=str(e))

@router.get("/api/cron/delivery-targets")
async def get_cron_delivery_targets():
    """Delivery targets the cron dropdown should offer.

    Always includes the implicit ``local`` option. Beyond that, the list is
    derived dynamically from the configured gateway platforms via
    ``cron.scheduler.cron_delivery_targets()`` — no hardcoded platform list. A
    configured platform that hasn't set its cron home channel is still returned
    with ``home_target_set: false`` so the UI can surface it as "configure a
    home channel first" rather than hiding it.
    """
    targets = [
        {
            "id": "local",
            "name": "Local (save only)",
            "home_target_set": True,
            "home_env_var": None,
        }
    ]
    try:
        from cron.scheduler import cron_delivery_targets

        targets.extend(cron_delivery_targets())
    except Exception:
        web_server_mod._log.exception("GET /api/cron/delivery-targets failed")
    return {"targets": targets}

@router.put("/api/cron/jobs/{job_id}")
async def update_cron_job(job_id: str, body: web_server_mod.CronJobUpdate, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    try:
        job = web_server_mod._call_cron_for_profile(selected, "update_job", job_id, body.updates)
    except ValueError as exc:
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    if not job:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/api/cron/jobs/{job_id}/pause")
async def pause_cron_job(job_id: str, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    job = web_server_mod._call_cron_for_profile(selected, "pause_job", job_id)
    if not job:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/api/cron/jobs/{job_id}/resume")
async def resume_cron_job(job_id: str, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    job = web_server_mod._call_cron_for_profile(selected, "resume_job", job_id)
    if not job:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/api/cron/jobs/{job_id}/trigger")
async def trigger_cron_job(job_id: str, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    job = web_server_mod._call_cron_for_profile(selected, "trigger_job", job_id)
    if not job:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return job

@router.delete("/api/cron/jobs/{job_id}")
async def delete_cron_job(job_id: str, profile: web_server_mod.Optional[str] = None):
    selected = profile or web_server_mod._find_cron_job_profile(job_id)
    if not selected:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    try:
        removed = web_server_mod._call_cron_for_profile(selected, "remove_job", job_id)
    except ValueError as exc:
        raise web_server_mod.HTTPException(status_code=400, detail=str(exc)) from exc
    if not removed:
        raise web_server_mod.HTTPException(status_code=404, detail="Job not found")
    return {"ok": True}

