---
title: "TempNav"
sidebar_label: "TempNav"
description: "Perspective view 00_Pages/00_Docked/TempNav (Page piece (not routed)): 6 components, 4 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/TempNav", "TempNav"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/00_Docked/TempNav`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/TempNav` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/TempNav/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; TempNav |
| Root | `ia.container.flex`, height 720, width 260 |
| Size | 6 components, 4 bindings, 1 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-10-24T13:51:33Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `items` | `[{"data": {"action": "page", "demoPage": "/enterprise", "localIcon"...` | |
| `lastClickPath` | `""` | |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x2, ia.display.tree x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Brand  ia.display.label
  Tree  ia.display.tree  [2 bindings; 1 event]
  Spacer  ia.container.flex
  SectionUser  ia.display.label
  User  ia.display.view  [view: 00_Pages/00_Docked/_Assets/User]
```

## Bindings

4 bindings: expr-struct 3, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

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
        itemPath = '/'.join(map(str, result))
return itemPath
```


- `props.items`: property `view.custom.items`

## Event Scripts And Handlers

- **`root/Tree`** `component.onItemClicked`, script action, scope `G`

```python
data = event.data
if data is None:
    return
Navigation.Nav.navigate(data)
# Mark click so selection sync does not collapse expansion
clickedPath = '/'.join(map(str, event.itemPath))
self.view.custom.lastClickPath = clickedPath
self.props.selection = [clickedPath]
```

- **`root/Tree`** change script on `custom.itemPath`

```python
if origin == "Binding" and currentValue.value is not None:
    if self.view.custom.lastClickPath:
        self.view.custom.lastClickPath = ""
        return
    selection = currentValue.value
    current_sel = None
    try:
        sel = self.props.selection
        if sel is not None and len(sel) > 0:
            current_sel = sel[0]
    except:
        current_sel = None
    if selection == current_sel:
        return
    items = self.props.items
    if selection is None or items is None:
        return
    try:
        self.props.selection = [selection]
        indexes = str(selection).split("/")
        for index in indexes:
            if index == "":
                continue
            item = items[int(index)]
            item.expanded = True
# ... 3 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [Navigation.Nav.findItemIndex](../../../../../scripting/reference/modules/navigation-nav.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/00\_Docked/\_Assets/User](./assets/user.md)

**Opens or names** (popups, scripts, expressions): [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](../boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Operations/AuditLog](../boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](../boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Groveport/Area/DomainKpis](../groveport/area/domainkpis.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](../groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](../groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](../groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](../groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](../groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](../groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](../groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/PlcOverview](../groveport/operations/plcoverview.md), [00\_Pages/Groveport/Operations/ReportsBuilder](../groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](../groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](../groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](../groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](../groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](../groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](../groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](../groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](../groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](../groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](../groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](../groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](../groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Utility/Overview](../groveport/utility/overview.md), [01\_Popups/00\_Faceplates/Evaporator](../../01-popups/00-faceplates/evaporator.md), [01\_Popups/00\_Faceplates/Sensor](../../01-popups/00-faceplates/sensor.md), [01\_Popups/00\_Faceplates/SolenoidValve](../../01-popups/00-faceplates/solenoidvalve.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `nav-brand` | 1 | stylesheet |
| `nav-dock` | 1 | stylesheet |
| `nav-section` | 1 | stylesheet |
| `nav-tree` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
