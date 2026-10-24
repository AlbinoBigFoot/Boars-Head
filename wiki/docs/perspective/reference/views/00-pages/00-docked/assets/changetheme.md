---
title: "ChangeTheme"
sidebar_label: "ChangeTheme"
description: "Perspective view 00_Pages/00_Docked/_Assets/ChangeTheme (Asset (embedded piece)): 25 components, 24 bindings, 7 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/ChangeTheme", "ChangeTheme"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/ChangeTheme`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/ChangeTheme` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/ChangeTheme/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; ChangeTheme |
| Root | `ia.container.flex`, height 210, width 220 |
| Size | 25 components, 24 bindings, 7 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T07:10:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x13, ia.display.label x8, ia.display.icon x4.

<details>
<summary>Component tree (25 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  Label  ia.display.label
  Light Dark Cont  ia.container.flex
    Options  ia.container.flex
      Light Cont  ia.container.flex  [3 bindings; 1 event]
        Light Ico  ia.display.icon  [1 binding]
        Light  ia.display.label
      Dark Cont  ia.container.flex  [3 bindings; 1 event]
        Dark Ico  ia.display.icon  [1 binding]
        Dark  ia.display.label
  Cool Warm Cont  ia.container.flex
    Options  ia.container.flex
      Cool Cont  ia.container.flex  [3 bindings; 1 event]
        Cool Ico  ia.display.icon  [1 binding]
        Cool  ia.display.label
      Warm Cont  ia.container.flex  [3 bindings; 1 event]
        Warm Ico  ia.display.icon  [1 binding]
        Warm  ia.display.label
  Anim Label  ia.display.label
  Anim Cont  ia.container.flex
    Options  ia.container.flex
      On Cont  ia.container.flex  [3 bindings; 1 event]
        On  ia.display.label
      Off Cont  ia.container.flex  [3 bindings; 1 event]
        Off  ia.display.label
```

</details>

## Bindings

24 bindings: expr 22, expr-struct 2.

<details>
<summary>All 24 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Light Dark Cont/Options/Light Cont`**

- `props.style.backgroundColor`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='light-warm','--neutral-100','--neutral-30')
```


- `props.style.color`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='light-warm','--neutral-10','--neutral-90')
```


- `props.style.cursor`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='light-warm','auto','pointer')
```


**`root/Light Dark Cont/Options/Light Cont/Light Ico`**

- `props.color`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='light-warm','var(--neutral-30)','var(--neutral-90)')
```


**`root/Light Dark Cont/Options/Dark Cont`**

- `props.style.backgroundColor`: expression

```js
if({session.props.theme}='dark' || {session.props.theme}='dark-cool' || {session.props.theme}='dark-warm','--neutral-100','--neutral-30')
```


- `props.style.color`: expression

```js
if({session.props.theme}='dark' || {session.props.theme}='dark-cool' || {session.props.theme}='dark-warm','--neutral-10','--neutral-90')
```


- `props.style.cursor`: expression

```js
if({session.props.theme}='dark' || {session.props.theme}='dark-cool' || {session.props.theme}='dark-warm','auto','pointer')
```


**`root/Light Dark Cont/Options/Dark Cont/Dark Ico`**

- `props.color`: expression

```js
if({session.props.theme}='dark' || {session.props.theme}='dark-cool' || {session.props.theme}='dark-warm','var(--neutral-30)','var(--neutral-90)')
```


**`root/Cool Warm Cont/Options/Cool Cont`**

- `props.style.backgroundColor`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='dark' || {session.props.theme}='dark-cool','--neutral-100','--neutral-30')
```


- `props.style.color`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='dark' || {session.props.theme}='dark-cool','--neutral-10','--neutral-90')
```


- `props.style.cursor`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='dark' || {session.props.theme}='dark-cool','auto','pointer')
```


**`root/Cool Warm Cont/Options/Cool Cont/Cool Ico`**

- `props.color`: expression

```js
if({session.props.theme}='light' || {session.props.theme}='light-cool' || {session.props.theme}='dark' || {session.props.theme}='dark-cool','var(--neutral-30)','var(--neutral-90)')
```


**`root/Cool Warm Cont/Options/Warm Cont`**

- `props.style.backgroundColor`: expression

```js
if({session.props.theme}='light-warm' || {session.props.theme}='dark-warm','--neutral-100','--neutral-30')
```


- `props.style.color`: expression

```js
if({session.props.theme}='light-warm' || {session.props.theme}='dark-warm','--neutral-10','--neutral-90')
```


- `props.style.cursor`: expression

```js
if({session.props.theme}='light-warm' || {session.props.theme}='dark-warm','auto','pointer')
```


**`root/Cool Warm Cont/Options/Warm Cont/Warm Ico`**

- `props.color`: expression

```js
if({session.props.theme}='light-warm' || {session.props.theme}='dark-warm','var(--neutral-30)','var(--neutral-90)')
```


**`root/Anim Cont/Options/On Cont`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({session.props.animations}, true),'--neutral-100','--neutral-30')
```


