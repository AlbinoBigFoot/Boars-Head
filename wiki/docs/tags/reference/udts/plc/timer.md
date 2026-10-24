---
title: "PLC/TIMER"
sidebar_label: "TIMER"
description: "UDT definition PLC/TIMER"
generated: true
---

:::note

:::
# UDT `PLC/TIMER`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; TIMER |
| Tag path | `[default]_types_/PLC/TIMER` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 5 (5 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Built-in timer` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

5 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `ACC` | Int4 | OPC `{TagPrefix}.ACC` | | yes | | | | |
| `DN` | Boolean | OPC `{TagPrefix}.DN` | | yes | | | | |
| `EN` | Boolean | OPC `{TagPrefix}.EN` | | yes | | | | |
| `PRE` | Int4 | OPC `{TagPrefix}.PRE` | | yes | | | | |
| `TT` | Boolean | OPC `{TagPrefix}.TT` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/Control\_Group\_DIO](control-group-dio.md) (as `Cycle_Fans_Timer`), [PLC/Control\_Group\_DIO](control-group-dio.md) (as `Defrost_Timer`), [PLC/Control\_Group\_DIO](control-group-dio.md) (as `Reheat_Timer`), [PLC/Control\_Group\_DIO](control-group-dio.md) (as `Runtime_Timer`), [PLC/Ethernet\_Message\_Config](ethernet-message-config.md) (as `TO_Timer`)

