---
title: Go-Live Checklist
sidebar_position: 5
description: The checklist to tick before, during and after a production cut-over of the BH HMI.
sources:
  - docs/plc-write-lock.md
  - docs/local-groveport-mode.md
  - gateways/standard/data/config/resources/core/ignition/security-properties/config.json
last_verified: 2026-10-23
---

# Go-Live Checklist

Copy this list into the release PR or ticket and tick it as you go.

## Before

- [ ] Change merged to `main`, reviewed, tagged; release notes list every view/tag/setting changed.
- [ ] Wiki updated for the change (`check_docs.py` clean, `npm run build` passes).
- [ ] Maintenance window agreed with the plant; operators informed.
- [ ] Production `.gwbk` downloaded; tag folder exports; SQL backup if the schema changes.
- [ ] Modules present on the target (Perspective, Reporting, WebDev, SQL Historian, Logix, Integration Toolkit,
  ApexCharts), license active (no trial watcher).
- [ ] Gateway settings prepared ([Promote To Production](promote-to-production.md#1-gateway-settings-first-install-or-when-they-changed)):
  RCP1 plant address, DB login, users and roles, co-branding, HTTPS, pruning.
- [ ] `_Config` values reviewed before import: `PlcWriteLock/Locked = true`, `DemoEnterpriseNav` as intended,
  permission matrix not overwritten by accident.
- [ ] Rollback trigger and owner agreed ([Rollback](rollback.md)).

## During

- [ ] SQL scripts applied (`-I`).
- [ ] Tags imported in order: `_Root` → `PLC` → `PLC_Ref` → `Config` → `Overview`/`Units` → `Devices` → instances → `_Config`.
- [ ] Project imported (Gateway web UI project import, or Designer File > Import).
- [ ] Gateway restarted if views stay stale.

## After

Gateway:
- [ ] Platform > Overview: no faulted modules; Connections > Devices: **RCP1 Connected**.
- [ ] Connections > Databases: `ignition` **Valid**; Services > Historians and Alarming > Journals running.
- [ ] Diagnostics > Logs: no new errors from `shared.*`, Perspective or the driver.
- [ ] `shared.PlcWriteLock` log line shows the expected lock state; the OPC UA write block is in the state the system integrator confirmed.

HMI (one user per role: ReadOnly, Maintenance, Engineering, Administrator):
- [ ] Login works with the co-branded screen; landing page is the Utility Overview (local mode).
- [ ] Nav tree complete for the mode; Admin items only for the roles that should see them.
- [ ] Utility Overview: CG tiles show values and states, charts render, no red binding overlays.
- [ ] Machine Room, Condensers and one CG page: values Good, faceplates open with values within seconds.
- [ ] Alarm Status shows active alarms; the header bell count matches; ack works for Maintenance and up only.
- [ ] Trending: add a tag, see history; a saved trend loads.
- [ ] Forms: open the Daily Rounds Log (Maintenance+), the PDF renders.
- [ ] Out Of Service log page loads.
- [ ] Audit Log (Engineering+) shows entries.
- [ ] Light and dark themes, 1920 and 1366 px widths.
- [ ] **No write test against the PLC** unless the commissioning plan says so, with the owner present.

Close-out:
- [ ] Post-deployment `.gwbk` taken.
- [ ] Release tagged and noted; note added to the release record.
