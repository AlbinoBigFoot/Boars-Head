---
title: "shared.TrendContext"
sidebar_label: "shared.TrendContext"
description: "Script module shared.TrendContext: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`  
**Lines:** 640. **Functions:** 40. **Called as:** `shared.TrendContext.<function>(...)`

## What the source says

```text
Trend context menu + session trend basket (2026-10-23). See docs/trending.md.

Every historized value in the HMI calls menu() from its right-click (events.dom.onContextMenu, wired by


        shared.TrendContext.menu(self, event, '{view.params.tagPath}/ZAT/Val')

The third argument is a path template: {view.params.x}, {view.custom.x}, {this.custom.x}, {session.custom.x},
{page.props.x} and {../Sibling.props.x} references are resolved against the component at click time.

Basket = session.custom.AdhocTrend.tags (what the Trending page, the faceplate trend and Saved Trends /
dbo.adhoc_trend_configs already use). session.custom.trend {pens, count, key} is a read-only summary bound from
it (session props), for the header badge and other readers. Pens are stored as full atomic history paths.


outside a known UDT instance fall back to one cached '.HistoryEnabled' property read per path.

The menu never writes tags: it only changes the session basket, navigates, and opens popups.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.perspective`, `system.tag` |
| Calls modules | [shared.AdhocTrend](./shared-adhoctrend.md), [shared.Alerts](./shared-alerts.md) |
| Called by modules | [shared.tagsTree](./shared-tagstree.md) |

<details>
<summary>Module constants (15)</summary>

| Name | Value |
|---|---|
| `POPUP_MENU` | `'TrendContextMenu'` |
| `VIEW_MENU` | `'01_Popups/TrendContext/Menu'` |
| `POPUP_QUICK` | `'TrendQuickHistory'` |
| `VIEW_QUICK` | `'01_Popups/TrendContext/QuickHistory'` |
| `POPUP_TOAST` | `'TrendToast'` |
| `VIEW_TOAST` | `'01_Popups/TrendContext/Toast'` |
| `POPUP_COPY` | `'TrendCopyPath'` |
| `VIEW_COPY` | `'01_Popups/TrendContext/CopyPath'` |
| `TREND_PAGE` | `'/trending'` |
| `MAX_PENS` | `10` |
| `MENU_W` | `236` |
| `ROW_H` | `30` |
| `HEAD_H` | `53` |
| `SEP_H` | `9` |
| `_REF` | `re.compile('\\{([^{}]+)\\}')` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_H`](#_h) (internal) | | 0 |
| [`_split`](#_split) (internal) | '[prov]a/b' -&gt; ('prov', 'a/b'); bare paths are [default]. | 0 |
| [`full`](#full) | | 0 |
| [`owner`](#owner) | (instancePath, typeId, memberPath) when path is under a known top-level UDT instance, else (None, None, None). | 0 |
| [`is_historized`](#is_historized) | True when the atomic tag at path has history enabled (no getConfiguration; see module doc). | 0 |
| [`_legacy`](#_legacy) (internal) | Pre-PAX member (saved trends) -&gt; PlantPAx member of the same device, else None. | 0 |
| [`history_path`](#history_path) | Full atomic path the historian stores: the path itself, or path + '/Value' for legacy \_Root/\* instances. | 0 |
| [`label`](#label) | Operator pen label: '&lt;Device&gt; &lt;Member&gt;' (e.g. 'CG-E4 Zone Temp', 'Comp 4 Discharge Pressure'). | 0 |
| [`units`](#units) | Engineering unit: static UDT engUnit when known, else one cached '.EngUnit' read. | 0 |
| [`all_paths`](#all_paths) | Every historized atomic tag the index knows (Trending page tag browser), full paths, sorted. | 1 |
| [`_walk`](#_walk) (internal) | | 0 |
| [`_ref`](#_ref) (internal) | | 0 |
| [`resolve`](#resolve) | Substitute \{...\} property references in a path template; '' when any reference is empty. | 0 |
| [`_cfg`](#_cfg) (internal) | | 0 |
| [`_tags`](#_tags) (internal) | | 0 |
| [`in_trend`](#in_trend) | | 0 |
| [`add`](#add) | Add a historized tag to the session trend. Returns (ok, message). | 0 |
| [`remove`](#remove) | Remove a tag (any stored form of it) from the session trend. Returns (ok, message). | 0 |
| [`toggle`](#toggle) | | 1 |
| [`summary`](#summary) | session.custom.trend from session.custom.AdhocTrend: \{pens: [\{tagPath, label, units, color, axis, plot\}], | 1 |
| [`_num`](#_num) (internal) | | 0 |
| [`_viewport`](#_viewport) (internal) | | 0 |
| [`menu`](#menu) | Right-click handler: open the trend context menu at the cursor (never a write action). | 126 |
| [`close_menu`](#close_menu) | | 1 |
| [`menu_action`](#menu_action) | Menu row click (01\_Popups/TrendContext/Menu). action: add \| remove \| open \| quick \| copy \| ticket. | 6 |
| [`open_trend`](#open_trend) | | 2 |
| [`quick_history`](#quick_history) | | 0 |
| [`copy_path`](#copy_path) | | 0 |
| [`toast`](#toast) | | 1 |
| [`copy_markdown`](#copy_markdown) | Markdown source for the CopyPath popup: a Copy button + one automatic copy attempt (client JS). | 1 |
| [`quick_key`](#quick_key) | | 0 |
| [`quick_series`](#quick_series) | Single-pen ApexCharts series from a Wide history dataset (t\_stamp + 'pen'). | 1 |
| [`is_tall`](#is_tall) | Tall history dataset (path, value, quality, timestamp): the only format that carries quality. | 0 |
| [`columns`](#columns) | Pen columns: Wide = the column names; Tall = 't\_stamp' + the distinct path / alias values. | 1 |
| [`_good`](#_good) (internal) | Quality code from a Tall row: bad / error codes are negative (Good = 192, Uncertain kept). | 0 |
| [`points`](#points) | [[epochMs, value\|None], ...] for one pen. The historian returns 0.0 for windows with bad quality (comm loss) | 1 |
| [`_ev`](#_ev) (internal) | | 0 |
| [`_ms`](#_ms) (internal) | | 0 |
| [`chart_zoomed`](#chart_zoomed) | zoomedHandler / scrolledHandler: remember the window (and pause a live Quick History). Zoom Area: kyvis passes | 8 |
| [`chart_reset`](#chart_reset) | Reset Zoom / the zoomed chip / double-click: full range again on the chart(s) named (root children). | 9 |

### \_H {#_h}

```python
def _H()
```
Line 43 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `_legacy`, `all_paths`, `history_path`, `is_historized`, `label`, `owner`, `units`

### \_split {#_split}

```python
def _split(path)
```
Line 49 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
'[prov]a/b' -> ('prov', 'a/b'); bare paths are [default].
```

