---
title: "PLC/udtFaultRecord"
sidebar_label: "udtFaultRecord"
description: "UDT definition PLC/udtFaultRecord"
generated: true
---

:::note

:::
# UDT `PLC/udtFaultRecord`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; udtFaultRecord |
| Tag path | `[default]_types_/PLC/udtFaultRecord` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 13 (12 atomic, 0 nested UDT, 1 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Lo 32 bits of Fault Timestamp Value` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

12 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Code` | Int2 | OPC `{TagPrefix}.Code` | | yes | | | | Fault Code by Type |
| `Info/` | Folder | | | | | | | |
| `Info/3` | Int4 | OPC `{TagPrefix}.Info[3]` | | yes | | | | Fault Specific Info |
| `Info/4` | Int4 | OPC `{TagPrefix}.Info[4]` | | yes | | | | Fault Specific Info |
| `Info/7` | Int4 | OPC `{TagPrefix}.Info[7]` | | yes | | | | Fault Specific Info |
| `Info/6` | Int4 | OPC `{TagPrefix}.Info[6]` | | yes | | | | Fault Specific Info |
| `Info/2` | Int4 | OPC `{TagPrefix}.Info[2]` | | yes | | | | Fault Specific Info |
| `Info/1` | Int4 | OPC `{TagPrefix}.Info[1]` | | yes | | | | Fault Specific Info |
| `Info/0` | Int4 | OPC `{TagPrefix}.Info[0]` | | yes | | | | Fault Specific Info |
| `Info/5` | Int4 | OPC `{TagPrefix}.Info[5]` | | yes | | | | Fault Specific Info |
| `TimeHigh` | Int4 | OPC `{TagPrefix}.TimeHigh` | | yes | | | | Hi 32 bits of Fault Timestamp Value |
| `TimeLow` | Int4 | OPC `{TagPrefix}.TimeLow` | | yes | | | | Lo 32 bits of Fault Timestamp Value |
| `Type` | Int2 | OPC `{TagPrefix}.Type` | | yes | | | | Fault Type (Program, I/O etc.) |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
