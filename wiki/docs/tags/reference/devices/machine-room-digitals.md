---
title: "Machine Room / Digitals (Instances)"
sidebar_label: "Machine Room / Digitals"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/Digitals: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/Digitals`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; Digitals**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/Digitals/udts.json`. 8 UDT instance(s): 8 x [\_Root/Digital](../udts/root/digital.md).

## FIRE

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/FIRE` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | FIRE |
| Description | Fire detection rollup (Program:RCP\_Alarm\_Circuit.FD\_Alarm) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Program:RCP_Alarm_Circuit/FD_Alarm` | |

## MR AD

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/MR AD` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | MR AD |
| Description | Machine Room ammonia detector (PLC AD\_MR1.Alm\_TgtDisagree) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]Boars_Head/GrovePort/Machine Room/Detectors/MR-AD1/DIn/Alm_TgtDisagree` | |

## RDISKS

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/RDISKS` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | RDISKS |
| Description | Rupture disks rollup (Program:RCP\_Alarm\_Circuit.PS\_Alarm) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Program:RCP_Alarm_Circuit/PS_Alarm` | |

## VL AD

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/VL AD` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | VL AD |
| Description | Vent Line ammonia detector (PLC AD\_VL.Alm\_TgtDisagree) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]Boars_Head/GrovePort/Machine Room/Detectors/VL-AD/DIn/Alm_TgtDisagree` | |

## Alarm Light

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Light` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | Alarm Light |
| Description | Alarm light on (\[RCP1\]Alarm\_Light.Sts\_Out) - shows Reset |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Controller:Global/Alarm_Light/Sts_Out` | |

## Alarm Circuit

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Circuit` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | Alarm Horn |
| Description | Alarm horn circuit on (\[RCP1\]Alarm\_Circuit.Sts\_Out) - shows Silence |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Controller:Global/Alarm_Circuit/Sts_Out` | |

## Alarm Reset

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Reset` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | Alarm Reset |
| Description | Reset alarm light and horn (\[RCP1\]ALARM.HMI\_Reset) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Controller:Global/ALARM/HMI_Reset` | |

## Alarm Silence

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Silence` |
| Type | [\_Root/Digital](../udts/root/digital.md) |
| Label | Alarm Silence |
| Description | Silence alarm horn (\[RCP1\]ALARM.HMI\_Silence) |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Value` | reference | yes | `[default]_RCP1_/Controller:Global/ALARM/HMI_Silence` | |

