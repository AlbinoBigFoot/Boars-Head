---
title: "shared.WebAuth"
sidebar_label: "shared.WebAuth"
description: "Script module shared.WebAuth: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`  
**Lines:** 73. **Functions:** 5. **Called as:** `shared.WebAuth.<function>(...)`

## What the source says

```text
Login check for WebDev resources that a logged-in Perspective session loads (iframe src, fetch from the iframe).

The browser sends the same HTTP session cookie to /system/webdev/... as to the Perspective client, and the gateway
keeps that browser's Perspective project sessions on the HTTP session (attribute "perspective-session",
a PerspectiveSessionCollection). perspectiveUser() returns the user of THIS project's session when its web auth
status is authenticated + authorized, else None. No HTTP Basic prompt, so it works inside an iframe.
WebDev's own require-auth is HTTP Basic only (and text resources have no auth at all). docs/security-access.md
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.util` |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `LOGGER` | `'BH.WebAuth'` |
| `PROJECT` | `'BH'` |
| `_ATTR` | `'perspective-session'` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_unwrap`](#_unwrap) (internal) | | 0 |
| [`perspectiveUser`](#perspectiveuser) | Username of the authenticated BH Perspective session of the browser that sent this request, else None. | 9 |
| [`hasBasicHeader`](#hasbasicheader) | | 1 |
| [`deny`](#deny) | Plain JSON refusal, no WWW-Authenticate header (an iframe must never get a Basic login prompt). | 58 |
| [`noStore`](#nostore) | | 6 |

### \_unwrap {#_unwrap}

```python
def _unwrap(v)
```
Line 14 of `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`.

_No docstring._

Used inside the module by: `perspectiveUser`

### perspectiveUser {#perspectiveuser}

```python
def perspectiveUser(request, project=None)
```
Line 20 of `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`.

```text
Username of the authenticated BH Perspective session of the browser that sent this request, else None.
```

<details>
<summary>Called from 9 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `globe/map` | webdev | `doGet` |
| `globe/mapMarkers` | webdev | `doGet` |
| `globe/mapMarkers` | webdev | `doPost` |
| `rack3d/lib` | webdev | `doGet` |
| `rack3d/state` | webdev | `doGet` |
| `rack3d/view` | webdev | `doGet` |
| `relay3d/lib` | webdev | `doGet` |
| `relay3d/state` | webdev | `doGet` |
| `relay3d/view` | webdev | `doGet` |
</details>

### hasBasicHeader {#hasbasicheader}

```python
def hasBasicHeader(request)
```
Line 51 of `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `globe/mapMarkers` | webdev | `doGet` |

### deny {#deny}

```python
def deny(request, status=401, reason=None)
```
Line 58 of `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`.

```text
Plain JSON refusal, no WWW-Authenticate header (an iframe must never get a Basic login prompt).
```

<details>
<summary>Called from 58 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `globe/map` | webdev | `doDelete` |
| `globe/map` | webdev | `doGet` |
| `globe/map` | webdev | `doHead` |
| `globe/map` | webdev | `doOptions` |
| `globe/map` | webdev | `doPatch` |
| `globe/map` | webdev | `doPost` |
| `globe/map` | webdev | `doPut` |
| `globe/map` | webdev | `doTrace` |
| `globe/mapMarkers` | webdev | `doGet` |
| `globe/mapMarkers` | webdev | `doPost` |
| `rack3d/lib` | webdev | `doDelete` |
| `rack3d/lib` | webdev | `doGet` |
| `rack3d/lib` | webdev | `doHead` |
| `rack3d/lib` | webdev | `doOptions` |
| `rack3d/lib` | webdev | `doPatch` |
| `rack3d/lib` | webdev | `doPost` |
| `rack3d/lib` | webdev | `doPut` |
| `rack3d/lib` | webdev | `doTrace` |
| `rack3d/state` | webdev | `doDelete` |
| `rack3d/state` | webdev | `doGet` |
| `rack3d/state` | webdev | `doHead` |
| `rack3d/state` | webdev | `doOptions` |
| `rack3d/state` | webdev | `doPatch` |
| `rack3d/state` | webdev | `doPost` |
| `rack3d/state` | webdev | `doPut` |
| `rack3d/state` | webdev | `doTrace` |
| `rack3d/view` | webdev | `doDelete` |
| `rack3d/view` | webdev | `doGet` |
| `rack3d/view` | webdev | `doHead` |
| `rack3d/view` | webdev | `doOptions` |
| `rack3d/view` | webdev | `doPatch` |
| `rack3d/view` | webdev | `doPost` |
| `rack3d/view` | webdev | `doPut` |
| `rack3d/view` | webdev | `doTrace` |
| `relay3d/lib` | webdev | `doDelete` |
| `relay3d/lib` | webdev | `doGet` |
| `relay3d/lib` | webdev | `doHead` |
| `relay3d/lib` | webdev | `doOptions` |
| `relay3d/lib` | webdev | `doPatch` |
| `relay3d/lib` | webdev | `doPost` |
| `relay3d/lib` | webdev | `doPut` |
| `relay3d/lib` | webdev | `doTrace` |
| `relay3d/state` | webdev | `doDelete` |
| `relay3d/state` | webdev | `doGet` |
| `relay3d/state` | webdev | `doHead` |
| `relay3d/state` | webdev | `doOptions` |
| `relay3d/state` | webdev | `doPatch` |
| `relay3d/state` | webdev | `doPost` |
| `relay3d/state` | webdev | `doPut` |
| `relay3d/state` | webdev | `doTrace` |
| `relay3d/view` | webdev | `doDelete` |
| `relay3d/view` | webdev | `doGet` |
| `relay3d/view` | webdev | `doHead` |
| `relay3d/view` | webdev | `doOptions` |
| `relay3d/view` | webdev | `doPatch` |
| `relay3d/view` | webdev | `doPost` |
| `relay3d/view` | webdev | `doPut` |
| `relay3d/view` | webdev | `doTrace` |
</details>

### noStore {#nostore}

```python
def noStore(request)
```
Line 69 of `gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `globe/map` | webdev | `doGet` |
| `globe/mapMarkers` | webdev | `doGet` |
| `rack3d/state` | webdev | `doGet` |
| `rack3d/view` | webdev | `doGet` |
| `relay3d/state` | webdev | `doGet` |
| `relay3d/view` | webdev | `doGet` |
