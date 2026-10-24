---
title: "shared.PlcRack"
sidebar_label: "shared.PlcRack"
description: "Script module shared.PlcRack: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcRack/code.py`  
**Lines:** 36. **Functions:** 1. **Called as:** `shared.PlcRack.<function>(...)`

## What the source says

```text
PLC Rack / IO helpers. UI only: nothing here
reads or writes a PLC value.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.perspective` |

<details>
<summary>Module constants (4)</summary>

| Name | Value |
|---|---|
| `POPUP_VIEW` | `'01_Popups/00_Faceplates/PlcRack/CardDetail'` |
| `WIDTH` | `900` |
| `HEIGHT` | `{'AI': 238, 'CTRL': 336}` |
| `DEFAULT_HEIGHT` | `334` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`openCard`](#opencard) | Pop one rack card (or the controller) out as its own faceplate. The popup id is per card, so several cards can be | 1 |

### openCard {#opencard}

```python
def openCard(sitePath, member, slot=0, kind='', title='', viewportW=0, viewportH=0)
```
Line 9 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcRack/code.py`.

```text
Pop one rack card (or the controller) out as its own faceplate. The popup id is per card, so several cards can be
open side by side; each opens bottom-centred (over the detail panel, never over the rack) at a staggered offset,
draggable and resizable, and is clamped on screen.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `02_Components/03_PLC/ModuleDetail` | view | `root/Header/PopOut event component.onActionPerformed` |