Used inside the module by: `full`, `is_historized`, `label`, `owner`

### full {#full}

```python
def full(path)
```
Line 59 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `copy_path`, `history_path`, `is_historized`

### owner {#owner}

```python
def owner(path)
```
Line 64 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
(instancePath, typeId, memberPath) when path is under a known top-level UDT instance, else (None, None, None).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `history_path`, `is_historized`, `label`

### is\_historized {#is_historized}

```python
def is_historized(path)
```
Line 79 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
True when the atomic tag at path has history enabled (no getConfiguration; see module doc).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `add`, `history_path`, `menu`

### \_legacy {#_legacy}

```python
def _legacy(tid, member)
```
Line 108 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Pre-PAX member (saved trends) -> PlantPAx member of the same device, else None.
```

Used inside the module by: `history_path`

### history\_path {#history_path}

```python
def history_path(path)
```
Line 119 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Full atomic path the historian stores: the path itself, or path + '/Value' for legacy _Root/* instances.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `add`, `in_trend`, `label`, `menu`, `quick_history`, `quick_key`, `remove`, `summary`, `units`

### label {#label}

```python
def label(path)
```
Line 136 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Operator pen label: '<Device> <Member>' (e.g. 'CG-E4 Zone Temp', 'Comp 4 Discharge Pressure').
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `add`, `menu`, `quick_history`, `remove`, `summary`

### units {#units}

```python
def units(path)
```
Line 160 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Engineering unit: static UDT engUnit when known, else one cached '.EngUnit' read.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `quick_history`, `summary`

### all\_paths {#all_paths}

```python
def all_paths()
```
Line 181 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Every historized atomic tag the index knows (Trending page tag browser), full paths, sorted.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.tagsTree.getHistoricalTags` | script | |

