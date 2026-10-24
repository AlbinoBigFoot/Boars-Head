---
title: "Tag Reference (Generated)"
sidebar_label: "Overview"
description: "Generated reference of the BH tag configuration: UDTs, instances, tag groups, _Config, _RCP1_."
generated: true
---

:::note

:::
They reflect the project files as of the last wiki update. For explanations start at [Tags](../index.md).

| Page | What | Count |
|---|---|---|
| [UDT Definitions](udts/index.md) | one page per UDT definition | 95 |
| [Device Instances](devices/index.md) | one page per device folder under `Boars_Head`; instances / resolved parts | 37 pages, 126 instances, 476 parts |
| [Tag Groups](tag-groups.md) | polling groups | 9 |
| [_Config Tags](config-tags.md) | runtime configuration tags | 67 |
| [_RCP1_ Mirror](rcp1-mirror.md) | pruned PLC browse | 35056 |
| [Alarm Index](alarm-index.md) | alarm definitions on UDT members | 32 |
| [History Index](history-index.md) | historized UDT members | 66 |
| [Tag Tree Inventory](tag-tree.md) | top-level folders, plain tags | |

Regenerate: `python -I wiki/tools/gen_all.py tags` (or all areas without an argument), then `cd wiki; npm run build`.
