---
title: "shared.FaceplateTrend"
sidebar_label: "shared.FaceplateTrend"
description: "Script module shared.FaceplateTrend: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/FaceplateTrend/code.py`  
**Lines:** 115. **Functions:** 1. **Called as:** `shared.FaceplateTrend.<function>(...)`

## What the source says

```text
Faceplate Trend tab defaults.

        * defaultPens - pens preselected when a device faceplate's Trend tab opens (mirrors the FT trend displays)
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag` |
| Calls modules | [shared.Pax](./shared-pax.md) |

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`defaultPens`](#defaultpens) | Full tag paths to preselect on the faceplate Trend tab for tagPath ([] = none). | 1 |

### defaultPens {#defaultpens}

```python
def defaultPens(tagPath)
```
Line 8 of `gateways/standard/data/projects/BH/ignition/script-python/shared/FaceplateTrend/code.py`.

```text
Full tag paths to preselect on the faceplate Trend tab for tagPath ([] = none).

Sensors: the PV (Value/Value).
Tanks (FT HTR-SP / LTR-SP "Level And Pump Pressure"): vessel level, plus the recirculator pumps pressure
(Sensors/<H|L>SL-Pumps Pressure) when the tank has pumps (HPR has none).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `binding custom.defaultPens` |
