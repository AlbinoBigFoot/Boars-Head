---
title: WebDev And Reporting
sidebar_position: 8
description: The WebDev endpoints in the BH project (enterprise globe, PLC Rack 3D; all login-gated) and the Reporting module resources (Operations Forms PDFs, custom report PDF).
sources:
  - gateways/standard/data/projects/BH/com.inductiveautomation.webdev/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.reporting/**/*
last_verified: 2026-10-24
---

# WebDev And Reporting

## WebDev

**WebDev** is an Ignition module that serves HTTP endpoints from project scripts, at
`http://<gateway>/system/webdev/BH/<resource>`. Designer: **Project Browser > Web Dev**. Disk:
`gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources/`.

| Resource | What | Auth |
|---|---|---|
| `globe/map` | the enterprise globe page: one Python resource (`doGet`) whose HTML is in `shared.GlobePage`, with the six theme stylesheets inlined; shown in an iframe on `/enterprise` | logged-in BH Perspective session (`shared.WebAuth`), else 401 |
| `globe/mapMarkers` | `doGet` returns the marker GeoJSON from `[default]_Config/MapMarkerGeoJson`. `doPost` (1) relays a marker hover / click to **one** Perspective page through `shared.Globe.relay` (HMAC token, session and page id checked), (2) writes a posted GeoJSON FeatureCollection to `_Config/MapMarkerGeoJson`, (3) writes a posted `{"__nav": true, "items": [...]}` document to `[default]_Config/Navigation`. `doPut` writes the body to `_Config/MapMarkerGeoJson`. | GET: logged-in BH session, or HTTP Basic as an HMI administrator (tools). Hover / navigate relay (POST): logged-in session **and** the HMAC token. Config writes (POST GeoJSON / `__nav`, PUT): HTTP Basic with a role in `_Config/Security/AdminRoles` |
| `rack3d/view`, `rack3d/state`, `rack3d/lib` | the PLC Rack 3D page: `view` serves the HTML, `state` returns the live rack as JSON (`shared.Rack3d`, read only, only below `[default]Boars_Head/`), `lib` serves the three.js files, CSS and a demo state file. GET only. Shown in the Inline Frame on `/operations/plcs/:plc/3d` | logged-in BH Perspective session (`shared.WebAuth`), else 401 |

:::note Every BH WebDev resource needs a login (2026-10-24)
WebDev's own authentication setting is HTTP Basic only, which would pop a browser login box inside the Perspective
iframe, and text resources have no authentication setting at all. So each resource starts with the project library
check `shared.WebAuth.perspectiveUser(request)`: it accepts the request only when the browser holds a logged-in BH
Perspective session and otherwise returns 401 JSON (`shared.WebAuth.deny`) with no Basic prompt. Copy that check into
any new WebDev resource. `globe/mapMarkers` config writes (`doPost` GeoJSON / `__nav`, `doPut`) can overwrite the marker
document **and the whole nav tree tag** `[default]_Config/Navigation`, so they also need HTTP Basic plus an admin role.
The `Lightspeed-FrontEnd` project's WebDev resources use WebDev's own `require-auth` (HTTP Basic, user source
`default`; writes need Administrator). Details and how to verify: [Security Access](../features/security-access.md).
:::

The globe is part of the **enterprise demo** and is unreachable in local Groveport mode (see
[Local Vs Enterprise](../features/local-vs-enterprise.md)). The Operations Forms deliberately have **no** WebDev
endpoint: PDFs are downloaded through the Perspective session, so nothing is served unauthenticated.

:::warning Temporary endpoints
A short-lived probe resource (a name starting with `_`) is sometimes added for a read-only check and removed
afterwards. If the generated [WebDev reference](./reference/webdev.md) lists
one that is still there after the work is done, it is a leftover: delete the resource in the Designer
(Project Browser > WebDev) and save.
:::

## Reporting

The **Reporting module** turns a report resource (layout + data sources + parameters) into a PDF. Designer:
**Project Browser > Reports**. Files: `com.inductiveautomation.reporting/reports/<Folder>/<Name>/data.bin`.

| Report | Parameter | Data source | Used by |
|---|---|---|---|
| `OpsForms/DailyRoundsLog` | `recordId` | script `shared.Forms.reportData` | Daily Rounds Print / Download PDF, Form History |
| `OpsForms/NH3ShiftLog` | `recordId` | script `shared.Forms.reportData` | NH3 Shift Log PDF |
| `OpsForms/PidVerificationCycle` | `recordId` | script `shared.Forms.reportData` | Annual P&ID progress / final PDF (landscape, about 24 pages) |
| `Reports/CustomReport` | `payload` (JSON from `shared.Reports.run`) | script `shared.Reports.reportData` | Report Builder PDF export (one generic layout for every source) |

How a PDF is produced (Forms example):

```python
# shared.Forms.downloadPdf(session, kind, recordId) - permission check first, then:
pdf = system.report.executeReport(path="OpsForms/DailyRoundsLog", project="BH",
                                  parameters={"recordId": recordId}, fileType="pdf")
system.perspective.download("DailyRounds_2026-10-23_jdoe.pdf", pdf)   # browser saves / prints it
```

Things to know:

- **Report scripts have no session.** `system.report.executeReport` runs in gateway scope, so the permission check
  happens in the library **before** the report runs (`shared.Forms.pdfBytes` / `downloadPdf`,
  `shared.Reports.output`).
- **Edit reports in the Report Designer.** Project Browser > Reporting > the report > edit the layout and save. The
  saved file is Ignition's binary form, so it does not diff in git; describe a layout change in the commit message.
- **Trial watermark.** The lab gateway runs a Reporting trial, so PDFs carry "Ignition Reporting Module Trial"
  until the module is licensed.
- **Email** is not built. The intended hook is `shared.Forms.pdfBytes(session, kind, id)` (same permission check)
  plus a sink such as `system.net.sendEmail` next to `downloadPdf`.

The generated [Reporting reference](./reference/reporting.md) shows each report's parameters and data-source
script.
