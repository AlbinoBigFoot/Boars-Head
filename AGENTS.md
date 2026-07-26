# AGENTS.md

## Cursor Cloud specific instructions

This repo is a **Docker Compose Ignition SCADA lab**, not a traditional code project.
There is no npm/pip/etc. dependency manager and **no lint/test/build tooling or CI**.
The deliverable is the `BH` Perspective HMI hosted by an Inductive Automation Ignition
gateway. See `README.md`, `gateways/README.md`, and `docs/` for domain details.

### Services (defined in `docker-compose.yml`, ports/passwords in `.env`)

| Service | Container | URL / port | Purpose |
|---------|-----------|------------|---------|
| `ignition-standard` | `bh-ignition-standard` | http://localhost:19088 | Primary gateway + `BH` Perspective HMI (**required**) |
| `mssql` | `bh-mssql` | `localhost,11433` | SQL Server backing adhoc-trend/historian (**required for full E2E**) |
| `ignition-edge` | `bh-ignition-edge` | http://localhost:19188 | Edge mirror gateway (optional) |
| `wiki` | `bh-wiki` | http://localhost:3030 | Docusaurus docs — **not runnable: `wiki/` build dir is absent from the repo** |

- BH Perspective HMI (the product): `http://localhost:19088/data/perspective/client/BH`
- Gateway config UI: `http://localhost:19088` — login `admin` / `GATEWAY_ADMIN_PASSWORD` from `.env`.

### Starting the stack (each fresh VM boot)

The snapshot already has Docker installed, images pulled, `.env` created, and the gateway
`data/` dirs seeded + initialized. Only the runtime processes need (re)starting:

1. `dockerd` is **not** auto-started (init is `tini`, no systemd). Start it if needed:
   `pgrep -x dockerd >/dev/null || sudo bash -c 'nohup dockerd >/var/log/dockerd.log 2>&1 &'`
2. Start the app services (do **not** include `wiki`):
   `sudo docker compose up -d ignition-standard ignition-edge mssql`
3. Gateways take ~30–60s to reach `ContextState = RUNNING`. Check:
   `curl -s http://localhost:19088/StatusPing` → `{"state":"RUNNING"}`.

### Non-obvious gotchas

- **Bind-mount ownership**: the Ignition container runs as uid/gid **2003**. The bind-mounted
  `gateways/*/data` must be owned by 2003 or init fails with `init.properties: Permission denied`
  (`sudo chown -R 2003:2003 gateways/standard/data gateways/edge/data`).
- **`core` resource-collection fault on a FRESH data dir**: the repo commits Perspective themes
  under `gateways/*/data/config/resources/core/...`. A first boot on a fresh gateway faults with
  `Resource collection path '.../config/resources/core' exists but is not empty` because Ignition
  wants to create `core` itself. Fix (only needed when re-seeding from scratch): move the committed
  `core` aside, boot once so Ignition creates `core` + `config.idb`, then overlay the committed
  `com.inductiveautomation.perspective/{themes,icons}` back into `core` and restart. This is already
  done in the snapshot.
- **Gateway mutates committed project source**: running `ignition-standard`/`ignition-edge`
  rehashes and rewrites `gateways/*/data/projects/.resources/*` (the content-addressed manifest).
  This shows as deleted/added `.resources/*` files in `git status`. It is expected churn — **do not
  commit it**; only the human-authored view/config files under `projects/` matter.
- **`.env` is gitignored** and already present with lab passwords. `docker compose` will error out
  if `GATEWAY_ADMIN_PASSWORD` / `MSSQL_SA_PASSWORD` are unset.

### MSSQL

- DB `ignition` + table `dbo.adhoc_trend_configs` (per `sql/adhoc_trend_configs.sql`) are already
  created in the `bh-mssql` named volume. When re-applying the schema, use sqlcmd with `-I`
  (QUOTED_IDENTIFIER ON) or the filtered index creation fails:
  `sudo docker exec -i bh-mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -I -d ignition < sql/adhoc_trend_configs.sql`
- The Ignition-side DB connection (named `ignition`) must be configured in the gateway UI; it is not
  auto-created.

### Optional: plant simulator

`python3 sim/build_plant_sim.py` (stdlib only) regenerates `sim/bh-plant-sim.csv` and OPC-UA sim
device/tag wiring so the HMI shows live-looking values without a real PLC.
