---
title: "shared.Integrations"
sidebar_label: "shared.Integrations"
description: "Script module shared.Integrations: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`  
**Lines:** 245. **Functions:** 20. **Called as:** `shared.Integrations.<function>(...)`

## What the source says

```text
Integration endpoints (API connections): [default]_Config/Integrations/<Name>, one Config/Integration UDT
instance each (Monday today; Oracle etc. later). Common members hold the endpoint and status; Settings is a
Document member for provider-specific values (Monday: workspaceId, boardId, groupId, columns).
The API token is write-only from the HMI: get() / listForView() only report hasToken; token() is for gateway-side
callers (shared.TicketLogger) and never goes to a view.
ticket-routing (2026-10-24): the view-facing calls (detail / listForView / settingsRows / save / setToken / add /
test) need Roles & Permissions TicketLogger/Settings (OneShot only); get() / token() stay open for the submit path
(shared.TicketLogger) and gateway scripts (pingAll timer).
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.net`, `system.tag`, `system.util` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Security](./shared-security.md), [shared.TicketLogger](./shared-ticketlogger.md) |
| Called by modules | [shared.TicketLogger](./shared-ticketlogger.md) |

<details>
<summary>Module constants (6)</summary>

| Name | Value |
|---|---|
| `BASE` | `'[default]_Config/Integrations'` |
| `TYPE_ID` | `'Config/Integration'` |
| `FIELDS` | `['Provider', 'Description', 'Enabled', 'Endpoint URL', 'A...` |
| `EDITABLE` | `{'description': 'Description', 'enabled': 'Enabled', 'url...` |
| `PROVIDERS` | `['Monday', 'Oracle', 'HTTP']` |
| `TESTERS` | `{'Monday': _testMonday}` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_path`](#_path) (internal) | | 0 |
| [`_toPy`](#_topy) (internal) | Document tag value -&gt; plain dict / list. | 0 |
| [`names`](#names) | | 0 |
| [`get`](#get) | Config and status for one integration, without the token. | 1 |
| [`_settingsAllowed`](#_settingsallowed) (internal) | | 0 |
| [`_requireSettings`](#_requiresettings) (internal) | | 0 |
| [`detail`](#detail) | get() for the view's runScript binding (rev only re-triggers it after Save / Test). | 1 |
| [`statusText`](#statustext) | | 0 |
| [`listForView`](#listforview) | Rows for the Integrations table (rev only re-triggers the runScript binding). | 1 |
| [`token`](#token) | | 1 |
| [`_flatten`](#_flatten) (internal) | | 0 |
| [`settingsRows`](#settingsrows) | Settings document as key / value rows (nested keys dotted: columns.Description). | 1 |
| [`unflatten`](#unflatten) | | 1 |
| [`save`](#save) | values: any of description, enabled, url, apiVersion, settings (dict). Changed members are audited. | 1 |
| [`setToken`](#settoken) | Replace the API token; the audit entry never carries the value. | 1 |
| [`add`](#add) | | 1 |
| [`_testMonday`](#_testmonday) (internal) | | 0 |
| [`_testHttp`](#_testhttp) (internal) | Any other provider until it has its own check: the endpoint must answer below HTTP 400. | 0 |
| [`test`](#test) | Run the provider check and write Connected / Last Check / Last Error. Returns [ok, message]. | 1 |
| [`pingAll`](#pingall) | | 1 |

### \_path {#_path}

```python
def _path(name, member=None)
```
Line 18 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

Used inside the module by: `add`, `get`, `save`, `setToken`, `test`, `token`

### \_toPy {#_topy}

```python
def _toPy(value)
```
Line 25 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Document tag value -> plain dict / list.
```

Used inside the module by: `get`

### names {#names}

```python
def names()
```
Line 39 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `add`, `listForView`, `pingAll`

### get {#get}

```python
def get(name)
```
Line 53 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Config and status for one integration, without the token.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.TicketLogger._cfg` | script | |

Used inside the module by: `_testHttp`, `detail`, `listForView`, `save`, `settingsRows`, `test`

### \_settingsAllowed {#_settingsallowed}

```python
def _settingsAllowed()
```
Line 76 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

Used inside the module by: `detail`, `listForView`, `settingsRows`

### \_requireSettings {#_requiresettings}

```python
def _requireSettings(what)
```
Line 80 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

Used inside the module by: `add`, `save`, `setToken`, `test`

### detail {#detail}

```python
def detail(name, rev=None)
```
Line 85 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
get() for the view's runScript binding (rev only re-triggers it after Save / Test).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `binding custom.detail` |

### statusText {#statustext}

```python
def statusText(cfg)
```
Line 92 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `listForView`

### listForView {#listforview}

```python
def listForView(rev=None)
```
Line 100 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Rows for the Integrations table (rev only re-triggers the runScript binding).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Integrations` | view | `binding custom.items` |

### token {#token}

```python
def token(name)
```
Line 112 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.TicketLogger._token` | script | |

Used inside the module by: `_testHttp`

### \_flatten {#_flatten}

```python
def _flatten(d, prefix='')
```
Line 117 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

Used inside the module by: `settingsRows`

### settingsRows {#settingsrows}

```python
def settingsRows(name, rev=None)
```
Line 128 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Settings document as key / value rows (nested keys dotted: columns.Description).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `root/Body/Settings binding props.data` |

### unflatten {#unflatten}

```python
def unflatten(rows)
```
Line 135 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `root/Body/Buttons/Save event component.onActionPerformed` |

### save {#save}

```python
def save(name, values, viewName=None)
```
Line 153 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
values: any of description, enabled, url, apiVersion, settings (dict). Changed members are audited.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `root/Body/Buttons/Save event component.onActionPerformed` |

### setToken {#settoken}

```python
def setToken(name, newToken, viewName=None)
```
Line 170 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Replace the API token; the audit entry never carries the value.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `root/Body/TokenRow/Replace event component.onActionPerformed` |

### add {#add}

```python
def add(name, provider, viewName=None)
```
Line 181 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/Integrations` | view | `root/AddRow/Add event component.onActionPerformed` |

### \_testMonday {#_testmonday}

```python
def _testMonday(name)
```
Line 196 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

### \_testHttp {#_testhttp}

```python
def _testHttp(name)
```
Line 204 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Any other provider until it has its own check: the endpoint must answer below HTTP 400.
```

### test {#test}

```python
def test(name)
```
Line 223 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

```text
Run the provider check and write Connected / Last Check / Last Error. Returns [ok, message].
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/IntegrationSection` | view | `root/Body/Buttons/Test event component.onActionPerformed` |

Used inside the module by: `pingAll`

### pingAll {#pingall}

```python
def pingAll()
```
Line 240 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Integrations/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `pingMonday` | gateway timer | `handleTimerEvent.py` |
