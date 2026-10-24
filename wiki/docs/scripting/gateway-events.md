---
title: Gateway Events
sidebar_position: 5
description: The BH gateway event scripts (timer, tag change, message handlers, startup) and the tag event scripts - what each does and how to change them safely.
sources:
  - gateways/standard/data/projects/BH/ignition/tag-change/**/*
  - gateways/standard/data/projects/BH/ignition/timer/**/*
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/tags.json
last_verified: 2026-10-24
---

# Gateway Events

**Gateway event scripts** run on the gateway with no user attached: on a timer, when a tag changes, when a
message arrives, or at startup / shutdown. In the Designer open **Project Browser > Scripting > Gateway Events**.
Ignition 8.3 stores each event as its own resource folder:

```text
gateways/standard/data/projects/BH/ignition/
  timer/<name>/handleTimerEvent.py + resource.json      (delay, fixed delay / rate, shared thread)
  tag-change/<name>/onTagChange.py + resource.json      (tag paths, change types)
  message/<name>/...                                    (gateway message handlers - none today)
```

The code and settings of every event are copied into the generated [Gateway Events reference](./reference/gateway-events.md).

## What runs today

| Event | Kind | Trigger | Calls | Purpose |
|---|---|---|---|---|
| `plcWriteLock` | tag change | `[default]_Config/PlcWriteLock/Locked` (value + quality) | `shared.PlcWriteLock.onLockChange` | applies `readOnly = Locked` to every `_RCP1_` tag and PLC UDT OPC member; forces the lock on at gateway startup |
| `plcWriteLockTest` | tag change | `[default]_Config/PlcWriteLock/_Test/Locked` | `shared.PlcWriteLock.onTestChange` | same logic, only on the memory test tags (safe to flip) |
| `overviewRebuild` | tag change | `[default]_Config/Rebuild` and every `.../Overview/Rebuild` tag (value change) | `shared.Overview.rebuildFromRebuildTag` | rebuilds the Overview / Details device tables when a Rebuild tag goes true (also at script start, so counts seed after a restart) |
| `rebuildOverviewInstances` | tag change | same 12 paths (value, quality, timestamp) | `shared.Overview.rebuildFromRebuildTag` | older copy of the same trigger (non-initial true only) |
| `pingMonday` | timer | every 300,000 ms (5 min), fixed delay, shared thread | `shared.Integrations.pingAll` | refreshes Connected / Last Check / Last Error on every `[default]_Config/Integrations/*` endpoint; the Ticket Logger gate reads `Monday/Connected` |

:::note Two rebuild events
`overviewRebuild` and `rebuildOverviewInstances` watch the same tags, so a Rebuild pulse rebuilds twice. It is
harmless (the rebuild is idempotent) but wasteful; one could be disabled after checking that nothing depends on the
quality / timestamp trigger. Parked, not changed.
:::

**No startup / shutdown or scheduled scripts** and **no gateway message handlers** exist in the project. The
`message/` folder is empty since 2026-10-23, when the PLC Write Lock page and its `plcWriteLock` message handler
were removed (the lock became a single boolean).

### How the PLC write lock gets a "startup" hook without a startup script

A tag-change event also fires once when its script starts (`initialChange = True`): on gateway start, on project
save. `shared.PlcWriteLock._onChange` uses that: if the JVM has been up for less than 10 minutes
(`STARTUP_S = 600`), it treats the call as a **gateway startup**, writes `Locked = true` and re-asserts
`readOnly`. A plain project save only re-asserts the current value.

## Tag event scripts

Scripts can also live **on a tag** (Tag Editor > Events, for example Value Changed). The project has exactly one,
on `[default]_Config/Sync File System`: when it is set true it calls `system.project.requestScan(10)` and resets
itself. It is a convenience to make the gateway re-read the project files after an external edit.

UDT member event scripts are not used (alarm rollups use expressions and gateway events instead).

## Changing a gateway event safely

1. Keep the event script **one line** that calls a library function (as all BH events do). Put the logic in
   `shared.*` so it is versioned, documented and testable from the Script Console.
2. Gateway scope has no session: do not call `system.perspective.*` without a session id, and remember
   `shared.Security.can()` returns True here.
3. Long work goes to a background thread (`system.util.invokeAsynchronous`), as `shared.PlcWriteLock` does, so the
   tag-change thread is never blocked.
4. Remember the event runs again with `initialChange = True` every time the project is saved. Make the
   handler idempotent.
5. Edit and save in the Designer (Project Browser > Scripting > Gateway Events); don't edit the event files by hand.
6. Watch **Diagnostics > Logs** for the module's logger after the change.
