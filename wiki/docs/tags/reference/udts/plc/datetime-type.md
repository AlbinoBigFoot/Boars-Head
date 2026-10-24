---
title: "PLC/DateTime_Type"
sidebar_label: "DateTime_Type"
description: "UDT definition PLC/DateTime_Type"
generated: true
---

:::note

:::
# UDT `PLC/DateTime_Type`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; DateTime\_Type |
| Tag path | `[default]_types_/PLC/DateTime_Type` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 7 (7 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `(text, 92 chars)` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

7 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Day` | Int4 | OPC `{TagPrefix}.Day` | | yes | | | | The day (1 - 31) |
| `Hour` | Int4 | OPC `{TagPrefix}.Hour` | | yes | | | | hour (0 - 23) |
| `Microseconds` | Int4 | OPC `{TagPrefix}.Microseconds` | | yes | | | | (0 - 999,999) |
| `Minute` | Int4 | OPC `{TagPrefix}.Minute` | | yes | | | | minute (0 - 59) |
| `Month` | Int4 | OPC `{TagPrefix}.Month` | | yes | | | | The month (1 - 12) |
| `Second` | Int4 | OPC `{TagPrefix}.Second` | | yes | | | | second (0 - 59) |
| `Year` | Int4 | OPC `{TagPrefix}.Year` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
