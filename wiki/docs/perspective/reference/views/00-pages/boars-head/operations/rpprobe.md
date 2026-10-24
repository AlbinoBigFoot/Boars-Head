---
title: "_RPProbe"
sidebar_label: "_RPProbe"
description: "Perspective view 00_Pages/Boars Head/Operations/_RPProbe (Page): 5 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_RPProbe", "_RPProbe", "/zz-rp-probe"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Operations/_RPProbe`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_RPProbe` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_RPProbe/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_RPProbe |
| Routes | `/zz-rp-probe` (Probe) |
| Root | `ia.container.flex`, no default size |
| Size | 5 components, 4 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:30:00Z by the Designer |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x1.

```text
root  ia.container.flex
  L0  ia.display.label  [1 binding]
  L1  ia.display.label  [1 binding]
  L2  ia.display.label  [1 binding]
  L3  ia.display.label  [1 binding]
```

## Bindings

4 bindings: expr 4.

**`root/L0`**

- `props.text`: expression

```js
'00 | ' + toStr({session.custom.Permissions._Test.Verify})
```


**`root/L1`**

- `props.text`: expression

```js
'01 | ' + toStr(runScript("shared.Security.permissions", 0, asList('ReadOnly'), tag('[default]_Config/RolesPermissions'), tag('[default]_Config/Security/FullPermissionRoles'), tag('[default]_Config/Security/RoleInherits'))['_Test']['Verify'])
```


**`root/L2`**

- `props.text`: expression

```js
'02 | ' + toStr(runScript("shared.Security.permissions", 0, asList('Maintenance'), tag('[default]_Config/RolesPermissions'), tag('[default]_Config/Security/FullPermissionRoles'), tag('[default]_Config/Security/RoleInherits'))['_Test']['Verify'])
```


**`root/L3`**

- `props.text`: expression

```js
'03 | ' + toStr(len(forEach({session.custom.Permissions}, 1)))
```


Project script calls: [shared.Security.permissions](../../../../../../scripting/reference/modules/shared-security.md).

## Tags And Data

- `[default]_Config/RolesPermissions`
- `[default]_Config/Security/FullPermissionRoles`
- `[default]_Config/Security/RoleInherits`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
