---
title: PLC Write Lock
sidebar_position: 8
description: How writes to the RCP1 production PLC are blocked in two layers (one boolean driving readOnly on 37,000 tags, and the OPC UA server permissions), how to unlock for a test, the fail-safes and how to verify.
sources:
  - docs/plc-write-lock.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py
  - gateways/standard/data/projects/BH/ignition/tag-change/plcWriteLock/*
  - gateways/standard/data/projects/BH/ignition/tag-change/plcWriteLockTest/*
last_verified: 2026-10-24
---

# PLC Write Lock

## What it does

`[RCP1]` is the **live production controller** of the Groveport plant. Until the owner has tested the HMI, nothing
may write to it. Writes are blocked in **two independent layers**, and a write reaches the PLC only when **both**
allow it:

| Layer | Where | Blocks | Managed by |
|---|---|---|---|
| Tag level (soft) | one boolean `[default]_Config/PlcWriteLock/Locked` (true = locked) drives `readOnly` on every tag that reads RCP1, plus the HMI write guards | writes through those tags and every HMI write path | the Designer Tag Browser |
| Server level (hard) | OPC UA permissions of the device `RCP1`: Anonymous / AuthenticatedUser = Browse + Read only | every OPC UA write and method call to `[RCP1]`, from any tag, script, Designer or OPC client of this gateway | changed by the system integrator |

| `Locked` | Server block | Result |
|---|---|---|
| true | ON | refused by the tag system |
| false | ON | the tag write goes out, the OPC UA server refuses it; the HMI shows the old value, no audit row |
| true | OFF | refused by the tag system |
| false | OFF | **the write reaches the PLC** |

Status 2026-10-23: `Locked = true`, server block **ON**.

:::info Redesigned 2026-10-23 (v2)
The PLC Write Lock page (`/operations/plc-write-lock`), its unlock popup, the gateway message handler, the
`PLC/WriteUnlock` matrix row and the scope tags were **removed**. User: "Just have a boolean under _Config that
allows me to unlock and lock the read only param of each tag." Older notes that mention the page are out of date.
:::

## How to unlock for a test (owner only)

1. Ask the system integrator to remove the OPC UA server block (it restarts the RCP1 driver; data tags read
   `Uncertain_LastKnownValue` for several minutes while the driver resamples).
2. In the Designer Tag Browser open `default > _Config > PlcWriteLock > Locked` and set it to **false**. The change
   applies itself within seconds; a full unlock of about 37,000 tags takes 30-60 s. The header shows a red **PLC
   Writes Unlocked** indicator (no click action).
3. Test.
4. **Relock both**: `Locked = true` first, then the system integrator restores the server block and confirms it.

:::danger Nobody unlocks casually
Never set `Locked = false` or make an `_RCP1_` tag writable outside an agreed test with the owner present, and never
import tag values into `_RCP1_`. Test the lock logic only with the TEST boolean below.
:::

## How it works

### The boolean drives `readOnly`

Ignition 8.3 cannot bind a tag's `readOnly` property to another tag (an Expression or Tag binding on `readOnly` is
dropped on import, tested 2026-10-23). So the gateway **tag-change event `plcWriteLock`** (value + quality changes
on `Locked`) calls `shared.PlcWriteLock.onLockChange`, which:

- computes from the file tag store which tags / UDT members have a different `readOnly` (a re-assert while locked
  changes nothing);
- applies `{name, readOnly}` with `system.tag.configure(parent, tags, "m")` per folder, in chunks of 5,000 with a
  2 s pause (configuration only, never a value);
- runs in **one background worker per target, gateway-wide** (lock + pending flag in `system.util.getGlobals()`,
  so they survive script reloads); the worker re-reads the boolean until it settles, so the end state always
  follows the latest value;
- logs every flip with counts (logger `shared.PlcWriteLock`), for example
  `PLC write lock (flip): Locked=False -> readOnly=False on 37322 tags / UDT members: 37300 changed, ...`.

What it covers: every AtomicTag under `[default]_RCP1_` (35,056 browsed controller tags; `_Diagnostics_` stays read
only) and every OPC member of the UDT **definitions** in `PLC/**`, `PLC_Ref`, `Devices`, `Units` (2,266 members;
instances inherit, no per-instance overrides).

### Fail-safe

- A bad, null or unreadable `Locked` counts as **locked**.
- At **gateway startup** (JVM up less than 10 minutes when the event script starts) `Locked` is forced back to
  `true` and `readOnly` re-asserted. A project save only re-asserts the current value.

### HMI guards

`shared.PlcWriteLock.writeAllowed(tagPath)` resolves the target through reference tags (up to 6 hops) and refuses
it when it lands under `_RCP1_` or on an `[RCP1]` OPC item while locked (unknown targets that name RCP1 count as
RCP1). Parameterised OPC members such as `[{PlcDevice}]{ResetCountTag}` are resolved with the instance parameters first (fixed 2026-10-24), so the LTU Reset Count write is recognised as an `[RCP1]` write. It is called by `shared.Audit.writeTag`, `shared.Alerts.confirmApplyWrite` (shows "PLC Writes Locked"
instead of the confirm) and `shared.ValveCommands._writeRaw`. See [Write Paths](../scripting/write-path.md).

### Testing without the PLC

The TEST boolean `[default]_Config/PlcWriteLock/_Test/Locked` (event `plcWriteLockTest`, `onTestChange`) drives the
same logic on memory tags `_Config/PlcWriteLock/_Test/Tags/*` and the test UDT `_types_/_PlcWriteLockTest/TestCard`.
Verified 2026-10-23: false -> the 6 test items writable, true -> read only, a burst of flips ends on the last
value; the real handler with `Locked = true` changed 0 of 37,322.

Read-only self check from the Script Console: `shared.PlcWriteLock.selfTest()` and
`shared.PlcWriteLock.counts()`.

## Where the pieces live

| Piece | Where |
|---|---|
| Library | `shared.PlcWriteLock` (Project Library) |
| Events | `ignition/tag-change/plcWriteLock`, `ignition/tag-change/plcWriteLockTest` |
| Tags | `_Config/PlcWriteLock/Locked`, `_Config/PlcWriteLock/_Test/*` |
| Header indicator | "PLC Writes Unlocked" pill in `00_Pages/00_Docked/Header` (hidden while locked) |
| Server block | resource `com.inductiveautomation.opcua/device/RCP1` `config.profile.rolePermissionMappings` (Browse and Read only); **changed by the system integrator** |

The 8.3 Gateway web UI does not show per-device OPC UA role permissions, which is why the server block is changed by
the system integrator. Do not change the gateway-wide `access-control` defaults instead.

## Known limitations

- The block does not cover anything that reaches the PLC without this gateway (Studio 5000, another HMI).
- Someone with gateway config rights can remove the override.
- An unlock or relock makes the gateway rewrite `tag-type-definition/default/PLC/udts.json` (and Devices): don't edit
  UDT definitions during a flip, and expect those files to show in `git status` afterwards.
- Refused writes are not audited (possible follow-up in `docs/ops-audit.md`).
