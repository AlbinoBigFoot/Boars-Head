---
title: "shared.Pax"
sidebar_label: "shared.Pax"
description: "Script module shared.Pax: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`  
**Lines:** 1268. **Functions:** 7. **Called as:** `shared.Pax.<function>(...)`

## What the source says

```text


A device's key (part()) comes from its UDT type and its configured PLC part (Motor, Valve, AIn ...);
FIELDS[part] maps an old HMI member (<Member>/Value) to the nested PAX member that replaces it. Read only.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag` |
| Called by modules | [shared.FaceplateTrend](./shared-faceplatetrend.md), [shared.Forms](./shared-forms.md), [shared.Overview](./shared-overview.md), [shared.ValveCommands](./shared-valvecommands.md) |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `FIELDS` | `{'AIn': {'Cfg_Desc': 'AIn/Cfg_Desc', 'Cfg_EU': 'AIn/Cfg_E...` |
| `KEYS` | `{'Devices/Compressor': 'Comp', 'Devices/DischargeSequence...` |
| `SUBS` | `['DI_HLCO', 'DI_HiLevel', 'DI_LoLo', 'DI_OPL', 'Fan 1', '...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`part`](#part) | Device key of an instance (its UDT type / configured PLC part; '' = not a PLC device). | 6 |
| [`device`](#device) | Device instance for a member root: &lt;device&gt;/Interlock, &lt;tank&gt;/LevelInput, &lt;tank&gt;/DI\_HLCO ... -&gt; the device. | 2 |
| [`resolve`](#resolve) | PAX member for &lt;base&gt;/&lt;leaf&gt; (base = a device or one of its SUBS roots) of a mapped device, else None. | 1 |
| [`configured`](#configured) | False when the part behind a PAX member is disabled on this instance (no PLC object, e.g. HPR PressAIn). | 1 |
| [`mapRows`](#maprows) | Overview table rows (cells = '&lt;device&gt;/&lt;field&gt;' member paths): mapped devices read their PAX members. | 1 |
| [`livePath`](#livepath) | '&lt;device&gt;/&lt;field&gt;/Value' of a PLC-mapped device -&gt; its PAX member (else the path itself) - for scripts that read | 6 |
| [`member`](#member) | PAX member path for an old field of a mapped device, else None. | 1 |

### part {#part}

```python
def part(devicePath)
```
Line 1171 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
Device key of an instance (its UDT type / configured PLC part; '' = not a PLC device).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | view | `root/Rows binding props.instances` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `binding custom.penOptions` |
| `shared.FaceplateTrend.defaultPens` | script | |
| `shared.Overview.buildInstancesPayload` | script | |
| `shared.Overview.discoverPointFields` | script | |
| `shared.ValveCommands._write` | script | |

Used inside the module by: `livePath`, `mapRows`, `member`

### device {#device}

```python
def device(base)
```
Line 1193 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
Device instance for a member root: <device>/Interlock, <tank>/LevelInput, <tank>/DI_HLCO ... -> the device.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | view | `root/Rows binding props.instances` |
| `shared.ValveCommands._write` | script | |

Used inside the module by: `livePath`, `resolve`

### resolve {#resolve}

```python
def resolve(base, leaf, pax=None)
```
Line 1200 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
PAX member for <base>/<leaf> (base = a device or one of its SUBS roots) of a mapped device, else None.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | view | `root/Rows binding props.instances` |

Used inside the module by: `livePath`

### configured {#configured}

```python
def configured(devicePath, rel, cache=None)
```
Line 1207 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
False when the part behind a PAX member is disabled on this instance (no PLC object, e.g. HPR PressAIn).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Overview.buildInstancesPayload` | script | |

Used inside the module by: `mapRows`

### mapRows {#maprows}

```python
def mapRows(rows)
```
Line 1223 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
Overview table rows (cells = '<device>/<field>' member paths): mapped devices read their PAX members.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.data` |

### livePath {#livepath}

```python
def livePath(path, cache=None)
```
Line 1245 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
'<device>/<field>/Value' of a PLC-mapped device -> its PAX member (else the path itself) - for scripts that read
device fields by literal path (shared.Forms live values).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_HLCO event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_HiLevel event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_LoLo event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_OPL event dom.onClick` |
| `shared.Forms.liveValues` | script | |
| `shared.ValveCommands._resolve` | script | |

### member {#member}

```python
def member(devicePath, field, pax=None)
```
Line 1264 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Pax/code.py`.

```text
PAX member path for an old field of a mapped device, else None.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Overview.buildInstancesPayload` | script | |

Used inside the module by: `mapRows`, `resolve`
