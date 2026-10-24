---
title: "PLC/FB_DuplexAlternator"
sidebar_label: "FB_DuplexAlternator"
description: "UDT definition PLC/FB_DuplexAlternator"
generated: true
---

:::note

:::
# UDT `PLC/FB_DuplexAlternator`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; FB\_DuplexAlternator |
| Tag path | `[default]_types_/PLC/FB_DuplexAlternator` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 17 (17 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

17 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_Lead` | Int2 | OPC `{TagPrefix}.Cfg_Lead` | | yes | | | | HMI Lead Device Setpoint$N 0 = Auto Alternate, &gt; 0 = fixed Lead |
| `Cfg_Runtime` | Float4 | OPC `{TagPrefix}.Cfg_Runtime` | | yes | | | | HMI Aternate runtime setpoint |
| `Cmd_AltMode` | Boolean | OPC `{TagPrefix}.Cmd_AltMode` | | yes | | | | Cmd - Auto Alternation Mode$N0=All Off, 1 = Runtime |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | |
| `Inp_N1Available` | Boolean | OPC `{TagPrefix}.Inp_N1Available` | | yes | | | | Device 1 is available to run in program mode |
| `Inp_N1Running` | Boolean | OPC `{TagPrefix}.Inp_N1Running` | | yes | | | | Device 1 is running |
| `Inp_N1Runtime` | Float4 | OPC `{TagPrefix}.Inp_N1Runtime` | | yes | | | | |
| `Inp_N2Available` | Boolean | OPC `{TagPrefix}.Inp_N2Available` | | yes | | | | Device 2 is available to run in program mode |
| `Inp_N2Running` | Boolean | OPC `{TagPrefix}.Inp_N2Running` | | yes | | | | Device 1 is running |
| `Inp_N2Runtime` | Float4 | OPC `{TagPrefix}.Inp_N2Runtime` | | yes | | | | |
| `Out_LagSelected` | Int2 | OPC `{TagPrefix}.Out_LagSelected` | | yes | | | | Selected Lag Device |
| `Out_LeadSelected` | Int2 | OPC `{TagPrefix}.Out_LeadSelected` | | yes | | | | Selected Lead Device |
| `Out_N1ResetTime` | Boolean | OPC `{TagPrefix}.Out_N1ResetTime` | | yes | | | | |
| `Out_N2ResetTime` | Boolean | OPC `{TagPrefix}.Out_N2ResetTime` | | yes | | | | |
| `Val_N1Runtime` | Float4 | OPC `{TagPrefix}.Val_N1Runtime` | | yes | | | | Device 1 elapsed runtime |
| `Val_N2Runtime` | Float4 | OPC `{TagPrefix}.Val_N2Runtime` | | yes | | | | Device 2 elapsed runtime |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
