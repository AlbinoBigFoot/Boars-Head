---
title: Operations Forms
sidebar_position: 3
description: Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification and Form History - the Excel workbooks as source of truth, required fields, PDFs, permissions and the Form Layout System.
sources:
  - docs/operations-forms.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py
  - gateways/standard/data/projects/BH/ignition/named-query/OpsForms/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/**/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.reporting/reports/OpsForms/**/*
  - sql/operations_forms.sql
last_verified: 2026-10-24
---

# Operations Forms

## What it does

The paper / Excel logs of the Groveport NH3 refrigeration plant, as HMI forms that save to SQL and print as PDFs
laid out like the original sheets:

| Form | Route | Replaces |
|---|---|---|
| **Daily Rounds Log** | `/operations/forms/daily-rounds` | "Daily Rounds Log" sheet of `NH3 Refrigeration Daily Log Workbook.xlsx` |
| **NH3 Shift Log** | `/operations/forms/shift-log` | "NH3 Shift Log" sheet of the same workbook |
| **Annual P&ID Verification** | `/operations/forms/pid-verification` | `Annual P&ID Verification.xlsx` (725 valves, 54 units, 6 categories) |
| **Form History** | `/operations/forms/history` | the filing cabinet: every submission and every P&ID cycle, with View and PDF |

:::info The workbooks are the source of truth
User, 2026-10-23: "We go by what is in the workbook and only in the workbook." Sections, rows, columns and
dropdown lists are copied from the workbook cells and data validations (both workbooks are in the repo root). If a
field is missing or different, compare it with the workbook first. Only the wording was cleaned up (Title Case,
"PSI" for "P.S.I.", "µS" for the conductivity unit).
:::

## How to use it (operators)

Nav: **Groveport > Operations > Forms**. You need `Forms/Use` (Maintenance and up); Read Only users do not see
the folder.

### Daily Rounds Log / NH3 Shift Log

1. **Name** defaults to your full name and **Date** to today (Daily Rounds has them in the form header; Shift Log
   also fills Operator 1). The Shift Log has **one Time In / Out field per operator**, like the workbook
   (stored as `op1_time` / `op2_time`; older records that stored separate in / out times still print).
2. Fill the sections. Daily Rounds can pre-fill about 85 readings with **Fill From Live Values** (see
   [Daily Rounds Fill From Live](./daily-rounds-fill-from-live.md)); everything stays editable.
3. **Required fields** have a red `*` and a red outline while empty; the outline clears as soon as the field is
   valid. The action bar says "N Required Fields Missing: ...".
4. **Submit**. With anything missing, Submit shows a red "Complete The Required Fields Before Submitting" summary
   and saves nothing. Otherwise a confirm dialog opens; after Submit the form is **read only** and the bar offers
   **Print / Download PDF**, **New Form**, **View History**.

Required rules: Daily Rounds = Name, Date. Shift Log = Date, Operator 1, Shift Status, Name, Sign-Off Date, plus
conditional ones (General Shift Summary when the status is "Abnormal - See Notes", Incoming Op. Reviewed? when an
incoming operator is entered, Comments when Any Open Items? = "Yes - See Comments", Time + Description on a used
alarm row, Time / Location / Description / Reportable on a used release row). The gateway checks the same rules
again (`shared.Forms.missing`).

![Daily Rounds Log, light, 1920 px](/img/features/operations-forms/daily-light-1920.png)

![NH3 Shift Log with a blocked submit](/img/features/operations-forms/shift-light-1920-blocked-submit.png)

### Annual P&ID Verification

One **shared yearly cycle**: every Maintenance+ user records valve checks on it over weeks, then someone clicks
**Complete Cycle**.

- No open cycle: **Start New Cycle** (year, drawing revision defaulting to `_Config/Forms/PidDrawingRevision`,
  performed by, reviewed by). Only one cycle can be open.
- Open cycle: header with **Save Header**, **Progress PDF**, **Complete Cycle** (confirm shows verified /
  remaining / discrepancies / verified-without-operator counts).
- Dashboard cards per category (verified / total, % complete, remaining, discrepancies, red "No Operator"); click
  a card to filter the table; filter by Unit, Show and search.
- Valve table (paged 100 rows): tick **Verified** inline (Verified By / Date default to you / today) or use the row
  editor. **Every change saves immediately** and is copied to `ops_pid_check_log`.
- A verified row with no operator is flagged red ("Missing Operator") on the page and in the PDF.
- A completed cycle is read only; its record is the PDF on Form History.

### Form History

- Tab **Daily Rounds & Shift Logs**: Form, From / To (last 30 days), User (only with `Forms/ViewAll`), table with
  a summary column and **View** / **PDF** actions (double-click = View, which opens the form read only).
- Tab **P&ID Verification Cycles**: year, status, revision, counts, completed by / at, **Open** / **PDF**.
- Without `Forms/ViewAll` (Engineering and up have it) you see only your own submissions.

