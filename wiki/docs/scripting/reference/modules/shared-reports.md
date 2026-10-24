---
title: "shared.Reports"
sidebar_label: "shared.Reports"
description: "Script module shared.Reports: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`  
**Lines:** 2730. **Functions:** 137. **Called as:** `shared.Reports.<function>(...)`

## What the source says

```text
Report builder engine (Production KPIs, Alarms, ... any source in the catalog).



Catalog   [default]_Config/Reports/Catalog (Document tag;
missing / older). Sources declare measures, scope tree, breakdowns, filters, sections, Top N lists.
Engine    run(session, definition) -> {ok, meta, sections:[{type, title, note, cards | charts | columns+rows}]}.
Permission (Reports/Use + the source's own row) is checked here on the gateway; the username always comes
from session.props.auth.user. Time buckets (hour / shift / day / week / total) and the shift schedule
(A 07-15, B 15-23, C 23-07) are built here; each source has one fetcher (FETCHERS) that returns per bucket x
scope records keyed by the catalog 'field' names.

day / shift / unit, replaced per time bucket by SQL historian data (FCM tag history) where the history
covers the bucket (each value keeps its source internally; the outputs carry no data-source labels -
user 2026-10-13: "get rid of all the demo data stuff").
alarms: alarm journal aggregates (named queries Reports/Alarms/*) + system.alarm.queryStatus for "now".
Output    PDF = Reporting resource Reports/CustomReport (one generic layout; payload JSON -> reportData below),
Excel = system.dataset.toExcel (one sheet per section), CSV = one file, or a zip of one per section.
Templates dbo.report_template via Reports/Templates/* (personal / shared; owner or Reports/ManageTemplates edits).
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.alarm`, `system.dataset`, `system.date`, `system.db`, `system.perspective`, `system.report`, `system.tag`, `system.user`, `system.util` |
| Logger names | `shared.Reports` |
| Calls modules | [shared.Alerts](./shared-alerts.md), [shared.ProductionMetrics](./shared-productionmetrics.md), [shared.Security](./shared-security.md) |

<details>
<summary>Module constants (37)</summary>

