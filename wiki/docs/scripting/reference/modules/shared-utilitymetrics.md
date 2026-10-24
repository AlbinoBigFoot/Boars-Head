---
title: "shared.UtilityMetrics"
sidebar_label: "shared.UtilityMetrics"
description: "Script module shared.UtilityMetrics: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`  
**Lines:** 320. **Functions:** 13. **Called as:** `shared.UtilityMetrics.<function>(...)`

## What the source says

```text
Utility Overview (OverviewKpis) metrics from the REAL plant data only: live reads for status / counts,
historian for the averages and dwell hours. No history for a CG / range -> None / 0 (the view shows No Data).

zone temp   : CG ZAT/Val (P_AIn, historized)  -> time-weighted average of the raw samples (Good time only)
dwell hours : CG CG/Sts_State (historized from 2026-10-24) -> raw samples, hours held per state (Good only)
History is cached in the gateway (system.util.getGlobals) for CACHE_MS: ONE batched queryTagHistory per refresh,
shared by every client. Live values are a single readBlocking per call.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.tag`, `system.util` |
| Logger names | `UtilityMetrics` |

<details>
<summary>Module constants (9)</summary>

| Name | Value |
|---|---|
| `SECTIONS` | `[('Freezer', ['A1', 'A2']), ('SuperChill', ['B1', 'B2']),...` |
| `STATUS_KEYS` | `['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']` |
| `DWELL_KEYS` | `['CLG', 'DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD', '...` |
| `MAIN_KEYS` | `['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']` |
| `DFT_KEYS` | `['DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD']` |
| `CACHE_MS` | `180000` |
| `STATE_TO_HMI` | `{0: 0, 1: 6, 2: 7, 3: 7, 4: 8, 5: 9, 6: 1, 7: 5, 8: 2, 9:...` |
| `HMI_TO_DWELL` | `{0: 'STOP', 1: 'CLG', 2: 'DFT', 3: 'FLT', 5: 'IDLE', 6: '...` |
| `HMI_NAMES` | `{0: 'Off', 1: 'Cooling', 2: 'Defrost', 3: 'Fault', 5: 'Id...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_base`](#_base) (internal) | | 0 |
| [`_coarse`](#_coarse) (internal) | | 0 |
| [`_k`](#_k) (internal) | Dataset paths come back without the [provider] prefix. | 0 |
| [`_is_good`](#_is_good) (internal) | | 0 |
| [`_raw`](#_raw) (internal) | ONE queryTagHistory for every path (temps + states): path -&gt; [(ms, value, good)] sorted by time. A path with | 0 |
| [`_avg_temp`](#_avg_temp) (internal) | Time-weighted average of the zone temp over the time it has Good samples (linear between neighbouring Good | 0 |
| [`_dwell_hours`](#_dwell_hours) (internal) | \{dwell key: hours\} the CG held each state (Good samples only); None = no Good state history in the range. | 0 |
| [`_history`](#_history) (internal) | Cached historian block for the last `hours` hours: \{'temp': \{path: avg\}, 'dwell': \{path: hrs\}\}. | 0 |
| [`get`](#get) | | 1 |
| [`_segments`](#_segments) (internal) | [(hmi\_code, start\_ms, end\_ms)] of Good Sts\_State samples, consecutive equal HMI codes merged. | 0 |
| [`_clock`](#_clock) (internal) | | 0 |
| [`_dur`](#_dur) (internal) | | 0 |
| [`cg`](#cg) | CG History view payload (AhuEvapHistory): REAL historian data of ONE CG, cached 3 minutes per CG. | 1 |

### \_base {#_base}

```python
def _base(area, short)
```
Line 22 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

Used inside the module by: `_history`, `get`

### \_coarse {#_coarse}

```python
def _coarse(h)
```
Line 26 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

Used inside the module by: `get`

### \_k {#_k}

```python
def _k(path)
```
Line 40 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
Dataset paths come back without the [provider] prefix.
```

Used inside the module by: `_history`, `_raw`, `cg`

### \_is\_good {#_is_good}

```python
def _is_good(q)
```
Line 46 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

Used inside the module by: `_raw`

### \_raw {#_raw}

```python
def _raw(paths, start, end)
```
Line 53 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
ONE queryTagHistory for every path (temps + states): path -> [(ms, value, good)] sorted by time. A path with
no rows has no history. Bounding values give the value in force at the start of the range.
```

Used inside the module by: `_history`, `cg`

### \_avg\_temp {#_avg_temp}

```python
def _avg_temp(pts, s_ms, e_ms)
```
Line 71 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
Time-weighted average of the zone temp over the time it has Good samples (linear between neighbouring Good
samples, the last Good sample held to the end of the range). Gaps (link outage, bad quality) are not counted.
None = no Good data in the range.
```

Used inside the module by: `_history`

### \_dwell\_hours {#_dwell_hours}

```python
def _dwell_hours(pts, s_ms, e_ms)
```
Line 97 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
{dwell key: hours} the CG held each state (Good samples only); None = no Good state history in the range.
```

Used inside the module by: `_history`, `cg`

### \_history {#_history}

```python
def _history(hours)
```
Line 116 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
Cached historian block for the last `hours` hours: {'temp': {path: avg}, 'dwell': {path: hrs}}.
```

Used inside the module by: `get`

### get {#get}

```python
def get(hours=24)
```
Line 149 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Utility/OverviewKpis` | view | `binding custom.metrics` |

### \_segments {#_segments}

```python
def _segments(pts, s_ms, e_ms)
```
Line 230 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
[(hmi_code, start_ms, end_ms)] of Good Sts_State samples, consecutive equal HMI codes merged.
```

Used inside the module by: `cg`

### \_clock {#_clock}

```python
def _clock(ms)
```
Line 250 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

Used inside the module by: `cg`

### \_dur {#_dur}

```python
def _dur(ms)
```
Line 254 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

_No docstring._

Used inside the module by: `cg`

### cg {#cg}

```python
def cg(tagPath, hours=12)
```
Line 269 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UtilityMetrics/code.py`.

```text
CG History view payload (AhuEvapHistory): REAL historian data of ONE CG, cached 3 minutes per CG.
series = Good ZAT/Val samples averaged into <= 90 time buckets (empty bucket = no point); status hours / rows =
Good CG/Sts_State samples. No history -> empty series / zero hours / no rows (the view shows No Data).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/_Shared/CG/AhuEvapHistory` | view | `binding custom.payload` |
