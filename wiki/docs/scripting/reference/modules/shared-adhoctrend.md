---
title: "shared.AdhocTrend"
sidebar_label: "shared.AdhocTrend"
description: "Script module shared.AdhocTrend: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`  
**Lines:** 1107. **Functions:** 52. **Called as:** `shared.AdhocTrend.<function>(...)`

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.dataset`, `system.date`, `system.perspective`, `system.tag`, `system.util` |
| Logger names | `AdhocTrend`, `trend-context` |
| Calls modules | [shared.TrendContext](./shared-trendcontext.md) |
| Called by modules | [shared.TrendContext](./shared-trendcontext.md) |

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`default_plots`](#default_plots) | | 2 |
| [`_default_plot_title`](#_default_plot_title) (internal) | | 0 |
| [`_is_string`](#_is_string) (internal) | | 0 |
| [`_as_list`](#_as_list) (internal) | | 0 |
| [`palette_colors`](#palette_colors) | | 4 |
| [`color_for_index`](#color_for_index) | | 2 |
| [`_cfg_get`](#_cfg_get) (internal) | | 3 |
| [`_cfg_set`](#_cfg_set) (internal) | | 0 |
| [`_plot_field`](#_plot_field) (internal) | | 0 |
| [`plain_plots`](#plain_plots) | | 5 |
| [`plain_pen_plots`](#plain_pen_plots) | | 6 |
| [`plain_disabled_pens`](#plain_disabled_pens) | | 4 |
| [`is_pen_enabled`](#is_pen_enabled) | | 0 |
| [`toggle_pen_enabled`](#toggle_pen_enabled) | | 1 |
| [`normalize_config`](#normalize_config) | | 1 |
| [`_path_segments`](#_path_segments) (internal) | | 0 |
| [`alias_for`](#alias_for) | | 4 |
| [`pen_label`](#pen_label) | | 1 |
| [`pen_labels`](#pen_labels) | | 0 |
| [`tag_kind`](#tag_kind) | | 0 |
| [`history_path`](#history_path) | | 0 |
| [`_warn_once`](#_warn_once) (internal) | | 0 |
| [`build_pens`](#build_pens) | | 2 |
| [`pens_for_plot`](#pens_for_plot) | | 1 |
| [`resolve_column`](#resolve_column) | | 0 |
| [`series_color_list`](#series_color_list) | | 2 |
| [`build_series`](#build_series) | | 1 |
| [`build_key`](#build_key) | | 1 |
| [`_new_plot_id`](#_new_plot_id) (internal) | | 0 |
| [`add_plot`](#add_plot) | | 0 |
| [`apply_add_plot`](#apply_add_plot) | | 0 |
| [`prompt_add_plot`](#prompt_add_plot) | | 1 |
| [`confirm_add_plot`](#confirm_add_plot) | | 1 |
| [`close_name_plot_popup`](#close_name_plot_popup) | | 2 |
| [`removable_plots`](#removable_plots) | | 0 |
| [`remove_plot`](#remove_plot) | | 1 |
| [`prompt_remove_plot`](#prompt_remove_plot) | | 1 |
| [`confirm_remove_plot`](#confirm_remove_plot) | | 1 |
| [`close_remove_plot_popup`](#close_remove_plot_popup) | | 2 |
| [`remove_plot_dropdown_options`](#remove_plot_dropdown_options) | | 1 |
| [`move_pen`](#move_pen) | | 2 |
| [`route_new_tag`](#route_new_tag) | | 0 |
| [`route_new_pen`](#route_new_pen) | | 3 |
| [`plot_dropdown_options`](#plot_dropdown_options) | | 2 |
| [`plot_options_overrides`](#plot_options_overrides) | | 0 |
| [`plot_chart_height`](#plot_chart_height) | | 1 |
| [`_ev`](#_ev) (internal) | | 0 |
| [`_ms`](#_ms) (internal) | | 0 |
| [`pause_live`](#pause_live) | | 3 |
| [`zoom_event`](#zoom_event) | | 4 |
| [`zoom_step`](#zoom_step) | | 2 |
| [`zoom_reset`](#zoom_reset) | | 9 |

### default\_plots {#default_plots}

```python
def default_plots()
```
Line 31 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Buttons/ClearPens event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | view | `root/LoadButton event component.onActionPerformed` |

### \_default\_plot\_title {#_default_plot_title}

```python
def _default_plot_title(index)
```
Line 36 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### \_is\_string {#_is_string}

```python
def _is_string(value)
```
Line 49 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### \_as\_list {#_as_list}

```python
def _as_list(value)
```
Line 53 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### palette\_colors {#palette_colors}

```python
def palette_colors(colors)
```
Line 91 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TagTree/AddToTrend event component.onActionPerformed` |
| `shared.TrendContext.add` | script | |
| `shared.TrendContext.summary` | script | |

