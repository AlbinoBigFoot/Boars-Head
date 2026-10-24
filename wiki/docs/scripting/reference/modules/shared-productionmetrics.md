---
title: "shared.ProductionMetrics"
sidebar_label: "shared.ProductionMetrics"
description: "Script module shared.ProductionMetrics: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/ProductionMetrics/code.py`  
**Lines:** 652. **Functions:** 3. **Called as:** `shared.ProductionMetrics.<function>(...)`

## What the source says

```text


copy. value = the metrics expr-struct of the Production views (Level1/Overview, Level2/Kpis, Level3/Kpis):
l1: {sel, day, shift, dtRe, L_*/Z_*/U_* live tag values}; l2: {zone, Z_*, U_*}; l3: {unitId, U_*}.
shared.Reports (custom report builder) calls l1 per day / shift / unit for the Production demo data.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date` |
| Called by modules | [shared.Reports](./shared-reports.md) |

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`l1`](#l1) | | 2 |
| [`l2`](#l2) | | 1 |
| [`l3`](#l3) | | 1 |

### l1 {#l1}

```python
def l1(value)
```
Line 9 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ProductionMetrics/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Production/Level1/Overview` | view | `binding custom.metrics` |
| `shared.Reports._Demo` | script | |

### l2 {#l2}

```python
def l2(value)
```
Line 536 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ProductionMetrics/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Production/Level2/Kpis` | view | `binding custom.metrics` |

### l3 {#l3}

```python
def l3(value)
```
Line 592 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ProductionMetrics/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/Production/Level3/Kpis` | view | `binding custom.metrics` |
