---
title: "Medium"
sidebar_label: "Medium"
description: "Perspective view 03_Elements/01_Status/NotificationIcons/Alarms/Medium (Element (small reusable part)): 3 components, 1 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/NotificationIcons/Alarms/Medium", "Medium"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/NotificationIcons/Alarms/Medium`.

| | |
|---|---|
| View path | `03_Elements/01_Status/NotificationIcons/Alarms/Medium` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/NotificationIcons/Alarms/Medium/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; NotificationIcons &gt; Alarms &gt; Medium |
| Root | `ia.container.coord`, height 20, width 20 |
| Size | 3 components, 1 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T04:25:28Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `unack` | `false` | input |

## Component Tree

Component types: ia.container.coord x1, ia.shapes.svg x1, ia.display.label x1.

```text
root  ia.container.coord  [1 binding]
  Shape  ia.shapes.svg
  Number  ia.display.label
```

## Bindings

1 bindings: expr 1.

**`root`**

- `props.style.classes`: expression

```js
if(coalesce({view.params.unack}, false), 'alarm-flash', '')
```


## Related Views

**Embedded in** (1): [00\_Pages/00\_Docked/Legend](../../../../00-pages/00-docked/legend.md)

**Opened or named by** (2): [03\_Elements/01\_Status/AlarmHeader](../../alarmheader.md), [03\_Elements/03\_Table/DeviceLabelAlarmIndicator](../../../03-table/devicelabelalarmindicator.md)
