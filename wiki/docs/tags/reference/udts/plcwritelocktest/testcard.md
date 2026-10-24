---
title: "_PlcWriteLockTest/TestCard"
sidebar_label: "TestCard"
description: "UDT definition _PlcWriteLockTest/TestCard: PLC write lock test UDT: memory members whose readOnly the TEST boolean drives at the definition level (instances inherit)."
generated: true
---

:::note

:::
# UDT `_PlcWriteLockTest/TestCard`

PLC write lock test UDT: memory members whose readOnly the TEST boolean drives at the definition level (instances inherit).

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; \_PlcWriteLockTest &gt; TestCard |
| Tag path | `[default]_types_/_PlcWriteLockTest/TestCard` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_PlcWriteLockTest/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 4 (3 atomic, 0 nested UDT, 1 folders) |
| Status | in use |

## Parameters

_No parameters._

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `OCmd_Start` | Boolean | memory = `False` | | yes | | | | |
| `Val_SP` | Float4 | memory = `50.0` | | yes | | | | |
| `Alarm/` | Folder | | | | | | | |
| `Alarm/Cfg_Limit` | Float4 | memory = `90.0` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

1 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]_Config/PlcWriteLock/_Test/Instance` | `_Test` |
