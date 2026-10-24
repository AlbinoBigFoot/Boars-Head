---
title: Promote To Production
sidebar_position: 3
description: Step-by-step promotion of the BH project, UDTs, tags and gateway settings from the lab to a production gateway, in the right order.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/**/udts.json
  - docs/plc-write-lock.md
  - docs/local-groveport-mode.md
last_verified: 2026-10-24
---

# Promote To Production

This is the procedure for moving a **reviewed, merged** change (or a first install) from the lab to a production
gateway. It assumes the change is on `main` and tagged (see [Making A Change](../git-workflow/making-a-change.md)).

:::danger Production is connected to the real plant
On the production gateway the PLC is reachable on the plant network, with no SecureLink in between. The write
protections are your safety net during the deployment: keep `[default]_Config/PlcWriteLock/Locked = true` and the
OPC UA block on until commissioning says otherwise.
:::

## 0. Prepare

- [ ] A maintenance window agreed with the plant (operators lose the HMI during a restart).
- [ ] The release: git tag (e.g. `release-2026-10-30`) and the list of changed files (`git diff --stat <prev-tag>..<tag>`).
- [ ] **A `.gwbk` of production** taken just now (Platform > System > Backup & Restore), plus an export of every tag
  folder you will touch, plus a SQL backup if the schema changes. These are your [rollback](rollback.md).
- [ ] The target has the same Ignition version (8.3.7) and the modules: Perspective, Reporting, WebDev, SQL Historian,
  Logix driver, **Integration Toolkit**, **ApexCharts** (8.3 builds). Install modules **before** the project, or
  bindings and charts fail.

## 1. Gateway Settings (First Install, Or When They Changed)

These are **not** in the project export. Set them in the Gateway web UI on the target:

| Setting | Lab Value | Production |
|---|---|---|
| Device `RCP1` (Logix) | `host.docker.internal`, forwarded port, slot 0 | The PLC's plant address, port 44818, slot 0. Consider 8.3 **deployment modes** so the hostname is the only per-environment difference |
| RCP1 OPC permissions | Browse/Read only (block on) | Keep on at first; decide with the owner when operators need commands ([RCP1](../gateway/devices-rcp1.md)) |
| Tag groups | `RCP1_*`, `PAX_*` (tuned for SecureLink) | Same files; on the plant LAN `PAX_Status` can go back to 1000 ms |
| DB connection `ignition` | `sa`, lab container | Least-privilege login, production SQL Server |
| Historian `historian`, journal `MSSQL` | pruning on: historian 2 years, journal 1 year | Confirm the retention with the site |
| Audit profiles `DevAudit`, `OpsAudit` | 90 days | Per plant policy (files are in git) |
| User source, roles, IdP `default` | lab users | Real users; roles `Administrator`, `OneShot`, `ReadOnly`, `Maintenance`, `Engineering` must exist (names matter: the permission matrix columns use them) |
| Security settings | lab | Password policy, HTTPS, no `temp` IdP |
| Co-branding | BH colours | Gateway web UI > Config > Perspective > Brand Customization, with the BH logo and colours |
| API key | lab `Access` | A new key (Config > Security > API Tokens), stored outside git |
| Trial watcher | running | **Not deployed**: production is licensed |

## 2. SQL Schema

Apply new or changed `sql/*.sql` scripts to the production database with `-I` (QUOTED_IDENTIFIER ON). The gateway
creates the historian, journal and audit tables itself. Read each script first: they create objects but don't migrate
data.

## 3. Tags

**Order matters**: a UDT must exist before anything that nests or inherits it, and definitions before instances.

| Step | Import | Why |
|---|---|---|
| 1 | `_types_/_Root` | Base types (`Analog`, `Digital`, `Document`, `Expression`, `MultiState`, `String`) inherited by almost everything |
| 2 | `_types_/PLC` (incl. `Modules`, `Controllers`, `Sites`) | The PlantPAx library (`P_Motor`, `P_AIn`, `P_DIn`, `P_ValveSO`, `P_Intlk` ...), nested by device types |
| 3 | `_types_/PLC_Ref` | Read-only references to PLC objects |
| 4 | `_types_/Config` | Config types, used by Devices and Units |
| 5 | `_types_/Overview`, `_types_/Units` | |
| 6 | `_types_/Devices` | Device types: nest PLC, PLC_Ref, Config and `_Root` |
| 7 | Instances: `Boars_Head/GrovePort/**` | The devices the HMI shows |
| 8 | `_Config/**` | Settings tags. **Check memory tag values** (below) |
| 9 | `_RCP1_` | Only on a first install, from a browse of the production PLC pruned to the PlantPAx whitelist (done by the system integrator). Never import `_RCP1_` with values |

How:
- Designer Tag Browser > right-click the provider/folder > **Import Tags** (JSON), collision policy **Overwrite** for
  definitions you changed, **Merge** for folders that contain production-only tags.
- Export the same folders from the lab: Tag Browser > right-click > **Export Tags** (JSON). You can also use the
  tracked `tags.json` / `udts.json` files from git (same format).

**Memory tag values are imported too.** Before importing `_Config`, check at least:
- `_Config/PlcWriteLock/Locked` = **`true`**;
- `_Config/DemoEnterpriseNav` = `false` for a local plant gateway;
- `_Config/RolesPermissions`, `_Config/Security/*`: don't overwrite production's live matrix with lab ticks unless
  that is the change;
- `_Config/Integrations/*` (Monday.com etc.): production values, not lab ones; secrets never come from git;
- `_Config/TicketLogger/Routing` and `DryRun`: not in git; set the production routing on the Ticket Logger Settings screen (OneShot role) and keep `DryRun` false.

After importing UDT changes, a write-lock re-assert happens on the next flip or gateway start; check that
`[RCP1]`-reading members are `readOnly` (gateway log `shared.PlcWriteLock`).

## 4. Project

Two ways; pick one and use it every time.

**A. Project export / import (recommended for production).**
1. In the lab: Designer > File > Export (or the Gateway web UI > Config > Projects > Export) of `BH`, from the release
   tag's checkout.
2. On the target: Gateway web UI > Config > Projects > Import (or Designer > File > Import), overwrite `BH`.
3. The gateway keeps the project's resource metadata correct itself.

**B. Copy from git (8.3 is file-based).** Only with the system integrator: copy the release checkout's
`projects/BH/` into the target gateway's data folder (**not** `.resources/`), then restart the gateway.

Either way the project's gateway events (`plcWriteLock`, `overviewRebuild`, `pingMonday` ...) start running as soon as
it loads.

## 5. Load And Verify

- If a view still shows the old version after a browser reload, **restart the gateway** in the window.
- Run the [Go-Live Checklist](go-live-checklist.md) "after" section: RCP1 connected, values Good, no binding error
  overlays, alarms, history, forms, OOS, logins per role, write lock state.
- Login everywhere: in a private browser window, open a deep link such as `/data/perspective/client/BH/operations/plcs`; it must show only "You must log in to continue". The WebDev resources (`globe/map`, `globe/mapMarkers`, `rack3d/*`) must answer 401 without a login. See [Security](../gateway/security.md).
- Mode: read `[default]_Config/DemoEnterpriseNav` in the target's Tag Browser (`false` for a local plant gateway).

## 6. Record It

- Tag the release in git if not done; note the deployment in the release notes / PR.
- Update this wiki if the procedure changed ([Contributing](../contributing/index.md)).
