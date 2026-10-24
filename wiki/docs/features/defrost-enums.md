---
title: Defrost Enums
sidebar_position: 15
description: Code-to-text enums for evaporator modes (Defrost Start Mode, Idle Fan Mode, PLC state) - the DataSet tags, lookup() in expressions, shared.Enums in scripts, and how to add an enum.
sources:
  - docs/evaporator-hmi-components.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/Enums/**/*.json
last_verified: 2026-10-23
---

# Defrost Enums

## What it does

PLCs store modes as numbers (`Cfg_DefrostStartMode = 2`). Operators need words ("Runtime"). The HMI keeps every
code-to-text list in **one place**: a memory **DataSet tag** per enum under `[default]_Config/Enums/<Group>/<Name>`.
Every screen, the confirm dialog and the audit log read the same list, so the words never disagree.

| Member (CG UDT / PLC) | Enum tag | Values (HMI label, short) |
|---|---|---|
| `Cfg_DefrostStartMode` | `Evaporator/DefrostStartMode` | 0 Time Of Day (ToD), 1 Cooling Time (Cooling), 2 Runtime (Runtime), 3 Digital Input (DI), 4 Analog Input (AI); 3 and 4 are display only (`selectable` false) |
| `Cfg_CycFans` | `Evaporator/CycleFans` | 0 Fans Off (Off), 1 Cycle Fans (Cycle), 2 Fans On (On); faceplate label **Idle Fan Mode** |
| `Sts_State` | `Evaporator/PlcState` | PLC state words 0 Off ... 10 Interlock, plus an `hmiStatus` column (the device Status code); status only |

Columns of every enum tag: `value` (Int4), `label`, `short`, `selectable` (Boolean), plus optional extras.

## Where the words show

- **Faceplate Configuration** (`_Assets/Evaporator/Configuration`): the row's `"enum"` key -> ConfigField
  `params.enumPath` -> `MultiStateInput` `params.enumPath`. The dropdown lists every row; non-selectable rows are
  listed but disabled, so a PLC-only mode still shows its name.
- **Faceplate Controls**: Defrost Mode / Idle Fan Mode KPIs with an expression:
  `lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(code), toStr(code), 'value', 'label')` (an unknown
  code shows as itself, a bad tag as a dash).
- **CG page panel** (`00_Pages/Groveport/_Shared/CG/AhuEvapPanel`): segment captions from `short`; a read-only
  "Current Mode: ..." label while the mode is not selectable.
- **Confirm dialog and OpsAudit**: `shared.Enums.describe(tagPath, value)` -> `Time Of Day (0) -> Runtime (2)` in
  `shared.Alerts.confirmApplyWrite` and `shared.Audit.writeTag`; anything else keeps raw values.

`MultiStateInput` never writes directly: a pick snaps the dropdown back and opens the confirm; Apply writes through
`shared.Audit.writeTag` (permission + PLC lock + audit), Cancel writes nothing.

## How To Change It

**Edit the words of an existing enum:** Tag Browser > `[default]_Config/Enums/<Group>/<Name>` > open the tag editor >
click the **Value** dataset editor and change the `label` / `short` text. Everything that shows the words updates.

**Add an enum:**
1. Tag Browser > right-click `_Config/Enums/<Group>` > **New Tag > Memory Tag**, data type **DataSet**, name it.
2. Edit its value: columns `value` (Int4), `label` (String), `short` (String), `selectable` (Boolean), one row per
   code.
3. For words in the confirm dialog and audit log, add the member name to `shared.Enums.MEMBERS`
   (`"Cfg_X": "<Group>/<Name>"`) in the script module (Project Library > `shared` > `Enums`).
4. In a faceplate ConfigSection row add `"enum": "<Group>/<Name>"` (the faceplate view's configuration list).
5. In expressions use `lookup()`: `toInt()` the code first (UDT members are Float4, PLC members Int2).
6. **Do not add another hard-coded `case()`** copy of the words anywhere.
7. Save, then test in a session: open the faceplate Configuration tab and the confirm dialog.

## Known limitations

- `Cfg_DefrostStopMode` (PLC 0 None / 1 DI Stop / 2 AI Stop) is not on FT or the UDT and has no enum yet.
- The enum tags are memory tags, so their values are edited live in the Tag Browser.
