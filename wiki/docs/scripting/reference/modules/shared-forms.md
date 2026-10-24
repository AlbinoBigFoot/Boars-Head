---
title: "shared.Forms"
sidebar_label: "shared.Forms"
description: "Script module shared.Forms: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`  
**Lines:** 776. **Functions:** 51. **Called as:** `shared.Forms.<function>(...)`

## What the source says

```text
Operations Forms (Operations > Forms): Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification, Form History.

Design: docs/operations-forms.md.

Every entry point takes the Perspective session and decides on the gateway: Forms/Use to fill / save anything,
Forms/ViewAll to see other users' submissions (otherwise only rows submitted_by = the session username). The
username always comes from session.props.auth.user (never from a view parameter). Named queries: OpsForms/*.
PDF output: Reporting module resources OpsForms/* (script data source -> reportData below); email can be added as
another sink next to downloadPdf (pdfBytes returns the bytes after the same permission check).
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.dataset`, `system.date`, `system.db`, `system.perspective`, `system.report`, `system.tag`, `system.user`, `system.util` |
| Logger names | `shared.Forms` |
| Calls modules | [shared.Pax](./shared-pax.md), [shared.Security](./shared-security.md) |

<details>
<summary>Module constants (11)</summary>

| Name | Value |
|---|---|
| `LOG` | `system.util.getLogger('shared.Forms')` |
| `PROJECT` | `'BH'` |
| `NQ` | `'OpsForms/'` |
| `CFG` | `'[default]_Config/Forms/'` |
| `USER_SOURCE` | `'default'` |
| `SCHEMA` | `_json.loads('{"DailyRounds": {"bools": ["prv_rd_visuals",...` |
| `PID_CATEGORIES` | `['Compressors', 'Recirculators & Pumps', 'Receivers & Ves...` |
| `PID_REPORT` | `'OpsForms/PidVerificationCycle'` |
| `CYCLE_BLANK` | `{'id': 0, 'allowed': True, 'cycle_year': '', 'drawing_rev...` |
| `SEL_BLANK` | `{'valve_pk': 0, 'pid': '', 'unit_id': '', 'unit_desc': ''...` |
| `FLAG_STYLE` | `{'backgroundColor': 'var(--alarm-critical)', 'color': '#f...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`username`](#username) | ------------------------------------------------------------------------------------------------ session / access | 0 |
| [`allowed`](#allowed) | Forms/&lt;action&gt; for the session (Roles & Permissions matrix via shared.Security). | 2 |
| [`displayName`](#displayname) | 'First Last' of the session user (internal user source), else the username. | 1 |
| [`context`](#context) | | 0 |
| [`operators`](#operators) | Operator names from [default]\_Config/Forms/Operators (comma-separated) plus the session user's own name. | 0 |
| [`operatorOptions`](#operatoroptions) | | 3 |
| [`_nq`](#_nq) (internal) | ------------------------------------------------------------------------------------------------ helpers | 0 |
| [`_py`](#_py) (internal) | Perspective / Java structures -&gt; plain Python (dates become epoch millis). | 0 |
| [`_rows`](#_rows) (internal) | | 0 |
| [`_str`](#_str) (internal) | | 0 |
| [`_blank`](#_blank) (internal) | | 0 |
| [`_dateOf`](#_dateof) (internal) | Date / epoch millis / 'yyyy-MM-dd' / java Date.toString() text -&gt; java Date (None when empty / unparseable). | 0 |
| [`_dateStr`](#_datestr) (internal) | Any date form -&gt; 'yyyy-MM-dd' ('' when empty). | 0 |
| [`_toDate`](#_todate) (internal) | | 0 |
| [`_get`](#_get) (internal) | Item of a dict / Perspective object wrapper (None when missing). | 0 |
| [`_today`](#_today) (internal) | | 0 |
| [`_num`](#_num) (internal) | | 0 |
| [`computed`](#computed) | Averages (Excel AVERAGE over the non-blank numeric cells), '' when none. | 0 |
| [`normalize`](#normalize) | View data -&gt; stored JSON shape: every schema key, strings trimmed, dates 'yyyy-MM-dd', bools True/False. | 0 |
| [`missing`](#missing) | Labels of required fields that are blank (same rules as the page's Required line). | 0 |
| [`blankData`](#blankdata) | ------------------------------------------------------------------------------------------------ form data | 0 |
| [`newData`](#newdata) | Defaults for a new form: Name (and Operator 1) = the logged-in user, dates = today (Date values). | 6 |
| [`forView`](#forview) | Stored JSON -&gt; view.custom.f (date keys back to Date objects for the date inputs). | 0 |
| [`merged`](#merged) | view.custom.f with updates applied (date keys stay Date values). | 1 |
| [`_fmt`](#_fmt) (internal) | | 0 |
| [`liveValues`](#livevalues) | Daily Rounds 'Fill From Live Values': \{field: text\} for every field mapped to a tag (one batched read). | 1 |
| [`_summary`](#_summary) (internal) | History table summary + flags. | 0 |
| [`submit`](#submit) | Validate on the gateway and insert. Returns \{ok, id, message, missing\}. | 2 |
| [`getSubmission`](#getsubmission) | One submission (dict with data) when the session may see it (own, or Forms/ViewAll); else None. | 0 |
| [`loadForView`](#loadforview) | \{formType, data (view shape), meta\} for a read-only render, or None. | 2 |
| [`history`](#history) | Submissions for the History table. Without Forms/ViewAll only the session user's own rows (enforced in SQL). | 1 |
| [`historyUsers`](#historyusers) | Submitter options for the History user filter (Forms/ViewAll only). | 1 |
| [`_reportFor`](#_reportfor) (internal) | ------------------------------------------------------------------------------------------------ PDF (Reporting) | 0 |
| [`pdfBytes`](#pdfbytes) | Report PDF bytes after the same visibility check as the History page (None when refused / failed). | 3 |
| [`downloadPdf`](#downloadpdf) | Print / Download PDF: browser download of the Reporting PDF. Returns a status message. | 7 |
| [`reportData`](#reportdata) | Script data source of the OpsForms reports (gateway, no session - pdfBytes checked access first). | 3 |
| [`_pidCycle`](#_pidcycle) (internal) | ------------------------------------------------------------------------------------------------ P&ID verification | 0 |
| [`pidBlankSel`](#pidblanksel) | | 1 |
| [`pidOpenCycle`](#pidopencycle) | The open cycle, always the full CYCLE\_BLANK shape (id 0 = none open). | 1 |
| [`pidStartCycle`](#pidstartcycle) | | 1 |
| [`pidSaveHeader`](#pidsaveheader) | | 1 |
| [`pidComplete`](#pidcomplete) | | 1 |
| [`pidSummary`](#pidsummary) | Dashboard (per category + overall) and the unit options of the selected category. | 1 |
| [`pidRows`](#pidrows) | Valve table rows for the cycle; Verified By / Date cells flagged red when verified without an operator. | 1 |
| [`pidSaveCheck`](#pidsavecheck) | Save one valve check immediately (upsert + audit log row). quick=True (table checkbox): Verified By defaults | 2 |
| [`pidCheck`](#pidcheck) | Selected valve for the editor panel: master data + this cycle's check (verified\_date as a Date). | 4 |
| [`pidSetField`](#pidsetfield) | Inline table edit (Verified checkbox or Notes): re-reads the stored check, changes that one field, saves. | 1 |
| [`pidDefaultRevision`](#piddefaultrevision) | | 1 |
| [`pidCycles`](#pidcycles) | History: open cycles for every Forms/Use user; completed cycles for Forms/ViewAll, or for cycles the user | 1 |
| [`pidCanView`](#pidcanview) | | 0 |
| [`_pidReportData`](#_pidreportdata) (internal) | | 0 |

### username {#username}

```python
def username(session)
```
Line 27 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
------------------------------------------------------------------------------------------------ session / access
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `allowed`, `context`, `displayName`, `getSubmission`, `history`, `pidCanView`, `pidComplete`, `pidCycles`, `pidSaveCheck`, `pidStartCycle`, `submit`

### allowed {#allowed}

```python
def allowed(session, action='Use')
```
Line 34 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Forms/<action> for the session (Roles & Permissions matrix via shared.Security).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root event system.onStartup` |

