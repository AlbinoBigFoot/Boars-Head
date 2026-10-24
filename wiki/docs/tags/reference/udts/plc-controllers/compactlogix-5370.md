---
title: "PLC/Controllers/CompactLogix_5370"
sidebar_label: "CompactLogix_5370"
description: "UDT definition PLC/Controllers/CompactLogix_5370: CompactLogix 5370 L3 controller base (read only)"
generated: true
---

:::note

:::
# UDT `PLC/Controllers/CompactLogix_5370`

CompactLogix 5370 L3 controller base (read only)

Family base for every 1769-L3x controller: Logix driver diagnostics \[\{DeviceName\}\]\[Diagnostics\]/..., identity Status -&gt; mode / faults. Site UDTs inherit it and add their cards

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Controllers &gt; CompactLogix\_5370 |
| Tag path | `[default]_types_/PLC/Controllers/CompactLogix_5370` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/Controllers/udts.json` |
| Inherits from | - |
| Inherited by | [PLC/Sites/BH\_Groveport\_RCP1](../plc-sites/bh-groveport-rcp1.md) |
| Own members | 21 (21 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `DeviceName` | String | - | own |
| `Description` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

9 members read OPC through the server `Ignition OPC UA Server`. Common prefix: `ns=1;s=[{DeviceName}][Diagnostics]/`. The Source column shows the part after the device.

## Structure

```mermaid
flowchart LR
  n0["PLC/Controllers/CompactLogix_5370"]
  style n0 stroke-width:3px
  n1["PLC/Sites/BH_Groveport_RCP1"] -- inherits --> n0
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Bus` | String | expr `'1769 Local Bus (CompactBus)'` | | yes | | | | Local I/O bus |
| `CommLoss` | Boolean | expr `!coalesce({[.]Connected}, false)` | | yes | | | 1 | Logix driver not connected to the controller |
| `Connected` | Boolean | OPC `[Diagnostics]/Connected` | PAX\_Status | yes | | | | Logix driver connected to the controller |
| `DeviceType` | Int4 | OPC `[Diagnostics]/Device/DeviceType` | PAX\_Faceplate | yes | | | | CIP identity device type (14 = PLC) |
| `ExtStatus` | Int4 | expr `(({[.]Status} >> 4) & 15)` | | yes | | | | CIP extended device status (Status bits 4-7) |
| `Family` | String | expr `'CompactLogix 5370 L3'` | | yes | | | | Controller family |
| `IOFault` | Boolean | expr `{[.]Connected} && (({[.]Status} >> 4) & 15) = 2` | | yes | | | 1 | At least one faulted I/O connection |
| `KeySwitch` | String | expr `case(({[.]Status} >> 12) & 3, 1, 'Run', 2, 'Program', 3, 'Remote', 'Unknown')` | | yes | | | | Mode switch (Status bits 12-13) |
| `MajorFault` | Boolean | expr `{[.]Connected} && (getBit({[.]Status}, 10) = 1 \|\| getBit({[.]Status},…` (full below) | | yes | | | 1 | Major fault (gated on Connected) |
| `MajorRevision` | Int4 | OPC `[Diagnostics]/Device/MajorRevision` | PAX\_Faceplate | yes | | | | Firmware major revision |
| `MinorFault` | Boolean | expr `{[.]Connected} && (getBit({[.]Status}, 8) = 1 \|\| getBit({[.]Status}, 9) = 1)` | | yes | | | 1 | Minor fault (gated on Connected: the driver keeps the last Status while disconnected) |
| `MinorRevision` | Int4 | OPC `[Diagnostics]/Device/MinorRevision` | PAX\_Faceplate | yes | | | | Firmware minor revision |
| `Mode` | String | expr `if((({[.]Status} >> 12) & 3) = 3, 'Remote ', '') + case((({[.]Status}…` (full below) | | yes | | | | Controller mode text |
| `NotRun` | Boolean | expr `{[.]Connected} && !((({[.]Status} >> 4) & 15) = 6 \|\| (({[.]Status} >> 4) & 15) = 2)` | | yes | | | 1 | Connected but not in run mode (Program / Faulted / Test) |
| `PowerSupply` | String | expr `'Separate 1769 Power Supply (Catalog Not In L5X)'` | | yes | | | | The L3 has no embedded supply (1769-UM021): the bank is powered by a separate 1769 power supply beside the controller |
| `ProductCode` | Int4 | OPC `[Diagnostics]/Device/ProductCode` | PAX\_Faceplate | yes | | | | CIP identity product code |
| `ProductName` | String | OPC `[Diagnostics]/Device/ProductName` | PAX\_Faceplate | yes | | | | CIP identity product name |
| `Run` | Boolean | expr `{[.]Connected} && (({[.]Status} >> 4) & 15) = 6` | | yes | | | | Controller in run (I/O connections in run mode) |
| `SerialNumber` | Int8 | OPC `[Diagnostics]/Device/SerialNumber` | PAX\_Faceplate | yes | | | | Controller serial number |
| `Status` | Int4 | OPC `[Diagnostics]/Device/Status` | PAX\_Status | yes | | | | CIP identity Status word: bit 8/9 minor fault, 10/11 major fault, bits 4-7 extended status (5 major fault, 6 run, 7 program), bits 12-13 mode switch (1 run, 2… |
| `VendorId` | Int4 | OPC `[Diagnostics]/Device/VendorId` | PAX\_Faceplate | yes | | | | CIP identity vendor (1 = Rockwell) |

<details>
<summary>Full expressions / references (2)</summary>

**`MajorFault`** (expr)

```
{[.]Connected} && (getBit({[.]Status}, 10) = 1 || getBit({[.]Status}, 11) = 1 || (({[.]Status} >> 4) & 15) = 5)
```

**`Mode`** (expr)

```
if((({[.]Status} >> 12) & 3) = 3, 'Remote ', '') + case((({[.]Status} >> 4) & 15), 0, 'Self Test', 1, 'Firmware Update', 2, 'I/O Fault', 3, 'No I/O', 4, 'Config Bad', 5, 'Major Fault', 6, 'Run', 7, 'Program', 'Unknown')
```


</details>

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `CommLoss` | Controller Communication Lost | Critical | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') | PLC communication lost: Logix driver \[Diagnostics\]/Connected = false for 12 s (active delay rides t… |
| `IOFault` | Controller I/O Fault | High | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') | CIP identity extended status 2: at least one faulted I/O connection. Suppressed while PLC communica… |
| `MajorFault` | Controller Major Fault | Critical | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') | CIP identity Status major fault (bits 10/11 or extended status 5). Suppressed while PLC communicati… |
| `MinorFault` | Controller Minor Fault | Low | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') | CIP identity Status minor fault (bits 8/9). Suppressed while PLC communication is lost. |
| `NotRun` | Controller Not In Run Mode | High | WhenTrue | `true` | replace(try(split(\{PathToTag\}, '/')\[1, 0\], ''), 'GrovePort', 'Groveport') + ' / ' + try(split(\{PathToTag\}, '/')\[2, 0\], '') + ' / PLC / ' + try(split(\{PathToTag\}, '/')\[4, 0\], '') | Controller connected but its extended status is not Run (6) or Run with I/O fault (2): Program, Fau… |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Not used by any instance or other UDT.
