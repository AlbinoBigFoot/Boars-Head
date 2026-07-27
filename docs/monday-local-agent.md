# Monday → local Cursor agent pipeline

Fully automatic path: Monday Tickets board `create_item` webhook → Tailscale Funnel → local Python proxy → Dylan-only filter → headless **Cursor Agent CLI** on this PC (not Cursor Cloud Automations).

## Architecture

```text
Monday create_item (board 18423731526, webhook 614195738)
  → https://desktop-tqun3fn.tailc23270.ts.net/monday-webhook
  → Tailscale Funnel → http://127.0.0.1:9876
  → scripts/monday_webhook_proxy.py
       ├─ echo challenge
       ├─ parse create_pulse / create_item
       ├─ enrich via Monday GraphQL (token from env or Ignition Monday tag file)
       ├─ filter Dylan Jones only (else log skip)
       └─ spawn: agent -p --force --trust --workspace <repo> <prompt>
            → branch + fix + scan + commit + draft PR (gh)
```

## Local agent CLI

| | |
|--|--|
| Binary | `C:\Users\dylan.jones\AppData\Local\cursor-agent\agent.cmd` |
| Override | env `CURSOR_AGENT_CMD` |
| Auth | already logged in via `agent login` (or set `CURSOR_API_KEY`) |
| Headless flags | `-p --force --trust --sandbox disabled --workspace <repo> --approve-mcps` |
| Prompt | `scripts/prompts/monday-hmi-fix.md` + ticket JSON |

Official docs: [Cursor CLI headless](https://cursor.com/docs/cli/headless).

## Dylan filter

Accept if **any** of:

| Signal | Default |
|--------|---------|
| Monday `userId` / creator id | `111292620` (Dylan Jones) |
| Email / name / Employee Name (`text`) / description / pulse name contains | `dylan.jones`, `dylan jones`, `djones@oneshotautomation`, `death2bigfoot@proton.me`, `dylan.jones@hbtech.com` |

Configure via `.env`:

```bash
MONDAY_AGENT_USER_IDS=111292620
MONDAY_AGENT_MATCH_SUBSTRINGS=dylan.jones,dylan jones,djones@oneshotautomation
```

Skips are logged to the proxy stderr / `logs/monday-agent/proxy-stderr.log`.

## Start / stop (service)

```powershell
# One-time: AtLogOn scheduled task
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\install-monday-webhook-task.ps1

# Start now
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\start-monday-webhook.ps1
# or: Start-ScheduledTask -TaskName 'BH-Monday-Local-Agent-Proxy'

# Stop
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\stop-monday-webhook.ps1
```

Task name: **`BH-Monday-Local-Agent-Proxy`**.

Funnel path `/monday-webhook` → `127.0.0.1:9876` is verified/repaired by the start script when Tailscale is available.

## Secrets (never commit)

| Source | Use |
|--------|-----|
| `.env` `PUSHOVER_TOKEN` / `PUSHOVER_USER` | setup + job start/finish notifications |
| `.env` `MONDAY_API_TOKEN` (optional) | item enrich; else read Ignition tag default from gitignored `…/_Config/Monday/tags.json` |
| Cursor agent login / `CURSOR_API_KEY` | headless agent auth |

## Verify

```powershell
# Filter unit tests (no agent spawn)
python scripts/monday_webhook_proxy.py --self-test

# Challenge echo (local)
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:9876/ -Body '{"challenge":"x"}' -ContentType application/json

# Challenge echo (Funnel)
Invoke-RestMethod -Method POST -Uri https://desktop-tqun3fn.tailc23270.ts.net/monday-webhook -Body '{"challenge":"x"}' -ContentType application/json

# Synthetic Dylan webhook (dry-run — set env first or use proxy --dry-run)
$env:MONDAY_AGENT_DRY_RUN = "1"
# restart proxy, then:
$body = @{
  event = @{
    type = "create_pulse"
    pulseId = "9990001"
    pulseName = "Synthetic dry-run ticket"
    userId = 111292620
    userName = "Dylan Jones"
    boardId = 18423731526
  }
} | ConvertTo-Json -Depth 5
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:9876/ -Body $body -ContentType application/json
```

**Live test:** submit a Ticket Logger ticket as Dylan (or create an item while logged in as Dylan). Expect Pushover START/FINISH and a local agent log under `logs/monday-agent/`.

## Draft PR note

Install GitHub CLI if needed: `winget install --id GitHub.cli -e`. Authenticate with `gh auth login`. The agent prompt asks for a **draft** PR and never merges.

## Related

- `docs/ticket-logger-monday.md` — board/columns/Ticket Logger
- `docs/cloud-agent/SUMMARY.md` — agent conventions + scan API
- `docs/tailscale-funnel.md` — Funnel for Perspective (gateway `/`); webhook uses `/monday-webhook`
