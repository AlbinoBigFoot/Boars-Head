---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Utility/Overview (Page): 54 components, 26 bindings, 5 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Utility/Overview", "Overview", "/", "/plants/groveport/utility-overview"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Utility/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Utility/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Utility &gt; Overview |
| Routes | `/` (Groveport Utility Overview)<br/>`/plants/groveport/utility-overview` (Groveport Utility Overview) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 54 components, 26 bindings, 5 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-08-21T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `highlightStatus` | `""` | not persistent |
| `highlightCg` | `""` | not persistent |
| `highlightArea` | `""` | not persistent |

## Component Tree

Component types: ia.container.flex x26, ia.display.view x21, ia.display.label x6, ia.container.coord x1.

<details>
<summary>Component tree (54 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Draw  ia.container.coord  [1 binding]
    FillMain  ia.container.flex
    FillEast  ia.container.flex
    FillNorth  ia.container.flex
    FillSouth  ia.container.flex
    OL_TopLeft  ia.container.flex
    OL_NBumpLeft  ia.container.flex
    OL_NBumpTop  ia.container.flex
    OL_NBumpRight  ia.container.flex
    OL_TopRight  ia.container.flex
    OL_Right  ia.container.flex
    OL_Left  ia.container.flex
    OL_BotLeft  ia.container.flex
    OL_SBumpLeft  ia.container.flex
    OL_SBumpBottom  ia.container.flex
    OL_SBumpRight  ia.container.flex
    OL_BotRight  ia.container.flex
    DivEast  ia.container.flex
    DivEastH1  ia.container.flex
    DivEastH2  ia.container.flex
    DivEastH3  ia.container.flex
    DivEastH4  ia.container.flex
    Room_MachineRoom  ia.container.flex  [1 event]
      Label  ia.display.label
    StatusStack  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatuses]
    Zone_Dock  ia.container.flex
    Lbl_Dock  ia.display.label
    CG-F2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-F3  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-E2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-E3  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-F1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-F4  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-E1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-E4  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-G5  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-G4  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-G3  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-G2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-G1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-B2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-C1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-B1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-A2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-A1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    CG-D1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Evaporator]
    UndSuperchill  ia.container.flex  [1 binding; 1 event]
      Label  ia.display.label
      Value  ia.display.label  [1 binding; 1 event]
    UndFreezer  ia.container.flex  [1 binding; 1 event]
      Label  ia.display.label
      Value  ia.display.label  [1 binding; 1 event]
    KpiRail  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewKpis]
