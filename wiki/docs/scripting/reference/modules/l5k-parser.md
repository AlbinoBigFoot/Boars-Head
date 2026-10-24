---
title: "L5K.Parser"
sidebar_label: "L5K.Parser"
description: "Script module L5K.Parser: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`  
**Lines:** 1318. **Functions:** 17. **Called as:** `L5K.Parser.<function>(...)`

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.dataset`, `system.util` |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `DATA_TYPE_MAPPING_IGNITION` | `{'BOOL': 'Boolean', 'BIT': 'Boolean', 'SINT': 'Int1', 'IN...` |
| `DATA_TYPE_MAPPING_SIMULATION` | `{'BOOL': 'Boolean', 'BIT': 'Boolean', 'SINT': 'Int16', 'I...` |
| `DEFAULT_SIMULATION` | `{'BOOL': 'false', 'BIT': 'false', 'SINT': '0', 'INT': '0'...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`searchOne`](#searchone) | | 0 |
| [`search`](#search) | | 0 |
| [`matchOne`](#matchone) | | 0 |
| [`findall`](#findall) | | 0 |
| [`findallOne`](#findallone) | | 0 |
| [`parseTags`](#parsetags) | | 0 |
| [`parseTag`](#parsetag) | | 0 |
| [`parse`](#parse) | | 1 |
| [`addSimulationTag`](#addsimulationtag) | | 0 |
| [`getSimulationUDTTags`](#getsimulationudttags) | | 0 |
| [`generateSimulationCSV`](#generatesimulationcsv) | | 1 |
| [`addUDTTag`](#addudttag) | | 0 |
| [`getUDTTags`](#getudttags) | | 0 |
| [`addTag`](#addtag) | | 0 |
| [`buildUDTTagOverrides`](#buildudttagoverrides) | | 0 |
| [`generateUDTExport`](#generateudtexport) | | 1 |
| [`generateTagExport`](#generatetagexport) | | 1 |

### searchOne {#searchone}

```python
def searchOne(regexStr, findStr, defaultStr=None, flags=re.DOTALL)
```
Line 7 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parseTag`, `parse`

### search {#search}

```python
def search(regexStr, findStr, flags=re.DOTALL)
```
Line 16 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parseTag`, `parseTags`, `parse`

### matchOne {#matchone}

```python
def matchOne(regexStr, findStr, defaultStr=None, flags=re.DOTALL)
```
Line 22 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### findall {#findall}

```python
def findall(regexStr, findStr, flags=re.DOTALL)
```
Line 31 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parseTag`, `parse`

### findallOne {#findallone}

```python
def findallOne(regexStr, findStr, flags=re.DOTALL)
```
Line 37 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parse`

### parseTags {#parsetags}

```python
def parseTags(currentUdts, localTags, folder, tagsSection, comments, allowHidden=False, selectTags=False, useStoredValues=True)
```
Line 43 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parse`

### parseTag {#parsetag}

```python
def parseTag(currentUdts, localTags, folder, tags, tagSection, sectionType, comments, allowHidden, selectTags, useStoredValues)
```
Line 63 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `parseTags`, `parse`

### parse {#parse}

```python
def parse(l5kFile, selectTags=False, allowHidden=False, useStoredValues=True)
```
Line 176 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Tools/L5K/Parser` | view | `root/FileUpload event component.onFileReceived` |

### addSimulationTag {#addsimulationtag}

```python
def addSimulationTag(udts, udtStrings, tagItem, opcItemPath, simulationFunctionValue=None)
```
Line 793 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `generateSimulationCSV`, `getSimulationUDTTags`

### getSimulationUDTTags {#getsimulationudttags}

```python
def getSimulationUDTTags(udts, udtStrings, dataType, opcItemPath, simulationFunctionValues)
```
Line 840 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `addSimulationTag`

### generateSimulationCSV {#generatesimulationcsv}

```python
def generateSimulationCSV(udtItems, globalTagItems, programItems)
```
Line 892 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Tools/L5K/Parser` | view | `root/Create Simulation Program Export event component.onActionPerformed` |

### addUDTTag {#addudttag}

```python
def addUDTTag(udtPrefix, udts, udtStrings, tagItem, inUDTInstance, udtsNotFound)
```
Line 922 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `generateUDTExport`, `getUDTTags`

### getUDTTags {#getudttags}

```python
def getUDTTags(udtPrefix, udts, udtStrings, dataType, udtsNotFound)
```
Line 1009 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `addUDTTag`

### addTag {#addtag}

```python
def addTag(deviceName, udtPrefix, udtStrings, udts, tagItem, comments, opcItemPath, inUDTInstance=False)
```
Line 1021 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `generateTagExport`

### buildUDTTagOverrides {#buildudttagoverrides}

```python
def buildUDTTagOverrides(udtName, udtTagsObj, udts, udtStrings)
```
Line 1145 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `addTag`

### generateUDTExport {#generateudtexport}

```python
def generateUDTExport(udtPrefix, udtItems, globalTagItems, programItems)
```
Line 1188 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Tools/L5K/Parser` | view | `root/Create UDT Tag Export event component.onActionPerformed` |

### generateTagExport {#generatetagexport}

```python
def generateTagExport(deviceName, udtPrefix, udtItems, globalTagItems, programItems, comments)
```
Line 1284 of `gateways/standard/data/projects/BH/ignition/script-python/L5K/Parser/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Tools/L5K/Parser` | view | `root/Create Tag Export event component.onActionPerformed` |
