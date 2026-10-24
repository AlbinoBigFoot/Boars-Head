---
title: "PLC/CONTROL"
sidebar_label: "CONTROL"
description: "UDT definition PLC/CONTROL"
generated: true
---

:::note

:::
# UDT `PLC/CONTROL`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; CONTROL |
| Tag path | `[default]_types_/PLC/CONTROL` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 10 (10 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Built-in Control` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

10 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `DN` | Boolean | OPC `{TagPrefix}.DN` | | yes | | | | |
| `EM` | Boolean | OPC `{TagPrefix}.EM` | | yes | | | | |
| `EN` | Boolean | OPC `{TagPrefix}.EN` | | yes | | | | |
| `ER` | Boolean | OPC `{TagPrefix}.ER` | | yes | | | | |
| `EU` | Boolean | OPC `{TagPrefix}.EU` | | yes | | | | |
| `FD` | Boolean | OPC `{TagPrefix}.FD` | | yes | | | | |
| `IN` | Boolean | OPC `{TagPrefix}.IN` | | yes | | | | |
| `LEN` | Int4 | OPC `{TagPrefix}.LEN` | | yes | | | | |
| `POS` | Int4 | OPC `{TagPrefix}.POS` | | yes | | | | |
| `UL` | Boolean | OPC `{TagPrefix}.UL` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/Control\_Group\_DIO](control-group-dio.md) (as `Status`)

