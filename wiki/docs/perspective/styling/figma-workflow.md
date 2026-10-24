---
title: Figma Workflow
sidebar_position: 7
description: How a graphic designed in Figma gets into a Perspective view - export as SVG, drag it onto the view in the Designer, choose Embedded, position it and bind it to tags.
sources:
  - "docs/themes.md"
  - "docs/theme-figma-tokens.md"
last_verified: 2026-10-24
---

# Figma Workflow

New HMI graphics (device symbols, icons, logos, panel drawings) are designed in Figma, in the project's design file,
and approved by the project owner before they go into a Perspective view. The hand-over to Ignition is manual and
takes a minute: **export an SVG from Figma and drag it onto the view in the Designer.**

## Add A Graphic From Figma

1. **In Figma**, select the frame or component. In the right-hand panel scroll to **Export**, choose **SVG** and click
   **Export**. Save the `.svg` file.
2. **In the Ignition Designer**, open the target view (Project Browser > Perspective > Views > the folder > the view).
3. **Drag the `.svg` file** from File Explorer onto the view canvas.
4. When the Designer asks how to import it, choose **Embedded**. This embeds the SVG in the view rather than linking
   an external file, so the graphic travels with the project and git.
5. **Position and size it** with the Property Editor (`position` x / y / width / height) or by dragging its handles.
6. **Bind its properties** (fill, stroke, visibility, opacity) to tags or view parameters as needed: select the
   graphic, click the binding icon next to the property, and use an expression or tag binding
   ([Bindings](../bindings.md)). For theme support use the theme classes and variables instead of raw hex colours
   ([Themes](./themes.md)).
7. Save (`Ctrl+S`) and test in a Perspective session in all four themes.

Tips:
- Export each component variant (for example each state or theme) as its own SVG, or one SVG with named groups that
  you toggle with visibility bindings.
- Keep one graphic per view or per `_Assets` view so it can be reused by embedding.
- Name the component in the Component Tree so bindings and handlers stay readable.

## Conventions For A Device Symbol

- Build a **component set** in the design file next to the existing device symbols (Sensor, Fan, Cooling Tower,
  Exhaust Fan, Pump, Compressor, Condenser, Evaporator, Tank, valves).
- Variants: `State = ...` and `Theme = Light | Dark | Light Warm | Dark Warm` (plus `fans = ...` where it applies).
  The Theme property maps one to one onto the four Perspective themes.
- 65 px wide base; use theme colours, never raw hex, so the graphic follows the theme.
- Text: Poppins SemiBold 8 (label), Regular 9 (value), SemiBold 7 (status).
- Only draw states that the PLC UDTs carry (see [Icons](./icons.md#status-icons-and-the-legend)).

## Check It

Compare the finished view in all four themes against the design variants, at 1920 and 1366 px.
