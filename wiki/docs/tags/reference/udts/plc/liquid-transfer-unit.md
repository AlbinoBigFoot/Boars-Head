---
title: "PLC/Liquid_Transfer_Unit"
sidebar_label: "Liquid_Transfer_Unit"
description: "UDT definition PLC/Liquid_Transfer_Unit"
generated: true
---

:::note

:::
# UDT `PLC/Liquid_Transfer_Unit`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Liquid\_Transfer\_Unit |
| Tag path | `[default]_types_/PLC/Liquid_Transfer_Unit` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 7 (4 atomic, 3 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

4 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Structure

```mermaid
flowchart LR
  n0["PLC/Liquid_Transfer_Unit"]
  style n0 stroke-width:3px
  n0 -- "COUNT" --> n1["PLC/COUNTER"]
  n0 -- "Count_Alarm" --> n2["PLC/P_Alarm"]
  n0 -- "LTU_Input" --> n3["PLC/P_DIn"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `COUNT` | UDT | nested [PLC/COUNTER](counter.md) | | | | | | |
| `Count_Alarm` | UDT | nested [PLC/P\_Alarm](p-alarm.md) | | | | | | |
| `Count_Alarm_SP` | Float4 | OPC `{TagPrefix}.Count_Alarm_SP` | | yes | | | | |
| `LTU_Input` | UDT | nested [PLC/P\_DIn](p-din.md) | | | | | | |
| `ResetDaily` | Boolean | OPC `{TagPrefix}.ResetDaily` | | yes | | | | |
| `ResetTime` | Int2 | OPC `{TagPrefix}.ResetTime` | | yes | | | | |
| `ZZZZZZZZZZLTU3` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZLTU3` | | yes | | | | |

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `COUNT` | [PLC/COUNTER](counter.md) | `TagPrefix = {TagPrefix}.COUNT; Description = {Description}; DeviceName = {DeviceName}` | enabled |
| `Count_Alarm` | [PLC/P\_Alarm](p-alarm.md) | `TagPrefix = {TagPrefix}.Count_Alarm; Description = {Description}; DeviceName = {DeviceName}` | enabled |
| `LTU_Input` | [PLC/P\_DIn](p-din.md) | `TagPrefix = {TagPrefix}.LTU_Input; Description = {Description}; DeviceName = {DeviceName}` | enabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
