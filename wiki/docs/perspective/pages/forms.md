---
title: Operations Forms
sidebar_position: 11
description: The Operations Forms pages - Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification and Form History - and the Form Layout System they are built with.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/**/view.json"
  - "docs/operations-forms.md"
last_verified: 2026-10-24
---

# Operations Forms

Paper forms from the plant's Excel workbooks, rebuilt as HMI pages that save to SQL and print to PDF. This guide
covers the views and the layout system. The data model, permissions and PDFs are on
[Features](../../features/index.md) and in `docs/operations-forms.md`.

![Daily Rounds Log](/img/perspective/forms-daily-rounds.png)

| Nav (Groveport > Operations > Forms) | Route | View |
|---|---|---|
| Daily Rounds Log | `/operations/forms/daily-rounds` | [`00_Pages/Groveport/Operations/Forms/DailyRounds`](../reference/views/00-pages/groveport/operations/forms/dailyrounds.md) |
| NH3 Shift Log | `/operations/forms/shift-log` | [`.../Forms/ShiftLog`](../reference/views/00-pages/groveport/operations/forms/shiftlog.md) |
| Annual P&ID Verification | `/operations/forms/pid-verification` | [`.../Forms/PidVerification`](../reference/views/00-pages/groveport/operations/forms/pidverification.md) |
| Form History | `/operations/forms/history` | [`.../Forms/History`](../reference/views/00-pages/groveport/operations/forms/history.md) (+ `_Assets/HistoryActions` cell) |

| | |
|---|---|
| PDF reports | Project Browser > Reporting > `OpsForms/*` |
| Scripts | `shared.Forms` (every read and write; enforces `Forms/Use` and `Forms/ViewAll` with the session username) |
| SQL | `ops_form_submission`, `ops_pid_*` through the named queries `OpsForms/*` |
| PDF | Reporting resources `OpsForms/DailyRoundsLog`, `NH3ShiftLog`, `PidVerificationCycle` |
| Operators | `[default]_Config/Forms/Operators` (dropdown list) |
| Permission | Nav leaves carry `data.permission: Forms/Use`, so the Forms folder disappears for Read Only users |

## Daily Rounds Log And NH3 Shift Log

- Sections, rows, columns and dropdown lists copy the Excel sheets. Name defaults to the logged-in user, dates to
  today.
- **Fill From Live Values** (Daily Rounds) reads current tag values into the fields (`shared.Forms.liveValues`);
  every field stays editable, because rounds are field-verified readings.
- **Required fields** get a red `*` and a red outline while empty; Submit with anything missing shows a red summary
  instead of the confirm. The gateway re-checks the same rules (`shared.Forms.missing`).
- **Submit** opens a confirm, inserts the record, then offers Print / Download PDF, New Form and View History. A
  submitted form is read only.
- On startup the view loads the operator list and, for History > View (`params.readOnly`, `params.submissionId`),
  the stored submission:

```python
# DailyRounds root onStartup (first lines)
v = self.view
v.custom.operators = shared.Forms.operatorOptions(self.session)
if v.params.readOnly or v.params.submissionId:
    rec = shared.Forms.loadForView(self.session, v.params.submissionId)
```

## Annual P&ID Verification

![Annual P&ID Verification](/img/perspective/forms-pid-verification.png)

One shared yearly cycle: every Maintenance+ user records valve checks on it over weeks, then **Complete Cycle**.
Dashboard cards per category (verified / total, % complete, remaining, discrepancies, verified without operator)
filter the paged valve table (725 valves); each check saves immediately with an audit row. A completed cycle is
read only; its record is the PDF on Form History.

## Form History

![Form History](/img/perspective/forms-history.png)

Lists submissions and P&ID cycles (`shared.Forms.history`, `historyUsers`, `pidCycles`). Users see their own rows;
`Forms/ViewAll` sees everyone's (enforced in the SQL). **View** opens the form read only as a popup; the PDF
button prints it. **Generate Report** opens the Report Builder on the Operations Forms source with the page's forms and date range (needs `Reports/Use`).

## The Form Layout System (2026-10-23)

Daily Rounds and Shift Log are composed from the same reusable pieces, designed first in Figma. The look comes from
the `form-*` style classes:

| Part | Classes |
|---|---|
| Page column (max 1440 px, fixed action bar) | `form-page`, root `bg-page` |
| Cards | `form-card`, `form-section-head`, `form-section-title`, `form-title`, `form-subtitle` |
| Fields | `form-label`, `form-input`, `form-input-required` (red outline), `form-required-marker`, `form-hint`, `form-note`, `form-check`, `form-calc` |
| Tables of readings | `form-th`, `form-row-label` |
| Banners | `form-banner`, `form-banner-error`, `form-banner-ok` |
| Action bar | `form-status`, `form-status-error`, `form-btn`, `form-btn-primary` |

The required outline is an expression on the input's `props.style.classes` that adds `form-input-required` while
the field is empty. See [Utilities And Design Classes](../styling/utilities-and-design-classes.md) and the
[style class catalog](../reference/style-classes.md) for each class's CSS. The P&ID page is still on the older
layout; applying the system to it is listed as a later item in `docs/operations-forms.md`. How to change the forms:
[Operations Forms](../../features/operations-forms.md#how-to-change-it).
