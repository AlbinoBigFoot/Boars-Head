---
title: "Navigation"
sidebar_label: "Navigation"
description: "Perspective view 00_Pages/00_Docked/Navigation (Docked view): 9 components, 8 bindings, 5 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/Navigation", "Navigation"]
---

:::note

:::


**Docked view**: `00_Pages/00_Docked/Navigation`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/Navigation` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Navigation/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; Navigation |
| Docked | shared left dock plant-nav (visible) |
| Root | `ia.container.flex`, height 720, width 260 |
| Size | 9 components, 8 bindings, 2 event handlers, 3 change scripts, 1 message handlers |
| Last saved | 2026-10-24T13:51:33Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `items` | `[{"data": {"action": "page", "demoPage": "/enterprise", "localIcon"...` | |
| `lastClickPath` | `""` | |
| `dockWidth` | `260` | not persistent |
| `autoExpanded` | `[]` | |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x3, ia.display.tree x1, ia.input.text-field x1.

```text
root  ia.container.flex  [2 bindings]
  Brand  ia.display.label  [1 binding]
  Tree  ia.display.tree  [2 bindings; 1 event]
  Spacer  ia.container.flex
  Search  ia.container.flex
    TextField  ia.input.text-field
    Clear  ia.display.label  [1 binding; 1 event]
    Count  ia.display.label  [1 binding]
  DateTime  ia.display.label  [1 binding]
```

## Bindings

8 bindings: expr-struct 4, expr 3, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/Brand`**

- `props.text`: property `page.props.path`, then script transform

Transform 1, script:

```python
return Navigation.Nav.pageTitle(value)
```


**`root/Tree`**

- `custom.itemPath`: structured expression (expr-struct), then script transform

```js
data: {page.props.path}
items: {this.props.items}
```

waitOnAll: `True`

Transform 1, script:

```python
itemPath = None
# value.data here is the current page path string (page.props.path)
pagePath = value.data
if pagePath is not None and len(value.items) > 0:
    result = Navigation.Nav.findItemIndex(value.items, page=str(pagePath))
    if result is not None:
        itemPath = "/".join(map(str, result))
return itemPath
```


- `props.items`: structured expression (expr-struct), then script transform

```js
items: {view.custom.items}
isAdmin: {session.custom.Administrator}
perms: {session.custom.Permissions}
demo: coalesce(try(toBoolean(tag('[default]_Config/DemoEnterpriseNav')), false), false)
```

waitOnAll: `True`

Transform 1, script:

```python
# json round-trip yields plain dicts — Perspective DotReferenceJythonMap
# from deepcopy/bindings does not support item assignment (n["items"] = ...).
raw = value["items"] if value["items"] is not None else []
items = system.util.jsonDecode(system.util.jsonEncode(raw))
is_admin = bool(value["isAdmin"])
# enterprise-demo-nav: [default]_Config/DemoEnterpriseNav shows data.demo nodes despite data.hidden
try:
    demo = bool(value["demo"])
except:
    demo = False
perms = system.util.jsonDecode(system.util.jsonEncode(value["perms"])) if value["perms"] is not None else {}
def granted(p):
    dev, _, act = str(p).partition("/")
    return bool((perms.get(dev) or {}).get(act))
# data.permission 'Device/Action' (Roles & Permissions row, security-tiers) wins over adminOnly; a folder whose
# every item was withheld that way (Admin for Maintenance) goes too
def filter_nodes(nodes):
    out = []
    for n in nodes or []:
        data = n.get("data") or {}
        if data.get("permission"):
            if not granted(data["permission"]):
                continue
        elif data.get("adminOnly") and not is_admin:
            continue
        if data.get("hidden") and not (demo and data.get("demo")):
            continue
        kids = n.get("items") or []
        if kids:
            kept = filter_nodes(kids)
            withheld = [k for k in kids if (k.get("data") or {}).get("permission")
                and not granted((k.get("data") or {}).get("permission"))]
            if not kept and withheld and not (data.get("page") or data.get("viewPath")):
                continue
            n["items"] = kept
        out.append(n)
    return out
return filter_nodes(items)
```


**`root/Search/Clear`**

- `meta.visible`: expression

```js
len({../TextField.props.text})>0
```


**`root/Search/Count`**

- `meta.visible`: expression

```js
len({../TextField.props.text})>0
```


**`root/DateTime`**

- `props.text`: expression, then format transform

```js
now(1000)
```

Transform 1, format `datetime` `MMM dd, yyyy h:mm:ss a`


## Event Scripts And Handlers

- **`root/Tree`** `component.onItemClicked`, script action, scope `G`

```python
data = event.data
if data is None:
    return
if not Navigation.Nav.navigate(data):
    return  # folder / no page: stay on the current page, keep the selection
# Mark click so selection sync does not collapse expansion
clickedPath = '/'.join(map(str, event.itemPath))
self.view.custom.lastClickPath = clickedPath
self.props.selection = [clickedPath]
```

- **`root/Search/Clear`** `dom.onClick`, script action, scope `G`

```python
self.getSibling("TextField").props.text = ""
self.parent.parent.getChild("Tree").refreshBinding("props.items")
self.getSibling("Count").props.text = ""
```

- **`root/Tree`** change script on `custom.itemPath`

```python
if origin != "Binding":
    return
items = self.props.items
if items is None:
    return

def node(path):
    n = None
    level = items
    for index in [i for i in str(path).split("/") if i != ""]:
        n = level[int(index)]
        level = n.items
    return n

def ancestors(path):
    parts = [i for i in str(path or "").split("/") if i != ""]
    return ["/".join(parts[:k]) for k in range(1, len(parts) + 1)]

target = currentValue.value
# A tree click keeps the clicked node's branch: several nodes share one page (e.g. every CG's
# "Devices" -> /devices) and target is only the first node with that page.
clicked = self.view.custom.lastClickPath or ""
keep = set(ancestors(target)) | set(ancestors(clicked))
# Collapse branches auto-expanded for the previous page (user-expanded ones are left alone).
auto = []
# ... 37 more line(s): see the view.json
```

- **`root/Tree`** change script on `props.items`

```python
# Fit the nav dock to the widest visible (expanded) row - no horizontal scrollbar.
try:
    # currentValue.value is a wrapped property value; props.items round-trips cleanly.
    items = system.util.jsonDecode(system.util.jsonEncode(self.props.items)) or []
except:
    return

def need(nodes, depth):
    w = 0
    for it in nodes or []:
        style = (it.get('icon') or {}).get('style') or {}
        per = 7.6 if 'nav-search-hit' in str(style.get('classes') or '') else 7.0
        w = max(w, 48 + 20 * depth + len(str(it.get('label') or '')) * per)
        if it.get('expanded'):
            w = max(w, need(it.get('items'), depth + 1))
    return w

width = int(min(480, max(260, need(items, 0) + 44)))
if width != self.view.custom.dockWidth:
    self.view.custom.dockWidth = width
    system.perspective.alterDock('plant-nav', {'size': width})
```

- **`root/Search/TextField`** change script on `props.text`

```python
text = currentValue.value
text = '' if text is None else str(text).strip()
tree = self.parent.parent.getChild('Tree')
countLbl = self.getSibling('Count')
if text == '':
    tree.refreshBinding('props.items')
    countLbl.props.text = ''
    return

# Work on a plain copy (never mutate props.items in place; icons fail to remount).
items = system.util.jsonDecode(system.util.jsonEncode(tree.props.items))
q = text.upper()
HIT = 'nav-search-hit'
PARENT = 'nav-search-parent'
found = [0]

def mark(item, cls):
    if not cls and 'icon' not in item:
        return
    ic = dict(item.get('icon') or {})
    style = dict(ic.get('style') or {})
    base = [c for c in str(style.get('classes') or '').split() if c not in (HIT, PARENT)]
    if cls:
        base.append(cls)
    style['classes'] = ' '.join(base)
# ... 31 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [Navigation.Nav.findItemIndex](../../../../../scripting/reference/modules/navigation-nav.md), [Navigation.Nav.navigate](../../../../../scripting/reference/modules/navigation-nav.md), [Navigation.Nav.pageTitle](../../../../../scripting/reference/modules/navigation-nav.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](../boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Operations/AuditLog](../boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](../boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](../boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Groveport/Area/DomainKpis](../groveport/area/domainkpis.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](../groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](../groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](../groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](../groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](../groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](../groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](../groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](../groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](../groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](../groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](../groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](../groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](../groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](../groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](../groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](../groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](../groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](../groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/PlcOverview](../groveport/operations/plcoverview.md), [00\_Pages/Groveport/Operations/ReportsBuilder](../groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](../groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](../groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](../groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](../groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](../groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](../groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](../groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](../groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](../groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](../groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](../groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](../groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Utility/Overview](../groveport/utility/overview.md), [01\_Popups/00\_Faceplates/Evaporator](../../01-popups/00-faceplates/evaporator.md), [01\_Popups/00\_Faceplates/Pump](../../01-popups/00-faceplates/pump.md), [01\_Popups/00\_Faceplates/Sensor](../../01-popups/00-faceplates/sensor.md), [01\_Popups/00\_Faceplates/SolenoidValve](../../01-popups/00-faceplates/solenoidvalve.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `nav-brand` | 1 | stylesheet |
| `nav-clock` | 1 | style class |
| `nav-dock` | 1 | stylesheet |
| `nav-search` | 1 | stylesheet |
| `nav-search-clear` | 1 | stylesheet |
| `nav-search-count` | 1 | stylesheet |
| `nav-search-field` | 1 | stylesheet |
| `nav-tree` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `[default]_Config/DemoEnterpriseNav`
- `[default]_Config/DemoEnterpriseNav shows data.demo nodes despite data.hidden`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
