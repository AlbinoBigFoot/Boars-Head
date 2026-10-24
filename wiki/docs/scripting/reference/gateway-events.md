---
title: "Gateway Events Reference"
sidebar_label: "Gateway Events"
sidebar_position: 3
description: "Gateway timer, tag change, message and startup event scripts of the BH project, plus tag event scripts."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Scripting > Gateway Events** (8.3 stores each event as its own resource under `gateways/standard/data/projects/BH/ignition/<kind>/<name>`). These scripts run in the **gateway scope**: no Perspective session, no `self`, `system.perspective` only through session ids.

## message (0)

_None in the project._

## scheduled (0)

_None in the project._

## shutdown (0)

_None in the project._

## startup (0)

_None in the project._

## tag-change (4)

### overviewRebuild

| Setting | Value |
|---|---|
| Scope | `G` |
| Enabled | `True` |
| changeTypes | `["ValueChange"]` |
| Tag paths | `[default]_Config/Rebuild`<br/>`[default]Evaporators/Overview/Rebuild`<br/>`[default]CoolingTowers/Overview/Rebuild`<br/>`[default]Compressors/Overview/Rebuild`<br/>`[default]Pumps/Overview/Rebuild`<br/>`[default]ExhaustFans/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Tanks/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Compressors/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Pumps/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Valves/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/ExhaustFans/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Sensors/Overview/Rebuild` |
| Last modified | `2026-07-24T21:43:23Z` by `admin` |

`onTagChange.py`:

```python
def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	"""
	Lightspeed-style Overview rebuild trigger.
	When any watched Overview/.../Rebuild tag goes True, rebuild Instances,
	DeviceCount, and ActiveAlarmCount via shared.Overview.
	"""
	# Run on startup too so counts seed after gateway restart / scan
	try:
		val = newValue.getValue() if hasattr(newValue, "getValue") else newValue
	except:
		val = newValue

	if val is not True and val != 1:
		return

	tagPath = None
	try:
		tagPath = str(event.getTagPath()) if event is not None and hasattr(event, "getTagPath") else None
	except:
		tagPath = None
	if not tagPath:
		try:
			tagPath = str(event.tagPath)
		except:
			pass
	if not tagPath:
		return

	shared.Overview.rebuildFromRebuildTag(tagPath)
```

### plcWriteLock

| Setting | Value |
|---|---|
| Scope | `G` |
| Enabled | `True` |
| changeTypes | `["ValueChange", "QualityChange"]` |
| Tag paths | `[default]_Config/PlcWriteLock/Locked` |
| Last modified | `2026-10-23T17:06:10Z` by `external` |

`onTagChange.py`:

```python
def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	# plc-write-lock: readOnly = Locked on every [default]_RCP1_ tag and PLC / Devices UDT OPC member; fail-safe locked on
	# bad / null and on gateway startup. Logic + gateway log: shared.PlcWriteLock
	shared.PlcWriteLock.onLockChange(initialChange, newValue, event)
```

### plcWriteLockTest

| Setting | Value |
|---|---|
| Scope | `G` |
| Enabled | `True` |
| changeTypes | `["ValueChange", "QualityChange"]` |
| Tag paths | `[default]_Config/PlcWriteLock/_Test/Locked` |
| Last modified | `2026-10-23T17:06:10Z` by `external` |

`onTagChange.py`:

```python
def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	# plc-write-lock: readOnly = Locked on every TEST tag (memory, never the PLC); fail-safe locked on
	# bad / null. Logic + gateway log: shared.PlcWriteLock
	shared.PlcWriteLock.onTestChange(initialChange, newValue, event)
```

### rebuildOverviewInstances

| Setting | Value |
|---|---|
| Scope | `G` |
| Enabled | `True` |
| changeTypes | `["ValueChange", "QualityChange", "TimestampChange"]` |
| Tag paths | `[default]_Config/Rebuild`<br/>`[default]Evaporators/Overview/Rebuild`<br/>`[default]CoolingTowers/Overview/Rebuild`<br/>`[default]Compressors/Overview/Rebuild`<br/>`[default]Pumps/Overview/Rebuild`<br/>`[default]ExhaustFans/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Tanks/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Compressors/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Pumps/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Valves/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/ExhaustFans/Overview/Rebuild`<br/>`[default]Boars_Head/GrovePort/Machine Room/Sensors/Overview/Rebuild` |
| Last modified | `2026-07-24T21:43:23Z` by `admin` |

`onTagChange.py`:

```python
def onTagChange(initialChange, newValue, previousValue, event, executionCount):
	if (not initialChange) and newValue.value: shared.Overview.rebuildFromRebuildTag(event.tagPath)
```

## timer (1)

### pingMonday

| Setting | Value |
|---|---|
| Scope | `G` |
| Enabled | `True` |
| delay | `300000` |
| fixedDelay | `true` |
| sharedThread | `true` |
| Last modified | `2026-07-25T04:15:00Z` by `external` |

`handleTimerEvent.py`:

```python
def handleTimerEvent():
	# Connection status (Connected / Last Check / Last Error) for every [default]_Config/Integrations endpoint.
	# The Ticket Logger access gate reads Integrations/Monday/Connected.
	shared.Integrations.pingAll()
```

## Tag event scripts (1)

Scripts on tags or UDT members (Tag Editor > **Events > Value Changed** etc.), found in the tag-definition / tag-type-definition files (the browsed `_RCP1_` tree is skipped: it has none).

### default/\_Config/Sync File System

| | |
|---|---|
| Store | `tag-definition` |
| Event | `valueChanged` |

```python
	if system.tag.readBlocking("[.]Sync File System")[0].value:
		system.project.requestScan(10)
		system.tag.writeBlocking("[.]Sync File System", False)
```
