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
| Standard Gateway | http://localhost:19088 | `inductiveautomation/ignition:8.1.43` |
| Edge Gateway | http://localhost:19188 | `inductiveautomation/ignition:8.3.7` (`IGNITION_EDITION=edge`) |
| MSSQL | localhost:11433 | `mcr.microsoft.com/mssql/server:2022-latest` |

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
4. While Standard remains **8.1** and Edge **8.3**, keep `GATEWAY_NETWORK_ALLOWJAVASERIALIZATION=true` (temporary; remove after both on 8.3).

## MSSQL from Ignition

- Host from containers: `mssql`
- Host from workstation: `localhost,11433` (or `MSSQL_PORT` from `.env`)
- Auth: SA password from `.env` (lab only — replace with least-privilege SQL user for real work)

## Perspective HMI (evaporators)

New to the BH Perspective project? Start here:

- **[docs/evaporator-hmi-components.md](docs/evaporator-hmi-components.md)** — pages, embedded device/element views, CSS (`fan-spin`, `alarm-flash`), scripts, tags, icons, and how Overview is wired
- **[docs/central-alarming.md](docs/central-alarming.md)** — Alarm Status Table, `/alarms`, priority row colors (unack vs ack)

## Source documents

| File | Purpose |
|------|---------|
| `FactoryTalk to Ignition Migration Tracker V6.xlsx` | Needs/Wants scope + ownership |
| `Refrigeration MCC IPs.xlsx` | OT device IPs on `10.80.31.0/24` |
| `docs/network-inventory.md` | Cleaned inventory + Ignition implications |
| `docs/ignition-license-quote-checklist.md` | Addon modules for distributor cost estimate |
| `docs/evaporator-hmi-components.md` | Evaporator Overview / component onboarding |
