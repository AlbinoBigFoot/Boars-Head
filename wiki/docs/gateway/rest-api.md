---
title: REST API
sidebar_position: 17
description: The Ignition 8.3 REST API endpoints used for health checks and the trial clock, the API token, and the 401 / 403 errors.
sources:
  - trial-watch/watch_trial.py
  - docs/plc-write-lock.md
last_verified: 2026-10-24
---

# REST API

Ignition 8.3 has a REST API under **`http://localhost:19088/data/api/v1/`**. In this project it is used only by the
`ignition-trial-watch` container (it resets the lab trial clock) and for quick health checks. Day-to-day changes are
made in the Designer and the Gateway web UI, not through the API. Authenticate with the header
`X-Ignition-API-Token: <name>:<secret>` (the `Access` key, see [Security](security.md#api-key-access)).

## The Token

The token is the `Access` API key (Gateway web UI > Config > Security > API Tokens). Its value lives in `.env`
(`IGNITION_API_TOKEN`) and is sent only as a request header. Never print it or paste it anywhere.

## Endpoints Used

| Method + Path | Effect |
|---|---|
| `GET /StatusPing` (no auth, not under `/data/api`) | `{"state":"RUNNING"}` when the gateway is up |
| `GET /data/api/v1/gateway-info` | Name, edition, version, license mode |
| `GET /data/api/v1/trial`, `POST` same | Read / reset the trial (used by `ignition-trial-watch`) |
| `GET /data/api/v1/modules/healthy` | Module states |
| `GET /data/api/v1/logs` | Gateway log entries |

The same information is in the Gateway web UI: Status > Overview, Status > Modules, Status > Logs.

## If A Change Does Not Show

After a `git pull`, merge or checkout, use **File > Update Project** in the Designer. If a view still shows the old
version after a browser reload, restart the gateway service (in the lab, `docker restart bh-ignition-standard`, then wait
for `curl.exe -s http://localhost:19088/StatusPing` to return `{"state":"RUNNING"}`, about 40 s).

## 401 / 403

- `401`: the token is missing, wrong, or in bare-secret form (needs `Access:<secret>`).
- `403` on write endpoints: the key lacks the `Write` level (Config > Security > General Settings, Gateway Write
  Permissions) - or, for `POST /trial`, the trial simply isn't expired yet.
