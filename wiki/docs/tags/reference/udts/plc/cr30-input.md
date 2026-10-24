---
title: "PLC/CR30_Input"
sidebar_label: "CR30_Input"
description: "UDT definition PLC/CR30_Input: Controller CR30_Input (read only)"
generated: true
---

:::note

:::
# UDT `PLC/CR30_Input`

Controller CR30\_Input (read only)

Standard PlantPAx CR30\_Input: ns=1;s=\[\{DeviceName\}\]\{TagPrefix\}.&lt;member&gt;, HMI member whitelist, every member readOnly, tag groups PAX\_Status / PAX\_Faceplate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; CR30\_Input |
| Tag path | `[default]_types_/PLC/CR30_Input` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 32 (32 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | - | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

32 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `ConnectionFaulted` | Boolean | OPC `{TagPrefix}.ConnectionFaulted` | PAX\_Status | yes | | | 1 | |
| `MajorFault` | Boolean | OPC `{TagPrefix}.MajorFault` | PAX\_Status | yes | | | 1 | |
| `MajorFaultCode` | Int1 | OPC `{TagPrefix}.MajorFaultCode` | PAX\_Status | yes | | | | |
| `MajorFaultType` | Int1 | OPC `{TagPrefix}.MajorFaultType` | PAX\_Status | yes | | | | |
| `MinorFault` | Boolean | OPC `{TagPrefix}.MinorFault` | PAX\_Status | yes | | | | |
| `Plugin2InPt00Data` | Boolean | OPC `{TagPrefix}.Plugin2InPt00Data` | PAX\_Status | yes | | | | |
| `Plugin2InPt01Data` | Boolean | OPC `{TagPrefix}.Plugin2InPt01Data` | PAX\_Status | yes | | | | |
| `Plugin2InPt02Data` | Boolean | OPC `{TagPrefix}.Plugin2InPt02Data` | PAX\_Status | yes | | | | |
| `Plugin2InPt03Data` | Boolean | OPC `{TagPrefix}.Plugin2InPt03Data` | PAX\_Status | yes | | | | |
| `Plugin2OutPt00Data` | Boolean | OPC `{TagPrefix}.Plugin2OutPt00Data` | PAX\_Status | yes | | | | |
| `Plugin2OutPt01Data` | Boolean | OPC `{TagPrefix}.Plugin2OutPt01Data` | PAX\_Status | yes | | | | |
| `Plugin2OutPt02Data` | Boolean | OPC `{TagPrefix}.Plugin2OutPt02Data` | PAX\_Status | yes | | | | |
| `Plugin2OutPt03Data` | Boolean | OPC `{TagPrefix}.Plugin2OutPt03Data` | PAX\_Status | yes | | | | |
| `Pt00Data` | Boolean | OPC `{TagPrefix}.Pt00Data` | PAX\_Status | yes | | | | |
| `Pt01Data` | Boolean | OPC `{TagPrefix}.Pt01Data` | PAX\_Status | yes | | | | |
| `Pt02Data` | Boolean | OPC `{TagPrefix}.Pt02Data` | PAX\_Status | yes | | | | |
| `Pt03Data` | Boolean | OPC `{TagPrefix}.Pt03Data` | PAX\_Status | yes | | | | |
| `Pt04Data` | Boolean | OPC `{TagPrefix}.Pt04Data` | PAX\_Status | yes | | | | |
| `Pt05Data` | Boolean | OPC `{TagPrefix}.Pt05Data` | PAX\_Status | yes | | | | |
| `Pt06Data` | Boolean | OPC `{TagPrefix}.Pt06Data` | PAX\_Status | yes | | | | |
| `Pt07Data` | Boolean | OPC `{TagPrefix}.Pt07Data` | PAX\_Status | yes | | | | |
| `Pt08Data` | Boolean | OPC `{TagPrefix}.Pt08Data` | PAX\_Status | yes | | | | |
| `Pt09Data` | Boolean | OPC `{TagPrefix}.Pt09Data` | PAX\_Status | yes | | | | |
| `Pt18Data` | Boolean | OPC `{TagPrefix}.Pt18Data` | PAX\_Status | yes | | | | |
| `Pt19Data` | Boolean | OPC `{TagPrefix}.Pt19Data` | PAX\_Status | yes | | | | |
| `Pt20Data` | Boolean | OPC `{TagPrefix}.Pt20Data` | PAX\_Status | yes | | | | |
| `Pt21Data` | Boolean | OPC `{TagPrefix}.Pt21Data` | PAX\_Status | yes | | | | |
| `RunMode` | Boolean | OPC `{TagPrefix}.RunMode` | PAX\_Status | yes | | | | |
| `SOF01ResetRequired` | Boolean | OPC `{TagPrefix}.SOF01ResetRequired` | PAX\_Status | yes | | | 1 | |
| `SOF02ResetRequired` | Boolean | OPC `{TagPrefix}.SOF02ResetRequired` | PAX\_Status | yes | | | 1 | |
| `SOF05` | Boolean | OPC `{TagPrefix}.SOF05` | PAX\_Status | yes | | | | |
| `SOF06` | Boolean | OPC `{TagPrefix}.SOF06` | PAX\_Status | yes | | | | |

## Alarms

| Member | Alarm | Priority | Mode | Enabled | Display path | Notes |
|---|---|---|---|---|---|---|
| `ConnectionFaulted` | Safety Relay Comm Loss | High | WhenTrue | `true` | | CR30 SafetyRelay:I.ConnectionFaulted |
| `MajorFault` | Safety Relay Major Fault | High | WhenTrue | `true` | | CR30 SafetyRelay:I.MajorFault |
| `SOF01ResetRequired` | LSS HLCO Output 0 Reset Required | Medium | WhenTrue | `true` | | CR30 SafetyRelay:I.SOF01ResetRequired |
| `SOF02ResetRequired` | HSS HLCO Output 1 Reset Required | Medium | WhenTrue | `true` | | CR30 SafetyRelay:I.SOF02ResetRequired |

Associated data `Site` / `Area` / `Device` come from the tag path (`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, never on instances: see [Alarms](../../../alarms.md).

## Used By

Nested in: [Devices/SafetyRelay](../devices/safetyrelay.md) (as `IO`)

Reached through nesting by 1 top-level instance(s).
