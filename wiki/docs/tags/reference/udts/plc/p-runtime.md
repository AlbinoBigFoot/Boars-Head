---
title: "PLC/P_RunTime"
sidebar_label: "P_RunTime"
description: "UDT definition PLC/P_RunTime: PlantPAx P_RunTime (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_RunTime`

PlantPAx P\_RunTime (read only)

Standard PlantPAx P\_RunTime: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_RunTime |
| Tag path | `[default]_types_/PLC/P_RunTime` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 11 (11 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

11 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | 1=Clear Program Commands on receipt$N0=Leave Set |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `MCmd_ClearMaxHrs` | Boolean | OPC `{TagPrefix}.MCmd_ClearMaxHrs` | PAX\_Faceplate | yes | | | | Maintenance Command to Clear Maximum (continuous) Run Time for any start |
| `MCmd_ClearStarts` | Boolean | OPC `{TagPrefix}.MCmd_ClearStarts` | PAX\_Faceplate | yes | | | | Maintenance Command to Clear Count of Starts (attempts) |
| `MCmd_ClearTotHrs` | Boolean | OPC `{TagPrefix}.MCmd_ClearTotHrs` | PAX\_Faceplate | yes | | | | Maintenance Command to Clear Total Running Time |
| `Val_CurRunHrs` | Float4 | OPC `{TagPrefix}.Val_CurRunHrs` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | | | Current running time this start (hours) |
| `Val_MaxRunHrs` | Float4 | OPC `{TagPrefix}.Val_MaxRunHrs` | PAX\_Faceplate | yes | | | | Maximum continuous running time for a given start (hours) |
| `Val_Starts` | Int4 | OPC `{TagPrefix}.Val_Starts` | PAX\_Status | yes | historian, OnChange, db 0.0 Absolute (Discrete) | fmt #0 | | Total number of motor starts or attempts |
| `Val_TotRunHrs` | Float4 | OPC `{TagPrefix}.Val_TotRunHrs` | PAX\_Status | yes | historian, OnChange, db 0.01 Absolute (Analog) | h fmt #0.0 | | Total accumulated running time (hours) |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Pump](../devices/pump.md) (as `RunTime`), [Devices/Evaporator](../devices/evaporator.md) (as `FansRunTime`)

Reached through nesting by 30 top-level instance(s).