Used inside the module by: `context`, `getSubmission`, `historyUsers`, `history`, `liveValues`, `pidCanView`, `pidCheck`, `pidComplete`, `pidCycles`, `pidOpenCycle`, `pidRows`, `pidSaveCheck`, `pidSaveHeader`, `pidStartCycle`, `pidSummary`, `submit`

### displayName {#displayname}

```python
def displayName(session)
```
Line 43 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
'First Last' of the session user (internal user source), else the username.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root event system.onStartup` |

Used inside the module by: `context`, `newData`, `operators`, `pidSaveCheck`, `submit`

### context {#context}

```python
def context(session)
```
Line 57 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### operators {#operators}

```python
def operators(session=None)
```
Line 62 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Operator names from [default]_Config/Forms/Operators (comma-separated) plus the session user's own name.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `operatorOptions`

### operatorOptions {#operatoroptions}

```python
def operatorOptions(session)
```
Line 77 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root event system.onStartup` |

### \_nq {#_nq}

```python
def _nq(path, params, getKey=False)
```
Line 82 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
------------------------------------------------------------------------------------------------ helpers
```

Used inside the module by: `_pidCycle`, `_pidReportData`, `getSubmission`, `historyUsers`, `history`, `pidCanView`, `pidCheck`, `pidComplete`, `pidCycles`, `pidOpenCycle`, `pidRows`, `pidSaveCheck`, `pidSaveHeader`, `pidStartCycle`, `pidSummary`, `reportData`, `submit`

### \_py {#_py}

```python
def _py(obj)
```
Line 86 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Perspective / Java structures -> plain Python (dates become epoch millis).
```