### \_walk {#_walk}

```python
def _walk(obj, dotted)
```
Line 196 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `_ref`

### \_ref {#_ref}

```python
def _ref(component, ref)
```
Line 212 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `resolve`

### resolve {#resolve}

```python
def resolve(component, template)
```
Line 233 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Substitute {...} property references in a path template; '' when any reference is empty.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `menu`

### \_cfg {#_cfg}

```python
def _cfg(session)
```
Line 255 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `_tags`, `add`, `remove`

### \_tags {#_tags}

```python
def _tags(session)
```
Line 262 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `add`, `in_trend`, `remove`

### in\_trend {#in_trend}

```python
def in_trend(session, path)
```
Line 271 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `menu`, `toggle`

### add {#add}

```python
def add(session, path, name=None)
```
Line 276 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Add a historized tag to the session trend. Returns (ok, message).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `toggle`

### remove {#remove}

```python
def remove(session, path, name=None)
```
Line 299 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Remove a tag (any stored form of it) from the session trend. Returns (ok, message).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `toggle`

### toggle {#toggle}

```python
def toggle(session, path, name=None)
```
Line 326 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/QuickHistory` | view | `root/Header/Trend event component.onActionPerformed` |

### summary {#summary}

```python
def summary(cfg)
```
Line 332 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
session.custom.trend from session.custom.AdhocTrend: {pens: [{tagPath, label, units, color, axis, plot}],
count, key: '|path|path|'} (read-only; written by the session-props binding).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `session-props` | session props | `binding custom.trend` |

### \_num {#_num}

```python
def _num(event, key)
```
Line 357 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `menu`

### \_viewport {#_viewport}

```python
def _viewport(component)
```
Line 368 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `menu`

### menu {#menu}

```python
def menu(component, event, template='', name=None)
```
Line 376 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Right-click handler: open the trend context menu at the cursor (never a write action).
```

