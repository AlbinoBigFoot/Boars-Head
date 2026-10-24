---
title: "shared.Scale"
sidebar_label: "shared.Scale"
description: "Script module shared.Scale: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`  
**Lines:** 89. **Functions:** 5. **Called as:** `shared.Scale.<function>(...)`

## What the source says

```text
Coordinate-container view scaling (Scout-style).
PROP_CENTER_V2: always center X and Y.
Bind root/Canvas props.style.transform via expr-struct + script:
return shared.Scale.cssTransform(value)

value keys:
scale / Scale          — truthy enables; falsy returns "none"
primaryViewWidth/Height — page.props.dimensions.primaryView.*
defaultViewWidth/Height — view.props.defaultSize.*
```

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_truthy`](#_truthy) (internal) | | 0 |
| [`_num`](#_num) (internal) | | 0 |
| [`_get`](#_get) (internal) | | 0 |
| [`transformParams`](#transformparams) | Return scale factor and pre-scale translate for cssTransform(), or None when scaling is off. | 0 |
| [`cssTransform`](#csstransform) | Return CSS transform string: scale(...) translate(...px, ...px). | 16 |

### \_truthy {#_truthy}

```python
def _truthy(v)
```
Line 12 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`.

_No docstring._

Used inside the module by: `transformParams`

### \_num {#_num}

```python
def _num(v)
```
Line 23 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`.

_No docstring._

Used inside the module by: `transformParams`

### \_get {#_get}

```python
def _get(value, *keys)
```
Line 32 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`.

_No docstring._

Used inside the module by: `transformParams`

### transformParams {#transformparams}

```python
def transformParams(value)
```
Line 45 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`.

```text
Return scale factor and pre-scale translate for cssTransform(), or None when scaling is off.
Matches: scale(s) translate(tx, ty) with transform-origin top left.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `cssTransform`

### cssTransform {#csstransform}

```python
def cssTransform(value)
```
Line 81 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Scale/code.py`.

```text
Return CSS transform string: scale(...) translate(...px, ...px).
Fits defaultSize into primaryView and keeps it centered (both axes).
```

<details>
<summary>Called from 16 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Machine Room/Overview` | view | `root/Canvas binding props.style.transform` |
| `00_Pages/Groveport/Condensers/Utility/Overview` | view | `root/Canvas binding props.style.transform` |
| `00_Pages/Groveport/Machine Room/Utility/Overview` | view | `root/Canvas binding props.style.transform` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/Handtman` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/Hopper` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/LazySusan` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/Loaders` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/RollStock` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Production/Level3/VatDumper` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw binding props.style.transform` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapDisplay` | view | `root/Canvas binding props.style.transform` |
</details>