Used inside the module by: `merged`, `normalize`

### \_rows {#_rows}

```python
def _rows(ds)
```
Line 96 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `_pidCycle`, `_pidReportData`, `getSubmission`, `historyUsers`, `history`, `pidCanView`, `pidCheck`, `pidCycles`, `pidOpenCycle`, `pidRows`, `pidStartCycle`, `pidSummary`, `reportData`

### \_str {#_str}

```python
def _str(v)
```
Line 107 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `_pidReportData`, `missing`, `normalize`, `pidSaveCheck`, `pidSaveHeader`, `pidSetField`, `pidStartCycle`, `reportData`

### \_blank {#_blank}

```python
def _blank(v)
```
Line 115 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `_pidReportData`, `missing`, `pidRows`

### \_dateOf {#_dateof}

```python
def _dateOf(v)
```
Line 119 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Date / epoch millis / 'yyyy-MM-dd' / java Date.toString() text -> java Date (None when empty / unparseable).
```

Used inside the module by: `_dateStr`, `_toDate`, `merged`

### \_dateStr {#_datestr}

```python
def _dateStr(v)
```
Line 136 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Any date form -> 'yyyy-MM-dd' ('' when empty).
```

Used inside the module by: `_pidReportData`, `history`, `normalize`, `pdfBytes`, `pidCheck`, `pidRows`, `pidSaveCheck`

### \_toDate {#_todate}

```python
def _toDate(s)
```
Line 142 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `forView`, `pidCheck`

### \_get {#_get}

