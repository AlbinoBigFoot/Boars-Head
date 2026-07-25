# Boars Head — FactoryTalk → Ignition

Contractor lab for converting FactoryTalk View SE to Ignition.  
Client: FBCO · Integrator: One Shot · Repo: [AlbinoBigFoot/Boars-Head](https://github.com/AlbinoBigFoot/Boars-Head)

## Quick start

```powershell
Copy-Item .env.example .env
# Edit .env — set GATEWAY_ADMIN_PASSWORD and MSSQL_SA_PASSWORD

# First-time only: seed host data dirs from images (empty bind mounts break Ignition init)
.\scripts\seed-gateway-data.ps1

docker compose pull
docker compose up -d
```

| Service | URL / port (defaults in `.env`) | Image |
|---------|------------|-------|
| Standard Gateway | http://localhost:19088 | `inductiveautomation/ignition:8.3.7` |
| Edge Gateway | http://localhost:19188 | `inductiveautomation/ignition:8.3.7` (`IGNITION_EDITION=edge`) |
| MSSQL | localhost:11433 | `mcr.microsoft.com/mssql/server:2022-latest` |
| Engineering Wiki | http://localhost:3030 | Docusaurus (`wiki/` — `docker compose up -d wiki`) |

Ports are remappable in `.env` if something else already binds common Ignition/SQL ports.

Gateway volumes are **bind-mounted** under `gateways/*/data` for Git. MSSQL uses named volume `bh-mssql-data` (internal).

## Planning (GSD)

| Doc | Purpose |
|-----|---------|
| `.planning/PRIORITIES.md` | Needs vs Wants + One Shot ToDo |
| `.planning/PROJECT.md` | Project context |
| `.planning/REQUIREMENTS.md` | Acceptance criteria |
| `.planning/ROADMAP.md` | Phases 1–7 |
| `.planning/STATE.md` | Current status |

Next: `/gsd-plan-phase 1` after the stack is healthy.

## Graphify

Knowledge graph of tracker + planning docs lives in `graphify-out/` (`GRAPH_REPORT.md`, `graph.html`).

```powershell
# Rebuild after planning docs change
# (agent runs /graphify — or graphify CLI if installed)
```

## Standard → Edge mirror

1. Commission both gateways (accept EULA via env already set).
2. Open Gateway Network on Standard → add Edge (`ignition-edge:8088` on Docker network `bh-ot`, or host ports).
3. Use EAM / project sync so Edge mirrors the Standard project.
4. Both gateways are on **8.3.7** — `GATEWAY_NETWORK_ALLOWJAVASERIALIZATION` can stay `false` (only needed for mixed 8.1↔8.3 GAN).

## MSSQL from Ignition

- Host from containers: `mssql`
- Host from workstation: `localhost,11433` (or `MSSQL_PORT` from `.env`)
- Auth: SA password from `.env` (lab only — replace with least-privilege SQL user for real work)

## Engineering wiki (Docusaurus)

Living archive for components, scripting, named queries, tags, and gateway settings:

```powershell
docker compose up -d --build wiki
```

Open http://localhost:3030. Search is local (`@easyops-cn/docusaurus-search-local`) — no Algolia signup. Source lives in `wiki/`.

## Perspective HMI

New to the BH Perspective project? Start here:

- **[Adhoc trending](wiki/docs/perspective/adhoc-trending.md)** (wiki: `/docs/perspective/adhoc-trending`) — `/trending`, saved configs, SQL, ApexCharts
- **[docs/evaporator-hmi-components.md](docs/evaporator-hmi-components.md)** — pages, embedded device/element views, CSS (`fan-spin`, `alarm-flash`), scripts, tags, icons, and how Overview is wired
- **[docs/central-alarming.md](docs/central-alarming.md)** — Alarm Status (`/alarms`), Alarm Journal (`/alarms/journal`), Device Type multi-select filter, priority row colors

## Source documents

| File | Purpose |
|------|---------|
| `FactoryTalk to Ignition Migration Tracker V6.xlsx` | Needs/Wants scope + ownership |
| `Refrigeration MCC IPs.xlsx` | OT device IPs on `10.80.31.0/24` |
| `docs/network-inventory.md` | Cleaned inventory + Ignition implications |
| `docs/ignition-license-quote-checklist.md` | Addon modules for distributor cost estimate |
| `docs/evaporator-hmi-components.md` | Evaporator Overview / component onboarding |