![Form History > View (read only popup)](/img/features/operations-forms/history-view-readonly.png)

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Views | `00_Pages/Groveport/Operations/Forms/{DailyRounds, ShiftLog, PidVerification, History}` + `_Assets/HistoryActions` |
| Library | `shared.Forms` (including the live-value paths) - [reference](../scripting/reference/modules/shared-forms.md) |
| Named queries | `OpsForms/Submission/{Insert, List, Get, Users}`, `OpsForms/Pid/{OpenCycle, CycleById, CreateCycle, UpdateCycleHeader, CompleteCycle, Summary, Units, Rows, Check, SaveCheck, Cycles, UserChecks}` |
| SQL | `ops_form_submission`, `ops_pid_valve`, `ops_pid_cycle`, `ops_pid_check`, `ops_pid_check_log` (`sql/operations_forms.sql`) |
| PDFs | Reporting resources `OpsForms/DailyRoundsLog`, `NH3ShiftLog`, `PidVerificationCycle` (parameter `recordId`, script data source `shared.Forms.reportData`) |
| Config tags | `[default]_Config/Forms/Operators` (comma-separated names for the Name / Operator / Verified By dropdowns), `PidDrawingRevision`, `SeedVersion` |
| Permissions | `Forms/Use` (Maintenance+), `Forms/ViewAll` (Engineering+) |
| Style | `form-*` style classes + a stylesheet block (the **Form Layout System**, below) |

Every entry point takes the session and decides on the gateway: `Forms/Use` to fill / save, `Forms/ViewAll` (or
`submitted_by = <your username>` in the SQL) to see others' rows. PDFs: `system.report.executeReport(...,
fileType='pdf')` then `system.perspective.download(...)`; no WebDev endpoint.

## The Form Layout System (2026-10-23)

Every form view is assembled from the same pieces, which gives all forms the same production look. To add or change a
form section, copy the matching component from an existing form view (Designer copy / paste):

| Part | Component | Look |
|---|---|---|
| Page | page root container | centred column, max 1440 px, 16 px gutter; the **action bar is a fixed footer** |
| Header card | header container | title 22/700, subtitle, "* Required" legend, header fields |
| Section card | `form-card` container (head + body) | `form-card`, head + body; side-by-side cards wrap on narrow screens |
| Field | caption label above an input | label 12/600 over a 32 px input; `required` = static or an expression |
| Repeated rows | flex-repeater table | table-like grid; wide tables stack into row cards under 1100 px (CSS container query) |
| Banners / action bar | banner containers and the footer bar | error / ok / info banners; status line left, buttons right |

Required styling: marker `*` and outline in `var(--error)`; the input's `props.style.classes` is an expression adding
`form-input-required` while the field's own rule says it is missing.

## How To Change It

All steps are Designer edits; save, then test in a Perspective session as a Maintenance user.

- **Fields, lists and required rules:** the forms match the Excel workbooks exactly: never add or remove a field
  unless the workbook changes. Open the form view (Project Browser > Perspective > Views >
  `00_Pages/Groveport/Operations/Forms` > `DailyRounds`, `ShiftLog`, `PidVerification` or `History`), select the
  field's component and edit its binding or its `required` expression.
- **Layout and look:** edit the component properties and the `form-*` style classes (Project Browser > Perspective >
  Style Classes).
- **Live-value mapping and the save/load logic:** the `shared.Forms` script module (Project Browser > Scripting >
  Project Library > `shared` > `Forms`).
- **Queries:** Project Browser > Named Queries > `OpsForms` > edit and **Test Query**.
- **PDF layouts:** Project Browser > Reporting > `OpsForms` > `DailyRoundsLog`, `NH3ShiftLog` or
  `PidVerificationCycle` (the Report Designer).
- **Add an operator:** Tag Browser > `[default]_Config/Forms/Operators` > append `, New Name` to the value.
- **Permissions:** the `Forms/Use` and `Forms/ViewAll` rows in the matrix tag `[default]_Config/RolesPermissions`
  ([Roles And Permissions](roles-permissions.md#how-to-change-it)).

## Known limitations and parked items

- **No email** yet (print / PDF only); the hook is `shared.Forms.pdfBytes` + a mail sink next to `downloadPdf`.
- PDFs carry the "Ignition Reporting Module Trial" watermark until Reporting is licensed.
- The Annual P&ID view has not been moved to the Form Layout System yet (mapping planned in `docs/operations-forms.md`).
- Not re-verified after the 2026-10-23 one-field Time In / Out change: a fresh Shift Log submit, History > View of
  record 2 and its PDF (dropdowns did not open in the last test).
- **Generate Report** buttons on Form History (and the Out Of Service Log) open the Report Builder with the Operations Forms
  source and the visible From / To dates, forms and user already selected.
- Test submissions ids 1-3 ("TEST") are in the lab database.
