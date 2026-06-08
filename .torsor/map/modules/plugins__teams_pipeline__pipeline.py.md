---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/teams_pipeline/pipeline.py

Symbols in `plugins/teams_pipeline/pipeline.py`.

- L52 `TeamsPipelineError` (class) — Base class for Teams meeting pipeline failures.
- L56 `TeamsPipelineRetryableError` (class) — Raised when the pipeline should be retried later.
- L60 `TeamsPipelineSinkError` (class) — Raised when an output sink fails.
- L64 `TeamsPipelineArtifactNotFoundError` (class) — Raised when meeting artifacts are not yet available.
- L77 `TeamsPipelineConfig` (class)
- L90 `from_dict(cls, payload: Optional[dict[str, Any]])` (method)
- L107 `NotionWriter` (class)
- L111 `__init__(self, *, api_key: str | None=None, transport: httpx.AsyncBaseTransport | None=None)` (method)
- L115 `write_summary(self, payload: TeamsMeetingSummaryPayload, config: dict[str, Any], existing_record: Optional[dict[str, Any]]=None)` (method)
- L158 `_build_properties(self, payload: TeamsMeetingSummaryPayload, config: dict[str, Any])` (method)
- L178 `_build_blocks(self, payload: TeamsMeetingSummaryPayload)` (method)
- L204 `LinearWriter` (class)
- L207 `__init__(self, *, api_key: str | None=None, transport: httpx.AsyncBaseTransport | None=None)` (method)
- L211 `write_summary(self, payload: TeamsMeetingSummaryPayload, config: dict[str, Any], existing_record: Optional[dict[str, Any]]=None)` (method)
- L269 `TeamsMeetingPipeline` (class) — Transcript-first Teams meeting pipeline with durable lifecycle state.
- L272 `__init__(self, *, graph_client: Any, store: TeamsPipelineStore, config: TeamsPipelineConfig | dict[str, Any] | None=None, transcribe_fn: TranscribeFn=transcribe_audio, summarize_fn: Optional[SummarizeFn]=None, notion_writer: Optional[NotionWriter]=None, linear_writer: Optional[LinearWriter]=None, teams_sender: Optional[SinkFn]=None)` (method)
- L293 `create_job_from_notification(self, notification: dict[str, Any])` (method)
- L326 `run_notification(self, notification: dict[str, Any])` (method)
- L332 `run_job(self, job_or_id: TeamsMeetingPipelineJob | str)` (method)
- L427 `_coerce_job(self, job_or_id: TeamsMeetingPipelineJob | str)` (method)
- L435 `_find_job_by_dedupe_key(self, dedupe_key: str)` (method)
- L444 `_persist_job(self, job: TeamsMeetingPipelineJob, **updates: Any)` (method)
- L450 `_transcribe_recording(self, job: TeamsMeetingPipelineJob, meeting_ref: TeamsMeetingRef, recording: MeetingArtifact)` (method)
- L477 `_prepare_audio_path(self, recording_path: Path)` (method)
- L503 `_generate_summary_payload(self, *, resolved_meeting: TeamsMeetingRef, transcript_text: str, artifacts: list[MeetingArtifact])` (method)
- L557 `_write_sinks(self, job: TeamsMeetingPipelineJob, payload: TeamsMeetingSummaryPayload)` (method)
- L583 `_collect_call_metrics(artifacts: list[MeetingArtifact])` (function)
- L592 `_collect_participants(meeting_ref: TeamsMeetingRef)` (function)
- L604 `_extract_meeting_id_from_resource(resource: str)` (function)
- L617 `_build_summary_prompt(meeting_ref: TeamsMeetingRef, transcript_text: str, artifacts: list[MeetingArtifact])` (function)
- L632 `_parse_summary_json(content: str)` (function)
- L651 `_heuristic_summary(transcript_text: str)` (function)
- L670 `_render_summary_markdown(payload: TeamsMeetingSummaryPayload)` (function)
