---
title: "PLC/COUNTER"
sidebar_label: "COUNTER"
description: "UDT definition PLC/COUNTER"
generated: true
---

:::note

:::
# UDT `PLC/COUNTER`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; COUNTER |
| Tag path | `[default]_types_/PLC/COUNTER` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 7 (7 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Built-in counter` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

7 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `ACC` | Int4 | OPC `{TagPrefix}.ACC` | | yes | | | | |
| `CD` | Boolean | OPC `{TagPrefix}.CD` | | yes | | | | |
| `CU` | Boolean | OPC `{TagPrefix}.CU` | | yes | | | | |
| `DN` | Boolean | OPC `{TagPrefix}.DN` | | yes | | | | |
| `OV` | Boolean | OPC `{TagPrefix}.OV` | | yes | | | | |
| `PRE` | Int4 | OPC `{TagPrefix}.PRE` | | yes | | | | |
| `UN` | Boolean | OPC `{TagPrefix}.UN` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [PLC/Ethernet\_Message\_Config](ethernet-message-config.md) (as `Device_Counter`), [PLC/Ethernet\_Message\_Config](ethernet-message-config.md) (as `MSG_Counter`), [PLC/Ethernet\_Message\_Config](ethernet-message-config.md) (as `RR_Counter`), [PLC/Liquid\_Transfer\_Unit](liquid-transfer-unit.md) (as `COUNT`)