<details>
<summary>Called from 126 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Condensers/Utility/Overview` | view | `root/Canvas/OAT/Value event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HND event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HND/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HND/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HOP event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HOP/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/HOP/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LDR event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LDR/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LDR/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LS event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LS/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/LS/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/RSM event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/RSM/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/RSM/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/ST event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/ST/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/ST/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/VD event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/VD/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw/VD/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/HND event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/HND/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/HND/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/LDR event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/LDR/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw/LDR/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/LS event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/LS/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/LS/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/RSM event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/RSM/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/RSM/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/ST event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/ST/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw/ST/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/HOP event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/HOP/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/HOP/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/VD event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/VD/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw/VD/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Handtman` | view | `root/Draw/HND event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Handtman` | view | `root/Draw/HND/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Handtman` | view | `root/Draw/HND/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Hopper` | view | `root/Draw/HOP event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Hopper` | view | `root/Draw/HOP/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Hopper` | view | `root/Draw/HOP/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/LazySusan` | view | `root/Draw/LS event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/LazySusan` | view | `root/Draw/LS/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/LazySusan` | view | `root/Draw/LS/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Loaders` | view | `root/Draw/LDR event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Loaders` | view | `root/Draw/LDR/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/Loaders` | view | `root/Draw/LDR/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/RollStock` | view | `root/Draw/RSM event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/RollStock` | view | `root/Draw/RSM/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/RollStock` | view | `root/Draw/RSM/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | view | `root/Draw/ST event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | view | `root/Draw/ST/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | view | `root/Draw/ST/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/VatDumper` | view | `root/Draw/VD event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/VatDumper` | view | `root/Draw/VD/Rate event dom.onContextMenu` |
| `00_Pages/Groveport/Production/Level3/VatDumper` | view | `root/Draw/VD/RunStatus event dom.onContextMenu` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw/UndFreezer/Value event dom.onContextMenu` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw/UndSuperchill/Value event dom.onContextMenu` |
| `00_Pages/Groveport/Utility/OverviewStatusTile` | view | `root/Status event dom.onContextMenu` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Groups/CoolingSchedule/CoolingLeft/Val event dom.onContextMenu` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Groups/RuntimeSchedule/RuntimeLeft/Val event dom.onContextMenu` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardTemperature/ZoneAirTemp/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/ModesSection/Rung/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/OperatingSection/Amps/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/OperatingSection/DisP/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/OperatingSection/Fla/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/OperatingSection/Runtime/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root/OperatingSection/Svp/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` | view | `root/KpiSection/Runtime/RuntimeVal event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` | view | `root/KpiSection/Starts/StartsVal event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root/Columns/Left/PressureSection/Actual/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root/Columns/Middle/SensorSection/Level/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root/Columns/Middle/SensorSection/Pressure/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DefrostSection/CoolingLeft/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DefrostSection/Runtime/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DefrostSection/TimeLeft/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveBleedSV/State event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveHotGasSV/State event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveLiquidSV/State event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveSuctionSV/State event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/TempSection/Zat/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` | view | `root/StatusSection/StatusChips/FaultCode/State event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/KpiSection/Runtime/RuntimeVal event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/KpiSection/Starts/StartsVal event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/StatusSection/StatusBanner event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Left/AinMaint/Raw/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/Comm event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/Gauge/Limits/PV/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | view | `root/Columns/Left/PressureSection/Actual/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | view | `root/Columns/Left/PressureSection/Start/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | view | `root/Columns/Left/PressureSection/Stop/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | view | `root/Columns/Left/PressureSection/Target/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Left/AinMaint/Raw/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/AinHome/Comm event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/AinHome/Gauge/Limits/PV/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Level/Mode/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Level/PV/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pressures/Kpis/PumpsPressure/Value/Val event dom.onContextMenu` |
| `01_Popups/00_Faceplates/_Assets/Valve/Controls` | view | `root/StatusSection/StatusBanner event dom.onContextMenu` |
| `02_Components/01_Devices/Compressor` | view | `root/BottomStrip/RightCol/FLARow/FLAEU event dom.onContextMenu` |
| `02_Components/01_Devices/Compressor` | view | `root/BottomStrip/RightCol/FLARow/FLAValue event dom.onContextMenu` |
| `02_Components/01_Devices/Compressor` | view | `root/BottomStrip/RightCol/SVPRow/SVPEU event dom.onContextMenu` |
| `02_Components/01_Devices/Compressor` | view | `root/BottomStrip/RightCol/SVPRow/SVPValue event dom.onContextMenu` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan1/FanStatus event dom.onContextMenu` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan2/FanStatus event dom.onContextMenu` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan3/FanStatus event dom.onContextMenu` |
| `02_Components/03_PLC/PointRow` | view | `root event dom.onContextMenu` |
| `03_Elements/00_Control/AnalogInput` | view | `root/EU event dom.onContextMenu` |
| `03_Elements/00_Control/AnalogInput` | view | `root/Value event dom.onContextMenu` |
| `03_Elements/00_Control/TimeInput` | view | `root/Value event dom.onContextMenu` |
| `03_Elements/00_Control/_Assets/Numeric` | view | `root/EngineeringUnit event dom.onContextMenu` |
| `03_Elements/00_Control/_Assets/Numeric` | view | `root/Value event dom.onContextMenu` |
| `03_Elements/01_Status/_Assets/Numeric` | view | `root event dom.onContextMenu` |
| `03_Elements/01_Status/_Assets/Numeric` | view | `root/Value event dom.onContextMenu` |
| `03_Elements/03_Table/Boolean` | view | `root event dom.onContextMenu` |
| `03_Elements/03_Table/DisplayTrend` | view | `root event dom.onContextMenu` |
| `03_Elements/03_Table/Numeric` | view | `root event dom.onContextMenu` |
| `03_Elements/03_Table/StateText` | view | `root event dom.onContextMenu` |
</details>

### close\_menu {#close_menu}

```python
def close_menu()
```
Line 412 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/Menu` | view | `root event dom.onKeyDown` |

Used inside the module by: `menu_action`

### menu\_action {#menu_action}

```python
def menu_action(component, action)
```
Line 419 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Menu row click (01_Popups/TrendContext/Menu). action: add | remove | open | quick | copy | ticket.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/Menu` | view | `root/AddToTrend event dom.onClick` |
| `01_Popups/TrendContext/Menu` | view | `root/CopyTagPath event dom.onClick` |
| `01_Popups/TrendContext/Menu` | view | `root/OpenTrend event dom.onClick` |
| `01_Popups/TrendContext/Menu` | view | `root/QuickHistory event dom.onClick` |
| `01_Popups/TrendContext/Menu` | view | `root/RemoveFromTrend event dom.onClick` |
| `01_Popups/TrendContext/Menu` | view | `root/TicketLogger event dom.onClick` |

