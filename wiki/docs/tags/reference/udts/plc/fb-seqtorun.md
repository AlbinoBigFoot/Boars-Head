---
title: "PLC/FB_SeqToRun"
sidebar_label: "FB_SeqToRun"
description: "UDT definition PLC/FB_SeqToRun"
generated: true
---

:::note

:::
# UDT `PLC/FB_SeqToRun`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; FB\_SeqToRun |
| Tag path | `[default]_types_/PLC/FB_SeqToRun` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 10 (10 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

10 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `In_Available` | Boolean | OPC `{TagPrefix}.In_Available` | | yes | | | | |
| `In_NumToRun` | Int4 | OPC `{TagPrefix}.In_NumToRun` | | yes | | | | |
| `In_SeqNumber` | Int4 | OPC `{TagPrefix}.In_SeqNumber` | | yes | | | | |
| `In_SeqStarting` | Boolean | OPC `{TagPrefix}.In_SeqStarting` | | yes | | | | |
| `In_SeqStopping` | Boolean | OPC `{TagPrefix}.In_SeqStopping` | | yes | | | | |
| `Out_Decrement` | Boolean | OPC `{TagPrefix}.Out_Decrement` | | yes | | | | |
| `Out_Increment` | Boolean | OPC `{TagPrefix}.Out_Increment` | | yes | | | | |
| `Out_Run` | Boolean | OPC `{TagPrefix}.Out_Run` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
