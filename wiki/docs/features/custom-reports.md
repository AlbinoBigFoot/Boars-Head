---
title: Report Builder
sidebar_position: 5
description: The custom Report Builder (guided 4-step popup) - sources, time ranges, templates, PDF / Excel / CSV export, permissions, architecture and how to add a source.
sources:
  - docs/report-builder.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py
  - gateways/standard/data/projects/BH/ignition/named-query/Reports/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/**/view.json
  - sql/report_template.sql
  - sql/report_run.sql
last_verified: 2026-10-24
---

# Report Builder

## What it does

Lets an operator or engineer build an ad-hoc report from plant data in a few clicks, preview it, export it as
**PDF, Excel or CSV**, and save the definition as a **template** (personal or shared).

## How to use it (operators)

Open it with **Generate Report** on **Alarm Status**, **Alarm Journal**, the **Out Of Service Log** or **Form History**
(the source and the page's filters, such as Area or the date range and form, are pre-selected; the button needs `Reports/Use`). It opens centred and sized to the window (from a 1366 x 768 laptop up).

1. **Data Source**: click a card, a **Quick Report** tile (straight to the preview), or a saved **Template** /
   **Recent** report on the right.
2. **Time Range**: Last Shift, Today, Yesterday, Last 7 Days, Last 30 Days or Custom. **Group Results By** (Total /
   Hour / Shift / Day / Week) follows the range and can be changed; Shifts All / A (07-15) / B (15-23) / C (23-07).
   **Skip To Preview** if the defaults are fine.
3. **Details** (optional): tick areas / devices and measures (the useful ones are pre-ticked). **Advanced Options**
   holds sections and their order, Top N, extra filters, title and notes.
4. **Preview & Export**: summary cards, chart, tables (first 25 rows); pick PDF / Excel / CSV and **Download**;
   **Save As Template** (optionally shared).

The right-hand **Your Report** panel always shows what will run; **Start Over** resets the source to its defaults.

![Step 1: data sources](/img/features/report-builder/after-1-source-1366x768-light.png)

![Step 2: custom time range](/img/features/report-builder/after-2-time-custom-1366x768-light.png)

![Step 4: preview and export](/img/features/report-builder/after-4-preview-1366x768-light.png)

### Sources

| Source | Data | Default measures | Permission row |
|---|---|---|---|
| Alarm History | alarm journal (`alarm_events`) + live status | Activations, High / Critical, Avg Time To Ack / Clear | `Reports/Alarms` |
| Zone Temperatures | historian, `<CG>/ZAT/Val` of the 19 evaporators | Avg / Lowest / Highest Zone Air Temp | `Reports/ZoneTemps` |
| Compressors | historian, `COMP n/Comp/{SucP, DisP, Amps, KW, TotalRuntime}` | Avg Suction / Discharge, Avg Amps, Run Hours In Period | `Reports/Compressors` |
| Equipment Runtime | historian run-hour / start counters of 30 devices | Run Hours In Period, Starts In Period | `Reports/Runtime` |
| Out Of Service | `dbo.oos_record` | Times Taken Out, Returned, Hours Out Of Service, Out Of Service Now | `Reports/OutOfService` |
| Operations Forms | `dbo.ops_form_submission` (own rows only without `Forms/ViewAll`) | Forms Submitted, Abnormal Shifts, Releases Logged | `Reports/Forms` |
| Production - FCM Chipotle Chicken Line | demo data from `shared.ProductionMetrics` + FCM history | LBS/HR, OEE ... | `Reports/Production`, **enterprise mode only** |

Historian rules: hourly `queryTagHistory`; hours before a tag's history row was created are skipped (the historian
would return 0); counters use the meter's rise, capped to what is physically possible. Real PLC history starts
2026-10-23 around 09:30, so longer ranges show `--` for earlier days.

## Reports in the navigation and Saved Reports (2026-10-24)

**Groveport > Operations > Reports** is a folder (visible with `Reports/Page`) with two pages:

- **Report Builder** (`/operations/reports`): the same data source cards and Quick Report tiles as step 1 of the
  popup; click one to open the guided builder.
