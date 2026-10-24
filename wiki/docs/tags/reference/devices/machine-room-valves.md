---
title: "Machine Room / Valves (Instances)"
sidebar_label: "Machine Room / Valves"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/Valves: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/Valves`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; Valves**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/Valves/udts.json`. 2 UDT instance(s): 1 x [Devices/Valve](../udts/devices/valve.md), 1 x [Overview/Valve Overview](../udts/overview/valve-overview.md).

## Main Liq SV

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Valves/Main Liq SV` |
| Type | [Devices/Valve](../udts/devices/valve.md) |
| Label | MAIN LIQ SV |
| Description | valve. Live PLC \[RCP1\] (read only): ValveTag=MAIN\_LIQ\_CV5. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `ValveTag` | `MAIN_LIQ_CV5` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]MAIN_LIQ_CV5` | 151 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |

## Overview

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Valves/Overview` |
| Type | [Overview/Valve Overview](../udts/overview/valve-overview.md) |

