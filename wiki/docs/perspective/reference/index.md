---
title: "Perspective Reference"
sidebar_label: "Perspective Reference"
description: "Generated reference for the BH Perspective project: views, routes, nav, session, styles."
generated: true
sidebar_position: 1
---

:::note

:::


Hand-written guides are one level up in [Perspective](../index.md).

| What | Count |
|---|---|
| Views | 322 |
| Bindings | 6672 (expr 5288, property 934, expr-struct 383, tag 56, query 7, tag-history 4) |
| Event actions, change scripts, message handlers | 1211 |
| Page routes | 94 |
| Style classes | 204 |
| Stylesheet classes (.psc-*) | 393 |
| Common patterns | 9 |

## Pages

- [All Views](./views-index.md)
- [Page Routes](./routes.md)
- [Nav Tree Items](./nav-tree.md)
- [Session Properties](./session-properties.md)
- [Common Binding Patterns](./common-patterns.md)
- [Style Class Catalog](./style-classes.md)
- [Stylesheet Index](./stylesheet.md)
- [Themes And Icons](./themes-and-icons.md)

Each view page lists its path, Designer location and routes, params and custom properties, a component tree, every binding (with expressions and transforms), every event script, the views it embeds and the views that embed it, its style classes and the tag paths it names.

To regenerate after a project change: `python -I wiki/tools/gen_all.py` (or `python -I wiki/tools/gen_perspective.py` for this area only).
