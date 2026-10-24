---
title: "PLC/Controller_Device"
sidebar_label: "Controller_Device"
description: "UDT definition PLC/Controller_Device"
generated: true
---

:::note

:::
# UDT `PLC/Controller_Device`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Controller\_Device |
| Tag path | `[default]_types_/PLC/Controller_Device` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 45 (44 atomic, 0 nested UDT, 1 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `(text, 79 chars)` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

44 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `DeviceName/` | Folder | | | | | | | |
| `DeviceName/22` | Int1 | OPC `{TagPrefix}.DeviceName[22]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/4` | Int1 | OPC `{TagPrefix}.DeviceName[4]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/31` | Int1 | OPC `{TagPrefix}.DeviceName[31]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/27` | Int1 | OPC `{TagPrefix}.DeviceName[27]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/8` | Int1 | OPC `{TagPrefix}.DeviceName[8]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/18` | Int1 | OPC `{TagPrefix}.DeviceName[18]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/20` | Int1 | OPC `{TagPrefix}.DeviceName[20]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/25` | Int1 | OPC `{TagPrefix}.DeviceName[25]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/9` | Int1 | OPC `{TagPrefix}.DeviceName[9]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/17` | Int1 | OPC `{TagPrefix}.DeviceName[17]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/21` | Int1 | OPC `{TagPrefix}.DeviceName[21]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/6` | Int1 | OPC `{TagPrefix}.DeviceName[6]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/32` | Int1 | OPC `{TagPrefix}.DeviceName[32]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/0` | Int1 | OPC `{TagPrefix}.DeviceName[0]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/16` | Int1 | OPC `{TagPrefix}.DeviceName[16]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/3` | Int1 | OPC `{TagPrefix}.DeviceName[3]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/1` | Int1 | OPC `{TagPrefix}.DeviceName[1]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/7` | Int1 | OPC `{TagPrefix}.DeviceName[7]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/2` | Int1 | OPC `{TagPrefix}.DeviceName[2]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/13` | Int1 | OPC `{TagPrefix}.DeviceName[13]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/26` | Int1 | OPC `{TagPrefix}.DeviceName[26]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/28` | Int1 | OPC `{TagPrefix}.DeviceName[28]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/15` | Int1 | OPC `{TagPrefix}.DeviceName[15]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/14` | Int1 | OPC `{TagPrefix}.DeviceName[14]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/11` | Int1 | OPC `{TagPrefix}.DeviceName[11]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/10` | Int1 | OPC `{TagPrefix}.DeviceName[10]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/24` | Int1 | OPC `{TagPrefix}.DeviceName[24]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/19` | Int1 | OPC `{TagPrefix}.DeviceName[19]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/30` | Int1 | OPC `{TagPrefix}.DeviceName[30]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/23` | Int1 | OPC `{TagPrefix}.DeviceName[23]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/12` | Int1 | OPC `{TagPrefix}.DeviceName[12]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/29` | Int1 | OPC `{TagPrefix}.DeviceName[29]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `DeviceName/5` | Int1 | OPC `{TagPrefix}.DeviceName[5]` | | yes | | | | ASCII string that identifies the catalog number of the controller &amp; memory board |
| `Device_Status` | Int2 | OPC `{TagPrefix}.Device_Status` | | yes | | | | set 1=flash updating; 4=flash bad; 5=faulted; 6=run; 7=pgm |
| `Fault_Status` | Int2 | OPC `{TagPrefix}.Fault_Status` | | yes | | | | Set 0=none,1=minor soft,2=minor hard,3=major soft,4=majorhard |
| `Keyswitch_Position` | Int2 | OPC `{TagPrefix}.Keyswitch_Position` | | yes | | | | Set 1=RUN, 2=PGM, 3=REM |
| `MajorRev` | Int1 | OPC `{TagPrefix}.MajorRev` | | yes | | | | Major product revision |
| `MinorRev` | Int1 | OPC `{TagPrefix}.MinorRev` | | yes | | | | Minor product revision |
| `ProductCode` | Int2 | OPC `{TagPrefix}.ProductCode` | | yes | | | | Identifies the type of controller |
| `ProductRev` | Int2 | OPC `{TagPrefix}.ProductRev` | | yes | | | | placeholder for current product revision |
| `SerialNumber` | Int4 | OPC `{TagPrefix}.SerialNumber` | | yes | | | | The serial number is assigned when the device is built. |
| `Status` | Int2 | OPC `{TagPrefix}.Status` | | yes | | | | placeholder for status |
| `Type` | Int2 | OPC `{TagPrefix}.Type` | | yes | | | | Identifies the device as a controller.Controller = 14 |
| `Vendor` | Int2 | OPC `{TagPrefix}.Vendor` | | yes | | | | Identifies the vendor of the device.Allen-Bradley = 0001 |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
