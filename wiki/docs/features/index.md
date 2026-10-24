---
title: Features
slug: /features
sidebar_position: 1
description: End-to-end guides to every BH HMI feature, for operators and developers - what it does, how to use it, where the pieces live, how to change it and what is still open.
sources:
  - docs/*.md
last_verified: 2026-10-24
---

# Features

One guide per feature. Each guide has the same parts:

1. **What it does**, in plain words.
2. **How to use it** (operators): where to click, what each field means, screenshots.
3. **Where the pieces live** (developers): views, scripts, tags, SQL, named queries.
4. **How it works** under the hood.
5. **How to change it** step by step in the Designer or the Gateway web UI. See also
   [Common Tasks](../getting-started/common-tasks.md).
6. **Known limitations and parked items**.

| Feature | Where in the HMI | Who can use it |
|---|---|---|
| [Out Of Service](./out-of-service.md) | right-click a device; Operations > Out Of Service Log | Maintenance and up |
| [Operations Forms](./operations-forms.md) | Operations > Forms (Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification, Form History) | Maintenance and up |
| [Daily Rounds Fill From Live](./daily-rounds-fill-from-live.md) | Daily Rounds Log > Fill From Live Values | Maintenance and up |
| [Report Builder And Saved Reports](./custom-reports.md) | Operations > Reports (Report Builder + Saved Reports); Generate Report buttons on Alarm Status / Journal, Out Of Service Log, Form History | roles with Reports/Use (page: Reports/Page) |
| [Trending And Add To Trend](./trending.md) | Operations > Trending, Saved Trends, right-click any value | everyone |
| [PLC Rack / IO](./plc-rack-io.md) | Operations > PLCs (PLC Overview) > RCP1 | everyone (read only) |
| [PLC Write Lock](./plc-write-lock.md) | Designer Tag Browser `_Config/PlcWriteLock/Locked` | the project owner only |
| [Alarms](./alarms.md) | Operations > Alarm Status, Alarm Journal; header bell; faceplate Alarms tabs | everyone; ack / shelve Maintenance and up |
| [Roles & Permissions / User Management](./roles-permissions.md) | Admin > User Management, Roles & Permissions | Administrator |
| [Audit Log](./audit-log.md) | Admin > Audit Log | Engineering and up |
| [Branding](./branding.md) | header logos, login screens | - |
| [Local Vs Enterprise Mode](./local-vs-enterprise.md) | the whole nav | administrators (one tag) |
| [Machine Room Level Switches](./machine-room-level-switches.md) | Machine Room page tiles | everyone |
| [Security Access](./security-access.md) | every page and WebDev resource | login required for everyone |
| [PLC Rack 3D View](./plc-rack-3d.md) | PLCs > RCP1 > 3D View | everyone (read only) |
| [Safety Relay 3D View](./safety-relay-3d.md) | Safety Relay page > 3D View | everyone (read only) |
| [Comm Loss And Value Quality](./comm-loss-quality.md) | every page and faceplate | everyone |
| [Ticket Logger](./ticket-logger.md) | right-click a value > Ticket Logger | everyone; Settings OneShot only |
| [Defrost Enums](./defrost-enums.md) | evaporator faceplate / CG panel modes | Maintenance and up to change |

The source documents these guides are built from live in the repo's `docs/` folder (for example
`docs/out-of-service.md`); they carry more verification detail and history.
