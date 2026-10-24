---
title: Enums (Code To Text)
sidebar_label: Enums
sidebar_position: 7
description: The _Config/Enums DataSet tags that turn PLC mode and state codes into words, how expressions and shared.Enums read them, and how to add one.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/Enums/**/tags.json
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py
last_verified: 2026-10-23
---

# Enums (Code To Text)

PLC members often hold a code (`Cfg_DefrostStartMode = 2`) where the operator wants a word ("Runtime"). Those words
live in **one place**: a memory **DataSet** tag per enum under `[default]_Config/Enums/<Group>/<Name>`. Expressions
read them with `lookup()`, scripts with `shared.Enums`. Do not add another hard-coded `case()` copy of a code list.

The tag folder `_Config/Enums` is tracked in git.

## Columns

| Column | Type | Meaning |
|---|---|---|
| `value` | Int4 | the code |
| `label` | String | the full word (dropdowns, confirm dialog, audit) |
| `short` | String | short caption (CG page segment buttons) |
| `selectable` | Boolean | false = listed but disabled in a dropdown (a PLC-only mode still shows its name) |
| extras | | optional, per enum (for example `hmiStatus`) |

## The Enums

### `Evaporator/DefrostStartMode`

PLC `CG_RL_Evap.Cfg_DefrostStartMode` (L5K: 0 TOD, 1 Liquid Time, 2 Run Time, 3 DI Initiate, 4 AI Initiate; FT
offers 0-2).

| value | label | short | selectable |
|---|---|---|---|
| 0 | Time Of Day | ToD | yes |
| 1 | Cooling Time | Cooling | yes |
| 2 | Runtime | Runtime | yes |
| 3 | Digital Input | DI | no |
| 4 | Analog Input | AI | no |

### `Evaporator/CycleFans`

PLC `CG_RL_Evap.Cfg_CycFans`, "Cycle Fans Mode for When the Unit is in Idle" (faceplate label **Idle Fan Mode**).

| value | label | short | selectable |
|---|---|---|---|
| 0 | Fans Off | Off | yes |
| 1 | Cycle Fans | Cycle | yes |
| 2 | Fans On | On | yes |

### `Evaporator/PlcState`

PLC `CG_RL_Evap.Sts_State` (the control-group phase, L5K wording) with the extra column `hmiStatus` = the
`Devices/Evaporator` HMI status code (the same map as the `HmiStatus` member). Status only: nothing writes it.

| value | label | short | hmiStatus |
|---|---|---|---|
| 0 | Off | Off | 0 |
| 1 | Pump Out | Pump Out | 6 |
| 2 | Soft Hot Gas | Soft HG | 7 |
| 3 | Main Hot Gas | Main HG | 7 |
| 4 | Bleed | Bleed | 8 |
| 5 | Fan Delay | Fan Delay | 9 |
| 6 | Cooling | Cooling | 1 |
| 7 | Idle | Idle | 5 |
| 8 | Cleanup | Cleanup | 2 |
| 9 | Permissive | Permissive | 5 |
| 10 | Interlock | Interlock | 3 |

`Cfg_DefrostStopMode` (PLC 0 None / 1 DI Stop / 2 AI Stop) has no enum yet (it is not on FT or the HMI).

The rows above are the values at the time of writing; the live tag values are in the gateway (memory DataSets are not stored in the
tag JSON files, see [Tags](index.md#where-tags-are-stored)).

## How They Are Read

**In an expression** (code first converted with `toInt()`; unknown codes show as themselves, a bad tag as a dash):

```text
lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt({view.custom.code}), toStr({view.custom.code}), 'value', 'label')
```

**In a script**: `shared.Enums` (project library, every function fail-safe: on any error it returns the raw value):

| Function | Returns |
|---|---|
| `rows(enumPath, dataset=None)` | the rows as dicts (`value`, `label`, `short`, `selectable`, extras) |
| `label(enumPath, value, default=None)` / `short(...)` | the word for a code |
| `options(enumPath, current=None, dataset=None)` | dropdown options (non-selectable rows disabled, the current value kept) |
| `forTagPath(tagPath)` | the enum of a member, from `shared.Enums.MEMBERS` (`Cfg_DefrostStartMode`, `Cfg_CycFans`) |
| `describe(tagPath, value, enumPath=None)` | "Time Of Day (0)" for confirm dialogs and the OpsAudit text |

`enumPath` is relative to `[default]_Config/Enums/` (for example `Evaporator/CycleFans`) or a full tag path.

**Where the words show:**

- Faceplate Configuration (`_Assets/Evaporator/Configuration`): ConfigSection rows carry `"enum"`, passed as
  `params.enumPath` to `ConfigField` and `MultiStateInput` (a pick opens `shared.Alerts.confirmApplyWrite`; while the
  [PLC Write Lock](plc-write-lock.md) is on the write is refused).
- Faceplate Controls: the Defrost Mode and Idle Fan Mode KPIs (`lookup()` as above).
- CG page panel (`00_Pages/Groveport/_Shared/CG/AhuEvapPanel`): segment captions from `short`; a read-only
  "Current Mode: ..." label while the mode is not selectable.
- Confirm dialog and OpsAudit: `describe()` -> `Time Of Day (0) -> Runtime (2)`.

## How To Add An Enum

1. Tag Browser > right-click `_Config/Enums/<Group>` > **New Tag > Memory Tag**, data type **DataSet**, then edit its
   value: columns `value` (Int4), `label`, `short`, `selectable` (Boolean), and any extras, one row per code.
2. For a member that should get words in the confirm dialog / audit, add it to `shared.Enums.MEMBERS` (Project
   Library > `shared` > `Enums`).
3. In a ConfigSection row add `"enum": "<Group>/<Name>"`; in an expression use `lookup()`.
4. Only use codes the PLC really has (check the L5K / L5X type), and Title Case labels.
5. Save and test the faceplate Configuration tab.

