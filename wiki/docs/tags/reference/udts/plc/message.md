---
title: "PLC/MESSAGE"
sidebar_label: "MESSAGE"
description: "UDT definition PLC/MESSAGE"
generated: true
---

:::note

:::
# UDT `PLC/MESSAGE`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; MESSAGE |
| Tag path | `[default]_types_/PLC/MESSAGE` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 29 (29 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Built-in Message` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

29 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Attribute` | Int2 | OPC `{TagPrefix}.Attribute` | | yes | | | | |
| `Channel` | Int1 | OPC `{TagPrefix}.Channel` | | yes | | | | |
| `Class` | Int2 | OPC `{TagPrefix}.Class` | | yes | | | | |
| `ConnectionRate` | Int4 | OPC `{TagPrefix}.ConnectionRate` | | yes | | | | |
| `DN` | Boolean | OPC `{TagPrefix}.DN` | | yes | | | | |
| `DN_LEN` | Int2 | OPC `{TagPrefix}.DN_LEN` | | yes | | | | |
| `DestinationLink` | Int2 | OPC `{TagPrefix}.DestinationLink` | | yes | | | | |
| `DestinationNode` | Int2 | OPC `{TagPrefix}.DestinationNode` | | yes | | | | |
| `EN_CC` | Boolean | OPC `{TagPrefix}.EN_CC` | | yes | | | | |
| `ER` | Boolean | OPC `{TagPrefix}.ER` | | yes | | | | |
| `ERR` | Int2 | OPC `{TagPrefix}.ERR` | | yes | | | | |
| `ERR_SRC` | Int1 | OPC `{TagPrefix}.ERR_SRC` | | yes | | | | |
| `EW` | Boolean | OPC `{TagPrefix}.EW` | | yes | | | | |
| `EXERR` | Int4 | OPC `{TagPrefix}.EXERR` | | yes | | | | |
| `Flags` | Int2 | OPC `{TagPrefix}.Flags` | | yes | | | | |
| `Group` | Int1 | OPC `{TagPrefix}.Group` | | yes | | | | |
| `Instance` | Int4 | OPC `{TagPrefix}.Instance` | | yes | | | | |
| `LocalIndex` | Int4 | OPC `{TagPrefix}.LocalIndex` | | yes | | | | |
| `Path` | String | OPC `{TagPrefix}.Path` | | yes | | | | |
| `REQ_LEN` | Int2 | OPC `{TagPrefix}.REQ_LEN` | | yes | | | | |
| `Rack` | Int1 | OPC `{TagPrefix}.Rack` | | yes | | | | |
| `RemoteElement` | String | OPC `{TagPrefix}.RemoteElement` | | yes | | | | |
| `RemoteIndex` | Int4 | OPC `{TagPrefix}.RemoteIndex` | | yes | | | | |
| `ST` | Boolean | OPC `{TagPrefix}.ST` | | yes | | | | |
| `Slot` | Int1 | OPC `{TagPrefix}.Slot` | | yes | | | | |
| `SourceLink` | Int2 | OPC `{TagPrefix}.SourceLink` | | yes | | | | |
| `TO` | Boolean | OPC `{TagPrefix}.TO` | | yes | | | | |
| `TimeoutMultiplier` | Int1 | OPC `{TagPrefix}.TimeoutMultiplier` | | yes | | | | |
| `UnconnectedTimeout` | Int4 | OPC `{TagPrefix}.UnconnectedTimeout` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
