# Tailscale Funnel — remote Perspective access

Expose the **Standard** Ignition gateway’s HTTP port to the public Internet via [Tailscale Funnel](https://tailscale.com/kb/1223/funnel) (HTTPS, no VPN for viewers).

## Prerequisites

| Requirement | Notes |
|-------------|--------|
| Tailscale client | Installed and logged in (`tailscale status`) |
| Funnel allowed on the tailnet | Admin console → **DNS** → enable **HTTPS certificates**; **Access controls** must allow Funnel (see [ACL steps](#tailscale-admin-steps-if-funnel-is-blocked)) |
| Standard gateway running | Docker `bh-ignition-standard`; host HTTP port from `.env` `STANDARD_HTTP_PORT` (default **19088**) |

Do **not** funnel Designer ports or commit Tailscale auth keys / gateway passwords.

## Start / stop

Proxy the **gateway root** (not a deep Perspective path alone) so login, static assets, and WebSockets resolve correctly.

```powershell
# Start (background) — uses host port from STANDARD_HTTP_PORT
tailscale funnel --bg --yes 19088

# Status
tailscale funnel status

# Stop Funnel + serve config
tailscale funnel reset
# or: tailscale serve reset
```

Equivalent target forms: `19088`, `localhost:19088`, `http://127.0.0.1:19088`.

## Public URL pattern

After Funnel starts, Tailscale prints a MagicDNS HTTPS URL shaped like:

```text
https://<machine-name>.<tailnet>.ts.net/
```

| Use | URL |
|-----|-----|
| Gateway home | `https://<machine>.<tailnet>.ts.net/` |
| Perspective client (BH) | `https://<machine>.<tailnet>.ts.net/data/perspective/client/BH/` |

Confirm the live hostname with `tailscale status` / `tailscale funnel status` (machine name can change). Project path `BH` comes from the Perspective project folder under `gateways/standard/data/projects/`.

## Security notes

- **Login is required** for Perspective project **BH**. Anonymous Funnel (or LAN) viewers cannot browse the HMI: opening `/data/perspective/client/BH/` shows Ignition’s **Log In** screen (“You must log in to continue”) before any page.
- Config is project-level (not per-page): `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-permissions/` requires security level **Authenticated** (`AllOf`). Project IdP is already **default** (Ignition IdP → user source `default`) via `ignition/global-props`.
- **Funnel is world-reachable** while enabled — anyone with the URL can hit the gateway / Perspective login challenge.
- Keep a **strong admin password** (already expected in `.env`; never commit it).
- For demos / visitors, create a **non-admin** Ignition user (Operator / Viewer) under Config → Security → Users, Sources and share that account — do not hand out admin.
- Funnel exposes the **HTTP gateway web UI**, not a Designer-only tunnel — still avoid sharing admin credentials; disable Funnel when demos end.
- Prefer stopping Funnel when not needed: `tailscale funnel reset`.

### How to test auth

1. Incognito / logged-out browser → `http://127.0.0.1:19088/data/perspective/client/BH/` (or the Funnel URL + same path).
2. Expect the Perspective **Log In** interstitial, not Plant / Evaporators / nav.
3. Optional API check (no cookies): `GET /data/perspective/project/BH` → **401 Unauthorized**.
4. Click **Continue to Log In** → default IdP username/password form → after success, HMI loads.

## Tailscale admin steps (if Funnel is blocked)

If `tailscale funnel` errors about Funnel / HTTPS / ACLs:

1. Open [Tailscale admin console](https://login.tailscale.com/admin) for the tailnet.
2. **DNS** → enable **HTTPS Certificates** (MagicDNS).
3. **Access controls** → ensure Funnel is permitted. Example node attribute (adjust to your policy):

   ```json
   "nodeAttrs": [
     {
       "target": ["autogroup:member"],
       "attr": ["funnel"]
     }
   ]
   ```

4. Approve any pending Funnel / HTTPS prompts for this node if the console asks.
5. Re-run `tailscale funnel --bg --yes 19088` on the lab PC.

Official docs: [Tailscale Funnel](https://tailscale.com/kb/1223/funnel), [Serve / Funnel use cases](https://tailscale.com/kb/1247/funnel-serve-use-cases).

## Lab reference

| Item | Value |
|------|--------|
| Compose service | `ignition-standard` / container `bh-ignition-standard` |
| Host HTTP | `STANDARD_HTTP_PORT` → container `8088` (see `docker-compose.yml`) |
| Local smoke test | `http://127.0.0.1:19088/data/perspective/client/BH/` |
