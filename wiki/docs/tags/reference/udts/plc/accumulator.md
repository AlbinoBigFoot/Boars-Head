---
title: "PLC/Accumulator"
sidebar_label: "Accumulator"
description: "UDT definition PLC/Accumulator"
generated: true
---

:::note

:::
# UDT `PLC/Accumulator`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Accumulator |
| Tag path | `[default]_types_/PLC/Accumulator` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 5 (1 atomic, 4 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

1 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Structure

```mermaid
flowchart LR
  n0["PLC/Accumulator"]
  style n0 stroke-width:3px
  n0 -- "CV" --> n1["PLC/P_PIDE"]
  n0 -- "HLCO" --> n2["PLC/P_DIn"]
  n0 -- "LT" --> n3["PLC/P_AIn"]
  n0 -- "SV" --> n4["PLC/P_ValveSO"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `CV` | UDT | nested [PLC/P\_PIDE](p-pide.md) | | | | | | |
| `HLCO` | UDT | nested [PLC/P\_DIn](p-din.md) | | | | | | |
| `LT` | UDT | nested [PLC/P\_AIn](p-ain.md) | | | | | | |
| `Level_SP` | Float4 | OPC `{TagPrefix}.Level_SP` | | yes | | | | |
| `SV` | UDT | nested [PLC/P\_ValveSO](p-valveso.md) | | | | | | |

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `CV` | [PLC/P\_PIDE](p-pide.md) | `TagPrefix = {TagPrefix}.CV; Description = {Description}; DeviceName = {DeviceName}` | enabled |
| `HLCO` | [PLC/P\_DIn](p-din.md) | `TagPrefix = {TagPrefix}.HLCO; Description = {Description}; DeviceName = {DeviceName}` | enabled |
| `LT` | [PLC/P\_AIn](p-ain.md) | `TagPrefix = {TagPrefix}.LT; Description = {Description}; DeviceName = {DeviceName}` | enabled |
| `SV` | [PLC/P\_ValveSO](p-valveso.md) | `TagPrefix = {TagPrefix}.SV; Description = {Description}; DeviceName = {DeviceName}` | enabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
