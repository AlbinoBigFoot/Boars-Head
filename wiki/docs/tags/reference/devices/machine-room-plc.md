---
title: "Machine Room / PLC (Instances)"
sidebar_label: "Machine Room / PLC"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/PLC: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/PLC`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; PLC**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/PLC/udts.json`. 1 UDT instance(s): 1 x [PLC/Sites/BH\_Groveport\_RCP1](../udts/plc-sites/bh-groveport-rcp1.md).

## RCP1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1` |
| Type | [PLC/Sites/BH\_Groveport\_RCP1](../udts/plc-sites/bh-groveport-rcp1.md) |
| Label | RCP1 PLC Rack |
| Description | Live PLC \[RCP1\] read only: controller diagnostics + local I/O cards |

| Parameter | Value |
|---|---|
| `Description` | `Refrigeration Control Panel 1 PLC` |
| `DeviceName` | `RCP1` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Connected` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Connected` | 1 tags |
| `DeviceType` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/DeviceType` | 1 tags |
| `MajorRevision` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/MajorRevision` | 1 tags |
| `MinorRevision` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/MinorRevision` | 1 tags |
| `ProductCode` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/ProductCode` | 1 tags |
| `ProductName` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/ProductName` | 1 tags |
| `SerialNumber` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/SerialNumber` | 1 tags |
| `Status` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/Status` | 1 tags |
| `VendorId` | OPC atomic | yes | `ns=1;s=[RCP1][Diagnostics]/Device/VendorId` | 1 tags |
| `MajorFaultRecordCode` | OPC atomic | yes | `ns=1;s=[RCP1]MajorFaultRecord_Code` | not in mirror |
| `MajorFaultRecordType` | OPC atomic | yes | `ns=1;s=[RCP1]MajorFaultRecord_Type` | not in mirror |
| `Slot01` | [PLC/Modules/1769\_IF8](../udts/plc-modules/type-1769-if8.md) | yes | (no PLC object) | |
| `Slot02` | [PLC/Modules/1769\_IF8](../udts/plc-modules/type-1769-if8.md) | yes | (no PLC object) | |
| `Slot03` | [PLC/Modules/1769\_IF8](../udts/plc-modules/type-1769-if8.md) | yes | (no PLC object) | |
| `Slot04` | [PLC/Modules/1769\_IF8](../udts/plc-modules/type-1769-if8.md) | yes | (no PLC object) | |
| `Slot05` | [PLC/Modules/1769\_IA16](../udts/plc-modules/type-1769-ia16.md) | yes | (no PLC object) | |
| `Slot06` | [PLC/Modules/1769\_IA16](../udts/plc-modules/type-1769-ia16.md) | yes | (no PLC object) | |
| `Slot07` | [PLC/Modules/1769\_IQ16](../udts/plc-modules/type-1769-iq16.md) | yes | (no PLC object) | |
| `Slot08` | [PLC/Modules/1769\_IQ16](../udts/plc-modules/type-1769-iq16.md) | yes | (no PLC object) | |
| `Slot09` | [PLC/Modules/1769\_IQ16](../udts/plc-modules/type-1769-iq16.md) | yes | (no PLC object) | |
| `Slot10` | [PLC/Modules/1769\_IA16](../udts/plc-modules/type-1769-ia16.md) | yes | (no PLC object) | |
| `Slot11` | [PLC/Modules/1769\_IA16](../udts/plc-modules/type-1769-ia16.md) | yes | (no PLC object) | |
| `Slot12` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot13` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot14` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot15` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot16` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot17` | [PLC/Modules/1769\_OA16](../udts/plc-modules/type-1769-oa16.md) | yes | (no PLC object) | |
| `Slot18` | [PLC/Modules/1769\_OW16](../udts/plc-modules/type-1769-ow16.md) | yes | (no PLC object) | |
| `Slot19` | [PLC/Modules/1769\_OW16](../udts/plc-modules/type-1769-ow16.md) | yes | (no PLC object) | |

