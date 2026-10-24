---
title: Gateway Event Scripts
sidebar_position: 11
description: Every gateway-scoped script of the BH project - tag change events, timers, message handlers and WebDev endpoints.
sources:
  - gateways/standard/data/projects/BH/ignition/tag-change/**/*
  - gateways/standard/data/projects/BH/ignition/timer/**/*
  - gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources/**/resource.json
last_verified: 2026-10-24
---

# Gateway Event Scripts

**Gateway event scripts** run inside the gateway (not in a browser session), in the scope of a project. Ignition
runs them for the project set as the gateway scripting project; here that is `BH`.

**Where:** Designer > Project Browser > **Scripting > Gateway Events** (tabs Startup, Shutdown, Timer, Tag Change,
Message, Scheduled). Files: `gateways/standard/data/projects/BH/ignition/<type>/<name>/`. Running scripts show in the
Gateway web UI under Diagnostics > Scripts.

## Current Inventory (2026-10-23)

| Type | Name | Trigger | Calls | Purpose |
|---|---|---|---|---|
| Tag Change | **`plcWriteLock`** | value + quality change of `[default]_Config/PlcWriteLock/Locked` | `shared.PlcWriteLock.onLockChange` | Sets `readOnly` on every RCP1 tag and UDT OPC member; fail-safe relock at startup ([RCP1 Device](devices-rcp1.md#layer-1-tag-readonly-the-write-lock-boolean)) |
| Tag Change | `plcWriteLockTest` | value + quality change of `[default]_Config/PlcWriteLock/_Test/Locked` | `shared.PlcWriteLock.onTestChange` | Same logic on memory test tags only |
| Tag Change | `overviewRebuild` | value change of the `Overview/Rebuild` tags (below) | `shared.Overview.rebuildFromRebuildTag` | Rebuilds the device lists, counts and active alarm counts that overview pages read; runs on startup too |
| Tag Change | `rebuildOverviewInstances` | value, quality, timestamp change of the same tags | `shared.Overview.rebuildFromRebuildTag` (not on the initial change) | Older duplicate of `overviewRebuild` |
| Timer | **`pingMonday`** | every 300 s, fixed delay, shared thread | `shared.Integrations.pingAll` | Updates Connected / Last Check / Last Error for every `[default]_Config/Integrations` endpoint; the Ticket Logger gate reads `Integrations/Monday/Connected` |
| Startup / Shutdown | none | | | |
| Message handlers | none | | | The old `plcWriteLock` handler was removed with the lock page (2026-10-23) |
| Scheduled | none | | | |

Watched `Rebuild` tags (both overview events): `[default]_Config/Rebuild`, `[default]Evaporators/Overview/Rebuild`,
`CoolingTowers/...`, `Compressors/...`, `Pumps/...`, `ExhaustFans/...`, and under
`[default]Boars_Head/GrovePort/Machine Room/`: `Tanks`, `Compressors`, `Pumps`, `Valves`, `ExhaustFans`, `Sensors`
(`.../Overview/Rebuild`). Set one to `true` to rebuild that list.

:::note Duplicate overview events
`overviewRebuild` and `rebuildOverviewInstances` watch the same tags and call the same function, so one flip runs
the rebuild twice. Harmless (idempotent) but wasteful; removing `rebuildOverviewInstances` is a candidate cleanup.
:::

## Removed On 2026-10-22 (Simulation Removal)

The timer `rcp1SimulateEnsure` and tag change `rcp1Simulate` (and every other sim/demo writer) were deleted with the
simulator. They still exist in older commits; don't bring them back. See `docs/sim-removal.md`.

## Other Gateway-Side Code

| Kind | Where | What |
|---|---|---|
| WebDev resources | `com.inductiveautomation.webdev/resources/globe/**`, `rack3d/**` | `globe/map` (the enterprise globe page, one Python resource with the theme CSS inlined) and `globe/mapMarkers` (`doGet`/`doPost`...); `rack3d/lib` (three.js files, CSS, `view.html`), `rack3d/state` (live PLC data as JSON) and `rack3d/view` (the PLC Rack 3D page). Served at `/system/webdev/BH/<folder>/<name>`. **All need a logged-in BH Perspective session** (`shared.WebAuth.perspectiveUser`, anonymous = 401); the globe is unreachable in local mode |
| Tag event scripts | On UDT members (value changed / alarm events) | See [Tags](../tags/index.md) |
| Perspective session events | Project > Perspective > Session Events | Run in the gateway per session; see [Perspective](../perspective/index.md) |
| Project library | `ignition/script-python/shared/**` | Called by all of the above; see [Scripting](../scripting/index.md) |

A **temporary** WebDev endpoint (a name starting with `_`; it must also start with the `shared.WebAuth` login check) for a one-off check must be deleted after use and never
committed.

## Adding Or Changing One

1. Designer > Gateway Events > the tab > add or edit. Keep the event body to one line that calls a `shared.*`
   function, so the logic lives in the library (versioned, testable, documented in the generated reference).
2. Save. The gateway restarts that event's script on save.
3. Check Diagnostics > Logs for errors from the logger you used (`system.util.getLogger("shared.X")`).
4. Update this page and run `python wiki/tools/gen_all.py`.
