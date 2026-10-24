---
title: "Machine Room / SafetyRelays (Instances)"
sidebar_label: "Machine Room / SafetyRelays"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/SafetyRelays: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/SafetyRelays`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; SafetyRelays**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/SafetyRelays/udts.json`. 1 UDT instance(s): 1 x [Devices/SafetyRelay](../udts/devices/safetyrelay.md).

## HLCO Safety Relay

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/SafetyRelays/HLCO Safety Relay` |
| Type | [Devices/SafetyRelay](../udts/devices/safetyrelay.md) |
| Label | HLCO Safety Relay |
| Description | safetyrelay. Live PLC \[RCP1\] (read only): ModuleTag=SafetyRelay:I, MajorFaultTag=SafetyRelay\_MajorFault, ResetAlmTag=SafetyRelay\_ResetAlm. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `ModuleTag` | `SafetyRelay:I` |
| `MajorFaultTag` | `SafetyRelay_MajorFault` |
| `ResetAlmTag` | `SafetyRelay_ResetAlm` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `IO` | [PLC/CR30\_Input](../udts/plc/cr30-input.md) | yes | `[RCP1]SafetyRelay:I` | 146 tags |
| `PlcMajorFault` | OPC atomic | yes | `ns=1;s=[RCP1]SafetyRelay_MajorFault` | 1 tags |
| `PlcResetAlm` | OPC atomic | yes | `ns=1;s=[RCP1]SafetyRelay_ResetAlm` | 1 tags |

