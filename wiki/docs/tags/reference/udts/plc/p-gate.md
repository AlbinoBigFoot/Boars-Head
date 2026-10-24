---
title: "PLC/P_Gate"
sidebar_label: "P_Gate"
description: "UDT definition PLC/P_Gate"
generated: true
---

:::note

:::
# UDT `PLC/P_Gate`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_Gate |
| Tag path | `[default]_types_/PLC/P_Gate` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 12 (12 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

12 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_GateDly` | Int4 | OPC `{TagPrefix}.Cfg_GateDly` | | yes | | | | Gate Delay (s): time after Gate Input true to enable On/Off Delay |
| `Cfg_OffDly` | Int4 | OPC `{TagPrefix}.Cfg_OffDly` | | yes | | | | Off Delay (s): Time after Inp or Gate goes to 0 for Out to go to 0 |
| `Cfg_OnDly` | Int4 | OPC `{TagPrefix}.Cfg_OnDly` | | yes | | | | On Delay (s): If Gate Delay done, time Inp must be true to set Out true |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | | yes | | | | 1=Error in Config: On Delay, Off Delay, Gate Delay Time Invalid (use 0 to 2147483 s) |
| `Inp` | Boolean | OPC `{TagPrefix}.Inp` | | yes | | | | Input Condition: e.g., result of comparison |
| `Inp_Gate` | Boolean | OPC `{TagPrefix}.Inp_Gate` | | yes | | | | Gate Input: 1=enable On Delay / Off Delay after Gate Delay, 0=disable |
| `Out` | Boolean | OPC `{TagPrefix}.Out` | | yes | | | | Output after On Delay, Off Delay, enabled by Gate |
| `P_Gate` | Boolean | OPC `{TagPrefix}.P_Gate` | | yes | | | | Unique Parameter Name for auto - discovery |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | | yes | | | | 1=Error in Config (see detail Err\_ bits for reason), display icon |
| `Sts_Gate` | Boolean | OPC `{TagPrefix}.Sts_Gate` | | yes | | | | 1=Gate Delay done, Output is enabled |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
