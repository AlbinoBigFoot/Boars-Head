---
title: "Machine Room / ExhaustFans (Instances)"
sidebar_label: "Machine Room / ExhaustFans"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/ExhaustFans: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/ExhaustFans`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; ExhaustFans**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/ExhaustFans/udts.json`. 3 UDT instance(s): 2 x [Devices/ExhaustFan](../udts/devices/exhaustfan.md), 1 x [Overview/Exhaust Fan Overview](../udts/overview/exhaust-fan-overview.md).

## BR EF

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/ExhaustFans/BR EF` |
| Type | [Devices/ExhaustFan](../udts/devices/exhaustfan.md) |
| Label | BR EF |
| Description | exhaustfan. Live PLC \[RCP1\] (read only): FanTag=BR\_EEF17, FailTag=BR\_EEF17\_FailToStart. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `FanTag` | `BR_EEF17` |
| `FailTag` | `BR_EEF17_FailToStart` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `DIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]BR_EEF17` | 52 tags |
| `FailToStart` | OPC atomic | yes | `ns=1;s=[RCP1]BR_EEF17_FailToStart` | 1 tags |

## MR EF

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/ExhaustFans/MR EF` |
| Type | [Devices/ExhaustFan](../udts/devices/exhaustfan.md) |
| Label | MR EF |
| Description | exhaustfan. Live PLC \[RCP1\] (read only): FanTag=MR\_EEF15, FailTag=MR\_EEF15\_FailToStart. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `FanTag` | `MR_EEF15` |
| `FailTag` | `MR_EEF15_FailToStart` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `DIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]MR_EEF15` | 52 tags |
| `FailToStart` | OPC atomic | yes | `ns=1;s=[RCP1]MR_EEF15_FailToStart` | 1 tags |

## Overview

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/ExhaustFans/Overview` |
| Type | [Overview/Exhaust Fan Overview](../udts/overview/exhaust-fan-overview.md) |

