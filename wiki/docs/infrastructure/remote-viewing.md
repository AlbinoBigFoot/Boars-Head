---
title: Remote Viewing
sidebar_position: 7
description: Showing the lab HMI to someone off-site with Tailscale Funnel, and the security rules around it.
sources:
  - docs/tailscale-funnel.md
last_verified: 2026-10-23
---

# Remote Viewing

For demos, the lab gateway can be published on a public HTTPS URL with **Tailscale Funnel** (`docs/tailscale-funnel.md`).

```powershell
tailscale funnel --bg --yes 19088     # publish the Standard gateway's HTTP port
tailscale funnel status               # shows the https://<machine>.<tailnet>.ts.net/ URL
tailscale funnel reset                # stop
```

- Funnel the **gateway root** (port 19088), not a deep path, so login, assets and WebSockets work. The HMI is then at
  `https://<machine>.<tailnet>.ts.net/data/perspective/client/BH/`.
- **The URL is reachable from the whole Internet** while Funnel runs. The HMI requires login (project
  `session-permissions` = Authenticated), but the Gateway web UI login page is exposed too.
- Give visitors a **non-admin** user (ReadOnly role); never share admin credentials.
- Stop Funnel when the demo ends.
- Never funnel the Designer or SQL ports.
- Remember the gateway is connected to the live PLC: the write protections must stay on
  ([RCP1 Device](../gateway/devices-rcp1.md#write-protection-two-layers)).
