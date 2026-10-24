---
title: The Edge Move
sidebar_position: 2
description: The plan to run the local Groveport HMI on an Ignition Edge gateway, what it needs, and the edition limits to resolve first.
sources:
  - docs/local-groveport-mode.md
  - docker-compose.yml
last_verified: 2026-10-23
---

# The Edge Move

**Plan (2026-10):** the local Groveport HMI moves to an **Ignition Edge** gateway at the plant. The **Standard**
gateway stays the enterprise / SCADA gateway (with the enterprise views). Status: **planned, not started.** Local
mode is already the default, so the project is ready on the HMI side.

## Steps

1. **Resolve the edition questions** below with Inductive Automation / the distributor. Several features may need a
   remote database through Standard, or must be hidden in local mode.
2. **Modules on Edge:** Perspective, Reporting (if licensed), WebDev (only for the globe; not needed locally),
   Logix driver, Integration Toolkit, ApexCharts.
3. **Gateway config on Edge** (not in the project): RCP1 device, tag groups, the `ignition` DB connection or remote
   alternatives, historian, alarm journal, audit profiles, users/roles/IdP.
4. **Tags:** UDT definitions first, then instances, then `_Config` (see
   [Promote To Production](promote-to-production.md#3-tags)).
5. **Mode:** on Edge, make sure `[default]_Config/DemoEnterpriseNav` exists and is `false` (Designer Tag Browser >
   `_Config`; see [Deployment Modes](deployment-modes.md#how-to-switch-modes)). If the tag is missing the nav shows
   local, but the route guard won't redirect `/` and the enterprise URLs.
6. **Co-branding:** Edge has none; the login screen stays stock. The header logos travel with the project.
7. **Verify** with the [Go-Live Checklist](go-live-checklist.md).

## Feature Dependencies On Edge

| Feature | Needs | Question For Edge |
|---|---|---|
| Operations Forms | SQL `ops_form_submission`, `ops_pid_*`; named queries `OpsForms/*`; Reporting PDFs | DB connection + Reporting? |
| Out Of Service | SQL `oos_record`, `oos_comment` | DB connection? |
| Reports | SQL `report_template`, `report_run`; `Reports/*` queries; Reporting PDF | DB + Reporting? (hidden in local mode today) |
| Saved trends | SQL `adhoc_trend_configs` | DB connection? |
| Alarm Journal page, Reports alarm source | DB alarm journal | DB journal? |
| OpsAudit / Audit Log | DB audit profile | DB audit? |
| Trending, Utility Overview charts | Tag history | Local retention vs sync to Standard |
| Login branding | Co-branding | Not on Edge |

**Not needed on Edge:** the enterprise views (globe + WebDev resource, site dashboards, Production, area KPIs) and the
`KPI/Groveport/**` / FCM KPI tags. They can stay in the project, unreachable, as they are in local mode now.

The lab already has an Edge container for rehearsal: [Edge Gateway](../infrastructure/edge-gateway.md).
