---
title: "shared.PlcWriteLock"
sidebar_label: "shared.PlcWriteLock"
description: "Script module shared.PlcWriteLock: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`  
**Lines:** 428. **Functions:** 26. **Called as:** `shared.PlcWriteLock.<function>(...)`

## What the source says

```text

Docs:
docs/plc-write-lock.md.

User (2026-10-23): "I don't need that PLC Write Lock view. Remove it, delete the view. Just have a boolean under _Config
that allows me to unlock and lock the read only param of each tag."

ONE boolean, [default]_Config/PlcWriteLock/Locked (true = locked), drives readOnly on every tag that reads the RCP1
controller (a LIVE PRODUCTION PLC):
- every AtomicTag under [default]_RCP1_ (the browsed controller tags);
- every OPC member of the UDT DEFINITIONS in TYPE_FOLDERS (PLC/** incl. Modules / Controllers / Sites, PLC_Ref,
Devices, Units) - set on the definition (_types_), so every instance inherits it; no per-instance overrides.
Ignition 8.3 cannot bind a tag's readOnly property to another tag's value (an Expression / Tag binding on readOnly is
dropped on import - checked 2026-10-23), so the gateway tag-change event 'plcWriteLock' on the boolean calls
onLockChange(), which applies readOnly = Locked (only the tags whose readOnly differs; in chunks of CHUNK tags, in one
background worker that re-reads the boolean until it settles) and logs each flip with counts.
Fail-safe: a bad / null / unreadable boolean counts as LOCKED; on gateway startup (JVM uptime < STARTUP_S) the lock is
forced: Locked is written true and readOnly re-asserted. HMI writes are refused while locked (writeAllowed: shared.Audit
.writeTag / shared.Alerts.confirmApplyWrite / shared.ValveCommands). readOnly is the SOFT layer; the HARD layer is the
OPC UA server device permission - a PLC write needs BOTH
Locked=false AND the server block removed.
Testing: the separate boolean TEST_LOCKED + tag-change event 'plcWriteLockTest' (onTestChange) drive only TEST_ROOT
memory tags and the TEST_TYPES UDT folder - they never touch [RCP1] / _RCP1_.
Configuration only: the configure payloads carry name + readOnly, never a value; nothing here writes a PLC value.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag`, `system.util` |
| Logger names | `shared.PlcWriteLock` |
| Calls modules | [shared.Alerts](./shared-alerts.md) |
| Called by modules | [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md), [shared.ValveCommands](./shared-valvecommands.md) |

<details>
<summary>Module constants (12)</summary>

