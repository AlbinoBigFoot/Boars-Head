---
title: "Navigation.Nav"
sidebar_label: "Navigation.Nav"
description: "Script module Navigation.Nav: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`  
**Lines:** 656. **Functions:** 25. **Called as:** `Navigation.Nav.<function>(...)`

## What the source says

```text
Navigation
Nav items without a view (no page/viewPath, or a page missing from page-config) land here.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.perspective`, `system.tag`, `system.util` |
| Logger names | `Alarm Double Click Navigation`, `Navigation.Nav`, `TreeDebug` |
| Calls modules | [Navigation.Faceplate](./navigation-faceplate.md), [shared.Globe](./shared-globe.md) |
| Called by modules | [shared.Globe](./shared-globe.md) |

<details>
<summary>Module constants (7)</summary>

| Name | Value |
|---|---|
| `NO_VIEW_PAGE` | `'/no-view'` |
| `NAV_TAG_PATH` | `'[default]_Config/Navigation'` |
| `NAV_CACHE_S` | `60` |
| `DEMO_TAG` | `'[default]_Config/DemoEnterpriseNav'` |
| `TITLE_SKIP` | `set(['Boars Head', 'Utility', 'Devices', 'Operations', 'A...` |
| `TITLE_HOME` | `'Boars Head International'` |
| `TITLE_LOCAL_HOME` | `'Groveport Utility Overview'` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_pageRoutes`](#_pageroutes) (internal) | page-config URLs for this project, cached 60 s. Empty set when they can't be read. | 0 |
| [`_hasRoute`](#_hasroute) (internal) | | 1 |
| [`navigate`](#navigate) | Navigate from the plant nav tree. | 9 |
| [`encodeUrlPayload`](#encodeurlpayload) | Encodes the payload with characters that are allowed in the url. | 0 |
| [`decodeUrlPayload`](#decodeurlpayload) | Inverse of encodeUrlPayload function. | 0 |
| [`decodeSpecialCases`](#decodespecialcases) | None is encoded as the string "None". | 0 |
| [`cleanObjForUrlEncoding`](#cleanobjforurlencoding) | urllib doesn't handle unicode, so convert before encoding. | 0 |
| [`findItemIndex`](#finditemindex) | Locate a tree index path by viewPath/tagPath and/or page-config route. | 2 |
| [`alarmNavigation`](#alarmnavigation) | Double Clicking on Alarm Event on a Alarm Summary page will execute below alarmNavigation function and navigate to a respective alarm event device details view | 0 |
| [`_to_py`](#_to_py) (internal) | Coerce Document / Java maps to plain Python via encode/decode. | 0 |
| [`_as_items`](#_as_items) (internal) | Document may be \{items:[...]\} or a bare list of tree nodes. | 0 |
| [`_deep_decode`](#_deep_decode) (internal) | Unwrap nested JSON strings that Document tags sometimes embed. | 0 |
| [`_read_nav_items_from_tag`](#_read_nav_items_from_tag) (internal) | Read live Navigation Document; fall back to tag defaultValue if empty. | 0 |
| [`getNavItems`](#getnavitems) | Full nav tree from the Document tag, cached gateway-wide for NAV\_CACHE\_S (nav edits show within a minute). | 0 |
| [`demoEnabled`](#demoenabled) | | 0 |
| [`_shown`](#_shown) (internal) | | 0 |
| [`pageTitle`](#pagetitle) | Header title for a page from its nav tree position, grouping folders skipped: | 1 |
| [`findItemData`](#finditemdata) | | 0 |
| [`_resolve_is_admin`](#_resolve_is_admin) (internal) | | 0 |
| [`_node_allowed`](#_node_allowed) (internal) | | 0 |
| [`seedCacheFrom`](#seedcachefrom) | Prime NavMasterTreeCache from a Python list (view.custom.items seed). | 0 |
| [`getChildrenAt`](#getchildrenat) | Return children at item\_path from the full master tree (no Loading stubs). | 0 |
| [`getMasterTree`](#getmastertree) | Full decoded nav tree (admin-filtered). Used by search helpers if needed. | 0 |
| [`findItemPath`](#finditempath) | Locate index path in master cache by viewPath / tagPath / page. | 0 |
| [`flushCache`](#flushcache) | | 1 |

### \_pageRoutes {#_pageroutes}

```python
def _pageRoutes()
```
Line 7 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
page-config URLs for this project, cached 60 s. Empty set when they can't be read.
```

Used inside the module by: `_hasRoute`

### \_hasRoute {#_hasroute}

```python
def _hasRoute(page)
```
Line 42 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Globe._routeOk` | script | |

Used inside the module by: `navigate`

### navigate {#navigate}

```python
def navigate(data=None)
```
Line 59 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Navigate from the plant nav tree.

BH tree item data shape:
  action: 'page' | 'faceplate' | '' (no view -> stays on the current page)
  page: page-config path e.g. '/evaporators'
  viewPath: Perspective view path (faceplate or legacy SPA)
  tagPath: device UDT path for faceplates / overview context

Also maps AdhocTrend viewPaths to page-config URLs; other payloads keep
the Lightspeed /data/<encoded> SPA style.
Returns True when it navigated (or opened a faceplate), False when the item has nowhere to go.
```

