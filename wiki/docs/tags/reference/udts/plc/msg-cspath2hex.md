---
title: "PLC/MSG_CSPath2Hex"
sidebar_label: "MSG_CSPath2Hex"
description: "UDT definition PLC/MSG_CSPath2Hex"
generated: true
---

:::note

:::
# UDT `PLC/MSG_CSPath2Hex`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; MSG\_CSPath2Hex |
| Tag path | `[default]_types_/PLC/MSG_CSPath2Hex` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 4 (4 atomic, 0 nested UDT, 0 folders) |
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

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `ERR` | Boolean | OPC `{TagPrefix}.ERR` | | yes | | | | |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | |
| `ErrorCode` | Int4 | OPC `{TagPrefix}.ErrorCode` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