| Name | Value |
|---|---|
| `BASE` | `'[default]_Config/PlcWriteLock/'` |
| `T_LOCKED` | `BASE + 'Locked'` |
| `RCP1_ROOT` | `'[default]_RCP1_'` |
| `TYPE_FOLDERS` | `('PLC', 'PLC_Ref', 'Devices', 'Units')` |
| `TEST_LOCKED` | `BASE + '_Test/Locked'` |
| `TEST_ROOT` | `BASE + '_Test/Tags'` |
| `TEST_TYPES` | `('_PlcWriteLockTest',)` |
| `CHUNK` | `5000` |
| `CHUNK_PAUSE_MS` | `2000` |
| `STARTUP_S` | `600` |
| `REAL` | `_Target('PLC', T_LOCKED, (RCP1_ROOT,), TYPE_FOLDERS, True...` |
| `TEST` | `_Target('TEST', TEST_LOCKED, (TEST_ROOT,), TEST_TYPES, Fa...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_text`](#_text) (internal) | | 0 |
| [`_norm`](#_norm) (internal) | [default]-qualified tag path with '/' separators and '..' segments resolved. | 0 |
| [`_under`](#_under) (internal) | | 0 |
| [`_isRcp1`](#_isrcp1) (internal) | | 0 |
| [`_lockedFrom`](#_lockedfrom) (internal) | Fail-safe: anything but a good, non-null False counts as locked. | 0 |
| [`status`](#status) | \{locked\}. Fail-safe: unreadable = locked. | 0 |
| [`isLocked`](#islocked) | | 0 |
| [`resolve`](#resolve) | (final tag path, kind) for a write target, following reference tags to their source. kind: rcp1-tag (under | 0 |
| [`writeAllowed`](#writeallowed) | False when a write to tagPath would reach the RCP1 controller while Locked (or the lock is unreadable). | 6 |
| [`_dataDir`](#_datadir) (internal) | ------------------------------------------------------------------------------------------------ tag store (files) | 0 |
| [`_resDir`](#_resdir) (internal) | | 0 |
| [`_readJson`](#_readjson) (internal) | | 0 |
| [`_unesc`](#_unesc) (internal) | | 0 |
| [`storeTags`](#storetags) | \{tag path: readOnly\} for every AtomicTag under a [default] folder, from the file-based tag store | 0 |
| [`typeMembers`](#typemembers) | \{'[default]\_types\_/&lt;folder&gt;/&lt;udt&gt;/&lt;member path&gt;': readOnly\} for the OPC members (opcOnly) - or every memory / | 0 |
| [`_chunks`](#_chunks) (internal) | [\{parent: [names]\}, ...] - whole parent folders per chunk, about CHUNK tags each. | 0 |
| [`_setReadOnly`](#_setreadonly) (internal) | Merge \{name, readOnly\} per parent (configuration only), CHUNK tags at a time with a pause between chunks. | 0 |
| [`_Target`](#_target) (internal) | What one boolean drives: the real RCP1 set, or the memory test set (never both). | 0 |
| [`apply`](#apply) | readOnly on every driven tag of target whose readOnly differs; returns \{total, changed, bad, mismatch\}. | 0 |
| [`_shared`](#_shared) (internal) | (Java lock, Java pending flag) per target, kept in the gateway globals so they survive project script reloads | 0 |
| [`_worker`](#_worker) (internal) | Applies until the boolean stops moving (one worker per target, gateway-wide; a flip during a run is picked up | 0 |
| [`_uptimeS`](#_uptimes) (internal) | | 0 |
| [`_onChange`](#_onchange) (internal) | | 0 |
| [`onLockChange`](#onlockchange) | Gateway tag-change event 'plcWriteLock' on [default]\_Config/PlcWriteLock/Locked (value + quality changes). | 1 |
| [`onTestChange`](#ontestchange) | Gateway tag-change event 'plcWriteLockTest' on the TEST boolean: drives only the memory test tags / test types. | 1 |
| [`counts`](#counts) | Read-only summary \{total, readOnly, writable\} of a target from the tag store files (verification). | 0 |
| [`selfTest`](#selftest) | Read-only check of the guards: nothing is written. | 0 |

### \_text {#_text}

```python
def _text(v)
```
Line 39 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `_norm`, `resolve`, `typeMembers`

### \_norm {#_norm}

```python
def _norm(path)
```
Line 48 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
[default]-qualified tag path with '/' separators and '..' segments resolved.
```

Used inside the module by: `resolve`, `writeAllowed`

### \_under {#_under}

```python
def _under(path, scope)
```
Line 66 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `_Target`, `_isRcp1`

### \_isRcp1 {#_isrcp1}

```python
def _isRcp1(path)
```
Line 70 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `resolve`

### \_lockedFrom {#_lockedfrom}

```python
def _lockedFrom(qv)
```
Line 75 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Fail-safe: anything but a good, non-null False counts as locked.
```

Used inside the module by: `_onChange`, `_worker`, `status`

### status {#status}

```python
def status()
```
Line 83 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
{locked}. Fail-safe: unreadable = locked.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `isLocked`, `selfTest`

### isLocked {#islocked}

```python
def isLocked()
```
Line 91 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `writeAllowed`

### resolve {#resolve}

```python
def resolve(tagPath, hops=6)
```
Line 96 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
(final tag path, kind) for a write target, following reference tags to their source. kind: rcp1-tag (under
[default]_RCP1_), rcp1-opc ([RCP1] OPC item elsewhere), opc, memory, expr, reference, reference-param, unknown, ...
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `selfTest`, `writeAllowed`

### writeAllowed {#writeallowed}

```python
def writeAllowed(tagPath, who='')
```
Line 138 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
False when a write to tagPath would reach the RCP1 controller while Locked (or the lock is unreadable).
Unresolvable targets that name RCP1 count as RCP1.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `02_Components/01_Devices/LTU` | view | `root/ResetRow/ResetCount event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Reset event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Silence event component.onActionPerformed` |
| `shared.Alerts.confirmApplyWrite` | script | |
| `shared.Audit._plcWriteBlocked` | script | |
| `shared.ValveCommands._plcAllowed` | script | |

Used inside the module by: `selfTest`

### \_dataDir {#_datadir}

```python
def _dataDir()
```
Line 157 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
------------------------------------------------------------------------------------------------ tag store (files)
```

Used inside the module by: `_resDir`

### \_resDir {#_resdir}

```python
def _resDir(kind)
```
Line 165 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `storeTags`, `typeMembers`

### \_readJson {#_readjson}

```python
def _readJson(path)
```
Line 170 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `storeTags`, `typeMembers`

### \_unesc {#_unesc}

```python
def _unesc(rel)
```
Line 178 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `storeTags`, `typeMembers`

### storeTags {#storetags}

```python
def storeTags(root)
```
Line 182 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
{tag path: readOnly} for every AtomicTag under a [default] folder, from the file-based tag store
(tag-definition/default/<root>/**/tags.json + udts.json) - far faster than browsing 35K tags.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_Target`

### typeMembers {#typemembers}

```python
def typeMembers(folders, opcOnly=True)
```
Line 222 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
{'[default]_types_/<folder>/<udt>/<member path>': readOnly} for the OPC members (opcOnly) - or every memory /
OPC member (test types) - defined in the UDT definitions under the given type folders (sub folders included).
Members of nested UDT instances are skipped: they come from their own type (no per-instance overrides).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_Target`

### \_chunks {#_chunks}

```python
def _chunks(paths)
```
Line 258 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
[{parent: [names]}, ...] - whole parent folders per chunk, about CHUNK tags each.
```

Used inside the module by: `_setReadOnly`

### \_setReadOnly {#_setreadonly}

```python
def _setReadOnly(paths, readOnly)
```
Line 276 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Merge {name, readOnly} per parent (configuration only), CHUNK tags at a time with a pause between chunks.
Returns the paths whose configure call did not report Good.
```

Used inside the module by: `apply`

### \_Target {#_target}

```python
class _Target
```
Line 300 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
What one boolean drives: the real RCP1 set, or the memory test set (never both).
```

Used inside the module by: `(module level)`

### apply {#apply}

```python
def apply(target, readOnly, why)
```
Line 323 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
readOnly on every driven tag of target whose readOnly differs; returns {total, changed, bad, mismatch}.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_worker`

### \_shared {#_shared}

```python
def _shared(name)
```
Line 337 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
(Java lock, Java pending flag) per target, kept in the gateway globals so they survive project script reloads
(each project save restarts the tag-change script; a module-level lock would let two workers run at once).
```

Used inside the module by: `_worker`

### \_worker {#_worker}

```python
def _worker(target, why)
```
Line 350 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Applies until the boolean stops moving (one worker per target, gateway-wide; a flip during a run is picked up
after it - the final state always follows the latest boolean value).
```

Used inside the module by: `_onChange`

### \_uptimeS {#_uptimes}

```python
def _uptimeS()
```
Line 372 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `_onChange`

### \_onChange {#_onchange}

```python
def _onChange(target, initialChange, newValue, startupForce)
```
Line 380 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

_No docstring._

Used inside the module by: `onLockChange`, `onTestChange`

### onLockChange {#onlockchange}

```python
def onLockChange(initialChange, newValue, event=None)
```
Line 400 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Gateway tag-change event 'plcWriteLock' on [default]_Config/PlcWriteLock/Locked (value + quality changes).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `plcWriteLock` | gateway tag-change | `onTagChange.py` |

### onTestChange {#ontestchange}

```python
def onTestChange(initialChange, newValue, event=None)
```
Line 405 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Gateway tag-change event 'plcWriteLockTest' on the TEST boolean: drives only the memory test tags / test types.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `plcWriteLockTest` | gateway tag-change | `onTagChange.py` |

### counts {#counts}

```python
def counts(which='PLC')
```
Line 410 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Read-only summary {total, readOnly, writable} of a target from the tag store files (verification).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### selfTest {#selftest}

```python
def selfTest()
```
Line 418 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PlcWriteLock/code.py`.

```text
Read-only check of the guards: nothing is written.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._