- **Saved Reports** (`/operations/reports/saved`): three tabs, **My Reports** (templates you saved), **Shared** (every
  shared template, including yours) and **Recent Runs** (your downloads; everyone's with `Reports/ManageTemplates`).
  Search, Source and Owner filters sit above the list (Name, Source, Time Range, Owner, Last Run, Shared). Each row
  has **its own six icon buttons** at the right end (no row selection needed; a double-click on a row runs it):
  - **Run** opens the builder at the preview; **Edit** opens it at Details;
  - **Download** is one icon that opens a small **PDF / Excel / CSV** menu at the cursor; the download is made straight
    from the template and adds a row to Recent Runs;
  - **Share / Unshare** (the owner with `Reports/ShareTemplates`; a manager for others' reports); the icon changes to
    a people icon while the report is shared;
  - **Rename** opens a small centred dialog;
  - **Delete** asks for confirmation (the owner, or `Reports/ManageTemplates` for shared ones).
  Every icon has a tooltip, and a disabled icon says why (not the owner, no share permission, not your run). On Recent
  Runs the actions are Run Again and the downloads. An empty tab shows a **Create A Report** button.
- The export buttons (PDF / Excel / CSV) in the builder's Preview & Export step, and the **Generate Report** buttons
  on the Alarm, Out Of Service and Forms pages, are disabled with an explanatory tooltip when the data or the
  `Reports/Use` permission is missing.

## Where the pieces live (developers)

| What | Where |
|---|---|
| Popup | `01_Popups/Reports/ReportBuilder` + `_Assets/` (SourceCard, ChoiceTile, CheckItem, SavedRow, SummaryLine, SectionItem, PreviewSection, PreviewCard, PreviewChart) |
| Reports page | `/operations/reports` -> `00_Pages/Groveport/Operations/Reports` (nav item under Operations, gated by the `Reports/Page` row: Administrator, OneShot, Engineering) |
| Engine | `shared.Reports` (about 2,500 lines) - [reference](../scripting/reference/modules/shared-reports.md) |
| Catalog | Document tag `[default]_Config/Reports/Catalog` (version 7; a fallback copy is embedded in the engine) |
| PDF layout | Reporting resource `Reports/CustomReport` (parameter `payload` = the run result as JSON) |
| SQL | `dbo.report_template`, `dbo.report_run`; named queries `Reports/Templates/*`, `Reports/Runs/*`, `Reports/Alarms/*`, `Reports/OOS/*`, `Reports/Forms/Submissions`, `Reports/History/*` |
| Style | `report-*` classes on top of the forms' `form-*` classes |

Open it from any script: `shared.Reports.open(sourceId=None, context={}, session=None, templateId=0, page=None)`.

## How it works

```text
view.custom.def --(one expr-struct + script transform)--> shared.Reports.builderModel() -> every step's lists
edits (tiles, checkboxes, fields) --page message rptEdit--> shared.Reports.applyEdit(def, edit) -> view.custom.def
Step 4: custom.preview = previewInstances(def, viewport width)   (runs only on step 4)
Download -> shared.Reports.download(session, def + format) -> output() -> run() -> fetcher -> PDF | Excel | CSV, logRun()
```

- A **definition** is JSON with the keys `version`, `source`, `title`, `notes`, `measures`, `scope`, `time` (`preset`,
  `start`, `end`), `shifts`, `filters`, `breakdown`, `sections` (each `type`, `on`, `topN`, `n`, `orderBy`) and `format`.
  `normalize()` fills / drops keys, so old templates keep loading.
- Each source has one **fetcher** in `FETCHERS` that returns records per time bucket x scope.
- **Popup placement**: `shared.Reports.popupPosition(page)` computes a window-relative box
  `min(1440, vw - 48) x min(880, vh - 48)` centred in the window (the old fixed 1500 x 900 popup was cut off on
  laptops).
- **Permissions** are checked on the gateway at every entry point with the session username: `Reports/Use`, the
  source's own row, `ShareTemplates`, `ManageTemplates` (shared template edits). Rows are added to the matrix
  only when missing.
- **Local vs enterprise**: sources with `"deployment": "enterprise"` are hidden unless
  `[default]_Config/DemoEnterpriseNav` is true (`shared.Reports.enterpriseMode()`, cached 30 s).

## How To Change It

All steps are Designer edits; save, then test in a session as a user with `Reports/Use`.

**Saved Reports / Report Builder pages:** Project Browser > Perspective > Views > `00_Pages` > `Groveport` >
`Operations` > `ReportsSaved` and `ReportsBuilder`. The rows are drawn by the row asset `01_Popups/Reports/_Assets/SavedListRow` (the icon buttons) and the Download menu by
`01_Popups/Reports/DownloadMenu`. The Saved Reports data is one binding on `custom.model` (a script
transform calling `shared.Reports.savedModel`); the tables use `onRowClick`, one table per tab. The two navigation
items are in the Navigation view's `custom.items` (Operations > Reports folder), gated by `data.permission`
`Reports/Page`. Saved templates are in SQL `dbo.report_template`, downloads in `dbo.report_run`.

**Change the popup:** Project Browser > Perspective > Views > `01_Popups/Reports` > `ReportBuilder` (and its
`_Assets`). Edit the component properties and the `report-*` style classes. Don't give the popup a fixed size: its
size and position come from the caller's viewport.

**Change the PDF layout:** Project Browser > Reporting > `Reports/CustomReport` (the Report Designer). Its `payload`
parameter is the run result as JSON.

**Change a query:** Project Browser > Named Queries > `Reports` > the folder (`Templates`, `Runs`, `Alarms`, `OOS`,
`Forms`, `History`) > edit and **Test Query**.

**Change a source's wording, measures or presets:** Tag Browser > `[default]_Config/Reports/Catalog` (a Document tag).
Edit the JSON for the source and raise its `version` so the engine uses the tag instead of its built-in fallback.

**Add a source:**
1. Data access: add parameterised named queries (Project Browser > Named Queries > `Reports`), or for historian
   members a historian source entry in the catalog plus its device list.
2. Add a fetcher in the `shared.Reports` script module (Project Library > `shared` > `Reports`): `facts(ctx)`,
   optional `topn`, `records`, `options`, and register it in `FETCHERS`.
3. Add the source's entry to the catalog Document tag (label, description, icon, permission, measures, scope,
   sections, defaults; `deployment: 'enterprise'` if demo-only) and raise the catalog `version`.
4. Add a `Reports/<Source>` row to the permission matrix tag `[default]_Config/RolesPermissions` and tick it for the
   roles that may use the source ([Roles And Permissions](roles-permissions.md#how-to-change-it)).
5. Save, then open the Report Builder and run the new source in each export format.

## Known limitations and open questions

1. Generate Report could be added to the CG / compressor pages.
3. Units (psig, °F, A, kW) are assumed, not read from `Cfg_EU`.
4. Scheduled / emailed reports are out of scope (on demand only); `report_run` could become the log.
5. The popup keeps its size if the browser is resized while open.
6. Historian device lists are stored in the catalog; add a device to the list after it is added or historized.
7. The compressor run-hour meter (`TotalRuntime` about 44,600) is read as hours; to confirm with the PLC.