```

</details>

## Bindings

26 bindings: expr-struct 20, expr 6.

<details>
<summary>All 26 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Draw`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
scale: {view.params.Scale}
defaultViewHeight: {view.props.defaultSize.height}
defaultViewWidth: {view.props.defaultSize.width}
primaryViewHeight: {page.props.dimensions.primaryView.height}
primaryViewWidth: {page.props.dimensions.primaryView.width}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Scale.cssTransform(value)
```


**`root/Draw/CG-F2`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-F2'
myArea: 'West PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-F3`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-F3'
myArea: 'West PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-E2`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-E2'
myArea: 'East PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-E3`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-E3'
myArea: 'East PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-F1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-F1'
myArea: 'West PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-F4`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-F4'
myArea: 'West PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-E1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-E1'
myArea: 'East PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-E4`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-E4'
myArea: 'East PH'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-G5`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-G5'
myArea: 'Dock'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-G4`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-G4'
myArea: 'Dock'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-G3`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-G3'
myArea: 'Dock'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-G2`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-G2'
myArea: 'Dock'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-G1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-G1'
myArea: 'Dock'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-B2`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-B2'
myArea: 'SuperChill'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-C1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-C1'
myArea: 'Club'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Club/Utility/CG-C1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Club/Utility/CG-C1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Club/Utility/CG-C1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-B1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-B1'
myArea: 'SuperChill'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-A2`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-A2'
myArea: 'Freezer'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-A1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-A1'
myArea: 'Freezer'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/CG-D1`**

- `props.style.opacity`: structured expression (expr-struct), then script + expression transform

```js
statusFilter: {view.custom.highlightStatus}
cgFilter: {view.custom.highlightCg}
areaFilter: {view.custom.highlightArea}
myCg: 'CG-D1'
myArea: 'Palletizing'
myStatus: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/HmiStatus')), false), false), try(tag('[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/HmiStatus'), null), null)
```

waitOnAll: `False`

Transform 1, script:

```python
# Priority: highlightCg > highlightArea+status > highlightArea > highlightStatus > none
status_f = value.get('statusFilter') or ''
cg_f = value.get('cgFilter') or ''
area_f = value.get('areaFilter') or ''
my_cg = value.get('myCg') or ''
my_area = value.get('myArea') or ''
raw = value.get('myStatus')
try:
    s = int(raw) if raw is not None else None
except:
    s = None

def coarse_code(sv):
    if sv == 1:
        return 'CLG'
    if sv in (2, 6, 7, 8, 9):
        return 'DFT'
    if sv == 3:
        return 'FLT'
    if sv == 5:
        return 'IDLE'
    return 'STOP'

def status_match(filt, sv):
    f = str(filt or '').strip().upper()
    if not f:
        return True
    # Stage-accurate dwell rows (StatusIndicator DFT PD/HG/BLD/FD)
    if f == 'DFT PD':
        return sv == 6
    if f == 'DFT HG':
        return sv == 7
    if f == 'DFT BLD':
        return sv == 8
    if f == 'DFT FD':
        return sv == 9
    # Coarse DFT (donut / stack) includes base + all stages
    if f == 'DFT':
        return sv in (2, 6, 7, 8, 9)
    return coarse_code(sv) == f
# ... 11 more line(s): see the view.json
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/HmiStatus')), false), false), {value}, 0.5)
```


**`root/Draw/UndSuperchill`**

- `props.style.classes`: expression

```js
trim(if(coalesce({session.custom.CanOpenFaceplates}, false), ' faceplate-hover', ''))
```


**`root/Draw/UndSuperchill/Value`**

- `props.text`: expression

```js
if(!isGood(tag('[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp/AIn/Val')),
	'— °F',
	numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp/AIn/Val'), 0), '0.00') + ' °F')
```


**`root/Draw/UndFreezer`**

- `props.style.classes`: expression

```js
trim(if(coalesce({session.custom.CanOpenFaceplates}, false), ' faceplate-hover', ''))
```


**`root/Draw/UndFreezer/Value`**

- `props.text`: expression

```js
if(!isGood(tag('[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp/AIn/Val')),
	'— °F',
	numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp/AIn/Val'), 0), '0.00') + ' °F')
```

</details>

## Event Scripts And Handlers

- **`root/Draw/Room_MachineRoom`** `dom.onClick`, script action, scope `G`

```python
Navigation.Nav.navigate({'action': 'page', 'page': '/machine-room'})
```

- **`root/Draw/UndSuperchill`** `dom.onClick`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp'
title = 'SUPERCHILL UND.FLOOR'
params = {'tagPath': tagPath, 'deviceType': 'Sensor', 'webGuiUrl': '', 'showControls': True,
    'showConfiguration': True, 'showInterlocks': True, 'showTrend': True, 'showAlarmConfiguration': True,
    'showAlarms': True, 'title': title}
Navigation.Faceplate.openFaceplate('sensor-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/Faceplate',
    False, title, 560, 640, params)
```

- **`root/Draw/UndSuperchill/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp/AIn/Val')
```

- **`root/Draw/UndFreezer`** `dom.onClick`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp'
title = 'FREEZER UND.FLOOR'
params = {'tagPath': tagPath, 'deviceType': 'Sensor', 'webGuiUrl': '', 'showControls': True,
    'showConfiguration': True, 'showInterlocks': True, 'showTrend': True, 'showAlarmConfiguration': True,
    'showAlarms': True, 'title': title}
Navigation.Faceplate.openFaceplate('sensor-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/Faceplate',
    False, title, 560, 640, params)
```

- **`root/Draw/UndFreezer/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp/AIn/Val')
```

- **`root`** message handler `UtilityOverviewHighlight` (scope: page)

```python
action = ''
try:
    action = str(payload.get('action') or '')
except:
    action = ''
status = ''
cg = ''
area = ''
try:
    status = str(payload.get('status') or '')
except:
    status = ''
try:
    cg = str(payload.get('cg') or '')
except:
    cg = ''
try:
    area = str(payload.get('area') or '')
except:
    area = ''
if action == 'select':
    cur = ''
    try:
        cur = str(self.view.custom.highlightCg or '')
    except:
# ... 53 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (3): [00\_Pages/Groveport/Utility/OverviewKpis](./overviewkpis.md), [00\_Pages/Groveport/Utility/OverviewStatuses](./overviewstatuses.md), [02\_Components/01\_Devices/Evaporator](../../../02-components/01-devices/evaporator.md)

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/Faceplate](../../../01-popups/00-faceplates/faceplate.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 3 | style class |
| `Fonts/Value` | 2 | style class |
| `bg-page` | 1 | style class |
| `fs-12` | 2 | style class |
| `fs-15` | 1 | style class |
| `fs-9` | 2 | style class |
| `fw-600` | 3 | style class |
| `fw-700` | 2 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

<details>
<summary>23 literal tag paths</summary>

- `[default]Boars_Head/GrovePort/Club/Utility/CG-C1/HmiStatus`
- `[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/HmiStatus`
- `[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/HmiStatus`
- `[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/HmiStatus`
- `[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/HmiStatus`
- `[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/HmiStatus`
- `[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/HmiStatus`
- `[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/HmiStatus`
- `[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/HmiStatus`
- `[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/HmiStatus`
- `[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp`
- `[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp/AIn/Val`
- `[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus`
- `[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/HmiStatus`
- `[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/HmiStatus`
- `[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp`
- `[default]Boars_Head/GrovePort/SuperChill/Sensors/Underfloor Temp/AIn/Val`
- `[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/HmiStatus`
- `[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/HmiStatus`
- `[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/HmiStatus`
- `[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/HmiStatus`
- `[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/HmiStatus`
- `[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/HmiStatus`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
