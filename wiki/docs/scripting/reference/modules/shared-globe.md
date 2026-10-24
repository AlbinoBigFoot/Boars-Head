---
title: "shared.Globe"
sidebar_label: "shared.Globe"
description: "Script module shared.Globe: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`  
**Lines:** 168. **Functions:** 8. **Called as:** `shared.Globe.<function>(...)`

## What the source says

```text
Globe landing page (WebDev iframe <-> Perspective page), scoped to ONE session + page.

The iframe at /system/webdev/BH/globe/map cannot talk to Perspective directly, so it POSTs
to /system/webdev/BH/globe/mapMarkers. The iframe src carries the owning session id, page id
and an HMAC token (iframeSrc); doPost hands the body to relay(), which verifies the token and
that the session/page is live, then system.perspective.sendMessage(..., scope='page') to that
page only. The Globe view's page-scoped handlers (globeHover / globeNavigate) do the rest.
See docs/globe-hover.md.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.perspective`, `system.security`, `system.tag`, `system.user`, `system.util` |
| Calls modules | [Navigation.Nav](./navigation-nav.md), [shared.Security](./shared-security.md) |

<details>
<summary>Module constants (8)</summary>

| Name | Value |
|---|---|
| `LOGGER` | `'BH.Globe'` |
| `INDEX_URL` | `'/system/webdev/BH/globe/map'` |
| `THEME_ALIASES` | `{'light': 'light-cool', 'dark': 'dark-cool'}` |
| `HOVER_MESSAGE` | `'globeHover'` |
| `NAV_MESSAGE` | `'globeNavigate'` |
| `_SECRET_KEY` | `'bh.globe.hmacSecret'` |
| `ADMIN_ROLES_TAG` | `'[default]_Config/Security/AdminRoles'` |
| `USER_SOURCE` | `'default'` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_secret`](#_secret) (internal) | Random per-gateway-run secret, shared by Perspective bindings and WebDev (getGlobals). | 0 |
| [`token`](#token) | | 0 |
| [`_same`](#_same) (internal) | | 0 |
| [`iframeSrc`](#iframesrc) | Globe iframe src for this session/page (bound on the Globe view's IFrame props.src). | 1 |
| [`_sessionHasPage`](#_sessionhaspage) (internal) | True when sessionId is a live BH session and pageId is one of its open pages. | 0 |
| [`_routeOk`](#_routeok) (internal) | | 0 |
| [`relay`](#relay) | Handle a globe marker POST body. Returns (httpStatus, reason). | 3 |
| [`adminWriter`](#adminwriter) | (httpStatus, user) for a config write on globe/mapMarkers (GeoJSON markers, Navigation document). | 3 |

### \_secret {#_secret}

```python
def _secret()
```
Line 22 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

```text
Random per-gateway-run secret, shared by Perspective bindings and WebDev (getGlobals).
```

Used inside the module by: `token`

### token {#token}

```python
def token(sessionId, pageId)
```
Line 36 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `iframeSrc`, `relay`

### \_same {#_same}

```python
def _same(a, b)
```
Line 41 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

_No docstring._

Used inside the module by: `relay`

### iframeSrc {#iframesrc}

```python
def iframeSrc(theme, sessionId, pageId)
```
Line 51 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

```text
Globe iframe src for this session/page (bound on the Globe view's IFrame props.src).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/LandingPage/Globe` | view | `root/Map/IFrame binding props.src` |

### \_sessionHasPage {#_sessionhaspage}

```python
def _sessionHasPage(sessionId, pageId)
```
Line 59 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

```text
True when sessionId is a live BH session and pageId is one of its open pages.
```

Used inside the module by: `relay`

### \_routeOk {#_routeok}

```python
def _routeOk(page)
```
Line 76 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

_No docstring._

Used inside the module by: `relay`

### relay {#relay}

```python
def relay(data)
```
Line 83 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

```text
Handle a globe marker POST body. Returns (httpStatus, reason).

Body: {"__globe": "hover"|"navigate", "sessionId", "pageId", "token", "page", "seq"?}
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/LandingPage/Globe` | view | `root message handler globeHover` |
| `00_Pages/Boars Head/LandingPage/Globe` | view | `root message handler globeNavigate` |
| `globe/mapMarkers` | webdev | `doPost` |

### adminWriter {#adminwriter}

```python
def adminWriter(request)
```
Line 126 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Globe/code.py`.

```text
(httpStatus, user) for a config write on globe/mapMarkers (GeoJSON markers, Navigation document).

The iframe's hover/navigate relay needs a logged-in BH session (shared.WebAuth); config writes check HTTP Basic
credentials here, BEFORE the body is looked at: a user of the 'default' user source holding a role listed
in _Config/Security/AdminRoles (shared.Security, no hard-coded role names). 401 = missing/invalid
credentials (sets WWW-Authenticate), 403 = valid user without an admin role, 200 = allowed.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `globe/mapMarkers` | webdev | `doGet` |
| `globe/mapMarkers` | webdev | `doPost` |
| `globe/mapMarkers` | webdev | `doPut` |