### color\_for\_index {#color_for_index}

```python
def color_for_index(colors, index)
```
Line 129 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `shared.TrendContext.summary` | script | |

### \_cfg\_get {#_cfg_get}

```python
def _cfg_get(cfg, key, default=None)
```
Line 140 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/AutoScale event dom.onClick` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |
| `shared.TrendContext.summary` | script | |

### \_cfg\_set {#_cfg_set}

```python
def _cfg_set(cfg, key, value)
```
Line 160 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### \_plot\_field {#_plot_field}

```python
def _plot_field(p, key, default=None)
```
Line 176 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### plain\_plots {#plain_plots}

```python
def plain_plots(cfg_or_plots)
```
Line 194 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/Plots binding props.instances` |
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | view | `root/LoadButton event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |
| `shared.TrendContext.summary` | script | |

### plain\_pen\_plots {#plain_pen_plots}

```python
def plain_pen_plots(cfg)
```
Line 235 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/Trend` | view | `root message handler AdhocTrendDeleteRow` |
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | view | `root/LoadButton event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |
| `shared.TrendContext.remove` | script | |
| `shared.TrendContext.summary` | script | |

### plain\_disabled\_pens {#plain_disabled_pens}

```python
def plain_disabled_pens(cfg)
```
Line 251 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/Trend` | view | `root message handler AdhocTrendDeleteRow` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |
| `shared.TrendContext.remove` | script | |

### is\_pen\_enabled {#is_pen_enabled}

```python
def is_pen_enabled(disabled_pens, alias, tag_path=None)
```
Line 283 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### toggle\_pen\_enabled {#toggle_pen_enabled}

```python
def toggle_pen_enabled(cfg, alias_or_path)
```
Line 304 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root message handler AdhocTrendDisableRow` |

### normalize\_config {#normalize_config}

```python
def normalize_config(cfg)
```
Line 321 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | view | `root/LoadButton event component.onActionPerformed` |

### \_path\_segments {#_path_segments}

```python
def _path_segments(tag_path)
```
Line 337 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### alias\_for {#alias_for}

```python
def alias_for(tag_path)
```
Line 355 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/Trend` | view | `root message handler AdhocTrendDeleteRow` |
| `shared.TrendContext.remove` | script | |
| `shared.TrendContext.summary` | script | |

### pen\_label {#pen_label}

```python
def pen_label(tag_path)
```
Line 367 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |

### pen\_labels {#pen_labels}

```python
def pen_labels(tag_paths)
```
Line 390 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### tag\_kind {#tag_kind}

```python
def tag_kind(tag_path)
```
Line 395 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### history\_path {#history_path}

```python
def history_path(tag)
```
Line 410 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### \_warn\_once {#_warn_once}

```python
def _warn_once(where, err)
```
Line 426 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### build\_pens {#build_pens}

```python
def build_pens(tags, colors, pen_plots=None, plots=None, disabled_pens=None)
```
Line 437 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `binding custom.pens` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |

### pens\_for\_plot {#pens_for_plot}

```python
def pens_for_plot(pens, pen_plots, plot_id, first_plot_id)
```
Line 497 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.pens` |

### resolve\_column {#resolve_column}

```python
def resolve_column(dataset, alias)
```
Line 559 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### series\_color\_list {#series_color_list}

```python
def series_color_list(pens)
```
Line 578 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchart binding props.options.colors` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchartPan binding props.options.colors` |

### build\_series {#build_series}

```python
def build_series(dataset, pens)
```
Line 606 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchart binding props.series` |

### build\_key {#build_key}

```python
def build_key(pens, aggregate)
```
Line 662 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `binding custom.key` |

### \_new\_plot\_id {#_new_plot_id}

```python
def _new_plot_id(plots)
```
Line 684 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### add\_plot {#add_plot}

```python
def add_plot(cfg, title=None, kind="analog")
```
Line 696 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### apply\_add\_plot {#apply_add_plot}

```python
def apply_add_plot(cfg, title=None, kind="analog")
```
Line 712 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### prompt\_add\_plot {#prompt_add_plot}

