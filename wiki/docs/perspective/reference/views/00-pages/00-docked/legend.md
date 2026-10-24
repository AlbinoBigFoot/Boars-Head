---
title: "Legend"
sidebar_label: "Legend"
description: "Perspective view 00_Pages/00_Docked/Legend (Docked view): 56 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/Legend", "Legend"]
---

:::note

:::


**Docked view**: `00_Pages/00_Docked/Legend`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/Legend` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Legend/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; Legend |
| Docked | right dock legend on /<br/>right dock legend on /enterprise<br/>right dock legend on /plants/forrest-city<br/>right dock legend on /plants/groveport<br/>right dock legend on /plants/groveport/classic<br/>right dock legend on /plants/groveport/club/epms<br/>right dock legend on /plants/groveport/club/production<br/>right dock legend on /plants/groveport/dock/epms<br/>right dock legend on /plants/groveport/dock/production<br/>right dock legend on /plants/groveport/east-ph/epms<br/>right dock legend on /plants/groveport/east-ph/production<br/>right dock legend on /plants/groveport/executive<br/>right dock legend on /plants/groveport/freezer/epms<br/>right dock legend on /plants/groveport/freezer/production<br/>right dock legend on /plants/groveport/machine-room/epms<br/>right dock legend on /plants/groveport/machine-room/production<br/>right dock legend on /plants/groveport/palletizing/epms<br/>right dock legend on /plants/groveport/palletizing/production<br/>right dock legend on /plants/groveport/production-overview<br/>right dock legend on /plants/groveport/production/handtman<br/>right dock legend on /plants/groveport/production/hopper<br/>right dock legend on /plants/groveport/production/lazy-susan<br/>right dock legend on /plants/groveport/production/level-2/forming<br/>right dock legend on /plants/groveport/production/level-2/packaging<br/>right dock legend on /plants/groveport/production/level-2/prep<br/>right dock legend on /plants/groveport/production/loaders<br/>right dock legend on /plants/groveport/production/roll-stock<br/>right dock legend on /plants/groveport/production/shrink-tunnel<br/>right dock legend on /plants/groveport/production/vat-dumper<br/>right dock legend on /plants/groveport/superchill/epms<br/>right dock legend on /plants/groveport/superchill/production<br/>right dock legend on /plants/groveport/utility-overview<br/>right dock legend on /plants/groveport/west-ph/epms<br/>right dock legend on /plants/groveport/west-ph/production<br/>right dock legend on /plants/holland<br/>right dock legend on /plants/new-castle<br/>right dock legend on /plants/petersburg<br/>shared right dock legend (onDemand) |
| Root | `ia.container.flex`, width 220 |
| Size | 56 components, 2 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:00:00Z by admin |

## Component Tree

Component types: ia.display.label x27, ia.container.flex x15, ia.display.view x14.

<details>
<summary>Component tree (56 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  FlexContainer  ia.container.flex
    CommLoss  ia.display.view  [view: 03_Elements/01_Status/NotificationIcons/CommLoss]
    Label  ia.display.label
  Label  ia.display.label
  FlexContainer_1  ia.container.flex
    Operator  ia.display.view  [view: 03_Elements/01_Status/Icons/Operator]
    Label  ia.display.label
  Label_3  ia.display.label
  FlexContainer_10  ia.container.flex
    Simulation  ia.display.view  [view: 03_Elements/01_Status/Icons/Maintenance]
    Label  ia.display.label
  Label_Program  ia.display.label
  FlexContainer_Program  ia.container.flex
    Program  ia.display.view  [view: 03_Elements/01_Status/Icons/Program]
    Label  ia.display.label
  Label_8  ia.display.label
  FlexContainer_NoMode  ia.container.flex
    NoMode  ia.display.view  [view: 03_Elements/01_Status/Icons/NoMode]
    Label  ia.display.label
  Label_9  ia.display.label
  FlexContainer_9  ia.container.flex
    Simulation  ia.display.view  [view: 03_Elements/01_Status/Icons/Hand]
    Label  ia.display.label
  Label_10  ia.display.label
  FlexContainer_Override  ia.container.flex
    Override  ia.display.view  [view: 03_Elements/01_Status/Icons/Override]
    Label  ia.display.label
  Label_12  ia.display.label
  FlexContainer_Interlock  ia.container.flex
    Interlock  ia.display.view  [view: 03_Elements/01_Status/Icons/Interlock]
    Label  ia.display.label
  Label_Override  ia.display.label
  FlexContainer_12  ia.container.flex
    Simulation  ia.display.view  [view: 03_Elements/01_Status/Icons/OutOfService]
    Label  ia.display.label
  Label_Interlock  ia.display.label
  FlexContainer_Faceplate  ia.container.flex
    Faceplate  ia.display.view  [view: 03_Elements/01_Status/Icons/Faceplate]
    Label  ia.display.label
  Label_AlarmGap0  ia.display.label
  FlexContainer_Critical  ia.container.flex
    Critical  ia.display.view  [view: 03_Elements/01_Status/NotificationIcons/Alarms/Critical]
    Label  ia.display.label
  Label_AlarmGap1  ia.display.label
  FlexContainer_High  ia.container.flex
    High  ia.display.view  [view: 03_Elements/01_Status/NotificationIcons/Alarms/High]
    Label  ia.display.label
  Label_AlarmGap2  ia.display.label
  FlexContainer_Medium  ia.container.flex
    Medium  ia.display.view  [view: 03_Elements/01_Status/NotificationIcons/Alarms/Medium]
    Label  ia.display.label
  Label_AlarmGap3  ia.display.label
  FlexContainer_Low  ia.container.flex
    Low  ia.display.view  [view: 03_Elements/01_Status/NotificationIcons/Alarms/Low]
    Label  ia.display.label
```

</details>

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** `dom.onMouseEnter`, script action, scope `G`

```python
for pid in ['userRolesLogin', 'changeTheme']:
    system.perspective.closePopup(pid)
try:
    self.session.custom.openHeaderPopup = ''
except:
    pass
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (14): [03\_Elements/01\_Status/Icons/Faceplate](../../03-elements/01-status/icons/faceplate.md), [03\_Elements/01\_Status/Icons/Hand](../../03-elements/01-status/icons/hand.md), [03\_Elements/01\_Status/Icons/Interlock](../../03-elements/01-status/icons/interlock.md), [03\_Elements/01\_Status/Icons/Maintenance](../../03-elements/01-status/icons/maintenance.md), [03\_Elements/01\_Status/Icons/NoMode](../../03-elements/01-status/icons/nomode.md), [03\_Elements/01\_Status/Icons/Operator](../../03-elements/01-status/icons/operator.md), [03\_Elements/01\_Status/Icons/OutOfService](../../03-elements/01-status/icons/outofservice.md), [03\_Elements/01\_Status/Icons/Override](../../03-elements/01-status/icons/override.md), [03\_Elements/01\_Status/Icons/Program](../../03-elements/01-status/icons/program.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/Critical](../../03-elements/01-status/notificationicons/alarms/critical.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/High](../../03-elements/01-status/notificationicons/alarms/high.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/Low](../../03-elements/01-status/notificationicons/alarms/low.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/Medium](../../03-elements/01-status/notificationicons/alarms/medium.md), [03\_Elements/01\_Status/NotificationIcons/CommLoss](../../03-elements/01-status/notificationicons/commloss.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 14 | style class |
| `bg-component` | 1 | stylesheet |
| `legend-dock` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
