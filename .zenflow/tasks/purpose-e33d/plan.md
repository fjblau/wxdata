# Auto

## Configuration
- **Artifacts Path**: {@artifacts_path} → `.zenflow/tasks/{task_id}`

---

## Agent Instructions

Ask the user questions when anything is unclear or needs their input. This includes:
- Ambiguous or incomplete requirements
- Technical decisions that affect architecture or user experience
- Trade-offs that require business context

Do not make assumptions on important decisions — get clarification first.

---

## Workflow Steps

### [x] Step: Implementation
<!-- chat-id: 7ceb8f5a-6142-41f3-a2ad-f282b4f0c1e1 -->

## Project Direction

**Purpose**: Demonstrate a multi-model atmospheric data platform using live weather station data — serving as a tangible showcase of the data architecture StratoChaser (radiosonde platform) needs to solve at scale.

**Stack**: React (Vite) + FastAPI + ArangoDB + Elasticsearch (live source: `sds2` index at 46.225.222.171:59200)

**Key concepts demonstrated**:
- BUFR field mapping: standard WMO fields vs. non-standard sensor payloads (the open payload problem)
- ArangoDB multi-model: documents (readings), graph (sensor→payload→reading relationships), KV (current conditions cache)
- Data product layer: raw ES sensor streams → structured, queryable API

### [ ] Step: Elasticsearch + BUFR mapping layer
- Add `elasticsearch8` to requirements
- Create `app/services/es_client.py` — connect to sds2, fetch latest + historical
- Create `app/services/bufr_map.py` — map sds2 fields to BUFR Table B descriptors, flag non-standard fields

### [ ] Step: ArangoDB multi-model schema
- Collections: `readings` (document), `sensors` (document), `payloads` (document)
- Edge collections: `sensor_readings`, `payload_sensors`
- Seed sensor and payload nodes from sds2 mapping

### [ ] Step: FastAPI routes
- `GET /api/current` — latest reading from ES, cached in Arango KV
- `GET /api/history` — time-range query from Arango readings collection
- `GET /api/bufr/fields` — full BUFR field map with standard/non-standard classification
- `GET /api/graph/sensors` — sensor→payload graph

### [ ] Step: React dashboard
- Current conditions panel (tempC, humidity, pressure, wind, AQI, space weather)
- BUFR field browser: table showing each field, its BUFR descriptor, and standard/custom status
- Simple time-series chart for key metrics

**Debug requests, questions, and investigations:** answer or investigate first. Do not create a plan upfront — the user needs an answer, not a plan. A plan may become relevant later once the investigation reveals what needs to change.

**For all other tasks**, before writing any code, assess the scope of the actual change (not the prompt length — a one-sentence prompt can describe a large feature). Scale your approach:

- **Trivial** (typo, config tweak, single obvious change): implement directly, no plan needed.
- **Small** (a few files, clear what to do): write 2–3 sentences in `plan.md` describing what and why, then implement. No substeps.
- **Medium** (multiple components, design decisions, edge cases): write a plan in `plan.md` with requirements, affected files, key decisions, verification. Break into 3–5 steps.
- **Large** (new feature, cross-cutting, unclear scope): gather requirements and write a technical spec first (`requirements.md`, `spec.md` in `{@artifacts_path}/`). Then write `plan.md` with concrete steps referencing the spec.

**Skip planning and implement directly when** the task is trivial, or the user explicitly asks to "just do it" / gives a clear direct instruction.

To reflect the actual purpose of the first step, you can rename it to something more relevant (e.g., Planning, Investigation). Do NOT remove meta information like comments for any step.

Rule of thumb for step size: each step = a coherent unit of work (component, endpoint, test suite). Not too granular (single function), not too broad (entire feature). Unit tests are part of each step, not separate.

Update `{@artifacts_path}/plan.md`.