### open\_trend {#open_trend}

```python
def open_trend()
```
Line 442 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/QuickHistory` | view | `root/Header/OpenTrend event component.onActionPerformed` |
| `01_Popups/TrendContext/Toast` | view | `root/Open event dom.onClick` |

Used inside the module by: `menu_action`

### quick\_history {#quick_history}

```python
def quick_history(path, name=None, hours=8)
```
Line 446 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `menu_action`

### copy\_path {#copy_path}

```python
def copy_path(path)
```
Line 454 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `menu_action`

### toast {#toast}

```python
def toast(text, kind='ok')
```
Line 460 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/QuickHistory` | view | `root/Header/Trend event component.onActionPerformed` |

Used inside the module by: `menu_action`

### copy\_markdown {#copy_markdown}

```python
def copy_markdown(path)
```
Line 467 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Markdown source for the CopyPath popup: a Copy button + one automatic copy attempt (client JS).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/CopyPath` | view | `root/Actions/Copy binding props.source` |

### quick\_key {#quick_key}

```python
def quick_key(path, aggregate='Average')
```
Line 482 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### quick\_series {#quick_series}

```python
def quick_series(dataset, name, color=None)
```
Line 489 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Single-pen ApexCharts series from a Wide history dataset (t_stamp + 'pen').
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/TrendContext/QuickHistory` | view | `root/Chart binding props.series` |

### is\_tall {#is_tall}

```python
def is_tall(dataset)
```
Line 505 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Tall history dataset (path, value, quality, timestamp): the only format that carries quality.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `points`

### columns {#columns}

```python
def columns(dataset)
```
Line 513 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Pen columns: Wide = the column names; Tall = 't_stamp' + the distinct path / alias values.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChart binding props.series` |

Used inside the module by: `quick_series`

### \_good {#_good}

```python
def _good(q)
```
Line 530 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Quality code from a Tall row: bad / error codes are negative (Good = 192, Uncertain kept).
```

Used inside the module by: `points`

### points {#points}

```python
def points(dataset, col)
```
Line 541 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
[[epochMs, value|None], ...] for one pen. The historian returns 0.0 for windows with bad quality (comm loss)
or no data (before the first sample), so Tall rows with a bad quality become None: ApexCharts leaves a gap
instead of drawing a false zero. Wide datasets carry no quality: only real nulls / NaN become gaps.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChart binding props.series` |

Used inside the module by: `quick_series`

### \_ev {#_ev}

```python
def _ev(obj, key)
```
Line 582 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `chart_zoomed`

### \_ms {#_ms}

```python
def _ms(v)
```
Line 593 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

_No docstring._

Used inside the module by: `chart_zoomed`

### chart\_zoomed {#chart_zoomed}

```python
def chart_zoomed(view, event, pause=False, chart=None)
```
Line 606 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
zoomedHandler / scrolledHandler: remember the window (and pause a live Quick History). Zoom Area: kyvis passes
no yaxis and any options update re-applies the yaxis config, so the chart binds its x options to the values they
had (zoomHoldMin / Max) and ApexCharts keeps the box.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChart event component.scrolledHandler` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChart event component.zoomedHandler` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChartPan event component.scrolledHandler` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChartPan event component.zoomedHandler` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/Chart event component.scrolledHandler` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/Chart event component.zoomedHandler` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/ChartPan event component.scrolledHandler` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/ChartPan event component.zoomedHandler` |

### chart\_reset {#chart_reset}

```python
def chart_reset(view, names)
```
Line 630 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py`.

```text
Reset Zoom / the zoomed chip / double-click: full range again on the chart(s) named (root children).
```

<details>
<summary>Called from 9 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChart event dom.onDoubleClick` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/AnalogChartPan event dom.onDoubleClick` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/ChartTools/Row/ResetZoom event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root/ChartTools/Row/ZoomChip event dom.onClick` |
| `01_Popups/TrendContext/QuickHistory` | view | `binding custom.live` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/Chart event dom.onDoubleClick` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/ChartPan event dom.onDoubleClick` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/ChartTools/Row/ResetZoom event component.onActionPerformed` |
| `01_Popups/TrendContext/QuickHistory` | view | `root/ChartTools/Row/ZoomChip event dom.onClick` |
</details>
