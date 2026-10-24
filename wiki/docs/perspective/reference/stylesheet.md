---
title: "Stylesheet Index"
sidebar_label: "Stylesheet Index"
description: "Section index of the BH Advanced Stylesheet (stylesheet.css): every comment block, its line range and the classes it defines."
generated: true
sidebar_position: 8
---

:::note

:::


Source: `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css` (Designer: Project Browser > Perspective > Styles > Advanced Stylesheet). 4899 lines, 393 `.psc-*` classes. Sections start at a comment in column 1. Selectors use `.psc-<class>` for project classes (`Fonts/Label` becomes `.psc-Fonts\/Label`).

## Sections

| Lines | Section comment | Rules | Classes |
|---|---|---|---|
| 1-203 | Direct stylesheet authoring is an advanced feature. Knowledge of CSS required. | 1 | |
| 204-213 | Base marker class for refrigeration status chips | 1 | Refridgeration\_STS |
| 214-220 | Cooling — Figma blue --- | 1 | Refridgeration\_STS, sts-CLG, sts-COOLING |
| 221-226 | Idle / standby — Figma green --- | 1 | Refridgeration\_STS, sts-IDLE |
| 227-233 | Off / stopped — Figma gray --- | 1 | Refridgeration\_STS, sts-OFF, sts-STOP |
| 234-241 | Defrost — Figma pink --- | 1 | Refridgeration\_STS, sts-DEFROST, sts-DFT |
| 242-248 | Abnormal: Fault / alarm — red + left accent --- | 1 | Refridgeration\_STS, sts-FAULT |
| 249-255 | Abnormal: Comm Loss (tag quality Bad) — theme-invariant red + accent --- | 1 | Refridgeration\_STS, sts-COMMLOSS |
| 256-262 | Fallback --- | 1 | Refridgeration\_STS, sts-UNKNOWN |
| 263-285 | Compressor CP/SV mode labels (overview bottom strip) | 4 | comp-mode, comp-mode-auto, comp-mode-manual, comp-mode-remote |
| 286-299 | Device graphic Comm Loss fill — the ONLY colored device body fill. | 1 | device-comm-loss |
| 300-308 | AnalogValue text when PV &gt; SP — theme-invariant (text only, not device fill) | 2 | analog-level-warning, analog-over-sp |
| 309-313 | Accent text matching AnalogValue Numeric value color (optional helpers) | 1 | analog-label |
| 314-330 | Compressor FLA/SVP strip — same 11px metrics as CP:/SV: mode labels; normal weight (not bold) | 2 | comp-analog, comp-analog-eu |
| 331-345 | Evaporator overview fan: counter-clockwise spin when Cooling/Running --- | 4 | fan-spin |
| 346-374 | Cooling tower side-profile fan: foreshortening pulse (scaleX), not Z-rotation. | 6 | ct-fan-side-spin |
| 375-392 | Spray droplets fall when tower is running. | 4 | ct-spray-run |
| 393-414 | Safety Relay ENET Comm LED: flashes green while comm is OK (comm loss = static red, no class) --- | 6 | led-comm-flash |
| 415-425 | /safety-relay page: the component is drawn at a fixed 536 x 404; zoom it to the viewport --- | 3 | safety-relay-zoom |
| 426-455 | /plc-rack: the rack scales to its width; narrow = two banks --- | 7 | plcrack-host, plcrack-rack, plcrack-u114, plcrack-u24, plcrack-u54, plcrack-u96 |
| 456-457 | /plc-rack end --- | 0 | |
| 458-473 | Alarm badge blink (1 Hz) when active AND unacknowledged --- | 4 | alarm-flash |
| 474-503 | Master animations toggle (ChangeTheme → Animations On/Off). | 1 | alarm-flash, animations-off, ct-fan-side-spin, ct-spray-run, fan-spin, led-comm-flash, status-dot-blink |
| 504-508 | Migrated from Designer Style Classes (Colors / Container / Fonts) | 0 | |
| 509-523 | Background / color utility (theme semantic tokens) --- | 4 | bg-component, bg-container, bg-disabled, bg-header |
| 524-541 | Container chrome --- | 3 | container-button, container-card |
| 542-552 | Device-type Unit Overview: 3-column wrap of unit cards | 1 | unit-overview-grid |
| 553-577 | Cards / embeds: allow flex shrink inside hosts; hide H-scroll chrome | 3 | container-card, unit-overview-grid, unit-overview-host, unit-overview-table |
| 578-591 | Keep vertical scroll when many rows; only suppress horizontal bars | 2 | unit-overview-grid, unit-overview-host |
| 592-628 | Scrollbars (global, matches Scout): thin rounded thumb on a transparent track, no arrow buttons. | 7 | container-card-border, themed-scroll, unit-overview-grid, unit-overview-host, unit-overview-table |
| 629-658 | CG AhuEvapHistory cards: 100% width + 2px margin overflows the rail and clips borders/charts. | 7 | ahu-evap-history-card, container-card-border, container-header, container-icon, container-item |
| 659-675 | Typography --- | 4 | Fonts/Header, Fonts/Label, Fonts/Title, Fonts/Value |
| 676-722 | Alarm Status Table row fills | 9 | alarm-row-cleared, alarm-row-critical, alarm-row-critical-ack, alarm-row-high, alarm-row-high-ack, alarm-row-low, alarm-row-low-ack, alarm-row-medium, alarm-row-medium-ack |
| 723-741 | Adhoc Trend toolbar (gear / Realtime\|Historical / time range) | 2 | adhoc-trend-share-label, adhoc-trend-toolbar-icon |
| 742-765 | Save Custom Trend dialog — opaque card (Designer Colors/Background classes removed) | 3 | adhoc-trend-save-dialog, adhoc-trend-save-label, adhoc-trend-save-title |
| 766-777 | Chart area, Tag Browser and Pens on their own surface: the surrounding bg-container / bg-header / | 2 | adhoc-trend-chart-host, adhoc-trend-pens, adhoc-trend-tag-browser, bg-component, bg-header |
| 778-790 | Faceplate Trend tab chart (\_Assets/Trend, every device faceplate): theme card background (was --neutral-40, gr | 2 | faceplate-trend-chart |
| 791-818 | Adhoc Trend ApexCharts — contain paint (no outer scrollbars); tip stays visible | 3 | adhoc-trend-apex, adhoc-trend-chart-host |
| 819-881 | Multi-plot stack: 1 plot fills area; 2+ share equal flex height. | 4 | adhoc-trend-apex, adhoc-trend-plot-slot, adhoc-trend-plots |
| 882-889 | After Pens collapse, force apex SVG/canvas to stretch with host | 1 | adhoc-trend-apex |
| 890-908 | Single-plot only: chart.toolbar.show is driven by showToolbar (n == 1). | 2 | adhoc-trend-apex |
| 909-939 | ApexCharts must stretch to host — avoid default ~800px leaving a right gap | 3 | adhoc-trend-apex, adhoc-trend-plot-header, adhoc-trend-plot-toolbar |
| 940-953 | Left cluster: gear / Realtime / range — flush left with comfortable gaps | 1 | adhoc-trend-plot-toolbar |
| 954-969 | Icon-only − / + / Save / Clear — beat .adhoc-trend-action-btn min-width:108px | 1 | adhoc-trend-add-plot-btn, adhoc-trend-clear-btn, adhoc-trend-remove-plot-btn, adhoc-trend-save-btn |
| 970-993 | PenPlot dropdown: single clean control — no stacked white chrome / overflow peek. | 3 | adhoc-trend-pen-plot-cell |
| 994-1009 | Pens table fills edge-to-edge — no orphan white column chrome after last col | 2 | container-card |
| 1010-1066 | Trending Pens table matches the chart card (same specificity as above, so it must stay after it) | 4 | adhoc-trend-pen-plot-cell, adhoc-trend-pen-plot-select, adhoc-trend-pen-plot-wrap, adhoc-trend-pens |
| 1067-1099 | Kill outer dropdown shell that stacks a second white rect above the control | 4 | adhoc-trend-pen-plot-cell, adhoc-trend-pen-plot-select, adhoc-trend-pen-plot-wrap |
| 1100-1110 | Open menu: compact list (portal may still pick up these when nested under cell) | 1 | adhoc-trend-pen-plot-cell, adhoc-trend-pen-plot-select, adhoc-trend-pen-plot-wrap |
| 1111-1124 | Saved trends Load/Delete embedded view — avoid clipped labels | 2 | adhoc-trend-load-delete-btn, adhoc-trend-load-delete-row |
| 1125-1140 | Adhoc Trend faceplate popup — Ticket Logger card look; fit without outer scroll | 1 | adhoc-trend-faceplate |
| 1141-1163 | Header + close must sit above ApexCharts pan/toolbar and nested embed layers | 3 | adhoc-trend-faceplate-close, adhoc-trend-faceplate-header |
| 1164-1176 | Embedded Trend view inside faceplate — fill remaining height, allow shrink | 1 | adhoc-trend-faceplate-embed |
| 1177-1194 | Faceplate: contain chart paint so outer popup does not grow a scrollbar | 2 | adhoc-trend-apex, adhoc-trend-chart-host, adhoc-trend-faceplate, adhoc-trend-faceplate-embed |
| 1195-1213 | Pens: expanded ~header + 2–3 rows; collapsed = 32px header docked at bottom. | 1 | adhoc-trend-faceplate, adhoc-trend-pens-faceplate |
| 1214-1285 | Collapsed Pens: header only — pin to bottom, free chart flex space above. | 7 | adhoc-trend-chart-host, adhoc-trend-faceplate, adhoc-trend-pens-collapsed, adhoc-trend-pens-faceplate, adhoc-trend-pens-header, adhoc-trend-toolbar-actions, adhoc-trend-toolbar-label |
| 1286-1296 | Trend column only (direct Plots child) — height:0 + flex grow fills space | 1 | adhoc-trend-chart-host, adhoc-trend-plots |
| 1297-1304 | Flex-repeater instances must be column flex so plot-slot/apex can grow | 1 | adhoc-trend-plots |
| 1305-1315 | Faceplate Trend column: chart band fills leftover; Pens sits flush below | 2 | adhoc-trend-chart-host, adhoc-trend-faceplate, adhoc-trend-faceplate-embed |
| 1316-1323 | Faceplate: same plots-column fill when pens docks to 32px | 1 | adhoc-trend-chart-host, adhoc-trend-faceplate, adhoc-trend-faceplate-embed, adhoc-trend-plots |
| 1324-1374 | Kill stray scroll gutter above ApexCharts toolbar / plot host | 7 | adhoc-trend-action-btn, adhoc-trend-action-btn-outline, adhoc-trend-apex, adhoc-trend-faceplate, adhoc-trend-plot-slot, adhoc-trend-plots, adhoc-trend-toolbar-actions-faceplate |
| 1375-1389 | Faceplate: chart canvas below header / Save / Clear; toolbar above zoom layer | 2 | adhoc-trend-apex, adhoc-trend-faceplate |
| 1390-1402 | Nested Trend embed must not force full popup height over the faceplate header | 1 | adhoc-trend-faceplate |
| 1403-1415 | Config ToolBar embed: size to content (no stretch gap); overflow visible for calendars | 1 | adhoc-trend-config-faceplate |
| 1416-1422 | Keep NE/N resize handles from eating the close hit target | 1 | |
| 1423-1465 | Companion Trend Configuration faceplate (left of AdhocTrend) | 5 | adhoc-trend-config-faceplate, adhoc-trend-config-faceplate-close, adhoc-trend-config-faceplate-header, adhoc-trend-config-toolbar |
| 1466-1474 | Trending page settings gear opens the toolbar as its own popup: give it a card (the rule above keeps | 1 | adhoc-trend-config-toolbar |
| 1475-1492 | Popups — hide Perspective chrome header (empty white bar when showCloseIcon=False). | 1 | |
| 1493-1509 | Config: overflow visible so date-time calendars are not clipped. | 2 | |
| 1510-1553 | Popup shell fills openPopup size — do NOT force nested embeds to 100% height | 4 | adhoc-trend-config-faceplate, adhoc-trend-faceplate |
| 1554-1566 | Date-time picker calendar must paint above config chrome / siblings | 2 | |
| 1567-1605 | AdhocTrend / Config / device faceplates: drag via .popup-drag. | 3 | faceplate |
| 1606-1612 | Same fit as AdhocTrend — container-card margin:2px otherwise scrollH = height+4. | 1 | faceplate |
| 1613-1643 | Device faceplate: widen only while Trend is selected (class on the view root). | 3 | faceplate, faceplate-trend-wide |
| 1644-1679 | Popups center in the page area, not the window: Perspective centers them in .popups-pane (fixed, full window), | 6 | |
| 1680-1695 | Adhoc ContextMenu / account popups — opaque shell (global .ia\_popup is transparent) | 2 | |
| 1696-1700 | ChangeTheme — sized to fit (220×210); no inner scrollbar | 1 | |
| 1701-1736 | Transparent modal backdrop (sibling of \#popup-changeTheme) so overlayDismiss | 5 | |
| 1737-1741 | Adhoc ContextMenu rows (Alerts/Menu) | 1 | container-item |
| 1742-1751 | Plant navigation dock — theme surfaces (light card in light; inverted in dark) | 1 | nav-dock |
| 1752-1772 | Docked status legend (right) | 2 | legend-dock, nav-brand |
| 1773-1787 | Plant home landing — feature overview cards | 2 | plant-feature-card, plant-feature-title |
| 1788-1910 | Groveport KPI dashboard (Lightspeed-style cards / grids) | 11 | Fonts/Label, kpi-card, kpi-card-header, kpi-chart, kpi-dashboard-grid, kpi-metrics, kpi-value, nav-search, nav-search-field |
| 1911-1947 | Clear (x) and result count overlay the field's right edge (Scout-style) so the field | 5 | nav-clock, nav-search-clear, nav-search-count |
| 1948-2001 | Nav search (Scout-style). Classes are set on the item icon by the search script | 7 | nav-search-hit, nav-search-parent, nav-section, nav-tree |
| 2002-2027 | Node icons 22px (Scout-sized). Items carry an inline 18px icon style, hence !important. | 4 | nav-tree, nav-tree-selected |
| 2028-2106 | Tree icons / expand arrows — theme via --icon-nav. | 7 | nav-tree |
| 2107-2122 | Top header dock — account + theme gear (Lightspeed-style top-right) | 1 | app-header |
| 2123-2171 | Header nav hamburger — left of SIM; toggles shared dock id plant-nav | 8 | app-header, color-icon, nav-menu-btn |
| 2172-2210 | Account permission badge (ReadOnly → lock; else lock\_open) | 7 | color-icon, perm-badge, perm-badge-read, perm-badge-write |
| 2211-2227 | Account / login chip | 2 | account-chip |
| 2228-2274 | Settings gear — Lightspeed Container/Icon equivalent. | 6 | account-settings, color-icon |
| 2275-2302 | Same fill=none protection on the account chip person icon | 5 | account-chip, account-popup, color-icon, theme-toggle-option |
| 2303-2308 | Labels/icons inherit option color so selected contrast is not stomped by font-\* classes | 1 | Fonts/Label, Fonts/Title, Fonts/Value, theme-toggle-option |
| 2309-2322 | Selected segment: matches ChangeTheme (neutral-100 fill + inverse text). | 1 | Fonts/Label, Fonts/Title, Fonts/Value, theme-toggle-option-selected |
| 2323-2336 | Scout-style device alarm chrome (feature/scout-alarm-icon-header) --- | 4 | alarm-priority-critical, alarm-priority-high, alarm-priority-low, alarm-priority-medium |
| 2337-2346 | AlarmFrame sits above drawings in DOM order. Drawings are inset 4px | 1 | device-graphic |
| 2347-2381 | Keep Perspective SVG under AlarmFrame / AlarmHeader stacking. | 5 | alarm-border, alarm-frame, alarm-header, device-graphic, icon-header |
| 2382-2393 | Sensor alarm: priority ring on the tag box + badge pinned to the box's left edge, so it sits in the same place | 2 | sensor-alarm-badge, sensor-badge-box |
| 2394-2424 | Sensor value pinned to a side of the tag box (params.valuePosition; auto keeps the orientation grid) | 6 | sensor-alarm-badge, sensor-badge-box, sensor-badge-box-value-left, sensor-badge-value, sensor-badge-value-bottom, sensor-badge-value-left, sensor-badge-value-right, sensor-badge-value-top |
| 2425-2443 | Sensor faceplate icon (params.faceplate): pinned right of the tag box like the alarm badge on the left, so no | 4 | sensor-badge-box, sensor-faceplate-icon, sensor-faceplate-icon-lowered, sensor-faceplate-icon-raised, sensor-faceplate-icon-side |
| 2444-2449 | the embed hosting a sensor clipped the badge outside its box | 1 | sensor-badge-box, sensor-component |
| 2450-2450 | Scout unack flash on priority letter badge | 0 | |
| 2451-2489 | Tank (LTR) device graphic ---- | 6 | tank-float, tank-float-active, tank-liquid, tank-sight, tank-stem, tank-vessel |
| 2490-2498 | Tick bars only — solid level color | 2 | tank-level-critical, tank-level-warning |
| 2499-2504 | HH / H / L / LL text beside ticks — color only, no fill | 1 | tank-level-mark |
| 2505-2512 | Device label + analog centered over vessel (width matches vessel; marginLeft bound by orientation) | 1 | tank-over-vessel |
| 2513-2514 | Device / Sensor orientation (Scout-style) --- | 0 | |
| 2515-2555 | Device layout — match ScoutMotors grid areas | 6 | component, device-vertical, icon-header, label, status, value |
| 2556-2579 | Sensor layout — Scout orientation; name in expanding badge; stem flush in assembly | 3 | notification-wrapper, value |
| 2580-2600 | Device name badge — expands with text; Figma double-border via outline | 1 | sensor-badge, tag-label |
| 2601-2607 | Sensor in alarm: the outer ring of the tag box takes the priority colour (after the base rule so it wins) | 1 | alarm-border, sensor-badge, tag-label |
| 2608-2615 | Sensor Comm Loss: the tag box is the sensor's graphic, so Bad PV qualit | 1 | device-comm-loss, sensor-badge, tag-label |
| 2616-2643 | Badge + stem share one grid cell so stem always touches. | 3 | nut, status, stem, stem-line |
| 2644-2713 | Sensor grid: no status text row - the IconHeader (notification-wrapper) | 10 | notification-wrapper, sensor-component, sensor-horizontal, sensor-value-away, sensor-vertical, sensor-vertical-reverse, value |
| 2714-2747 | horizontal: icons centred under the tag box (the stem line adds 24 px on the box's far side of the column) | 6 | notification-wrapper, sensor-component, sensor-horizontal, sensor-horizontal-reverse, sensor-value-under, value |
| 2748-2789 | Nav Button — Figma Components / Nav Button (259:2242) | 2 | nav-button, nav-button-shape |
| 2790-2809 | Dark chevron underlay = stroke | 1 | nav-button-stroke |
| 2810-2859 | Inset fill — leaves a continuous outline of the underlay | 3 | nav-button, nav-button-fill, nav-button-label |
| 2860-2865 | StatusDot (binary safety LED: green OK / red alarm) --- | 1 | status-dot-root |
| 2866-2901 | Perspective flex hosts stretch cross-axis by default → width ≠ height → oval. | 4 | status-dot, status-dot-alarm, status-dot-ok, status-dot-unknown |
| 2902-2920 | Safetys widget --- | 3 | safetys-body, safetys-title, safetys-widget |
| 2921-2963 | Embedded views scroll when their host box is smaller than content | 4 | safetys-embed, safetys-fan, safetys-widget, status-dot, status-dot-root |
| 2964-2970 | Match indicator column height to stacked fans; space MR AD…FIRE top-to-bottom | 1 | safetys-indicators, safetys-widget |
| 2971-3010 | Unified Faceplate (Scout-style tabbed shell) | 4 | container-button, faceplate, faceplate-header, faceplate-title |
| 3011-3056 | In-view Close X — native popup header is hidden globally | 4 | faceplate-button, faceplate-button-selected, faceplate-close |
| 3057-3092 | Tab label text on light chrome — not inverse (--text-inverse / Fonts/Button) | 8 | faceplate-body, faceplate-buttons-1, faceplate-buttons-2, faceplate-buttons-3, faceplate-buttons-4, faceplate-buttons-5, faceplate-tab-text |
| 3093-3138 | Valve / solenoid: left vertical tabs (deviceType Valve\|Solenoid\|SolenoidValve) | 4 | faceplate-button, faceplate-button-selected, faceplate-content, faceplate-tabs-vertical |
| 3139-3225 | The vertical-tab display:flex !important above must not resurrect tabs hidden by their display binding | 13 | faceplate-alarm-field-label, faceplate-alarm-fields, faceplate-alarm-list, faceplate-alarm-name, faceplate-alarm-row, faceplate-alarm-row-alt, faceplate-body, faceplate-button, faceplate-button-selected, faceplate-content, faceplate-kpi-label, faceplate-kpi-row ... +3 |
| 3226-3228 | Faceplate Controls / Interlocks polish (260730-m0m) --- | 1 | faceplate-buttons-6 |
| 3229-3234 | Panel config rows: AnalogInput value + EU + pencil need ~118px; do not clip icon. | 1 | config-input-row, faceplate-kpi-row, faceplate-section-card |
| 3235-3264 | Shared Modes row (faceplate Controls) | 5 | faceplate-cmd-btn, faceplate-cmd-row, faceplate-mode-btn, faceplate-mode-btn-active |
| 3265-3271 | Disabled commands (e.g. Start Defrost while defrosting) must read as unavailable | 1 | faceplate-cmd-btn |
| 3272-3280 | CG bottom control panel (AhuEvapPanel): larger text inside the shared AnalogInput/TimeInput | 1 | Fonts/Value, analog-input-edit, cg-panel, config-input-row |
| 3281-3307 | LTU card (Machine Room): larger value, edit field and pencil inside the shared AnalogInput element. | 4 | Fonts/Label, Fonts/Value, analog-input-edit, cg-panel, config-input-label, config-input-row, faceplate-trend-empty, ltu-sp |
| 3308-3339 | Configuration AnalogInput / MultiStateInput — keep label + value + edit as a tight cluster | 5 | config-input-label, config-input-row, faceplate-config-row, faceplate-interlock-header, faceplate-interlocks |
| 3340-3359 | Status chips: size to content so overflow:auto does not paint bars | 2 | faceplate-interlock-channels, faceplate-interlock-colhdr |
| 3360-3406 | Repeater instance wrappers: fixed row height, no nested scroll chrome | 6 | faceplate-interlock-cond, faceplate-interlock-fault, faceplate-interlock-instance, faceplate-interlock-ok, faceplate-interlock-row, faceplate-interlock-sts, faceplate-interlocks |
| 3407-3443 | Bypass column: box only — hide caption text nodes, keep the checkbox icon | 4 | faceplate-interlock-bypass, faceplate-interlock-sts |
| 3444-3468 | Device Not Ready reason dots (empty labels collapse without these) | 3 | faceplate-nrdy-active, faceplate-nrdy-dot, faceplate-nrdy-label |
| 3469-3543 | Pump / motor faceplate fault status codes (text + class, not color-only) | 14 | Refridgeration\_STS, config-field-label, faceplate-cmd-row-fill, faceplate-fault-active, faceplate-fault-chip, faceplate-fault-chips, faceplate-fault-ok, faceplate-fault-state, faceplate-ls-off, faceplate-ls-on, faceplate-status-banner, sts-RUN ... +3 |
| 3544-3554 | Analog/string config editors: same slot display vs edit so the pencil does not jump | 1 | analog-input-edit, config-input-row |
| 3555-3568 | Lightspeed-inspired site picker + overview cards | 2 | site-card |
| 3569-3644 | Globe marker hover → Site rail slide-out / dim (class on embedded view host). | 10 | site-card, site-card-pen, site-card-pen-label, site-card-pen-unit, site-card-pen-value, site-rail, site-rail-card--dim, site-rail-card--hot |
| 3645-3723 | Kill overflow scrollbars on pen value/unit flex wrappers | 13 | kpi-coming-chart, kpi-coming-meter-row, kpi-dashboard-chart-card, kpi-domain-subsection, kpi-hero-pen, overview-card, site-card, site-card-pen |
| 3724-3783 | Domain tabs — quiet classic strip; active = underline only (no CTA fill bar) | 7 | kpi-domain-panel, kpi-domain-tabs |
| 3784-3860 | Nested hosts inside a domain panel must not grow their own scrollbars | 13 | container-card, kpi-chart-shell, kpi-coming-chart, kpi-dashboard-chart-card, kpi-dashboard-page, kpi-domain-panel, kpi-domain-subsection, kpi-exec-callout, kpi-exec-chart, kpi-exec-page, kpi-exec-stat, kpi-hero-pen |
| 3861-3864 | Apex often puts overflow:auto on the chart's parent flex — clip H-scroll only | 1 | kpi-exec-page |
| 3865-3873 | Also kill scrollbars on classic Groveport KPI chart hosts | 1 | kpi-coming-chart, kpi-dashboard-chart-card |
| 3874-3920 | KPI / Groveport charts — theme-aware axis + legend (critical in dark modes) | 7 | Fonts/Heading, Fonts/Label, kpi-chart-shell, kpi-coming-chart, kpi-coming-subcard, kpi-dashboard-page, kpi-exec-chart, kpi-hero-pen |
| 3921-3955 | Utility Overview KPI rail — Apex axis/legend/datalabel chrome follows theme | 3 | utility-kpi-chart, utility-kpi-rail |
| 3956-3961 | Tall shared tooltips (status-by-area) must not be clipped by Apex host paint | 1 | utility-kpi-chart |
| 3962-3978 | Dwell hours: labels stay in Apex y-gutter (no extra translate — that wasted width). | 3 | utility-dwell-chart, utility-kpi-chart, utility-kpi-rail |
| 3979-3995 | Utility Overview KPI tables — no horizontal scrollbar | 2 | utility-kpi-rail, utility-kpi-table |
| 3996-4006 | Production Overview device tiles — button-like hover affordance | 2 | prod-device-tile |
| 4007-4009 | Type-scale utilities (fs-\*, fw-\*, text-\*) and other shared classes are Perspective style | 0 | |
| 4010-4029 | Header alarm indicator count badge (Scout AlarmNotification): top-right of the bell, priority colour | 1 | header-alarm-count |
| 4030-4048 | Header icons without button boxes (user 2026-09-29: the boxed bell clipped its count) - hamburger, alarms, loc | 2 | account-chip, account-settings, header-icon, nav-menu-btn, perm-badge |
| 4049-4060 | HMI Out Of Service: only the Out Of Service icon and the OUT OF SERVIC | 2 | alarm-border, alarm-frame, alarm-header, device-oos, sensor-alarm-badge |
| 4061-4096 | Native component context menu (meta.contextMenu - Ticket Logger, Out Of Service) styled like the trend value | 4 | |
| 4097-4136 | Trend X-trace contrast: solid card, shaded time row, darker | 6 | adhoc-trend-apex, faceplate-trend-chart |
| 4137-4156 | Header icon sizes (user 2026-09-29: too small, trend especially) - after and over the older 22 px !important | 3 | account-chip, color-icon, header-icon, header-icon-trend, perm-badge |
| 4157-4167 | Safetys Reset / Silence: FT MachineRoom RESET is red, SILENCE | 2 | safetys-alarm-btn, safetys-reset |
| 4168-4174 | Faceplate Web GUI clickable: the drag strip normally ends 56 px from | 1 | faceplate-webgui |
| 4175-4183 | Ticket Logger drag strip: Perspective's drag strip covered | 1 | ticket-logger |
| 4184-4195 | Ticket Logger Settings gear: corner icon button, faceplate-close hover chip | 2 | ticket-logger-gear |
| 4196-4205 | Integrations accordion header (98\_Configuration/IntegrationSection) | 2 | integration-section-header |
| 4206-4219 | dropdown-subtle (on dropdownOptionStyle.classes): neutral option highlight - nav-tree selection tokens - inste | 2 | dropdown-subtle |
| 4220-4221 | end Ticket Logger block | 0 | |
| 4222-4232 | Faceplate hover: anything that opens a faceplate gets the header-icon | 2 | faceplate-hover |
| 4233-4246 | CG page nav buttons | 3 | cg-nav-arrow, cg-nav-btn |
| 4247-4310 | Valve orientation | 12 | device-graphic, valve-horizontal, valve-horizontal-reverse, valve-label, valve-status, valve-value, valve-vertical-reverse |
| 4311-4339 | HMI Out Of Service log: header notes badge (same shape as the alarm count, th | 7 | header-oos-count, oos-chip, oos-chip-progress, oos-chip-ready, oos-chip-returned, oos-chip-waiting, oos-memo |
| 4340-4360 | Memo column: one line with an ellipsis (the full memo is in the detail pane); the cell's .content is a flex | 3 | oos-comment, oos-memo-cell |
| 4361-4398 | Header branding: Boar's Head lockup after the hamburger (click = | 13 | brand-logo-full, brand-logo-mark, brand-logo-slot, integrator-badge, integrator-divider, integrator-logo-full, integrator-logo-mark, integrator-logo-slot |
| 4399-4399 | end Header branding | 0 | |
| 4400-4479 | Operations Forms layout system | 17 | form-btn, form-btn-primary, form-input, form-input-required, form-page, form-row-label, form-stack, form-td, form-td-cap, form-thead, form-tr |
| 4480-4481 | end Operations Forms layout system ==== | 0 | |
| 4482-4482 | trend-context:begin | 0 | |
| 4483-4616 | Trend context menu / toast / copy / quick history popups: own card, transparent chrome + modal backdrop | 23 | trend-ctx-close, trend-ctx-copy, trend-ctx-copy-card, trend-ctx-copy-path, trend-ctx-head, trend-ctx-icon, trend-ctx-link, trend-ctx-menu, trend-ctx-muted, trend-ctx-path, trend-ctx-quick, trend-ctx-row ... +8 |
| 4617-4633 | Header trend icon basket badge | 1 | trend-badge |
| 4634-4668 | Popup close X: Perspective's default drag strip (.popup-drag, top 10px, 18px tall, full width) sat on top of t | 5 | trend-ctx-close-btn |
| 4669-4821 | Chart tools (Trending page once above the plots, faceplate Trend tab, Quick History): Figma Dev Jam | 29 | trend-chart, trend-divider, trend-hint, trend-live-on, trend-seg, trend-seg-group, trend-seg-on, trend-switch, trend-switch-box, trend-switch-label, trend-switch-state, trend-switch-state-on ... +9 |
| 4822-4822 | trend-context:end | 0 | |
| 4823-4897 | Admin pages | 16 | admin-btn-danger, admin-cell-click, admin-group, admin-list-item, admin-list-item-selected, admin-md, admin-row, admin-tab, form-input |
| 4898-4899 | end Admin pages ==== | 0 | |

## Class To Line Index

<details>
<summary>393 classes referenced in selectors</summary>

| Class | Lines | Also a style class |
|---|---|---|
| `account-chip` | 2212, 2224, 2276, 2277, 2278, 2279, 2283, 2286, 4035, 4150 | |
| `account-popup` | 2289 | |
| `account-settings` | 2232, 2245, 2246, 2251, 2254, 2255, 2256, 2257, 2269, 2272, 4036 | |
| `adhoc-trend-action-btn` | 1358 | |
| `adhoc-trend-action-btn-outline` | 1365, 1371 | |
| `adhoc-trend-add-plot-btn` | 955 | |
| `adhoc-trend-apex` | 794, 795, 796, 797, 803, 804, 815, 867, 883, 884, 885, 892 ... | |
| `adhoc-trend-chart-host` | 768, 792, 793, 1178, 1179, 1180, 1181, 1191, 1272, 1289, 1306, 1312 ... | |
| `adhoc-trend-clear-btn` | 958 | |
| `adhoc-trend-config-faceplate` | 1404, 1405, 1424, 1546 | |
| `adhoc-trend-config-faceplate-close` | 1443, 1451 | |
| `adhoc-trend-config-faceplate-header` | 1435 | |
| `adhoc-trend-config-toolbar` | 1456, 1468 | |
| `adhoc-trend-faceplate` | 1126, 1180, 1181, 1182, 1183, 1184, 1185, 1196, 1216, 1236, 1237, 1247 ... | |
| `adhoc-trend-faceplate-close` | 1151, 1159 | |
| `adhoc-trend-faceplate-embed` | 1165, 1178, 1179, 1191, 1307, 1318 | |
| `adhoc-trend-faceplate-header` | 1142 | |
| `adhoc-trend-load-delete-btn` | 1118 | |
| `adhoc-trend-load-delete-row` | 1112 | |
| `adhoc-trend-pen-plot-cell` | 973, 979, 980, 985, 986, 987, 988, 989, 1019, 1020, 1021, 1046 ... | |
| `adhoc-trend-pen-plot-select` | 1045, 1083, 1090, 1103 | |
| `adhoc-trend-pen-plot-wrap` | 1022, 1031, 1050, 1051, 1052, 1053, 1068, 1076, 1084, 1091, 1102 | |
| `adhoc-trend-pens` | 770, 771, 774, 1011, 1012, 1013, 1014 | |
| `adhoc-trend-pens-collapsed` | 1215, 1216 | |
| `adhoc-trend-pens-faceplate` | 1196, 1216, 1236, 1237, 1247, 1248, 1249, 1250 | |
| `adhoc-trend-pens-header` | 1227 | |
| `adhoc-trend-plot-header` | 918 | |
| `adhoc-trend-plot-slot` | 852, 867, 868, 1326, 1338 | |
| `adhoc-trend-plot-toolbar` | 925, 941, 942 | |
| `adhoc-trend-plots` | 822, 837, 838, 839, 840, 1289, 1298, 1299, 1300, 1317, 1318, 1325 | |
| `adhoc-trend-remove-plot-btn` | 956 | |
| `adhoc-trend-save-btn` | 957 | |
| `adhoc-trend-save-dialog` | 743 | |
| `adhoc-trend-save-label` | 759 | |
| `adhoc-trend-save-title` | 750 | |
| `adhoc-trend-share-label` | 731 | |
| `adhoc-trend-tag-browser` | 769 | |
| `adhoc-trend-toolbar-actions` | 1255 | |
| `adhoc-trend-toolbar-actions-faceplate` | 1349 | |
| `adhoc-trend-toolbar-icon` | 727 | |
| `adhoc-trend-toolbar-label` | 1265 | yes |
| `admin-btn-danger` | 4846 | yes |
| `admin-cell-click` | 4833 | yes |
| `admin-group` | 4836 | yes |
| `admin-list-item` | 4827 | yes |
| `admin-list-item-selected` | 4830 | yes |
| `admin-md` | 4849, 4850, 4854, 4858, 4864, 4869, 4877, 4882, 4889, 4893 | |
| `admin-row` | 4826 | yes |
| `admin-tab` | 4839 | yes |
| `ahu-evap-history-card` | 630 | |
| `alarm-border` | 2361, 2602, 2603, 4056 | |
| `alarm-flash` | 470, 485, 496 | |
| `alarm-frame` | 2354, 2361, 4051 | |
| `alarm-header` | 2369, 2370, 2371, 4052 | |
| `alarm-priority-critical` | 2324 | |
| `alarm-priority-high` | 2327 | |
| `alarm-priority-low` | 2333 | |
| `alarm-priority-medium` | 2330 | |
| `alarm-row-cleared` | 718 | |
| `alarm-row-critical` | 682 | |
| `alarm-row-critical-ack` | 686 | |
| `alarm-row-high` | 691 | |
| `alarm-row-high-ack` | 695 | |
| `alarm-row-low` | 709 | |
| `alarm-row-low-ack` | 713 | |
| `alarm-row-medium` | 700 | |
| `alarm-row-medium-ack` | 704 | |
| `analog-input-edit` | 3275, 3276, 3283, 3284, 3545 | |
| `analog-label` | 310 | |
| `analog-level-warning` | 305 | |
| `analog-over-sp` | 301 | |
| `animations-off` | 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500 | |
| `app-header` | 2108, 2156, 2157, 2162, 2163 | |
| `bg-component` | 511, 771 | |
| `bg-container` | 514 | |
| `bg-disabled` | 517 | |
| `bg-header` | 520, 770 | |
| `brand-logo-full` | 4377 | |
| `brand-logo-mark` | 4369 | |
| `brand-logo-slot` | 4369, 4374, 4377 | |
| `cg-nav-arrow` | 4238 | |
| `cg-nav-btn` | 4234, 4243 | |
| `cg-panel` | 3274, 3275, 3276, 3294 | |
| `color-icon` | 2140, 2195, 2254, 2276, 4140, 4149, 4150, 4153 | yes |
| `comp-analog` | 315 | |
| `comp-analog-eu` | 324 | |
| `comp-mode` | 264 | |
| `comp-mode-auto` | 274 | |
| `comp-mode-manual` | 278 | |
| `comp-mode-remote` | 282 | |
| `component` | 2540 | |
| `config-field-label` | 3539 | |
| `config-input-label` | 3294, 3319 | |
| `config-input-row` | 3230, 3274, 3282, 3294, 3313, 3546, 3547 | |
| `container-button` | 526, 529, 3007 | yes |
| `container-card` | 533, 570, 995, 996, 997, 998, 1003, 1004, 1005, 1006, 3839 | |
| `container-card-border` | 623, 630 | |
| `container-header` | 643 | |
| `container-icon` | 647 | |
| `container-item` | 654, 1738 | |
| `ct-fan-side-spin` | 370, 481, 492 | |
| `ct-spray-run` | 389, 483, 494 | |
| `device-comm-loss` | 291, 292, 293, 294, 295, 296, 2610, 2611 | |
| `device-graphic` | 2341, 2349, 2370, 2371, 4262, 4298, 4299 | |
| `device-oos` | 4051, 4052, 4053, 4056 | |
| `device-vertical` | 2516 | |
| `dropdown-subtle` | 4208, 4209, 4214 | |
| `faceplate` | 1587, 1588, 1601, 1602, 1607, 1608, 1620, 1621, 1627, 1628, 1629, 1630 ... | |
| `faceplate-alarm-field-label` | 3219 | |
| `faceplate-alarm-fields` | 3214 | |
| `faceplate-alarm-list` | 3196 | |
| `faceplate-alarm-name` | 3210 | yes |
| `faceplate-alarm-row` | 3201 | |
| `faceplate-alarm-row-alt` | 3206 | |
| `faceplate-body` | 3083, 3173, 3174 | |
| `faceplate-button` | 3025, 3119, 3140, 3155, 3157, 3159 | |
| `faceplate-button-selected` | 3040, 3120, 3141, 3145, 3156, 3158, 3160 | |
| `faceplate-buttons-1` | 3077 | |
| `faceplate-buttons-2` | 3078 | |
| `faceplate-buttons-3` | 3079 | |
| `faceplate-buttons-4` | 3080 | |
| `faceplate-buttons-5` | 3081 | |
| `faceplate-buttons-6` | 3227 | |
| `faceplate-close` | 3012, 3020 | |
| `faceplate-cmd-btn` | 3257, 3261, 3266, 3267 | yes |
| `faceplate-cmd-row` | 3253 | |
| `faceplate-cmd-row-fill` | 3497, 3501 | |
| `faceplate-config-row` | 3309 | |
| `faceplate-content` | 3094, 3101, 3174 | |
| `faceplate-fault-active` | 3492 | |
| `faceplate-fault-chip` | 3481 | yes |
| `faceplate-fault-chips` | 3470, 3475 | |
| `faceplate-fault-ok` | 3489 | |
| `faceplate-fault-state` | 3485 | |
| `faceplate-header` | 2986, 3007 | |
| `faceplate-hover` | 4224, 4228 | |
| `faceplate-interlock-bypass` | 3408, 3417, 3418, 3419, 3420, 3421, 3426, 3427, 3428, 3429 | |
| `faceplate-interlock-channels` | 3353 | |
| `faceplate-interlock-colhdr` | 3341 | |
| `faceplate-interlock-cond` | 3386 | |
| `faceplate-interlock-fault` | 3398, 3402 | |
| `faceplate-interlock-header` | 3334 | |
| `faceplate-interlock-instance` | 3363 | |
| `faceplate-interlock-ok` | 3394 | |
| `faceplate-interlock-row` | 3373 | |
| `faceplate-interlock-sts` | 3394, 3402, 3439 | yes |
| `faceplate-interlocks` | 3328, 3361, 3362 | |
| `faceplate-kpi-label` | 3188 | yes |
| `faceplate-kpi-row` | 3182, 3231 | |
| `faceplate-ls-off` | 3535 | |
| `faceplate-ls-on` | 3530 | |
| `faceplate-mode-btn` | 3236 | |
| `faceplate-mode-btn-active` | 3246 | |
| `faceplate-nrdy-active` | 3461 | |
| `faceplate-nrdy-dot` | 3445 | |
| `faceplate-nrdy-label` | 3465 | |
| `faceplate-section` | 3192 | yes |
| `faceplate-section-card` | 3230, 3231 | yes |
| `faceplate-status-banner` | 3509 | |
| `faceplate-tab-text` | 3058, 3154 | |
| `faceplate-tabs-vertical` | 3101, 3105, 3119, 3120, 3140, 3141, 3145, 3154, 3155, 3156, 3157, 3158 ... | |
| `faceplate-title` | 3002 | yes |
| `faceplate-trend-chart` | 780, 781, 784, 785, 786, 4101, 4110, 4117, 4121, 4126, 4133 | |
| `faceplate-trend-empty` | 3299 | |
| `faceplate-trend-wide` | 1614, 1615 | |
| `faceplate-webgui` | 4170, 4171 | |
| `fan-spin` | 341, 479, 490 | |
| `Fonts/Header` | 661 | yes |
| `Fonts/Heading` | 3908 | |
| `Fonts/Label` | 664, 1866, 2304, 2313, 3294, 3904 | yes |
| `Fonts/Title` | 669, 2306, 2315 | yes |
| `Fonts/Value` | 672, 2305, 2314, 3274, 3282 | yes |
| `form-btn` | 4446, 4450 | yes |
| `form-btn-primary` | 4447, 4451 | yes |
| `form-input` | 4406, 4409, 4413, 4417, 4426, 4427, 4432, 4433, 4434, 4438, 4439, 4440 ... | yes |
| `form-input-required` | 4432, 4433, 4434 | yes |
| `form-page` | 4403 | |
| `form-row-label` | 4476 | yes |
| `form-stack` | 4459, 4462, 4469, 4473, 4476 | |
| `form-td` | 4469 | |
| `form-td-cap` | 4455, 4473 | |
| `form-thead` | 4459 | |
| `form-tr` | 4462, 4476 | |
| `header-alarm-count` | 4011 | |
| `header-icon` | 4032, 4033, 4034, 4035, 4036, 4043, 4140, 4149, 4150, 4153 | |
| `header-icon-trend` | 4153 | |
| `header-oos-count` | 4313 | |
| `icon-header` | 2377, 2529 | yes |
| `integration-section-header` | 4197, 4202 | |
| `integrator-badge` | 4395 | |
| `integrator-divider` | 4365 | |
| `integrator-logo-full` | 4390 | |
| `integrator-logo-mark` | 4382 | |
| `integrator-logo-slot` | 4382, 4387, 4390 | |
| `kpi-card` | 1805 | |
| `kpi-card-header` | 1819 | |
| `kpi-chart` | 1836 | |
| `kpi-chart-shell` | 3788, 3796, 3802, 3808, 3809, 3810, 3811, 3815, 3816, 3817, 3875, 3876 ... | |
| `kpi-coming-chart` | 3681, 3787, 3795, 3868, 3869, 3880, 3881, 3882, 3890, 3895 | |
| `kpi-coming-meter-row` | 3687, 3694, 3695, 3698, 3699 | |
| `kpi-coming-subcard` | 3911 | |
| `kpi-dashboard-chart-card` | 3676, 3786, 3794, 3830, 3866, 3867 | |
| `kpi-dashboard-grid` | 1795 | |
| `kpi-dashboard-page` | 3823, 3908 | |
| `kpi-domain-panel` | 3777, 3785, 3786, 3787, 3788, 3789, 3793, 3794, 3795, 3796 | |
| `kpi-domain-subsection` | 3711, 3785, 3793 | |
| `kpi-domain-tabs` | 3725, 3733, 3734, 3743, 3744, 3759, 3760, 3761, 3768, 3773 | |
| `kpi-exec-callout` | 3837 | |
| `kpi-exec-chart` | 3842, 3847, 3848, 3849, 3850, 3854, 3855, 3856, 3883, 3884, 3885, 3891 | |
| `kpi-exec-page` | 3839, 3862 | |
| `kpi-exec-stat` | 3836 | |
| `kpi-hero-pen` | 3673, 3705, 3789, 3900, 3904 | |
| `kpi-metrics` | 1846, 1860, 1866 | |
| `kpi-value` | 1832 | yes |
| `label` | 2534 | |
| `led-comm-flash` | 405, 410, 486, 497 | |
| `legend-dock` | 1753 | |
| `ltu-sp` | 3282, 3283, 3284, 3289 | |
| `nav-brand` | 1761 | |
| `nav-button` | 2756, 2833, 2838, 2839 | |
| `nav-button-fill` | 2811, 2833 | |
| `nav-button-label` | 2837, 2839 | |
| `nav-button-shape` | 2773 | |
| `nav-button-stroke` | 2791 | |
| `nav-clock` | 1941 | yes |
| `nav-dock` | 1743 | |
| `nav-menu-btn` | 2124, 2137, 2140, 2141, 2142, 2143, 2149, 2152, 4033 | |
| `nav-search` | 1874, 1886, 1887, 1895, 1896 | |
| `nav-search-clear` | 1913, 1921, 1928 | |
| `nav-search-count` | 1914, 1932 | |
| `nav-search-field` | 1894 | |
| `nav-search-hit` | 1952, 1960, 1961, 1962, 1963, 1967, 1968 | |
| `nav-search-parent` | 1973, 1977, 1978, 1979, 1980 | |
| `nav-section` | 1984 | |
| `nav-tree` | 1952, 1960, 1961, 1962, 1963, 1967, 1968, 1973, 1977, 1978, 1979, 1980 ... | |
| `nav-tree-selected` | 2021 | |
| `notification-wrapper` | 2568, 2669, 2695, 2715, 2720, 2739, 2744 | |
| `nut` | 2638 | |
| `oos-chip` | 4316 | |
| `oos-chip-progress` | 4327 | |
| `oos-chip-ready` | 4330 | |
| `oos-chip-returned` | 4324 | |
| `oos-chip-waiting` | 4333 | |
| `oos-comment` | 4354 | |
| `oos-memo` | 4336 | |
| `oos-memo-cell` | 4342, 4346 | |
| `overview-card` | 3668 | |
| `perm-badge` | 2173, 2186, 2195, 2196, 2197, 2198, 2204, 2207, 4034, 4149 | |
| `perm-badge-read` | 2189 | |
| `perm-badge-write` | 2192 | |
| `plant-feature-card` | 1774 | |
| `plant-feature-title` | 1784 | yes |
| `plcrack-host` | 427 | |
| `plcrack-rack` | 432 | |
| `plcrack-u114` | 436 | |
| `plcrack-u24` | 446 | |
| `plcrack-u54` | 441 | |
| `plcrack-u96` | 451 | |
| `prod-device-tile` | 3997, 4000 | yes |
| `Refridgeration_STS` | 205, 215, 216, 222, 228, 229, 235, 236, 243, 250, 257, 3520 ... | |
| `safety-relay-zoom` | 416, 421 | |
| `safetys-alarm-btn` | 4159, 4164 | |
| `safetys-body` | 2917 | |
| `safetys-embed` | 2927, 2928, 2929, 2930, 2931, 2932, 2933, 2939, 2940 | |
| `safetys-fan` | 2941 | |
| `safetys-indicators` | 2965 | |
| `safetys-reset` | 4159, 4164 | |
| `safetys-title` | 2913 | |
| `safetys-widget` | 2903, 2927, 2928, 2929, 2930, 2931, 2932, 2933, 2939, 2940, 2941, 2945 ... | |
| `sensor-alarm-badge` | 2387, 2421, 4053 | |
| `sensor-badge` | 2581, 2582, 2583, 2584, 2602, 2603, 2610, 2611 | |
| `sensor-badge-box` | 2384, 2387, 2395, 2401, 2406, 2411, 2416, 2427, 2432, 2436, 2440, 2445 | |
| `sensor-badge-box-value-left` | 2421 | |
| `sensor-badge-value` | 2395 | |
| `sensor-badge-value-bottom` | 2416 | |
| `sensor-badge-value-left` | 2401 | |
| `sensor-badge-value-right` | 2406 | |
| `sensor-badge-value-top` | 2411 | |
| `sensor-component` | 2446, 2700, 2709, 2715, 2720, 2725, 2734, 2739, 2744 | |
| `sensor-faceplate-icon` | 2427 | |
| `sensor-faceplate-icon-lowered` | 2440 | |
| `sensor-faceplate-icon-raised` | 2436 | |
| `sensor-faceplate-icon-side` | 2432 | |
| `sensor-horizontal` | 2699, 2700, 2709, 2715, 2720 | |
| `sensor-horizontal-reverse` | 2724, 2725, 2734, 2739, 2744 | |
| `sensor-value-away` | 2656, 2669, 2682, 2695 | |
| `sensor-value-under` | 2720, 2744 | |
| `sensor-vertical` | 2647, 2656, 2665, 2669 | |
| `sensor-vertical-reverse` | 2673, 2682, 2691, 2695 | |
| `site-card` | 3556, 3564, 3592, 3607, 3659, 3663 | |
| `site-card-pen` | 3617, 3646, 3647, 3648, 3652, 3653, 3654 | |
| `site-card-pen-label` | 3621 | |
| `site-card-pen-unit` | 3635 | |
| `site-card-pen-value` | 3624 | |
| `site-rail` | 3571, 3574, 3575 | |
| `site-rail-card--dim` | 3584, 3585, 3592 | |
| `site-rail-card--hot` | 3598, 3599, 3607 | |
| `status` | 2551, 2637 | |
| `status-dot` | 2871, 2951 | |
| `status-dot-alarm` | 2894 | |
| `status-dot-blink` | 487, 498 | yes |
| `status-dot-ok` | 2890 | |
| `status-dot-root` | 2861, 2940, 2945 | |
| `status-dot-unknown` | 2898 | |
| `stem` | 2618 | |
| `stem-line` | 2631 | |
| `sts-CLG` | 216 | |
| `sts-COMMLOSS` | 250 | |
| `sts-COOLING` | 215 | |
| `sts-DEFROST` | 235 | |
| `sts-DFT` | 236 | |
| `sts-FAULT` | 243 | |
| `sts-IDLE` | 222 | |
| `sts-OFF` | 228 | |
| `sts-RUN` | 3520 | |
| `sts-RUNNING` | 3521 | |
| `sts-STARTING` | 3525 | |
| `sts-STOP` | 229 | |
| `sts-STOPPING` | 3526 | |
| `sts-UNKNOWN` | 257 | |
| `tag-label` | 2582, 2584, 2602, 2603, 2610, 2611 | |
| `tank-float` | 2478 | |
| `tank-float-active` | 2485 | |
| `tank-level-critical` | 2491 | |
| `tank-level-mark` | 2501 | |
| `tank-level-warning` | 2495 | |
| `tank-liquid` | 2468 | |
| `tank-over-vessel` | 2506 | |
| `tank-sight` | 2460 | |
| `tank-stem` | 2474 | |
| `tank-vessel` | 2452 | |
| `theme-toggle-option` | 2297, 2304, 2305, 2306 | yes |
| `theme-toggle-option-selected` | 2313, 2314, 2315, 2316, 2317, 2318 | yes |
| `themed-scroll` | 612 | |
| `ticket-logger` | 4177, 4178 | |
| `ticket-logger-gear` | 4185, 4191 | |
| `trend-badge` | 4618 | |
| `trend-chart` | 4671, 4672, 4673 | |
| `trend-ctx-close` | 4575 | |
| `trend-ctx-close-btn` | 4659, 4666 | |
| `trend-ctx-copy` | 4608 | |
| `trend-ctx-copy-card` | 4516 | |
| `trend-ctx-copy-path` | 4538 | |
| `trend-ctx-head` | 4520 | |
| `trend-ctx-icon` | 4567 | |
| `trend-ctx-link` | 4603 | |
| `trend-ctx-menu` | 4507 | |
| `trend-ctx-muted` | 4571 | |
| `trend-ctx-path` | 4531 | |
| `trend-ctx-quick` | 4516 | |
| `trend-ctx-row` | 4551, 4556 | |
| `trend-ctx-row-muted` | 4559 | |
| `trend-ctx-sep` | 4544 | |
| `trend-ctx-text` | 4563 | |
| `trend-ctx-title` | 4524 | |
| `trend-ctx-toast` | 4578 | |
| `trend-ctx-toast-dot` | 4587 | |
| `trend-ctx-toast-text` | 4596 | |
| `trend-ctx-toast-warn` | 4593 | |
| `trend-divider` | 4762 | |
| `trend-hint` | 4815 | |
| `trend-live-on` | 4758 | |
| `trend-seg` | 4695, 4706, 4711, 4719, 4722, 4729 | |
| `trend-seg-group` | 4689 | |
| `trend-seg-on` | 4725 | |
| `trend-switch` | 4776 | |
| `trend-switch-box` | 4767, 4773 | |
| `trend-switch-label` | 4779 | |
| `trend-switch-state` | 4785 | |
| `trend-switch-state-on` | 4791 | |
| `trend-tool-btn` | 4695, 4706, 4729, 4733, 4740, 4743 | |
| `trend-tool-compact` | 4752 | |
| `trend-tool-icon` | 4748 | |
| `trend-tools` | 4676 | |
| `trend-tools-compact` | 4681, 4706 | |
| `trend-tools-row` | 4684 | |
| `trend-zoom-chip` | 4794 | |
| `trend-zoom-chip-link` | 4809 | |
| `trend-zoom-chip-text` | 4803 | |
| `unit-overview-grid` | 543, 554, 555, 563, 567, 568, 569, 570, 584, 585, 610 | |
| `unit-overview-host` | 556, 557, 571, 572, 573, 574, 579, 580, 586, 587, 611 | |
| `unit-overview-table` | 558, 616 | |
| `utility-dwell-chart` | 3965, 3968, 3969 | |
| `utility-kpi-chart` | 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3946, 3950 ... | |
| `utility-kpi-rail` | 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3945, 3949 ... | |
| `utility-kpi-table` | 3980, 3981, 3982, 3983, 3984, 3990 | |
| `value` | 2546, 2574, 2665, 2691, 2709, 2734 | |
| `valve-horizontal` | 4271, 4279, 4293, 4298, 4302, 4306 | |
| `valve-horizontal-reverse` | 4272, 4286, 4294, 4299, 4303, 4307 | |
| `valve-label` | 4259, 4293, 4294 | |
| `valve-status` | 4268, 4306, 4307 | |
| `valve-value` | 4265, 4302, 4303 | |
| `valve-vertical-reverse` | 4248, 4259, 4262, 4265, 4268 | |

</details>

## Custom Properties (CSS Variables)

<details>
<summary>104 variables defined in the stylesheet</summary>

| Variable | First value |
|---|---|
| `--accent` | `var(--callToAction, var(--accent-cold))` |
| `--accent-cold` | `#114599` |
| `--accent-warm` | `#c45c26` |
| `--alarm-color` | `var(--alarm-critical)` |
| `--alarm-critical` | `#e22028` |
| `--alarm-critical-ack` | `#8b1519` |
| `--alarm-high` | `#ec8629` |
| `--alarm-high-ack` | `#9a5619` |
| `--alarm-low` | `#916aad` |
| `--alarm-low-ack` | `#5a3f6c` |
| `--alarm-medium` | `#f5e11b` |
| `--alarm-medium-ack` | `#9e9012` |
| `--alarm-row-fg-dark` | `#212121` |
| `--alarm-row-fg-light` | `#ffffff` |
| `--analog-over-sp` | `#c62828` |
| `--border` | `var(--neutral-30)` |
| `--border-nav` | `var(--neutral-30)` |
| `--border-strong` | `var(--neutral-50)` |
| `--borderRadius` | `4px` |
| `--boxShadow1` | `0 1px 3px rgba(0, 0, 0, 0.12)` |
| `--comp-mode-auto` | `#2e7d32` |
| `--comp-mode-manual` | `#FF9800` |
| `--comp-mode-remote` | `#00bcd4` |
| `--cool-10` | `#f2f4f8` |
| `--cool-100` | `#121619` |
| `--cool-20` | `#dde1e6` |
| `--cool-30` | `#c1c7cd` |
| `--cool-40` | `#a2a9b0` |
| `--cool-50` | `#878d96` |
| `--cool-60` | `#697077` |
| `--cool-70` | `#4d5358` |
| `--cool-80` | `#343a3f` |
| `--cool-90` | `#21272a` |
| `--ct-water` | `#5BC0EB` |
| `--device-safety` | `#c62828` |
| `--deviceFill-commLoss` | `#c62828` |
| `--deviceFill-faulted` | `var(--neutral-100)` |
| `--deviceFill-running` | `var(--neutral-10)` |
| `--deviceFill-stopped` | `var(--neutral-60)` |
| `--header-icon` | `26px` |
| `--icon` | `var(--neutral-90)` |
| `--icon-disabled` | `var(--neutral-40)` |
| `--icon-muted` | `var(--neutral-60)` |
| `--icon-nav` | `var(--neutral-70)` |
| `--nav-bg` | `var(--surface-nav)` |
| `--nav-border` | `var(--border-nav)` |
| `--nav-brand` | `var(--text-secondary)` |
| `--nav-hover` | `var(--surface-nav-hover)` |
| `--nav-icon` | `var(--icon-nav)` |
| `--nav-selected` | `var(--surface-nav-selected)` |
| `--nav-text` | `var(--text-nav)` |
| `--nav-text-muted` | `var(--text-nav-muted)` |
| `--status-cooling` | `#1e88e5` |
| `--status-defrost` | `#ec407a` |
| `--status-idle` | `#228b22` |
| `--status-level-critical` | `#c62828` |
| `--status-level-warning` | `#fbc02d` |
| `--status-off` | `#9e9e9e` |
| `--status-unknown` | `#607d8b` |
| `--sts-accent-width` | `4px` |
| `--sts-border` | `var(--neutral-50)` |
| `--sts-cooling-bg` | `var(--status-cooling)` |
| `--sts-cooling-fg` | `#ffffff` |
| `--sts-defrost` | `var(--status-defrost)` |
| `--sts-fault` | `#c62828` |
| `--sts-idle-bg` | `var(--status-idle)` |
| `--sts-idle-fg` | `#ffffff` |
| `--sts-off-bg` | `var(--status-off)` |
| `--sts-off-fg` | `#ffffff` |
| `--sts-unknown-bg` | `var(--neutral-60)` |
| `--sts-unknown-fg` | `var(--neutral-10)` |
| `--surface` | `var(--neutral-10)` |
| `--surface-card` | `var(--neutral-20)` |
| `--surface-component` | `var(--neutral-30)` |
| `--surface-container` | `var(--neutral-30)` |
| `--surface-disabled` | `var(--neutral-40)` |
| `--surface-header` | `var(--neutral-30)` |
| `--surface-nav` | `var(--neutral-20)` |
| `--surface-nav-hover` | `var(--neutral-30)` |
| `--surface-nav-selected` | `var(--neutral-40)` |
| `--surface-page` | `var(--neutral-10)` |
| `--surface-raised` | `var(--neutral-20)` |
| `--surface-sunken` | `var(--neutral-30)` |
| `--tank-float` | `#767676` |
| `--tank-float-active` | `var(--status-idle)` |
| `--tank-float-stroke` | `#161616` |
| `--text` | `var(--neutral-100)` |
| `--text-inverse` | `var(--neutral-10)` |
| `--text-muted` | `var(--neutral-60)` |
| `--text-nav` | `var(--neutral-90)` |
| `--text-nav-muted` | `var(--neutral-60)` |
| `--text-on-accent` | `#ffffff` |
| `--text-secondary` | `var(--neutral-80)` |
| `--text-subtle` | `var(--neutral-50)` |
| `--warm-10` | `#f7f3f2` |
| `--warm-100` | `#171414` |
| `--warm-20` | `#e5e0df` |
| `--warm-30` | `#cac5c4` |
| `--warm-40` | `#ada8a8` |
| `--warm-50` | `#8f8b8b` |
| `--warm-60` | `#736f6f` |
| `--warm-70` | `#565151` |
| `--warm-80` | `#3c3838` |
| `--warm-90` | `#272525` |

</details>