| Name | Value |
|---|---|
| `LOG` | `system.util.getLogger('shared.Reports')` |
| `PROJECT` | `'BH'` |
| `NQ` | `'Reports/'` |
| `CATALOG_TAG` | `'[default]_Config/Reports/Catalog'` |
| `DEPLOY_TAG` | `'[default]_Config/DemoEnterpriseNav'` |
| `POPUP_ID` | `'reportBuilder'` |
| `POPUP_VIEW` | `'01_Popups/Reports/ReportBuilder'` |
| `REPORT_PATH` | `'Reports/CustomReport'` |
| `FALLBACK` | `_json.loads('{"presets": [{"def": {"breakdown": "day", "m...` |
| `SHIFT_START` | `{'A': 7, 'B': 15, 'C': 23}` |
| `PDF_COLS` | `8` |
| `PDF_MAX_ROWS` | `1500` |
| `PREVIEW_ROWS` | `25` |
| `MAX_PENS` | `6` |
| `HOUR` | `3600000` |
| `DAY` | `86400000` |
| `RECORDS_DEFAULT` | `200` |
| `RECORDS_MAX` | `2000` |
| `TIME_PRESETS` | `[('lastShift', 'Last Shift'), ('today', 'Today'), ('yeste...` |
| `TIME_IDS` | `[k for k, v in TIME_PRESETS]` |
| `COUNT_UNITS` | `('', 'count', 'alarms', 'events', 'devices', 'forms', 'sh...` |
| `HIST_MODES` | `{'avg': ['Average'], 'min': ['Minimum'], 'max': ['Maximum...` |
| `FORM_LABELS` | `{'DailyRounds': 'Daily Rounds Log', 'ShiftLog': 'NH3 Shif...` |
| `FETCHERS` | `{'production': {'facts': _prodFacts, 'topn': _prodTopN}, ...` |
| `CARD_ROW` | `104` |
| `CARDS_PER_ROW` | `4` |
| `CHART_H` | `236` |
| `TABLE_HEAD` | `36` |
| `SEC_BAR` | `32` |
| `PREVIEW_W` | `812` |
| `PREVIEW_COLS` | `9` |
| `BD_SHORT` | `{'none': 'Total', 'hour': 'By Hour', 'shift': 'By Shift',...` |
| `SCOPE_TITLES` | `{'alarms': 'Areas & Devices', 'zoneTemps': 'Units', 'comp...` |
| `SHIFT_HOURS` | `(('A', '07:00 - 15:00'), ('B', '15:00 - 23:00'), ('C', '2...` |
| `POPUP_MAX` | `(1440, 880)` |
| `POPUP_MIN` | `(960, 560)` |
| `POPUP_MARGIN` | `24` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`username`](#username) | ------------------------------------------------------------------------------------------------ session / access | 0 |
| [`displayName`](#displayname) | | 0 |
| [`allowed`](#allowed) | Reports/&lt;action&gt; for the session (Roles & Permissions matrix via shared.Security). No session -&gt; False. | 0 |
| [`sourceAllowed`](#sourceallowed) | | 0 |
| [`context`](#context) | | 0 |
| [`catalog`](#catalog) | | 0 |
| [`enterpriseMode`](#enterprisemode) | Deployment switch (docs/local-groveport-mode.md): True only while [default]\_Config/DemoEnterpriseNav is a good | 0 |
| [`deployed`](#deployed) | A source is offered unless it is enterprise-only ('deployment': 'enterprise') and the HMI is in local mode. | 0 |
| [`sources`](#sources) | | 0 |
| [`source`](#source) | Catalog source by id; None for an unknown or a hidden (enterprise-only in local mode) source. | 0 |
| [`clientCatalog`](#clientcatalog) | | 0 |
| [`sourceOptions`](#sourceoptions) | | 0 |
| [`_measure`](#_measure) (internal) | | 0 |
| [`_applies`](#_applies) (internal) | | 0 |
| [`scopeItems`](#scopeitems) | [\{id, label, level, parent\}] - static catalog tree, plus the fetcher's dynamic options (alarm areas / devices). | 0 |
| [`scopeTree`](#scopetree) | | 0 |
| [`measureGroups`](#measuregroups) | | 0 |
| [`_py`](#_py) (internal) | Perspective / Java structures -&gt; plain Python (dates become epoch millis). | 0 |
| [`_ms`](#_ms) (internal) | | 0 |
| [`_ymd`](#_ymd) (internal) | | 0 |
| [`_ctxDay`](#_ctxday) (internal) | yyyy-MM-dd for a context date: java Date, epoch ms or text; '' when empty / unreadable. | 0 |
| [`_defaultSections`](#_defaultsections) (internal) | | 0 |
| [`normalize`](#normalize) | Any (partial) definition -&gt; a complete, valid one (unknown ids dropped, defaults filled). | 3 |
| [`defaultDefinition`](#defaultdefinition) | | 1 |
| [`_autoTitle`](#_autotitle) (internal) | | 0 |
| [`applyPreset`](#applypreset) | | 0 |
| [`_now`](#_now) (internal) | ------------------------------------------------------------------------------------------------ time | 0 |
| [`_mid`](#_mid) (internal) | | 0 |
| [`_addD`](#_addd) (internal) | | 0 |
| [`_addH`](#_addh) (internal) | | 0 |
| [`_fmtT`](#_fmtt) (internal) | | 0 |
| [`_shiftStart`](#_shiftstart) (internal) | Start of the shift running at ms (A 07:00, B 15:00, C 23:00 - C starts the evening before after midnight). | 0 |
| [`window`](#window) | | 0 |
| [`_windowLabel`](#_windowlabel) (internal) | | 0 |
| [`shiftOf`](#shiftof) | | 0 |
| [`buckets`](#buckets) | [\{t, t1, label, shift, day\}] local time; t = bucket start (shift start for 'shift', may precede s). | 0 |
| [`_days`](#_days) (internal) | | 0 |
| [`_num`](#_num) (internal) | ------------------------------------------------------------------------------------------------ aggregation | 0 |
| [`mvalue`](#mvalue) | Measure value from a record keyed by fields (ratio = num / den x scale). | 0 |
| [`aggregate`](#aggregate) | Aggregate one measure over records (catalog agg). | 0 |
| [`fmtValue`](#fmtvalue) | | 0 |
| [`header`](#header) | | 0 |
| [`_parseHM`](#_parsehm) (internal) | ------------------------------------------------------------------------------------------------ production fetcher | 0 |
| [`_summaryVal`](#_summaryval) (internal) | | 0 |
| [`_flat`](#_flat) (internal) | shared.ProductionMetrics.l1 output -&gt; flat record keyed by the catalog 'field' names. | 0 |
| [`_combine`](#_combine) (internal) | Merge records (shifts of a day, days of a week, units of a zone) with each field's catalog aggregation. | 0 |
| [`_Demo`](#_demo) (internal) | | 0 |
| [`_histPaths`](#_histpaths) (internal) | Tag paths (under historyRoot) a measure needs for this scope, or None when it has no history there. | 0 |
| [`_histValue`](#_histvalue) (internal) | Bucket value of a measure from the hourly historian averages (None when no samples). | 0 |
| [`_historian`](#_historian) (internal) | Replace demo values by SQL historian averages where the tag history covers the whole bucket. | 0 |
| [`_prodFacts`](#_prodfacts) (internal) | | 0 |
| [`_prodTopN`](#_prodtopn) (internal) | | 0 |
| [`_almFilters`](#_almfilters) (internal) | ------------------------------------------------------------------------------------------------ alarms fetcher | 0 |
| [`_almPath`](#_almpath) (internal) | Alarm source path -&gt; (area, device) after Boars\_Head/&lt;Site&gt;/&lt;Area&gt;/&lt;Type&gt;/&lt;Device&gt;; else Other. | 0 |
| [`_almCurrent`](#_almcurrent) (internal) | Active / unacknowledged alarm counts now per scope (system.alarm.queryStatus). | 0 |
| [`_almFacts`](#_almfacts) (internal) | | 0 |
| [`_almTopN`](#_almtopn) (internal) | | 0 |
| [`_almOptions`](#_almoptions) (internal) | Area / device scope items from the journal's last 30 days (cached 10 min). | 0 |
| [`_almRecords`](#_almrecords) (internal) | Event List: the latest activations in the window (newest first). | 0 |
| [`_histDevices`](#_histdevices) (internal) | | 0 |
| [`_histMember`](#_histmember) (internal) | | 0 |
| [`_histHours`](#_histhours) (internal) | | 0 |
| [`_histData`](#_histdata) (internal) | \{(path, ignitionMode): \{hourStart: value\}\} for every device x measure member (one query per mode). | 0 |
| [`_histDevValue`](#_histdevvalue) (internal) | | 0 |
| [`_histScopeValue`](#_histscopevalue) (internal) | Scope value from its devices: averages average, min / max / spread take the extreme, counters add up. | 0 |
| [`_histFacts`](#_histfacts) (internal) | | 0 |
| [`_histTopN`](#_histtopn) (internal) | Devices ranked by the Top N entry's measure over the whole window (+ the report's other measures). | 0 |
| [`_localMs`](#_localms) (internal) | ------------------------------------------------------------------------------------------------ out of service fetcher | 0 |
| [`_oosRows`](#_oosrows) (internal) | | 0 |
| [`_oosMatch`](#_oosmatch) (internal) | | 0 |
| [`_oosOverlap`](#_oosoverlap) (internal) | | 0 |
| [`_oosFacts`](#_oosfacts) (internal) | | 0 |
| [`_oosTopN`](#_oostopn) (internal) | | 0 |
| [`_oosRecords`](#_oosrecords) (internal) | | 0 |
| [`_oosOptions`](#_oosoptions) (internal) | | 0 |
| [`_formRows`](#_formrows) (internal) | | 0 |
| [`_formMatch`](#_formmatch) (internal) | | 0 |
| [`_formFacts`](#_formfacts) (internal) | | 0 |
| [`_formTopN`](#_formtopn) (internal) | | 0 |
| [`_formRecords`](#_formrecords) (internal) | | 0 |
| [`_scopeObjs`](#_scopeobjs) (internal) | ------------------------------------------------------------------------------------------------ engine | 0 |
| [`_context`](#_context) (internal) | | 0 |
| [`_srcNote`](#_srcnote) (internal) | Section note about the data source: none (labels removed at the user's request). | 0 |
| [`_srcNoteUnused`](#_srcnoteunused) (internal) | | 0 |
| [`_cards`](#_cards) (internal) | | 0 |
| [`_grainWord`](#_grainword) (internal) | | 0 |
| [`_trend`](#_trend) (internal) | | 0 |
| [`_table`](#_table) (internal) | | 0 |
| [`run`](#run) | Run a report definition for the session: \{ok, message, definition, meta, sections\}. | 0 |
| [`_isEmpty`](#_isempty) (internal) | True when nothing in the report has data (every card blank / zero, every table without rows). | 0 |
| [`_tableCols`](#_tablecols) (internal) | Perspective table columns that fit PREVIEW\_W exactly: each column gets what its longest header word and its | 0 |
| [`_tableParts`](#_tableparts) (internal) | Split a table section into parts of &lt;= PREVIEW\_COLS columns (key columns repeated), like the PDF. | 0 |
| [`paneWidth`](#panewidth) | Usable table width of the preview pane for a browser viewport width (popupPosition sizes the popup). | 0 |
| [`preview`](#preview) | | 0 |
| [`previewInstances`](#previewinstances) | | 1 |
| [`sectionItems`](#sectionitems) | | 0 |
| [`_tile`](#_tile) (internal) | | 0 |
| [`_rangeText`](#_rangetext) (internal) | Second line of a time tile: the dates the preset covers right now. | 0 |
| [`_joinLabels`](#_joinlabels) (internal) | | 0 |
| [`_unitText`](#_unittext) (internal) | | 0 |
| [`builderModel`](#buildermodel) | Everything the report builder shows for one definition: Step 1 source cards and quick reports, Step 2 time / | 1 |
| [`applyEdit`](#applyedit) | | 1 |
| [`_applyEdit`](#_applyedit) (internal) | | 0 |
| [`_customDate`](#_customdate) (internal) | Custom start / end as epoch ms for the date inputs. | 0 |
| [`_runRows`](#_runrows) (internal) | ------------------------------------------------------------------------------------------------ saved + recent | 0 |
| [`savedList`](#savedlist) | Step 1 rail: saved templates (own + shared) or the session user's last 10 downloads. | 1 |
| [`loadSaved`](#loadsaved) | Saved row click: \{definition, templateId, name, shared, canEdit, message\} or None. | 1 |
| [`logRun`](#logrun) | One row in dbo.report\_run per download (Recent list). Never fails the download. | 0 |
| [`_safe`](#_safe) (internal) | ------------------------------------------------------------------------------------------------ output | 0 |
| [`_pdfBlocks`](#_pdfblocks) (internal) | Sections -&gt; PDF blocks: \{title, note, cards[[...12]], charts[\{chartTitle, pens, rows\}], head, rows\}. | 0 |
| [`_datasets`](#_datasets) (internal) | Sections -&gt; [(sheet name, dataset)] for Excel / CSV (raw numbers, one sheet per section). | 0 |
| [`output`](#output) | Run + render in the definition's format: (bytes, filename, contentType, message); bytes None when refused. | 1 |
| [`download`](#download) | Generate button: browser download of the report. Returns a status message. | 1 |
| [`reportData`](#reportdata) | Script data source of Reports/CustomReport (no session - output() checked access and ran the report). | 1 |
| [`_nq`](#_nq) (internal) | ------------------------------------------------------------------------------------------------ templates | 0 |
| [`templates`](#templates) | Own + shared templates: [\{id, name, source, sourceLabel, owner, kind, canEdit, updated\}]. | 0 |
| [`templateOptions`](#templateoptions) | | 0 |
| [`loadTemplate`](#loadtemplate) | | 0 |
| [`saveTemplate`](#savetemplate) | Save (owner / manager) or Save As (a new template owned by the session user): \{ok, id, message\}. | 2 |
| [`deleteTemplate`](#deletetemplate) | | 2 |
| [`startState`](#startstate) | | 1 |
| [`_rangeRule`](#_rangerule) (internal) | Time range rule of a definition: 'Last 7 Days', or the dates of a custom range. | 0 |
| [`_lastRuns`](#_lastruns) (internal) | \{(source, title): newest download time\} of the session user. | 0 |
| [`_runList`](#_runlist) (internal) | Recent Runs rows (own, or every user's with ManageTemplates). | 0 |
| [`savedModel`](#savedmodel) | Saved Reports page: \{rows, owners, sources, counts, tab\}. Tabs: mine (own templates), shared (every shared | 1 |
| [`renameTemplate`](#renametemplate) | | 2 |
| [`setTemplateShared`](#settemplateshared) | | 1 |
| [`runFromRun`](#runfromrun) | Recent Runs: download that run's report again (own runs only). | 3 |
| [`startModel`](#startmodel) | | 1 |
| [`templateRows`](#templaterows) | Reports page table rows. | 0 |
| [`runTemplate`](#runtemplate) | Reports page: download a saved template's report (format override optional). Returns a status message. | 3 |
| [`_callerPage`](#_callerpage) (internal) | The Perspective page of the calling component / view script (self.page up the stack), else None. | 0 |
| [`popupPosition`](#popupposition) | Popup box centred in the browser viewport and never larger than it (minus POPUP\_MARGIN on each side). | 0 |
| [`centerBox`](#centerbox) | | 1 |
| [`_evNum`](#_evnum) (internal) | | 0 |
| [`menuBox`](#menubox) | A w x h small-menu position at the click (clientX / clientY), kept inside the browser viewport. | 1 |
| [`open`](#open) | Open the report builder popup (any page): shared.Reports.open('alarms', \{'areas': [...], 'origin': '...'\}). | 12 |
| [`close`](#close) | | 2 |

### username {#username}

```python
def username(session)
```
Line 49 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ session / access
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_formRows`, `_lastRuns`, `_runList`, `_runRows`, `allowed`, `context`, `deleteTemplate`, `displayName`, `loadSaved`, `loadTemplate`, `logRun`, `saveTemplate`, `savedModel`, `templates`

### displayName {#displayname}

```python
def displayName(session)
```
Line 56 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `context`, `run`, `saveTemplate`

### allowed {#allowed}

```python
def allowed(session, action='Use')
```
Line 69 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Reports/<action> for the session (Roles & Permissions matrix via shared.Security). No session -> False.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_runList`, `context`, `deleteTemplate`, `loadTemplate`, `open`, `run`, `saveTemplate`, `savedList`, `savedModel`, `sourceAllowed`, `templates`

### sourceAllowed {#sourceallowed}

```python
def sourceAllowed(session, src)
```
Line 80 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `clientCatalog`, `loadSaved`, `loadTemplate`, `measureGroups`, `run`, `saveTemplate`, `scopeItems`, `startState`

### context {#context}

```python
def context(session)
```
Line 90 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `startState`

### catalog {#catalog}

```python
def catalog()
```
Line 96 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_defaultSections`, `builderModel`, `clientCatalog`, `defaultDefinition`, `normalize`, `sectionItems`, `source`, `sources`

### enterpriseMode {#enterprisemode}

```python
def enterpriseMode()
```
Line 115 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Deployment switch (docs/local-groveport-mode.md): True only while [default]_Config/DemoEnterpriseNav is a good
True. Missing / bad tag = local Groveport mode, so enterprise-only sources stay hidden (cached 30 s).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `deployed`

### deployed {#deployed}

```python
def deployed(src)
```
Line 132 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
A source is offered unless it is enterprise-only ('deployment': 'enterprise') and the HMI is in local mode.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `source`, `sources`

### sources {#sources}

```python
def sources()
```
Line 137 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `clientCatalog`, `normalize`

### source {#source}

```python
def source(sourceId)
```
Line 141 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Catalog source by id; None for an unknown or a hidden (enterprise-only in local mode) source.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_applyEdit`, `_autoTitle`, `builderModel`, `loadSaved`, `loadTemplate`, `measureGroups`, `normalize`, `run`, `saveTemplate`, `scopeItems`, `sectionItems`, `startState`

### clientCatalog {#clientcatalog}

```python
def clientCatalog(session)
```
Line 149 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_runList`, `_runRows`, `applyPreset`, `builderModel`, `defaultDefinition`, `sourceOptions`, `startModel`, `startState`, `templates`

### sourceOptions {#sourceoptions}

```python
def sourceOptions(session)
```
Line 158 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `startState`

### \_measure {#_measure}

```python
def _measure(src, mid)
```
Line 162 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_autoTitle`, `_context`, `_histPaths`, `_histTopN`, `builderModel`

### \_applies {#_applies}

```python
def _applies(m, level)
```
Line 169 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_cards`, `_prodFacts`, `_table`, `_trend`

### scopeItems {#scopeitems}

```python
def scopeItems(session, sourceId)
```
Line 174 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
[{id, label, level, parent}] - static catalog tree, plus the fetcher's dynamic options (alarm areas / devices).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `scopeTree`

### scopeTree {#scopetree}

```python
def scopeTree(session, sourceId)
```
Line 187 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_applyEdit`, `builderModel`

### measureGroups {#measuregroups}

```python
def measureGroups(session, sourceId)
```
Line 205 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `builderModel`

### \_py {#_py}

```python
def _py(obj)
```
Line 220 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Perspective / Java structures -> plain Python (dates become epoch millis).
```

Used inside the module by: `applyEdit`, `defaultDefinition`, `normalize`, `open`, `startState`

### \_ms {#_ms}

```python
def _ms(v)
```
Line 230 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_customDate`, `normalize`, `window`

### \_ymd {#_ymd}

```python
def _ymd(ms)
```
Line 246 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_applyEdit`, `_ctxDay`, `defaultDefinition`, `normalize`

### \_ctxDay {#_ctxday}

```python
def _ctxDay(v)
```
Line 250 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
yyyy-MM-dd for a context date: java Date, epoch ms or text; '' when empty / unreadable.
```

Used inside the module by: `defaultDefinition`

### \_defaultSections {#_defaultsections}

```python
def _defaultSections(src)
```
Line 264 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `defaultDefinition`, `normalize`

### normalize {#normalize}

```python
def normalize(defn)
```
Line 280 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Any (partial) definition -> a complete, valid one (unknown ids dropped, defaults filled).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Download/Body/Download event component.onActionPerformed` |
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Save/Body/ShareRow/Save event component.onActionPerformed` |
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Save/Body/TplRow/SaveAs event component.onActionPerformed` |

Used inside the module by: `_applyEdit`, `_runList`, `applyEdit`, `applyPreset`, `builderModel`, `defaultDefinition`, `download`, `loadSaved`, `loadTemplate`, `run`, `saveTemplate`, `sectionItems`, `templates`

### defaultDefinition {#defaultdefinition}

```python
def defaultDefinition(session, sourceId=None, ctx=None)
```
Line 350 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root/Footer/StartOver event component.onActionPerformed` |

Used inside the module by: `applyEdit`, `startState`

### \_autoTitle {#_autotitle}

```python
def _autoTitle(d)
```
Line 391 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `applyEdit`, `defaultDefinition`, `download`, `run`

### applyPreset {#applypreset}

```python
def applyPreset(session, presetId)
```
Line 401 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `applyEdit`, `startState`

### \_now {#_now}

```python
def _now()
```
Line 409 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ time
```

Used inside the module by: `_Demo`, `_almOptions`, `_applyEdit`, `_customDate`, `_oosFacts`, `_oosOptions`, `_oosRecords`, `_oosTopN`, `run`, `window`

### \_mid {#_mid}

```python
def _mid(ms)
```
Line 413 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_Demo`, `_almOptions`, `_applyEdit`, `_customDate`, `_days`, `_histData`, `_histHours`, `_historian`, `_shiftStart`, `_windowLabel`, `buckets`, `window`

### \_addD {#_addd}

```python
def _addD(ms, n)
```
Line 417 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_almOptions`, `_days`, `_shiftStart`, `buckets`, `window`

### \_addH {#_addh}

```python
def _addH(ms, n)
```
Line 421 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_histData`, `_histHours`, `_historian`, `_shiftStart`, `buckets`, `window`

### \_fmtT {#_fmtt}

```python
def _fmtT(ms, pattern)
```
Line 425 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_almFilters`, `_almOptions`, `_formRecords`, `_formRows`, `_oosRecords`, `_oosRows`, `_rangeText`, `_windowLabel`, `buckets`

### \_shiftStart {#_shiftstart}

```python
def _shiftStart(ms)
```
Line 429 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Start of the shift running at ms (A 07:00, B 15:00, C 23:00 - C starts the evening before after midnight).
```

Used inside the module by: `window`

### window {#window}

```python
def window(d)
```
Line 438 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_context`, `_rangeText`, `_windowLabel`

### \_windowLabel {#_windowlabel}

```python
def _windowLabel(d, short=False)
```
Line 458 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_autoTitle`, `_rangeRule`, `builderModel`, `run`

### shiftOf {#shiftof}

```python
def shiftOf(hour)
```
Line 473 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_formRows`, `_histHours`, `_historian`, `_rangeText`, `_windowLabel`, `buckets`

### buckets {#buckets}

```python
def buckets(s, e, grain, shifts)
```
Line 477 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
[{t, t1, label, shift, day}] local time; t = bucket start (shift start for 'shift', may precede s).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_context`

### \_days {#_days}

```python
def _days(t0, t1)
```
Line 518 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_Demo`, `_prodTopN`

### \_num {#_num}

```python
def _num(v)
```
Line 528 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ aggregation
```

Used inside the module by: `_almRecords`, `_almTopN`, `_flat`, `_histData`, `_histDevValue`, `_historian`, `aggregate`, `mvalue`

### mvalue {#mvalue}

```python
def mvalue(m, v)
```
Line 537 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Measure value from a record keyed by fields (ratio = num / den x scale).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_cards`, `_trend`, `aggregate`

### aggregate {#aggregate}

```python
def aggregate(m, recs)
```
Line 547 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Aggregate one measure over records (catalog agg).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_cards`, `_table`

### fmtValue {#fmtvalue}

```python
def fmtValue(m, v, unit=False)
```
Line 573 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_cards`, `_histTopN`, `_table`

### header {#header}

```python
def header(m)
```
Line 590 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_histTopN`, `_table`

### \_parseHM {#_parsehm}

```python
def _parseHM(s)
```
Line 598 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ production fetcher
```

Used inside the module by: `_flat`

### \_summaryVal {#_summaryval}

```python
def _summaryVal(rows, metric)
```
Line 606 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_flat`

### \_flat {#_flat}

```python
def _flat(r, level)
```
Line 617 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
shared.ProductionMetrics.l1 output -> flat record keyed by the catalog 'field' names.
```

Used inside the module by: `_Demo`

### \_combine {#_combine}

```python
def _combine(recs, aggs, weighted=True)
```
Line 638 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Merge records (shifts of a day, days of a week, units of a zone) with each field's catalog aggregation.
```

Used inside the module by: `_Demo`

### \_Demo {#_demo}

```python
class _Demo
```
Line 665 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

Used inside the module by: `_prodFacts`, `_prodTopN`

### \_histPaths {#_histpaths}

```python
def _histPaths(src, m, sc)
```
Line 742 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Tag paths (under historyRoot) a measure needs for this scope, or None when it has no history there.
```

Used inside the module by: `_historian`

### \_histValue {#_histvalue}

```python
def _histValue(src, m, sc, paths, hourly, hours)
```
Line 763 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Bucket value of a measure from the hourly historian averages (None when no samples).
```

Used inside the module by: `_historian`

### \_historian {#_historian}

```python
def _historian(ctx, facts)
```
Line 780 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Replace demo values by SQL historian averages where the tag history covers the whole bucket.
```

Used inside the module by: `_prodFacts`

### \_prodFacts {#_prodfacts}

```python
def _prodFacts(ctx)
```
Line 855 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_prodTopN {#_prodtopn}

```python
def _prodTopN(ctx, spec)
```
Line 870 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

### \_almFilters {#_almfilters}

```python
def _almFilters(ctx, scopes=None)
```
Line 899 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ alarms fetcher
```

Used inside the module by: `_almFacts`, `_almRecords`, `_almTopN`

### \_almPath {#_almpath}

```python
def _almPath(src_path)
```
Line 908 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Alarm source path -> (area, device) after Boars_Head/<Site>/<Area>/<Type>/<Device>; else Other.
```

Used inside the module by: `_almCurrent`

### \_almCurrent {#_almcurrent}

```python
def _almCurrent(ctx)
```
Line 920 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Active / unacknowledged alarm counts now per scope (system.alarm.queryStatus).
```

Used inside the module by: `_almFacts`

### \_almFacts {#_almfacts}

```python
def _almFacts(ctx)
```
Line 946 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_almTopN {#_almtopn}

```python
def _almTopN(ctx, spec)
```
Line 989 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_almOptions {#_almoptions}

```python
def _almOptions(src)
```
Line 1020 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Area / device scope items from the journal's last 30 days (cached 10 min).
```

### \_almRecords {#_almrecords}

```python
def _almRecords(ctx, spec)
```
Line 1045 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Event List: the latest activations in the window (newest first).
```

### \_histDevices {#_histdevices}

```python
def _histDevices(src, sc)
```
Line 1069 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_histFacts`, `_histTopN`

### \_histMember {#_histmember}

```python
def _histMember(m, dev)
```
Line 1078 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_histData`, `_histDevValue`

### \_histHours {#_histhours}

```python
def _histHours(ctx, t0, t1)
```
Line 1085 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_histFacts`, `_histTopN`

### \_histData {#_histdata}

```python
def _histData(ctx, devs, measures)
```
Line 1095 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
{(path, ignitionMode): {hourStart: value}} for every device x measure member (one query per mode).
```

Used inside the module by: `_histFacts`, `_histTopN`

### \_histDevValue {#_histdevvalue}

```python
def _histDevValue(m, dev, data, hours)
```
Line 1140 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_histScopeValue`, `_histTopN`

### \_histScopeValue {#_histscopevalue}

```python
def _histScopeValue(m, devs, data, hours)
```
Line 1198 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Scope value from its devices: averages average, min / max / spread take the extreme, counters add up.
```

Used inside the module by: `_histFacts`

### \_histFacts {#_histfacts}

```python
def _histFacts(ctx)
```
Line 1214 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_histTopN {#_histtopn}

```python
def _histTopN(ctx, spec)
```
Line 1231 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Devices ranked by the Top N entry's measure over the whole window (+ the report's other measures).
```

### \_localMs {#_localms}

```python
def _localMs(txt)
```
Line 1258 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ out of service fetcher
```

Used inside the module by: `_formRows`, `_oosRows`

### \_oosRows {#_oosrows}

```python
def _oosRows(ctx)
```
Line 1267 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_oosFacts`, `_oosRecords`, `_oosTopN`

### \_oosMatch {#_oosmatch}

```python
def _oosMatch(sc, r)
```
Line 1279 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_oosFacts`, `_oosRecords`, `_oosTopN`

### \_oosOverlap {#_oosoverlap}

```python
def _oosOverlap(r, t0, t1, now)
```
Line 1284 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_oosFacts`, `_oosTopN`

### \_oosFacts {#_oosfacts}

```python
def _oosFacts(ctx)
```
Line 1289 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_oosTopN {#_oostopn}

```python
def _oosTopN(ctx, spec)
```
Line 1311 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_oosRecords {#_oosrecords}

```python
def _oosRecords(ctx, spec)
```
Line 1340 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_oosOptions {#_oosoptions}

```python
def _oosOptions(src)
```
Line 1354 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_formRows {#_formrows}

```python
def _formRows(ctx)
```
Line 1378 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_formFacts`, `_formRecords`, `_formTopN`

### \_formMatch {#_formmatch}

```python
def _formMatch(sc, r)
```
Line 1402 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_formFacts`, `_formRecords`, `_formTopN`

### \_formFacts {#_formfacts}

```python
def _formFacts(ctx)
```
Line 1406 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_formTopN {#_formtopn}

```python
def _formTopN(ctx, spec)
```
Line 1422 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_formRecords {#_formrecords}

```python
def _formRecords(ctx, spec)
```
Line 1438 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_scopeObjs {#_scopeobjs}

```python
def _scopeObjs(src, ids)
```
Line 1460 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ engine
```

Used inside the module by: `_autoTitle`, `_context`, `builderModel`

### \_context {#_context}

```python
def _context(d, src, grain=None, shifts=None)
```
Line 1474 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `run`

### \_srcNote {#_srcnote}

```python
def _srcNote(srcs)
```
Line 1483 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Section note about the data source: none (labels removed at the user's request).
```

Used inside the module by: `_cards`, `_table`, `_trend`

### \_srcNoteUnused {#_srcnoteunused}

```python
def _srcNoteUnused(srcs)
```
Line 1488 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

### \_cards {#_cards}

```python
def _cards(ctx, res)
```
Line 1499 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `run`

### \_grainWord {#_grainword}

```python
def _grainWord(g, n)
```
Line 1538 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `_cards`

### \_trend {#_trend}

```python
def _trend(ctx, res)
```
Line 1543 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `run`

### \_table {#_table}

```python
def _table(ctx, res, kind='table')
```
Line 1589 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `run`

### run {#run}

```python
def run(session, defn, preview=False)
```
Line 1648 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Run a report definition for the session: {ok, message, definition, meta, sections}.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `output`, `preview`

### \_isEmpty {#_isempty}

```python
def _isEmpty(sections)
```
Line 1727 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
True when nothing in the report has data (every card blank / zero, every table without rows).
```

Used inside the module by: `run`

### \_tableCols {#_tablecols}

```python
def _tableCols(cols, rows=None, width=None)
```
Line 1758 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Perspective table columns that fit PREVIEW_W exactly: each column gets what its longest header word and its
values need (headers never break inside a word), scaled to the pane; long values wrap (white-space normal) and
every cell is aligned with its header.
```

Used inside the module by: `preview`

### \_tableParts {#_tableparts}

```python
def _tableParts(s)
```
Line 1791 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Split a table section into parts of <= PREVIEW_COLS columns (key columns repeated), like the PDF.
```

Used inside the module by: `preview`

### paneWidth {#panewidth}

```python
def paneWidth(vw=None)
```
Line 1806 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Usable table width of the preview pane for a browser viewport width (popupPosition sizes the popup).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `previewInstances`

### preview {#preview}

```python
def preview(session, defn, width=None)
```
Line 1816 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `previewInstances`

### previewInstances {#previewinstances}

```python
def previewInstances(session, defn, vw=None)
```
Line 1853 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

vw = the browser viewport width (page.props.dimensions.viewport.width), so tables fill the pane.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `binding custom.preview` |

### sectionItems {#sectionitems}

```python
def sectionItems(session, defn)
```
Line 1873 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `builderModel`

### \_tile {#_tile}

```python
def _tile(id_, label, detail, selected, kind)
```
Line 1900 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `builderModel`, `startModel`

### \_rangeText {#_rangetext}

```python
def _rangeText(preset)
```
Line 1904 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Second line of a time tile: the dates the preset covers right now.
```

Used inside the module by: `builderModel`

### \_joinLabels {#_joinlabels}

```python
def _joinLabels(labels, most=3)
```
Line 1918 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `builderModel`

### \_unitText {#_unittext}

```python
def _unitText(m)
```
Line 1925 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `builderModel`

### builderModel {#buildermodel}

```python
def builderModel(session, defn)
```
Line 1930 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Everything the report builder shows for one definition: Step 1 source cards and quick reports, Step 2 time /
group-by / shift tiles, Step 3 scope and measure rows, advanced sections and filters, and the right-rail summary.
The view has exactly one computing binding (this call); every component binds to a key of the result.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `binding custom.model` |

### applyEdit {#applyedit}

```python
def applyEdit(session, defn, edit)
```
Line 1997 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root message handler rptEdit` |

### \_applyEdit {#_applyedit}

```python
def _applyEdit(session, d, e, k)
```
Line 2015 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `applyEdit`

### \_customDate {#_customdate}

```python
def _customDate(d, key)
```
Line 2087 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Custom start / end as epoch ms for the date inputs.
```

Used inside the module by: `builderModel`

### \_runRows {#_runrows}

```python
def _runRows(session)
```
Line 2093 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ saved + recent
```

Used inside the module by: `savedList`

### savedList {#savedlist}

```python
def savedList(session, tab='templates')
```
Line 2111 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Step 1 rail: saved templates (own + shared) or the session user's last 10 downloads.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `binding custom.saved` |

### loadSaved {#loadsaved}

```python
def loadSaved(session, kind, savedId)
```
Line 2124 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Saved row click: {definition, templateId, name, shared, canEdit, message} or None.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root message handler rptLoadSaved` |

Used inside the module by: `runFromRun`, `startState`

### logRun {#logrun}

```python
def logRun(session, d, title)
```
Line 2144 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
One row in dbo.report_run per download (Recent list). Never fails the download.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `download`

### \_safe {#_safe}

```python
def _safe(s)
```
Line 2154 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ output
```

Used inside the module by: `_datasets`, `output`

### \_pdfBlocks {#_pdfblocks}

```python
def _pdfBlocks(r)
```
Line 2159 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Sections -> PDF blocks: {title, note, cards[[...12]], charts[{chartTitle, pens, rows}], head, rows}.
```

Used inside the module by: `output`

### \_datasets {#_datasets}

```python
def _datasets(r)
```
Line 2203 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Sections -> [(sheet name, dataset)] for Excel / CSV (raw numbers, one sheet per section).
```

Used inside the module by: `output`

### output {#output}

```python
def output(session, defn)
```
Line 2243 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Run + render in the definition's format: (bytes, filename, contentType, message); bytes None when refused.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `Reports/CustomReport` | report | `data source` |

Used inside the module by: `download`

### download {#download}

```python
def download(session, defn)
```
Line 2281 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Generate button: browser download of the report. Returns a status message.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Download/Body/Download event component.onActionPerformed` |

Used inside the module by: `runFromRun`, `runTemplate`

### reportData {#reportdata}

```python
def reportData(data)
```
Line 2292 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Script data source of Reports/CustomReport (no session - output() checked access and ran the report).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `Reports/CustomReport` | report | `data source` |

### \_nq {#_nq}

```python
def _nq(path, params, getKey=False)
```
Line 2338 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
------------------------------------------------------------------------------------------------ templates
```

Used inside the module by: `_lastRuns`, `_runList`, `_runRows`, `deleteTemplate`, `loadSaved`, `loadTemplate`, `logRun`, `saveTemplate`, `templates`

### templates {#templates}

```python
def templates(session, sourceId='')
```
Line 2342 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Own + shared templates: [{id, name, source, sourceLabel, owner, kind, canEdit, updated}].
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `savedList`, `savedModel`, `templateOptions`, `templateRows`

### templateOptions {#templateoptions}

```python
def templateOptions(session, sourceId='')
```
Line 2372 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### loadTemplate {#loadtemplate}

```python
def loadTemplate(session, templateId)
```
Line 2377 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `loadSaved`, `renameTemplate`, `runTemplate`, `setTemplateShared`, `startState`

### saveTemplate {#savetemplate}

```python
def saveTemplate(session, templateId, name, defn, isShared=False, saveAs=False)
```
Line 2399 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Save (owner / manager) or Save As (a new template owned by the session user): {ok, id, message}.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Save/Body/ShareRow/Save event component.onActionPerformed` |
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Save/Body/TplRow/SaveAs event component.onActionPerformed` |

Used inside the module by: `renameTemplate`, `setTemplateShared`

### deleteTemplate {#deletetemplate}

```python
def deleteTemplate(session, templateId)
```
Line 2434 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsSaved` | view | `root message handler rptPageDelete` |
| `01_Popups/Reports/ReportBuilder` | view | `root message handler rptDeleteTemplate` |

### startState {#startstate}

```python
def startState(session, sourceId='', ctx=None, templateId=0)
```
Line 2445 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root event system.onStartup` |

### \_rangeRule {#_rangerule}

```python
def _rangeRule(d)
```
Line 2477 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Time range rule of a definition: 'Last 7 Days', or the dates of a custom range.
```

Used inside the module by: `_runList`, `templates`

### \_lastRuns {#_lastruns}

```python
def _lastRuns(session)
```
Line 2483 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
{(source, title): newest download time} of the session user.
```

Used inside the module by: `savedModel`

### \_runList {#_runlist}

```python
def _runList(session)
```
Line 2494 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Recent Runs rows (own, or every user's with ManageTemplates).
```

Used inside the module by: `savedModel`

### savedModel {#savedmodel}

```python
def savedModel(session, tab='mine', sourceId='', owner='', search='', refresh=0)
```
Line 2518 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Saved Reports page: {rows, owners, sources, counts, tab}. Tabs: mine (own templates), shared (every shared
template), runs (Recent Runs). Owner visibility is enforced in the SQL (own + shared only).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsSaved` | view | `binding custom.model` |

### renameTemplate {#renametemplate}

```python
def renameTemplate(session, templateId, name)
```
Line 2562 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/RenameReport` | view | `root/Buttons/Save event component.onActionPerformed` |
| `01_Popups/Reports/RenameReport` | view | `root/Name event component.onActionPerformed` |

### setTemplateShared {#settemplateshared}

```python
def setTemplateShared(session, templateId, flag)
```
Line 2571 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Share event dom.onClick` |

### runFromRun {#runfromrun}

```python
def runFromRun(session, runId, fmt='')
```
Line 2583 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Recent Runs: download that run's report again (own runs only).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/DownloadMenu` | view | `root/Csv event component.onActionPerformed` |
| `01_Popups/Reports/DownloadMenu` | view | `root/Pdf event component.onActionPerformed` |
| `01_Popups/Reports/DownloadMenu` | view | `root/Xls event component.onActionPerformed` |

### startModel {#startmodel}

```python
def startModel(session)
```
Line 2594 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Operations/ReportsBuilder` | view | `binding custom.model` |

### templateRows {#templaterows}

```python
def templateRows(session, sourceId='')
```
Line 2604 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Reports page table rows.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### runTemplate {#runtemplate}

```python
def runTemplate(session, templateId, fmt='')
```
Line 2610 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Reports page: download a saved template's report (format override optional). Returns a status message.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/DownloadMenu` | view | `root/Csv event component.onActionPerformed` |
| `01_Popups/Reports/DownloadMenu` | view | `root/Pdf event component.onActionPerformed` |
| `01_Popups/Reports/DownloadMenu` | view | `root/Xls event component.onActionPerformed` |

### \_callerPage {#_callerpage}

```python
def _callerPage()
```
Line 2627 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
The Perspective page of the calling component / view script (self.page up the stack), else None.
```

Used inside the module by: `open`

### popupPosition {#popupposition}

```python
def popupPosition(page=None)
```
Line 2649 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Popup box centred in the browser viewport and never larger than it (minus POPUP_MARGIN on each side).
Perspective otherwise sizes a popup from the view's defaultSize and centres it in the popups pane beside the docked

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `open`, `paneWidth`

### centerBox {#centerbox}

```python
def centerBox(page, w, h)
```
Line 2665 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text

```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Rename event dom.onClick` |

### \_evNum {#_evnum}

```python
def _evNum(event, key)
```
Line 2678 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

Used inside the module by: `menuBox`

### menuBox {#menubox}

```python
def menuBox(page, event, w, h)
```
Line 2689 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
A w x h small-menu position at the click (clientX / clientY), kept inside the browser viewport.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Download event dom.onClick` |

### open {#open}

```python
def open(sourceId=None, context=None, session=None, templateId=0, page=None)
```
Line 2708 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

```text
Open the report builder popup (any page): shared.Reports.open('alarms', {'areas': [...], 'origin': '...'}).
The context pre-selects the source (and areas / scope / shift / day); the popup is sized to the caller's viewport.
```

<details>
<summary>Called from 12 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Alarms/Journal` | view | `root/Filters/GenerateReport event component.onActionPerformed` |
| `00_Pages/Boars Head/Alarms/Summary` | view | `root/Filters/GenerateReport event component.onActionPerformed` |
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root/Filters/GenerateReport event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/History` | view | `root/Tabs/Forms/Filters/ReportBtn/GenerateReport event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/ReportsBuilder` | view | `root message handler rptStart` |
| `00_Pages/Groveport/Operations/ReportsSaved` | view | `root/Card/Tables/Empty/Create event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/ReportsSaved` | view | `root/Head/New event component.onActionPerformed` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/GenerateReport event component.onActionPerformed` |
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root event dom.onDoubleClick` |
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Edit event dom.onClick` |
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Run event dom.onClick` |
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/RunAgain event dom.onClick` |
</details>

### close {#close}

```python
def close()
```
Line 2729 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Reports/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/Reports/ReportBuilder` | view | `root/Footer/Cancel event component.onActionPerformed` |
| `01_Popups/Reports/ReportBuilder` | view | `root/Header/Close event dom.onClick` |
