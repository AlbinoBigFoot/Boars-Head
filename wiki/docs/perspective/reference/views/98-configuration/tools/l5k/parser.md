---
title: "Parser"
sidebar_label: "Parser"
description: "Perspective view 98_Configuration/Tools/L5K/Parser (Configuration / tool view): 26 components, 10 bindings, 5 event scripts."
generated: true
keywords: ["98_Configuration/Tools/L5K/Parser", "Parser"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/Tools/L5K/Parser`.

| | |
|---|---|
| View path | `98_Configuration/Tools/L5K/Parser` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/Tools/L5K/Parser/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; Tools &gt; L5K &gt; Parser |
| Root | `ia.container.coord`, width 1359 |
| Size | 26 components, 10 bindings, 5 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2025-10-06T22:26:57Z by admin |

## Component Tree

Component types: ia.display.label x11, ia.input.button x4, ia.input.checkbox x3, ia.display.accordion x2, ia.input.text-field x2, ia.container.coord x1, ia.input.fileupload x1, ia.container.tab x1, ia.display.view x1.

<details>
<summary>Component tree (26 components)</summary>

```text
root  ia.container.coord  [3 bindings]
  FileUpload  ia.input.fileupload  [1 event]
  Label  ia.display.label
  TabContainer  ia.container.tab
    Accordion  ia.display.accordion  [1 binding]
    EmbeddedView  ia.display.view  [1 binding; view: 98_Configuration/Tools/L5K/Tags]
    Accordion_0  ia.display.accordion  [1 binding]
  Label_1  ia.display.label
  Label_2  ia.display.label
  Label_3  ia.display.label
  Label_4  ia.display.label
  Device Name  ia.input.text-field
  Create Simulation Device  ia.input.button  [1 binding; 1 event]
  Create Simulation Program Export  ia.input.button  [1 binding; 1 event]
  Create UDT Tag Export  ia.input.button  [1 binding; 1 event]
  Create Tag Export  ia.input.button  [1 binding; 1 event]
  Label_5  ia.display.label
  Label_6  ia.display.label
  Checkbox  ia.input.checkbox
  Checkbox_0  ia.input.checkbox
  Checkbox_1  ia.input.checkbox
  Label_7  ia.display.label
  UDT Prefix  ia.input.text-field
  Label_8  ia.display.label
  Label_9  ia.display.label
  Label_10  ia.display.label
```

</details>

## Bindings

10 bindings: expr 5, property 3, expr-struct 2.

**`root`**

- `custom.parsedFile`: expression, then script transform

```js
now(0)
```

Transform 1, script:

```python
return {
  "parsed": False,
  "udts": [],
  "tags": [],
  "programs": [],
  "comments": {},
  "success": True,
  "error": ""
}
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

**`root/TabContainer/Accordion`**

- `props.items`: property `/root.custom.parsedFile`, then script transform

Transform 1, script:

```python
if value.parsed and value.success:
    ret = []
    for udt in value.udts:
        name = udt.name
        description = udt.description
        stringFamily = udt.stringFamily
        tags = udt.tags
        ret.append({
          "expanded": False,
          "header": {
            "toggle": {
              "enabled": True,
              "expandedIcon": {
                "path": "material/expand_less",
                "color": "",
                "style": {
                  "classes": ""
                }
              },
              "collapsedIcon": {
                "path": "material/expand_more",
                "color": "",
                "style": {
                  "classes": ""
                }
              }
            },
            "content": {
              "type": "text",
              "text": name,
              "description": description,
              "stringFamily": stringFamily,
              "useDefaultViewWidth": False,
              "useDefaultViewHeight": False,
              "viewPath": "",
              "viewParams": {},
              "style": {
                "classes": ""
              }
            },
# ... 23 more line(s): see the view.json
```


**`root/TabContainer/EmbeddedView`**

- `props.params.tags`: property `/root.custom.parsedFile.tags`

**`root/TabContainer/Accordion_0`**

- `props.items`: property `/root.custom.parsedFile`, then script transform

Transform 1, script:

```python
if value.parsed and value.success:
    ret = []
    for program in value.programs:
        name = program.name
        tags = program.tags
        ret.append({
          "expanded": False,
          "header": {
            "toggle": {
              "enabled": True,
              "expandedIcon": {
                "path": "material/expand_less",
                "color": "",
                "style": {
                  "classes": ""
                }
              },
              "collapsedIcon": {
                "path": "material/expand_more",
                "color": "",
                "style": {
                  "classes": ""
                }
              }
            },
            "content": {
              "type": "text",
              "text": name,
              "useDefaultViewWidth": False,
              "useDefaultViewHeight": False,
              "viewPath": "",
              "viewParams": {},
              "style": {
                "classes": ""
              }
            },
            "height": "40px",
            "reverse": False,
            "style": {
              "classes": ""
# ... 19 more line(s): see the view.json
```


**`root/Create Simulation Device`**

- `props.enabled`: expression

```js
len({../Device Name.props.text}) > 0
```


**`root/Create Simulation Program Export`**

- `props.enabled`: expression

```js
{parent.custom.parsedFile.parsed} && {parent.custom.parsedFile.success}
```


**`root/Create UDT Tag Export`**

- `props.enabled`: expression

```js
{parent.custom.parsedFile.parsed} && {parent.custom.parsedFile.success}
```


**`root/Create Tag Export`**

- `props.enabled`: expression

```js
{parent.custom.parsedFile.parsed} && {parent.custom.parsedFile.success} && len({../Device Name.props.text})
```


## Event Scripts And Handlers

- **`root/FileUpload`** `component.onFileReceived`, script action, scope `G`

```python
import traceback
l5kFile = event.file.getString()
selectTags = self.getSibling("Checkbox").props.selected
allowHidden = self.getSibling("Checkbox_0").props.selected
useStoredValues = self.getSibling("Checkbox_1").props.selected

try:
    (udts, tags, programs, comments) = L5K.Parser.parse(l5kFile, selectTags, allowHidden, useStoredValues)
    success = True
    error = ""
except:
    udts = []
    tags = []
    programs = []
    comments = {}
    success = False
    error = "Error parsing L5K file. Please try again."
    log = system.util.getLogger("L5K Parser")
    log.info(traceback.format_exc())
    system.perspective.openPopup(id="message", view="98_Configuration/Tools/L5K/Message", params={"message":error, "error":True}, title="Error")
    
self.parent.custom.parsedFile = {"udts":udts, "tags":tags, "programs":programs, "comments":comments, "parsed":True, "success":success, "error":error}
```

- **`root/Create Simulation Device`** `component.onActionPerformed`, script action, scope `G`

```python
deviceName = self.getSibling("Device Name").props.text
devices = system.dataset.toPyDataSet(system.device.listDevices())
exists = False
for device in devices:
    if device["Name"] == deviceName:
        exists = True
        break

if not exists:
    system.device.addDevice(deviceName=deviceName, deviceType="ProgrammableSimulatorDevice", deviceProps={})
    system.perspective.openPopup(id="message", view="98_Configuration/Tools/L5K/Message", params={"message":"Device '%s' added" % deviceName, "error":False}, title="Message")
else:
    system.perspective.openPopup(id="message", view="98_Configuration/Tools/L5K/Message", params={"message":"Device '%s' already exists" % deviceName, "error":True}, title="Error")
```

- **`root/Create Simulation Program Export`** `component.onActionPerformed`, script action, scope `G`

```python
udts = self.parent.getChild("TabContainer").getChild("Accordion").props.items
tags = self.parent.getChild("TabContainer").getChild("EmbeddedView").props.params.tags
programs = self.parent.getChild("TabContainer").getChild("Accordion_0").props.items
csv = L5K.Parser.generateSimulationCSV(udts, tags, programs)
system.perspective.download(filename="instructions.csv", data=csv, contentType="application/csv")
```

- **`root/Create UDT Tag Export`** `component.onActionPerformed`, script action, scope `G`

```python
udtPrefix = self.getSibling("UDT Prefix").props.text
udts = self.parent.getChild("TabContainer").getChild("Accordion").props.items
tags = self.parent.getChild("TabContainer").getChild("EmbeddedView").props.params.tags
programs = self.parent.getChild("TabContainer").getChild("Accordion_0").props.items
json = L5K.Parser.generateUDTExport(udtPrefix, udts, tags, programs)    
system.perspective.download(filename="udts.json", data=json, contentType="application/json")
```

- **`root/Create Tag Export`** `component.onActionPerformed`, script action, scope `G`

```python
deviceName = self.getSibling("Device Name").props.text
udtPrefix = self.getSibling("UDT Prefix").props.text
udts = self.parent.getChild("TabContainer").getChild("Accordion").props.items
tags = self.parent.getChild("TabContainer").getChild("EmbeddedView").props.params.tags
programs = self.parent.getChild("TabContainer").getChild("Accordion_0").props.items
comments = self.parent.custom.parsedFile.comments
json = L5K.Parser.generateTagExport(deviceName, udtPrefix, udts, tags, programs, comments)
system.perspective.download(filename="tags.json", data=json, contentType="application/json")
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [L5K.Parser.generateSimulationCSV](../../../../../../scripting/reference/modules/l5k-parser.md), [L5K.Parser.generateTagExport](../../../../../../scripting/reference/modules/l5k-parser.md), [L5K.Parser.generateUDTExport](../../../../../../scripting/reference/modules/l5k-parser.md), [L5K.Parser.parse](../../../../../../scripting/reference/modules/l5k-parser.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [98\_Configuration/Tools/L5K/Tags](./tags.md)

**Opens or names** (popups, scripts, expressions): [98\_Configuration/Tools/L5K/Message](./message.md)
