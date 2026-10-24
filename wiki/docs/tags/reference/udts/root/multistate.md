---
title: "_Root/Multistate"
sidebar_label: "Multistate"
description: "UDT definition _Root/Multistate: multistate"
generated: true
---

:::note

:::
# UDT `_Root/Multistate`

multistate

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; \_Root &gt; Multistate |
| Tag path | `[default]_types_/_Root/Multistate` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_Root/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 1 (1 atomic, 0 nested UDT, 0 folders) |
| Status | no instances |

## Parameters

_No parameters._

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Value` | Int4 | reference | | | historian, OnChange, db 0.0 Absolute (Discrete) | | | |

<details>
<summary>State labels (1 members)</summary>

| Member | States (value = label) |
|---|---|
| `Value` | 0 = Start, 1 = Stop, 2 = Auto |

</details>

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/CoolingTower](../devices/coolingtower.md) (as `Status`), [Units/AHU](../units/ahu.md) (as `Status`)