- `props.style.color`: expression

```js
if(coalesce({session.props.animations}, true),'--neutral-10','--neutral-90')
```


- `props.style.cursor`: expression

```js
if(coalesce({session.props.animations}, true),'auto','pointer')
```


**`root/Anim Cont/Options/Off Cont`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({session.props.animations}, true),'--neutral-30','--neutral-100')
```


- `props.style.color`: expression

```js
if(coalesce({session.props.animations}, true),'--neutral-90','--neutral-10')
```


- `props.style.cursor`: expression

```js
if(coalesce({session.props.animations}, true),'pointer','auto')
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onMouseLeave`, script action, scope `G`

```python
try:
    system.perspective.closePopup('changeTheme')
except:
    pass
try:
    self.session.custom.openHeaderPopup = ''
except:
    pass
```

- **`root/Light Dark Cont/Options/Light Cont`** `dom.onClick`, script action, scope `G`

```python
# Cool uses light-cool/dark-cool (stock light/dark omit BH tokens like --ct-water).
# Accept legacy light/dark as cool aliases.
currTheme = self.session.props.theme
light_ok = ['light', 'light-cool', 'light-warm']
if currTheme not in light_ok:
    if currTheme in ('dark', 'dark-cool'):
        self.session.props.theme = 'light-cool'
    elif currTheme == 'dark-warm':
        self.session.props.theme = 'light-warm'
elif currTheme == 'light':
    self.session.props.theme = 'light-cool'
```

- **`root/Light Dark Cont/Options/Dark Cont`** `dom.onClick`, script action, scope `G`

```python
# Cool uses light-cool/dark-cool (stock light/dark omit BH tokens like --ct-water).
currTheme = self.session.props.theme
dark_ok = ['dark', 'dark-cool', 'dark-warm']
if currTheme not in dark_ok:
    if currTheme in ('light', 'light-cool'):
        self.session.props.theme = 'dark-cool'
    elif currTheme == 'light-warm':
        self.session.props.theme = 'dark-warm'
elif currTheme == 'dark':
    self.session.props.theme = 'dark-cool'
```

- **`root/Cool Warm Cont/Options/Cool Cont`** `dom.onClick`, script action, scope `G`

```python
# Cool must use light-cool/dark-cool so BH --ct-water and cool neutrals load.
# Stock light/dark bundles do not include disk theme overrides.
currTheme = self.session.props.theme
cool_ok = ['light-cool', 'dark-cool']
if currTheme not in cool_ok:
    if currTheme in ('light-warm', 'light'):
        self.session.props.theme = 'light-cool'
    elif currTheme in ('dark-warm', 'dark'):
        self.session.props.theme = 'dark-cool'
```

- **`root/Cool Warm Cont/Options/Warm Cont`** `dom.onClick`, script action, scope `G`

```python
# Warm stays on light-warm/dark-warm (those thin themes expose --ct-water).
currTheme = self.session.props.theme
warm_ok = ['light-warm', 'dark-warm']
if currTheme not in warm_ok:
    if currTheme in ('light', 'light-cool'):
        self.session.props.theme = 'light-warm'
    elif currTheme in ('dark', 'dark-cool'):
        self.session.props.theme = 'dark-warm'
```

- **`root/Anim Cont/Options/On Cont`** `dom.onClick`, script action, scope `G`

```python
self.session.props.animations = True
try:
    js = "document.documentElement.classList.remove('animations-off');"
    if hasattr(system.perspective, 'runJavaScriptAsync'):
        system.perspective.runJavaScriptAsync(js)
    elif hasattr(system.perspective, 'runJavaScript'):
        system.perspective.runJavaScript(js)
except:
    pass
```

- **`root/Anim Cont/Options/Off Cont`** `dom.onClick`, script action, scope `G`

```python
self.session.props.animations = False
try:
    js = "document.documentElement.classList.add('animations-off');"
    if hasattr(system.perspective, 'runJavaScriptAsync'):
        system.perspective.runJavaScriptAsync(js)
    elif hasattr(system.perspective, 'runJavaScript'):
        system.perspective.runJavaScript(js)
except:
    pass
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [00\_Pages/00\_Docked/\_Assets/UserSettings](./usersettings.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Header` | 2 | style class |
| `account-popup` | 1 | stylesheet |
| `bg-component` | 6 | stylesheet |
| `theme-toggle` | 4 | style class |
| `theme-toggle-option` | 6 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
