---
title: "Tag Groups (Generated)"
sidebar_label: "Tag Groups"
description: "Every tag group with its mode, rates and how many tags use it."
generated: true
---

:::note

:::
Tag groups decide how often OPC tags are polled. **Direct** = always polled at `rate` (ms). **Leased** = polled at `leasedRate` while something (a view, a binding) subscribes to the tag, otherwise at `rate` (0 = not at all). Designer: **Tag Browser > (gear) Edit Tag Groups**; Gateway web UI: **Config > Tags > Tag Groups**; on disk `gateways/standard/data/config/resources/core/ignition/tag-group/<provider>/<group>/config.json`.

Why the groups are set this way: [History And Polling](../history.md).

| Provider | Group | Mode | Rate (ms) | Leased rate (ms) | OPC data mode | Used by (OPC tags) | In git |
|---|---|---|---|---|---|---|---|
| default | `Default` | Direct | 1000.0 | | Subscribed | 1266 UDT OPC members | no |
| default | `Default Historical` | Direct | 10000.0 | | Subscribed | | no |
| default | `PAX_Config` | Direct | 30000 | | Subscribed | 23 UDT OPC members | yes |
| default | `PAX_Faceplate` | Leased | 60000 | 1000 | Subscribed | 385 UDT OPC members | yes |
| default | `PAX_Status` | Direct | 5000 | | Subscribed | 482 UDT OPC members | yes |
| default | `RCP1_Faceplate` | Leased | 0 | 1000 | Subscribed | 17109 \`\_RCP1\_\` tags | yes |
| default | `RCP1_Status` | Leased | 0 | 1000 | Subscribed | 17947 \`\_RCP1\_\` tags | yes |
| System | `Default` | Direct | 1000.0 | | Subscribed | | no |
| System | `Default Historical` | Direct | 10000.0 | | Subscribed | | no |

A member without a `tagGroup` uses the `Default` group.