```python
def prompt_add_plot()
```
Line 725 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Buttons/AddPlot event component.onActionPerformed` |

### confirm\_add\_plot {#confirm_add_plot}

```python
def confirm_add_plot(cfg, title)
```
Line 741 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/NamePlot` | view | `root/Buttons/Confirm event component.onActionPerformed` |

### close\_name\_plot\_popup {#close_name_plot_popup}

```python
def close_name_plot_popup()
```
Line 754 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/NamePlot` | view | `root/Buttons/Cancel event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/NamePlot` | view | `root/Buttons/Confirm event component.onActionPerformed` |

### removable\_plots {#removable_plots}

```python
def removable_plots(cfg)
```
Line 762 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### remove\_plot {#remove_plot}

```python
def remove_plot(cfg, plot_id)
```
Line 772 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/Header/RemovePlot event component.onActionPerformed` |

### prompt\_remove\_plot {#prompt_remove_plot}

```python
def prompt_remove_plot(cfg)
```
Line 800 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Buttons/RemovePlot event component.onActionPerformed` |

### confirm\_remove\_plot {#confirm_remove_plot}

```python
def confirm_remove_plot(cfg, plot_id)
```
Line 833 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | view | `root/Buttons/Confirm event component.onActionPerformed` |

### close\_remove\_plot\_popup {#close_remove_plot_popup}

```python
def close_remove_plot_popup()
```
Line 841 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | view | `root/Buttons/Cancel event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | view | `root/Buttons/Confirm event component.onActionPerformed` |

### remove\_plot\_dropdown\_options {#remove_plot_dropdown_options}

```python
def remove_plot_dropdown_options(cfg)
```
Line 849 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | view | `root/PlotSelect/Dropdown binding props.options` |

### move\_pen {#move_pen}

```python
def move_pen(cfg, tag_or_alias, plot_id)
```
Line 854 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Pen` | view | `root/PlotSelect binding props.value` |
| `98_Configuration/AdhocTrend/_Assets/PenPlot` | view | `root/Plot binding props.value` |

### route\_new\_tag {#route_new_tag}

```python
def route_new_tag(cfg, tag_path, data_type=None)
```
Line 876 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### route\_new\_pen {#route_new_pen}

```python
def route_new_pen(cfg, tag_path, data_type=None)
```
Line 919 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root/AddToTrend event dom.onClick` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TagTree/AddToTrend event component.onActionPerformed` |
| `shared.TrendContext.add` | script | |

### plot\_dropdown\_options {#plot_dropdown_options}

```python
def plot_dropdown_options(plots)
```
Line 924 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Pen` | view | `root/PlotSelect binding props.options` |
| `98_Configuration/AdhocTrend/_Assets/PenPlot` | view | `root/Plot binding props.options` |

### plot\_options\_overrides {#plot_options_overrides}

```python
def plot_options_overrides(kind)
```
Line 932 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### plot\_chart\_height {#plot_chart_height}

```python
def plot_chart_height(faceplate_mode=False, pens_collapsed=False, plot_count=1, viewport_height=None)
```
Line 953 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/Plots binding props.instances` |

### \_ev {#_ev}

```python
def _ev(obj, key)
```
Line 989 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### \_ms {#_ms}

```python
def _ms(v)
```
Line 1000 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

### pause\_live {#pause_live}

```python
def pause_live(cfg)
```
Line 1013 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/DragMode/ModePan event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomArea event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomTime event component.onActionPerformed` |

### zoom\_event {#zoom_event}

```python
def zoom_event(session, plot_id, event, chart=None)
```
Line 1026 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchart event component.scrolledHandler` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchart event component.zoomedHandler` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchartPan event component.scrolledHandler` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchartPan event component.zoomedHandler` |

### zoom\_step {#zoom_step}

```python
def zoom_step(session, factor)
```
Line 1058 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/ZoomIn event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/ZoomOut event component.onActionPerformed` |

### zoom\_reset {#zoom_reset}

```python
def zoom_reset(session)
```
Line 1094 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py`.

_No docstring._

<details>
<summary>Called from 9 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/ResetZoom event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/ChartTools/Row/ZoomChip event dom.onClick` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Icons/LivePause event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range1H event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range24H event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range7D event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/Trend` | view | `root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range8H event component.onActionPerformed` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchart event dom.onDoubleClick` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root/apexchartPan event dom.onDoubleClick` |
</details>
