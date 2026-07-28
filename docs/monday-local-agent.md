# Monday → local Cursor agent pipeline

Fully automatic path: Monday Tickets board `create_item` webhook → Tailscale Funnel → local Python proxy → **Dylan-only filer filter** → headless **Cursor Agent CLI** on this PC (not Cursor Cloud Automations).

Non-Dylan tickets never spawn an agent; they get a **Pushover** “ticket added” notification instead.

## Architecture

```text
Monday create_item (board 18423731526, webhook 614195738)
  → https://desktop-tqun3fn.tailc23270.ts.net/monday-webhook
    → Tailscale Funnel → http://127.0.0.1:9876
  → scripts/monday_webhook_proxy.py
       ├─ echo challenge
       ├─ parse create_pulse / create_item
       ├─ enrich via Monday GraphQL (token from env or Ignition Monday tag file)
       ├─ filter Dylan Jones filer only
       │    ├─ accept → spawn: agent -p --force --trust --workspace <repo> <prompt>
       │    └─ reject → Pushover “Monday ticket added by {filer}: {name}” + link (no agent)
            → branch + fix + scan + commit + draft PR (gh)
```

## Why filer ≠ Monday creator

Ticket Logger (`shared.TicketLogger`) creates board items with the gateway’s Monday **API token**. That token belongs to Dylan, so every HMI-submitted ticket has:

- webhook `userId` = Dylan (`111292620`)
- GraphQL `items.creator` = Dylan

The **real filer** is stored in:

| Source | Column / field |
|--------|----------------|
| Employee Name | `text` |
| Email | `email` |
| Description line | `Created By: …` inside `long_text7` |

The filter **must** use those when present. Trusting webhook/`creator.id` alone falsely auto-agents every Ticket Logger ticket (e.g. Tylor Slack).

## Dylan filter

### When Employee Name / Email / `Created By` is present (Ticket Logger)

Accept only if filer identity matches Dylan (name/email substrings). **Ignore** API `creator.id` / webhook `userId` (token owner).

### When those are empty (manual Monday UI create)

Accept if Monday `creator.id` / webhook `userId` is `111292620`, or creator name/email matches Dylan substrings.

### Never

- Match against ticket **title**, description body, or update **text** (too loose).
- Spawn an agent when enrich fails and filer columns are unknown (avoids false accepts if Monday API is down). Still Pushover-notifies.

### Match substrings / ids

| Signal | Default |
|--------|---------|
| Monday user id (manual creates only) | `111292620` |
| Email / name | `dylan.jones`, `dylan jones`, `djones@oneshotautomation`, `death2bigfoot@proton.me`, `dylan.jones@hbtech.com` |

Configure via `.env`:

```bash
MONDAY_AGENT_USER_IDS=111292620
MONDAY_AGENT_MATCH_SUBSTRINGS=dylan.jones,dylan jones,djones@oneshotautomation
```

Accept/reject decisions are logged to `logs/monday-agent/proxy-stderr.log` with `source=filer_columns|monday_creator|enrich_failed`.

## Local agent CLI

| | |
|--|--|
| Binary | `C:\Users\dylan.jones\AppData\Local\cursor-agent\agent.cmd` |
| Override | env `CURSOR_AGENT_CMD` |
| Auth | already logged in via `agent login` (or set `CURSOR_API_KEY`) |
| Headless flags | `-p --force --trust --sandbox disabled --workspace <repo> --approve-mcps` |
| Prompt | `scripts/prompts/monday-hmi-fix.md` + ticket JSON |

Official docs: [Cursor CLI headless](https://cursor.com/docs/cli/headless).

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
| `.env` `PUSHOVER_TOKEN` / `PUSHOVER_USER` | non-Dylan ticket alerts + Dylan job start/finish |
| `.env` `MONDAY_API_TOKEN` (optional) | item enrich; else read Ignition tag default from gitignored `…/_Config/Monday/tags.json` |
| Cursor agent login / `CURSOR_API_KEY` | headless agent auth |

## Verify

```powershell
# Filter unit tests (no agent spawn, no Pushover)
python scripts/monday_webhook_proxy.py --self-test

# Challenge echo (local)
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:9876/ -Body '{"challenge":"x"}' -ContentType application/json

# Challenge echo (Funnel)
Invoke-RestMethod -Method POST -Uri https://desktop-tqun3fn.tailc23270.ts.net/monday-webhook -Body '{"challenge":"x"}' -ContentType application/json

# Synthetic Dylan Ticket Logger webhook (dry-run)
$env:MONDAY_AGENT_DRY_RUN = "1"
# restart proxy with --dry-run, then:
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

Self-test covers: Tylor-style Ticket Logger (reject despite Dylan `userId`), Dylan Employee Name (accept), email column (accept), title-substring trap (reject).

**Live test:** submit a Ticket Logger ticket as Dylan → agent + START/FINISH Pushover. Submit as anyone else → Pushover only, no `logs/monday-agent/*` agent spawn.

## Draft PR note

Install GitHub CLI if needed: `winget install --id GitHub.cli -e`. Authenticate with `gh auth login`. The agent prompt asks for a **draft** PR and never merges.

## Related

- `docs/ticket-logger-monday.md` — board/columns/Ticket Logger
- `docs/cloud-agent/SUMMARY.md` — agent conventions + scan API
- `docs/ignition-resource-signatures.md` — mandatory signature + CAS repair after project edits
- `docs/tailscale-funnel.md` — Funnel for Perspective (gateway `/`); webhook uses `/monday-webhook`
