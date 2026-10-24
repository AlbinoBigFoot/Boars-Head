---
title: "PLC/P_Intlk"
sidebar_label: "P_Intlk"
description: "UDT definition PLC/P_Intlk: PlantPAx P_Intlk (read only)"
generated: true
---

:::note

:::
# UDT `PLC/P_Intlk`

PlantPAx P\_Intlk (read only)

Standard PlantPAx P\_Intlk: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_Intlk |
| Tag path | `[default]_types_/PLC/P_Intlk` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 51 (50 atomic, 0 nested UDT, 1 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

50 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cfg_CondTxt/` | Folder | | | | | | | |
| `Cfg_CondTxt/Cfg_CondTxt_0_` | String | OPC `{TagPrefix}.Cfg_CondTxt[0]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_10_` | String | OPC `{TagPrefix}.Cfg_CondTxt[10]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_11_` | String | OPC `{TagPrefix}.Cfg_CondTxt[11]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_12_` | String | OPC `{TagPrefix}.Cfg_CondTxt[12]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_13_` | String | OPC `{TagPrefix}.Cfg_CondTxt[13]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_14_` | String | OPC `{TagPrefix}.Cfg_CondTxt[14]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_15_` | String | OPC `{TagPrefix}.Cfg_CondTxt[15]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_1_` | String | OPC `{TagPrefix}.Cfg_CondTxt[1]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_2_` | String | OPC `{TagPrefix}.Cfg_CondTxt[2]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_3_` | String | OPC `{TagPrefix}.Cfg_CondTxt[3]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_4_` | String | OPC `{TagPrefix}.Cfg_CondTxt[4]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_5_` | String | OPC `{TagPrefix}.Cfg_CondTxt[5]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_6_` | String | OPC `{TagPrefix}.Cfg_CondTxt[6]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_7_` | String | OPC `{TagPrefix}.Cfg_CondTxt[7]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_8_` | String | OPC `{TagPrefix}.Cfg_CondTxt[8]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_CondTxt/Cfg_CondTxt_9_` | String | OPC `{TagPrefix}.Cfg_CondTxt[9]` | PAX\_Config | yes | | | | Interlock condition text |
| `Cfg_Bypassable` | Int2 | OPC `{TagPrefix}.Cfg_Bypassable` | PAX\_Faceplate | yes | | | | Set bits indicate which conditions can be bypassed |
| `Cfg_Desc` | String | OPC `{TagPrefix}.Cfg_Desc` | PAX\_Faceplate | yes | | | | |
| `Cfg_HasNav` | Int2 | OPC `{TagPrefix}.Cfg_HasNav` | PAX\_Faceplate | yes | | | | Set bits indicate which Navigation buttons are enabled |
| `Cfg_Label` | String | OPC `{TagPrefix}.Cfg_Label` | PAX\_Faceplate | yes | | | | |
| `Cfg_Latched` | Int2 | OPC `{TagPrefix}.Cfg_Latched` | PAX\_Faceplate | yes | | | | Set bits indicate which conditions are latched (sealed in) |
| `Cfg_OKState` | Int2 | OPC `{TagPrefix}.Cfg_OKState` | PAX\_Faceplate | yes | | | | Bits indicate which state (0 or 1) of each input is OK to run |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | PAX\_Faceplate | yes | | | | 1=Clear Program Commands on receipt$N0=Leave Set |
| `Cfg_Tag` | String | OPC `{TagPrefix}.Cfg_Tag` | PAX\_Faceplate | yes | | | | |
| `Inf_Lib` | String | OPC `{TagPrefix}.Inf_Lib` | PAX\_Faceplate | yes | | | | |
| `Inf_Type` | String | OPC `{TagPrefix}.Inf_Type` | PAX\_Faceplate | yes | | | | |
| `Inp_LatchDefeat` | Boolean | OPC `{TagPrefix}.Inp_LatchDefeat` | PAX\_Status | yes | | | | Latch Defeat 1=Do$Nnot latch inputs even if configured for latching |
| `MSet_Bypass00` | Boolean | OPC `{TagPrefix}.MSet_Bypass00` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 00: 1=Bypass |
| `MSet_Bypass01` | Boolean | OPC `{TagPrefix}.MSet_Bypass01` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 0\`: 1=Bypass |
| `MSet_Bypass02` | Boolean | OPC `{TagPrefix}.MSet_Bypass02` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 02: 1=Bypass |
| `MSet_Bypass03` | Boolean | OPC `{TagPrefix}.MSet_Bypass03` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 03: 1=Bypass |
| `MSet_Bypass04` | Boolean | OPC `{TagPrefix}.MSet_Bypass04` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 04: 1=Bypass |
| `MSet_Bypass05` | Boolean | OPC `{TagPrefix}.MSet_Bypass05` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 05: 1=Bypass |
| `MSet_Bypass06` | Boolean | OPC `{TagPrefix}.MSet_Bypass06` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 06: 1=Bypass |
| `MSet_Bypass07` | Boolean | OPC `{TagPrefix}.MSet_Bypass07` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 07: 1=Bypass |
| `MSet_Bypass08` | Boolean | OPC `{TagPrefix}.MSet_Bypass08` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 08: 1=Bypass |
| `MSet_Bypass09` | Boolean | OPC `{TagPrefix}.MSet_Bypass09` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 09: 1=Bypass |
| `MSet_Bypass10` | Boolean | OPC `{TagPrefix}.MSet_Bypass10` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 10: 1=Bypass |
| `MSet_Bypass11` | Boolean | OPC `{TagPrefix}.MSet_Bypass11` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 11: 1=Bypass |
| `MSet_Bypass12` | Boolean | OPC `{TagPrefix}.MSet_Bypass12` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 12: 1=Bypass |
| `MSet_Bypass13` | Boolean | OPC `{TagPrefix}.MSet_Bypass13` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 13: 1=Bypass |
| `MSet_Bypass14` | Boolean | OPC `{TagPrefix}.MSet_Bypass14` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 14: 1=Bypass |
| `MSet_Bypass15` | Boolean | OPC `{TagPrefix}.MSet_Bypass15` | PAX\_Faceplate | yes | | | | Maint. Bypass Toggle for Interlock Cond. 15: 1=Bypass |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | PAX\_Faceplate | yes | | | | Operator Command to Reset Latched Interlocks |
| `Rdy_Reset` | Boolean | OPC `{TagPrefix}.Rdy_Reset` | PAX\_Faceplate | yes | | | | 1=Ready to receive OCmd\_Reset (reset required) |
| `Sts_BypActive` | Boolean | OPC `{TagPrefix}.Sts_BypActive` | PAX\_Status | yes | | | | 1=Interlock Bypassing is Active (ignore bypassable interlocks) |
| `Sts_FirstOut` | Int2 | OPC `{TagPrefix}.Sts_FirstOut` | PAX\_Status | yes | | | | Interlock First Out Status (bit 1 is First Not-OK condition) |
| `Sts_Intlk` | Int2 | OPC `{TagPrefix}.Sts_Intlk` | PAX\_Status | yes | | | | Individual Interlock Status (1=Stop, 0=OK) |
| `Sts_IntlkOK` | Boolean | OPC `{TagPrefix}.Sts_IntlkOK` | PAX\_Status | yes | | | | Overall Interlock Status (1=OK to run, 0=Stop) |
| `Sts_NBIntlkOK` | Boolean | OPC `{TagPrefix}.Sts_NBIntlkOK` | PAX\_Status | yes | | | | Non-Bypassable Interlock Status (1=All NB Interlocks OK to run) |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Valve](../devices/valve.md) (as `Intlk`), [Devices/Compressor](../devices/compressor.md) (as `Intlk`), [Devices/Pump](../devices/pump.md) (as `Intlk`), [Devices/Evaporator](../devices/evaporator.md) (as `Intlk`)

Reached through nesting by 39 top-level instance(s).
