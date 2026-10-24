---
title: "shared.ValveCommands"
sidebar_label: "shared.ValveCommands"
description: "Script module shared.ValveCommands: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`  
**Lines:** 247. **Functions:** 19. **Called as:** `shared.ValveCommands.<function>(...)`

## What the source says

```text
Valve / pump faceplate command helpers (SO/MO).
Plant Digitals are often valueSource=reference → RCP1 atomics; resolve before write.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag`, `system.util` |
| Logger names | `shared.ValveCommands` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Pax](./shared-pax.md), [shared.PlcWriteLock](./shared-plcwritelock.md), [shared.Security](./shared-security.md) |

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_resolve`](#_resolve) (internal) | Prefer OPC/Memory sourceTagPath when path is a reference leaf. | 0 |
| [`_plcAllowed`](#_plcallowed) (internal) | plc-write-lock: shared.PlcWriteLock.writeAllowed (an error blocks only paths naming RCP1). | 0 |
| [`_qualityGood`](#_qualitygood) (internal) | | 0 |
| [`_writeRaw`](#_writeraw) (internal) | Write resolved paths (raw, no audit); Bad qualities are logged. | 0 |
| [`_write`](#_write) (internal) | Operator writes go through OpsAudit; audit=False writes raw. | 0 |
| [`startPump`](#startpump) | | 1 |
| [`stopPump`](#stoppump) | | 1 |
| [`resetPump`](#resetpump) | | 1 |
| [`openValve`](#openvalve) | Open command. SO → Cmd + Cmd\_Open; MO → pulse Cmd\_Open. | 2 |
| [`closeValve`](#closevalve) | Close command. SO → clear Cmd/Cmd\_Open + pulse Cmd\_Close; MO → Cmd\_Close. | 2 |
| [`resetValve`](#resetvalve) | | 2 |
| [`writeTag`](#writetag) | Write one tag path, resolving Digitals reference → source when needed. | 5 |
| [`_readBool`](#_readbool) (internal) | | 0 |
| [`enableDevice`](#enabledevice) | | 1 |
| [`disableDevice`](#disabledevice) | | 1 |
| [`bypassActive`](#bypassactive) | | 1 |
| [`bypassDevice`](#bypassdevice) | Pulse Cmd\_Bypass (or OCmd\_Bypass) and set Interlock/Sts\_BypActive. active=None toggles. | 1 |
| [`setMode`](#setmode) | Set OPER/MAINT/PROG mutually exclusive (Valve / EF / CT style). | 3 |
| [`setPumpMode`](#setpumpmode) | Set Sts\_Oper/Sts\_Maint/Sts\_Prog mutually exclusive (Pump style). | 3 |

### \_resolve {#_resolve}

```python
def _resolve(path)
```
Line 7 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Prefer OPC/Memory sourceTagPath when path is a reference leaf.
```

Used inside the module by: `_readBool`, `_writeRaw`

### \_plcAllowed {#_plcallowed}

```python
def _plcAllowed(path)
```
Line 20 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
plc-write-lock: shared.PlcWriteLock.writeAllowed (an error blocks only paths naming RCP1).
```

Used inside the module by: `_writeRaw`

### \_qualityGood {#_qualitygood}

```python
def _qualityGood(q)
```
Line 30 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

Used inside the module by: `_writeRaw`

### \_writeRaw {#_writeraw}

```python
def _writeRaw(paths, vals)
```
Line 41 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Write resolved paths (raw, no audit); Bad qualities are logged.
```

Used inside the module by: `_write`

### \_write {#_write}

```python
def _write(paths, vals, audit=True, label=None, viewName='Faceplate/Controls')
```
Line 70 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Operator writes go through OpsAudit; audit=False writes raw.
```

Used inside the module by: `bypassDevice`, `closeValve`, `disableDevice`, `enableDevice`, `openValve`, `resetPump`, `resetValve`, `setMode`, `setPumpMode`, `startPump`, `stopPump`, `writeTag`

### startPump {#startpump}

```python
def startPump(tagPath)
```
Line 96 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/StatusSection/CmdRow/BtnStart event component.onActionPerformed` |

### stopPump {#stoppump}

```python
def stopPump(tagPath)
```
Line 108 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/StatusSection/CmdRow/BtnStop event component.onActionPerformed` |

### resetPump {#resetpump}

```python
def resetPump(tagPath)
```
Line 120 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root/StatusSection/CmdRow/BtnReset event component.onActionPerformed` |

### openValve {#openvalve}

```python
def openValve(tagPath, valveType='MO')
```
Line 127 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Open command. SO → Cmd + Cmd_Open; MO → pulse Cmd_Open.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | view | `root/BtnOpen event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | view | `root/BtnOpen event component.onActionPerformed` |

### closeValve {#closevalve}

```python
def closeValve(tagPath, valveType='MO')
```
Line 143 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Close command. SO → clear Cmd/Cmd_Open + pulse Cmd_Close; MO → Cmd_Close.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | view | `root/BtnClose event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | view | `root/BtnClose event component.onActionPerformed` |

### resetValve {#resetvalve}

```python
def resetValve(tagPath)
```
Line 158 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | view | `root/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | view | `root/BtnReset event component.onActionPerformed` |

### writeTag {#writetag}

```python
def writeTag(tagPath, value)
```
Line 165 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Write one tag path, resolving Digitals reference → source when needed.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Sensor/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/LockRow/BtnLock event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/LockRow/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/ModeRow/BtnOper event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/ModeRow/BtnProg event component.onActionPerformed` |

### \_readBool {#_readbool}

```python
def _readBool(path, default=False)
```
Line 173 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

Used inside the module by: `bypassActive`

### enableDevice {#enabledevice}

```python
def enableDevice(tagPath, cmd_leaf='Cmd_Enable', sts_leaf='Disabled')
```
Line 180 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root message handler writeValue` |

### disableDevice {#disabledevice}

```python
def disableDevice(tagPath, cmd_leaf='Cmd_Disable', sts_leaf='Disabled')
```
Line 188 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root message handler writeValue` |

### bypassActive {#bypassactive}

```python
def bypassActive(tagPath)
```
Line 196 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root/DeviceBypass/Body/Cmds/BtnBypass event component.onActionPerformed` |

Used inside the module by: `bypassDevice`

### bypassDevice {#bypassdevice}

```python
def bypassDevice(tagPath, active=None, cmd_leaf='Cmd_Bypass')
```
Line 203 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Pulse Cmd_Bypass (or OCmd_Bypass) and set Interlock/Sts_BypActive. active=None toggles.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root message handler writeValue` |

### setMode {#setmode}

```python
def setMode(tagPath, mode)
```
Line 222 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Set OPER/MAINT/PROG mutually exclusive (Valve / EF / CT style).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeMaint event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeOper event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeProg event dom.onClick` |

### setPumpMode {#setpumpmode}

```python
def setPumpMode(tagPath, mode)
```
Line 236 of `gateways/standard/data/projects/BH/ignition/script-python/shared/ValveCommands/code.py`.

```text
Set Sts_Oper/Sts_Maint/Sts_Prog mutually exclusive (Pump style).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeMaint event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeOper event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root/ModeRow/ModeProg event dom.onClick` |
