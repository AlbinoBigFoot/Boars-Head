---
title: "Globe"
sidebar_label: "Globe"
description: "Perspective view 00_Pages/Boars Head/LandingPage/Globe (Page): 9 components, 10 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/LandingPage/Globe", "Globe", "/enterprise"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/LandingPage/Globe`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/LandingPage/Globe` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/LandingPage/Globe/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; LandingPage &gt; Globe |
| Routes | `/enterprise` (Boars Head International) |
| Root | `ia.container.flex`, height 900, width 1600 |
| Size | 9 components, 10 bindings, 0 event handlers, 1 change scripts, 3 message handlers |
| Last saved | 2026-08-01T18:45:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `theme` | `""` | bound (property) |
| `hoverPage` | `""` | |
| `hoverSeq` | `0` | |

## Component Tree

Component types: ia.display.view x5, ia.container.flex x3, ia.display.iframe x1.

```text
root  ia.container.flex  [2 bindings]
  Map  ia.container.flex
    IFrame  ia.display.iframe  [1 binding]
  SiteRail  ia.container.flex  [1 binding]
    Site_Groveport  ia.display.view  [1 binding; view: 02_Components/02_Widgets/SiteCard]
    Site_NewCastle  ia.display.view  [1 binding; view: 02_Components/02_Widgets/SiteCard]
    Site_ForrestCity  ia.display.view  [1 binding; view: 02_Components/02_Widgets/SiteCard]
    Site_Petersburg  ia.display.view  [1 binding; view: 02_Components/02_Widgets/SiteCard]
    Site_Holland  ia.display.view  [1 binding; view: 02_Components/02_Widgets/SiteCard]
```

## Bindings

10 bindings: expr 5, expr-struct 3, property 2.

**`(view)`**

- `custom.theme`: property `session.props.theme`

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Map/IFrame`**

- `props.src`: structured expression (expr-struct), then script transform

```js
theme: {view.custom.theme}
sessionId: {session.props.id}
pageId: {page.props.pageId}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Globe.iframeSrc(value['theme'], value['sessionId'], value['pageId'])
```


**`root/SiteRail`**

- `custom.hoverPage`: property `view.custom.hoverPage`

**`root/SiteRail/Site_Groveport`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.hoverPage}, '') = '', '', if({view.custom.hoverPage} = '/plants/groveport', 'site-rail-card--hot', 'site-rail-card--dim'))
```


**`root/SiteRail/Site_NewCastle`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.hoverPage}, '') = '', '', if({view.custom.hoverPage} = '/plants/new-castle', 'site-rail-card--hot', 'site-rail-card--dim'))
```


**`root/SiteRail/Site_ForrestCity`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.hoverPage}, '') = '', '', if({view.custom.hoverPage} = '/plants/forrest-city', 'site-rail-card--hot', 'site-rail-card--dim'))
```


**`root/SiteRail/Site_Petersburg`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.hoverPage}, '') = '', '', if({view.custom.hoverPage} = '/plants/petersburg', 'site-rail-card--hot', 'site-rail-card--dim'))
```


**`root/SiteRail/Site_Holland`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.hoverPage}, '') = '', '', if({view.custom.hoverPage} = '/plants/holland', 'site-rail-card--hot', 'site-rail-card--dim'))
```


## Event Scripts And Handlers

- **`root/SiteRail`** change script on `custom.hoverPage`

```python
page = currentValue.value
if page is None or str(page).strip() == '':
    return
js = "(function(){\n  var tryScroll = function(n){\n    var el = document.querySelector('.psc-site-rail .psc-site-rail-card--hot');\n    var rail = document.querySelector('.psc-site-rail');\n    if (el && rail) {\n      el.scrollIntoView({behavior: 'smooth', block: 'nearest', inline: 'nearest'});\n      var er = el.getBoundingClientRect();\n      var rr = rail.getBoundingClientRect();\n      if (er.bottom > rr.bottom + 2 || er.top < rr.top - 2) {\n        rail.scrollTop += (er.top - rr.top) - Math.max(0, (rr.height - er.height) / 2);\n      }\n      return;\n    }\n    if (n > 0) setTimeout(function(){ tryScroll(n - 1); }, 50);\n  };\n  tryScroll(30);\n})();"
try:
    if hasattr(system.perspective, 'runJavaScriptAsync'):
        system.perspective.runJavaScriptAsync(js)
    elif hasattr(system.perspective, 'runJavaScript'):
        system.perspective.runJavaScript(js)
except:
    pass
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

- **`root`** message handler `globeHover` (scope: page)

```python
# Per-session globe hover: shared.Globe.relay sends this to this page only (docs/globe-hover.md).
# Requests can arrive out of order; the newest seq (iframe Date.now()) wins.
try:
    seq = float(payload.get('seq') or 0)
except:
    seq = 0.0
try:
    last = float(self.view.custom.hoverSeq or 0)
except:
    last = 0.0
if seq and seq < last:
    return
self.view.custom.hoverSeq = seq
self.view.custom.hoverPage = payload.get('page') or ''
```

- **`root`** message handler `globeNavigate` (scope: page)

```python
# Per-session globe marker click (route already checked by shared.Globe.relay)
page = payload.get('page') or ''
if page:
    Navigation.Nav.navigate({'action': 'page', 'page': page})
```

Project script calls: [Navigation.Nav.navigate](../../../../../../scripting/reference/modules/navigation-nav.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Globe.iframeSrc](../../../../../../scripting/reference/modules/shared-globe.md), [shared.Globe.relay](../../../../../../scripting/reference/modules/shared-globe.md).

## Related Views

**Embeds** (1): [02\_Components/02\_Widgets/SiteCard](../../../02-components/02-widgets/sitecard.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `site-rail` | 1 | stylesheet |
| `themed-scroll` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