<details>
<summary>Called from 9 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/00_Docked/Navigation` | view | `root/Tree event component.onItemClicked` |
| `00_Pages/00_Docked/TempNav` | view | `root/Tree event component.onItemClicked` |
| `00_Pages/Boars Head/LandingPage/Globe` | view | `root message handler globeNavigate` |
| `00_Pages/Groveport/Site/OverviewExecutive` | view | `root/Header/TitleRow/HeaderActions/BtnClassic event component.onActionPerformed` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw/Room_MachineRoom event dom.onClick` |
| `02_Components/00_Controls/NavButton` | view | `root event dom.onClick` |
| `02_Components/01_Devices/Evaporator` | view | `root event dom.onClick` |
| `02_Components/02_Widgets/SiteCard` | view | `root event dom.onClick` |
| `03_Elements/03_Table/CgHit` | view | `root event dom.onDoubleClick` |
</details>

### encodeUrlPayload {#encodeurlpayload}

```python
def encodeUrlPayload(payload)
```
Line 160 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Encodes the payload with characters that are allowed in the url.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `navigate`

### decodeUrlPayload {#decodeurlpayload}

```python
def decodeUrlPayload(encodedPayload)
```
Line 169 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Inverse of encodeUrlPayload function.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### decodeSpecialCases {#decodespecialcases}

```python
def decodeSpecialCases(obj)
```
Line 184 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
None is encoded as the string "None".
CAUTION: This means any actual string "None" in the payload will be converted to None.
Ampersands in strings were replaced during encoding.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `decodeUrlPayload`

### cleanObjForUrlEncoding {#cleanobjforurlencoding}

```python
def cleanObjForUrlEncoding(obj)
```
Line 203 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
urllib doesn't handle unicode, so convert before encoding.
This also handles the conversion from perspective object to vanilla PyDictionary.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `encodeUrlPayload`

### findItemIndex {#finditemindex}

```python
def findItemIndex(items, viewPath=None, tagPath=None, page=None, currentPath=[])
```
Line 220 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Locate a tree index path by viewPath/tagPath and/or page-config route.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/00_Docked/Navigation` | view | `root/Tree binding custom.itemPath` |
| `00_Pages/00_Docked/TempNav` | view | `root/Tree binding custom.itemPath` |

### alarmNavigation {#alarmnavigation}

```python
def alarmNavigation(source='')
```
Line 248 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Double Clicking on Alarm Event on a Alarm Summary page will execute below alarmNavigation function and navigate to a respective alarm event device details view
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### \_to\_py {#_to_py}

```python
def _to_py(obj)
```
Line 271 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Coerce Document / Java maps to plain Python via encode/decode.
```

Used inside the module by: `_as_items`, `_node_allowed`, `findItemPath`, `getChildrenAt`, `getMasterTree`, `seedCacheFrom`

### \_as\_items {#_as_items}

```python
def _as_items(obj)
```
Line 293 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Document may be {items:[...]} or a bare list of tree nodes.
```

Used inside the module by: `_read_nav_items_from_tag`, `seedCacheFrom`

### \_deep\_decode {#_deep_decode}

```python
def _deep_decode(node)
```
Line 308 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Unwrap nested JSON strings that Document tags sometimes embed.
```

Used inside the module by: `_read_nav_items_from_tag`, `seedCacheFrom`

### \_read\_nav\_items\_from\_tag {#_read_nav_items_from_tag}

```python
def _read_nav_items_from_tag()
```
Line 327 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Read live Navigation Document; fall back to tag defaultValue if empty.
```

Used inside the module by: `getNavItems`

### getNavItems {#getnavitems}

```python
def getNavItems()
```
Line 362 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Full nav tree from the Document tag, cached gateway-wide for NAV_CACHE_S (nav edits show within a minute).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `findItemPath`, `getChildrenAt`, `getMasterTree`, `pageTitle`

### demoEnabled {#demoenabled}

```python
def demoEnabled()
```
Line 382 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_node_allowed`, `navigate`, `pageTitle`

### \_shown {#_shown}

```python
def _shown(data, demo)
```
Line 390 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

Used inside the module by: `pageTitle`

### pageTitle {#pagetitle}

```python
def pageTitle(path)
```
Line 399 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Header title for a page from its nav tree position, grouping folders skipped:
/machine-room -> 'Groveport Machine Room', /tanks -> 'Groveport Machine Room Tanks'. A device-type page is
named after its tag folder (nav 'Comps' -> 'Compressors'). A node's data.title overrides the whole title.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/00_Docked/Navigation` | view | `root/Brand binding props.text` |

### findItemData {#finditemdata}

```python
def findItemData(tagPath)
```
Line 444 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `alarmNavigation`

### \_resolve\_is\_admin {#_resolve_is_admin}

```python
def _resolve_is_admin(is_admin)
```
Line 476 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

Used inside the module by: `getChildrenAt`, `getMasterTree`

### \_node\_allowed {#_node_allowed}

```python
def _node_allowed(node, is_admin, perms=None)
```
Line 481 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

Used inside the module by: `getChildrenAt`, `getMasterTree`

### seedCacheFrom {#seedcachefrom}

```python
def seedCacheFrom(items)
```
Line 509 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Prime NavMasterTreeCache from a Python list (view.custom.items seed).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### getChildrenAt {#getchildrenat}

```python
def getChildrenAt(item_path, is_admin=None)
```
Line 527 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Return children at item_path from the full master tree (no Loading stubs).

Kept for optional callers; the Navigation Tree UI binds the full tree
from view.custom.items and does not use this for expand/collapse.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### getMasterTree {#getmastertree}

```python
def getMasterTree(is_admin=None)
```
Line 593 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Full decoded nav tree (admin-filtered). Used by search helpers if needed.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### findItemPath {#finditempath}

```python
def findItemPath(viewPath=None, tagPath=None, page=None)
```
Line 623 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

```text
Locate index path in master cache by viewPath / tagPath / page.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### flushCache {#flushcache}

```python
def flushCache()
```
Line 655 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `globe/mapMarkers` | webdev | `doPost` |
