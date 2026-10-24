---
title: "PLC/P_Alarm"
sidebar_label: "P_Alarm"
description: "UDT definition PLC/P_Alarm"
generated: true
---

:::note

:::
# UDT `PLC/P_Alarm`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; P\_Alarm |
| Tag path | `[default]_types_/PLC/P_Alarm` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 46 (46 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

46 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Ack` | Boolean | OPC `{TagPrefix}.Ack` | | yes | | | | Alarm acknowledged status: 1=Ack rcvd |
| `Alm` | Boolean | OPC `{TagPrefix}.Alm` | | yes | | | | Alarm output 1=In Alarm |
| `Cfg_AckReqd` | Boolean | OPC `{TagPrefix}.Cfg_AckReqd` | | yes | | | | 1=Acknowledge required for this Alarm |
| `Cfg_AllowDisable` | Boolean | OPC `{TagPrefix}.Cfg_AllowDisable` | | yes | | | | 1=Allow Maintenance to Disable this Alarm |
| `Cfg_AllowShelve` | Boolean | OPC `{TagPrefix}.Cfg_AllowShelve` | | yes | | | | 1=Allow Operator to Shelve this Alarm |
| `Cfg_AlmMinOnT` | Int4 | OPC `{TagPrefix}.Cfg_AlmMinOnT` | | yes | | | | Minimum time Alm output stays on (sec) |
| `Cfg_Exists` | Boolean | OPC `{TagPrefix}.Cfg_Exists` | | yes | | | | 1=Alarm configured to exist, 0=Does not exist, don$'t scan |
| `Cfg_MaxShelfT` | Int2 | OPC `{TagPrefix}.Cfg_MaxShelfT` | | yes | | | | Auto unshelve after shelved this long (1..32767 minutes) |
| `Cfg_PCmdClear` | Boolean | OPC `{TagPrefix}.Cfg_PCmdClear` | | yes | | | | 1=Clear Program Commands on receipt$N0=Leave Set |
| `Cfg_ResetReqd` | Boolean | OPC `{TagPrefix}.Cfg_ResetReqd` | | yes | | | | 1=Latched Alarm, a Reset is required to clear this Alarm |
| `Cfg_Severity` | Int2 | OPC `{TagPrefix}.Cfg_Severity` | | yes | | | | Alarm Severity: 1..250=Low, 251..500=Medium, 501..750=High, 751..1000=Urgent |
| `Disabled` | Boolean | OPC `{TagPrefix}.Disabled` | | yes | | | | 1=Alarm has been Disabled by Maintanance (inhibits new alarm) |
| `EnableIn` | Boolean | OPC `{TagPrefix}.EnableIn` | | yes | | | | Enable Input - System Defined Parameter |
| `EnableOut` | Boolean | OPC `{TagPrefix}.EnableOut` | | yes | | | | Enable Output - System Defined Parameter |
| `Err_Severity` | Boolean | OPC `{TagPrefix}.Err_Severity` | | yes | | | | 1=Error in Config: Invalid Severity (use 1 to 4) |
| `Err_Timer` | Boolean | OPC `{TagPrefix}.Err_Timer` | | yes | | | | 1=Error in Config: Alarm Min On Time, Shelf Time (use 0 to 2147483) |
| `Inp` | Boolean | OPC `{TagPrefix}.Inp` | | yes | | | | Alarm Condition Input 1=Alarm |
| `Inp_Reset` | Boolean | OPC `{TagPrefix}.Inp_Reset` | | yes | | | | 1=Reset Alarm requiring reset |
| `MCmd_Disable` | Boolean | OPC `{TagPrefix}.MCmd_Disable` | | yes | | | | Maintenance Command to Disable alarm (inhibits new alarm) |
| `MCmd_Enable` | Boolean | OPC `{TagPrefix}.MCmd_Enable` | | yes | | | | Maintenance Command to Enable alarm (allows new alarm) |
| `MCmd_Test` | Boolean | OPC `{TagPrefix}.MCmd_Test` | | yes | | | | Maintenance Command to Test alarm (issued for minimum alarm time) |
| `OCmd_Ack` | Boolean | OPC `{TagPrefix}.OCmd_Ack` | | yes | | | | Operator Command to Acknowledge alarm |
| `OCmd_Reset` | Boolean | OPC `{TagPrefix}.OCmd_Reset` | | yes | | | | Operator Command to Reset latched alarm |
| `OCmd_Shelve` | Boolean | OPC `{TagPrefix}.OCmd_Shelve` | | yes | | | | Operator Command to Shelve Alarm (inhibits new alarm) |
| `OCmd_Unshelve` | Boolean | OPC `{TagPrefix}.OCmd_Unshelve` | | yes | | | | Operator Command to Unshelve alarm (allows new alarm) |
| `PCfg_AllowExist` | Boolean | OPC `{TagPrefix}.PCfg_AllowExist` | | yes | | | | 1=Alarm can be configured to exist, 0=other configs make alarm meaningless |
| `PCmd_Ack` | Boolean | OPC `{TagPrefix}.PCmd_Ack` | | yes | | | | Program Command to Acknowledge alarm |
| `PCmd_Reset` | Boolean | OPC `{TagPrefix}.PCmd_Reset` | | yes | | | | Program Command to Reset latched alarm |
| `PCmd_Suppress` | Boolean | OPC `{TagPrefix}.PCmd_Suppress` | | yes | | | | Program Command to Suppress by Design (inhibits new alarm) |
| `PCmd_Unshelve` | Boolean | OPC `{TagPrefix}.PCmd_Unshelve` | | yes | | | | Program Command to Unshelve (e.g., on shift change) |
| `PCmd_Unsuppress` | Boolean | OPC `{TagPrefix}.PCmd_Unsuppress` | | yes | | | | Program Command to Unsuppress (allows new alarm) |
| `P_Alarm` | Boolean | OPC `{TagPrefix}.P_Alarm` | | yes | | | | Unique Parameter Name for auto - discovery |
| `Rdy_Ack` | Boolean | OPC `{TagPrefix}.Rdy_Ack` | | yes | | | | Ready to receive OCmd\_Ack (enables button) |
| `Rdy_Disable` | Boolean | OPC `{TagPrefix}.Rdy_Disable` | | yes | | | | Ready to receive MCmd\_Disable (enables button) |
| `Rdy_Enable` | Boolean | OPC `{TagPrefix}.Rdy_Enable` | | yes | | | | Ready to receive MCmd\_Enable (enables button) |
| `Rdy_Reset` | Boolean | OPC `{TagPrefix}.Rdy_Reset` | | yes | | | | Ready to receive OCmd\_Reset (enables button) |
| `Rdy_Shelve` | Boolean | OPC `{TagPrefix}.Rdy_Shelve` | | yes | | | | Ready to receive OCmd\_Shelve (enables button) |
| `Rdy_Test` | Boolean | OPC `{TagPrefix}.Rdy_Test` | | yes | | | | Ready to receive MCmd\_Test (enables button) |
| `Rdy_Unshelve` | Boolean | OPC `{TagPrefix}.Rdy_Unshelve` | | yes | | | | Ready to receive OCmd\_Unshelve (enables button) |
| `Shelved` | Boolean | OPC `{TagPrefix}.Shelved` | | yes | | | | 1=Alarm has been Shelved by Operator (inhibits new alarm) |
| `Sts_AlmInh` | Boolean | OPC `{TagPrefix}.Sts_AlmInh` | | yes | | | | 1=Alarm has been suppressed, shelved or disabled, display $QI$Q icon |
| `Sts_Err` | Boolean | OPC `{TagPrefix}.Sts_Err` | | yes | | | | 1=Error in Config: see detail Err\_ bits for reason |
| `Suppressed` | Boolean | OPC `{TagPrefix}.Suppressed` | | yes | | | | 1=Alarm has been Suppressed by Program (inhibits new alarm) |
| `Val_MinToUnshelve` | Int4 | OPC `{TagPrefix}.Val_MinToUnshelve` | | yes | | | | Number of minutes until this alarm unshelves itself (mmm:ss) |
| `Val_Notify` | Int1 | OPC `{TagPrefix}.Val_Notify` | | yes | | | | Current Alarm Severity and Acknowledgement (enumeration) |
| `Val_SecToUnshelve` | Int4 | OPC `{TagPrefix}.Val_SecToUnshelve` | | yes | | | | Number of Seconds until this alarm unshelves itself (mmm:ss) |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/Liquid\_Transfer\_Unit](liquid-transfer-unit.md) (as `Count_Alarm`)