```python
def _get(obj, k)
```
Line 146 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Item of a dict / Perspective object wrapper (None when missing).
```

Used inside the module by: `merged`, `normalize`

### \_today {#_today}

```python
def _today()
```
Line 157 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `pidSaveCheck`, `submit`

### \_num {#_num}

```python
def _num(v)
```
Line 161 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `computed`

### computed {#computed}

```python
def computed(formType, data)
```
Line 169 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Averages (Excel AVERAGE over the non-blank numeric cells), '' when none.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `normalize`, `reportData`

### normalize {#normalize}

```python
def normalize(formType, raw)
```
Line 178 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
View data -> stored JSON shape: every schema key, strings trimmed, dates 'yyyy-MM-dd', bools True/False.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `submit`

### missing {#missing}

```python
def missing(formType, data)
```
Line 196 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Labels of required fields that are blank (same rules as the page's Required line).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `submit`

### blankData {#blankdata}

```python
def blankData(formType)
```
Line 213 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
------------------------------------------------------------------------------------------------ form data
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `forView`, `newData`

### newData {#newdata}

```python
def newData(session, formType)
```
Line 221 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Defaults for a new form: Name (and Operator 1) = the logged-in user, dates = today (Date values).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root message handler opsFormsClearDailyRounds` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/New event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root message handler opsFormsClearShiftLog` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root/Footer/Bar/ActionBar/New event component.onActionPerformed` |

### forView {#forview}

```python
def forView(formType, data)
```
Line 234 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Stored JSON -> view.custom.f (date keys back to Date objects for the date inputs).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `loadForView`

### merged {#merged}

```python
def merged(formType, current, updates)
```
Line 244 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
view.custom.f with updates applied (date keys stay Date values).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Fill event component.onActionPerformed` |

### \_fmt {#_fmt}

```python
def _fmt(v, fmt)
```
Line 254 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `liveValues`

### liveValues {#livevalues}

```python
def liveValues(session)
```
Line 269 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Daily Rounds 'Fill From Live Values': {field: text} for every field mapped to a tag (one batched read).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Fill event component.onActionPerformed` |

### \_summary {#_summary}

```python
def _summary(formType, data)
```
Line 320 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
History table summary + flags.
```

Used inside the module by: `submit`

### submit {#submit}

```python
def submit(session, formType, raw)
```
Line 353 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Validate on the gateway and insert. Returns {ok, id, message, missing}.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root message handler opsFormsSubmitDailyRounds` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root message handler opsFormsSubmitShiftLog` |

### getSubmission {#getsubmission}

```python
def getSubmission(session, submissionId)
```
Line 380 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
One submission (dict with data) when the session may see it (own, or Forms/ViewAll); else None.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `loadForView`, `pdfBytes`

### loadForView {#loadforview}

```python
def loadForView(session, submissionId)
```
Line 401 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
{formType, data (view shape), meta} for a read-only render, or None.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root event system.onStartup` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root event system.onStartup` |

### history {#history}

```python
def history(session, formType='', start=None, end=None, userFilter='')
```
Line 411 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Submissions for the History table. Without Forms/ViewAll only the session user's own rows (enforced in SQL).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/History` | view | `root/Tabs/Forms/Table binding props.data` |

### historyUsers {#historyusers}

```python
def historyUsers(session)
```
Line 436 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Submitter options for the History user filter (Forms/ViewAll only).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/History` | view | `root/Tabs/Forms/Filters/User/V binding props.options` |

### \_reportFor {#_reportfor}

```python
def _reportFor(kind)
```
Line 449 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
------------------------------------------------------------------------------------------------ PDF (Reporting)
```

Used inside the module by: `pdfBytes`

### pdfBytes {#pdfbytes}

```python
def pdfBytes(session, kind, recordId)
```
Line 455 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Report PDF bytes after the same visibility check as the History page (None when refused / failed).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `OpsForms/DailyRoundsLog` | report | `data source` |
| `OpsForms/NH3ShiftLog` | report | `data source` |
| `OpsForms/PidVerificationCycle` | report | `data source` |

Used inside the module by: `downloadPdf`

### downloadPdf {#downloadpdf}

```python
def downloadPdf(session, kind, recordId)
```
Line 480 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Print / Download PDF: browser download of the Reporting PDF. Returns a status message.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Pdf event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Print event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Completed/Pdf event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Cycle/Row/Btns/Pdf event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root/Footer/Bar/ActionBar/Pdf event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root/Footer/Bar/ActionBar/Print event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions` | view | `root/Pdf event component.onActionPerformed` |

### reportData {#reportdata}

```python
def reportData(kind, recordId, data)
```
Line 489 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Script data source of the OpsForms reports (gateway, no session - pdfBytes checked access first).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `OpsForms/DailyRoundsLog` | report | `data source` |
| `OpsForms/NH3ShiftLog` | report | `data source` |
| `OpsForms/PidVerificationCycle` | report | `data source` |

### \_pidCycle {#_pidcycle}

```python
def _pidCycle(cycleId)
```
Line 527 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
------------------------------------------------------------------------------------------------ P&ID verification
```

Used inside the module by: `_pidReportData`, `pdfBytes`, `pidCanView`, `pidSaveCheck`

### pidBlankSel {#pidblanksel}

```python
def pidBlankSel()
```
Line 539 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root message handler opsFormsPidComplete` |

Used inside the module by: `pidCheck`

### pidOpenCycle {#pidopencycle}

```python
def pidOpenCycle(session)
```
Line 543 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
The open cycle, always the full CYCLE_BLANK shape (id 0 = none open).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `binding custom.cycle` |

### pidStartCycle {#pidstartcycle}

```python
def pidStartCycle(session, year, revision, performedBy, reviewedBy)
```
Line 559 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/NoCycle/Row/Btn/Start event component.onActionPerformed` |

### pidSaveHeader {#pidsaveheader}

```python
def pidSaveHeader(session, cycleId, revision, performedBy, reviewedBy)
```
Line 574 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Cycle/Row/Btns/SaveHdr event component.onActionPerformed` |

### pidComplete {#pidcomplete}

```python
def pidComplete(session, cycleId)
```
Line 582 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root message handler opsFormsPidComplete` |

### pidSummary {#pidsummary}

```python
def pidSummary(session, cycleId, category='')
```
Line 591 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Dashboard (per category + overall) and the unit options of the selected category.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `binding custom.summary` |

### pidRows {#pidrows}

```python
def pidRows(session, cycleId, category='', unit='', search='', show='All')
```
Line 622 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Valve table rows for the cycle; Verified By / Date cells flagged red when verified without an operator.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Table binding props.data` |

### pidSaveCheck {#pidsavecheck}

```python
def pidSaveCheck(session, cycleId, valvePk, verified, verifiedBy, verifiedDate, notes, quick=False)
```
Line 646 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Save one valve check immediately (upsert + audit log row). quick=True (table checkbox): Verified By defaults
to the session user's name and Date to today when blank; unticking clears neither (the record stays visible).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Editor/Valve/Btns/Quick event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Editor/Valve/Btns/Save event component.onActionPerformed` |

Used inside the module by: `pidSetField`

### pidCheck {#pidcheck}

```python
def pidCheck(session, cycleId, valvePk)
```
Line 666 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Selected valve for the editor panel: master data + this cycle's check (verified_date as a Date).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Editor/Valve/Btns/Quick event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Editor/Valve/Btns/Save event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Table event component.onEditCellCommit` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Table event component.onSelectionChange` |

Used inside the module by: `pidSetField`

### pidSetField {#pidsetfield}

```python
def pidSetField(session, cycleId, valvePk, column, value)
```
Line 683 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
Inline table edit (Verified checkbox or Notes): re-reads the stored check, changes that one field, saves.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Main/Table event component.onEditCellCommit` |

### pidDefaultRevision {#piddefaultrevision}

```python
def pidDefaultRevision()
```
Line 698 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root event system.onStartup` |

### pidCycles {#pidcycles}

```python
def pidCycles(session)
```
Line 705 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

```text
History: open cycles for every Forms/Use user; completed cycles for Forms/ViewAll, or for cycles the user
recorded checks in (enforced in SQL).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/Forms/History` | view | `root/Tabs/Cycles/Table binding props.data` |

### pidCanView {#pidcanview}

```python
def pidCanView(session, cycleId)
```
Line 723 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `pdfBytes`

### \_pidReportData {#_pidreportdata}

```python
def _pidReportData(cycleId, data)
```
Line 735 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Forms/code.py`.

_No docstring._

Used inside the module by: `reportData`
