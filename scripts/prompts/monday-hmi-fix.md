# Monday ticket → local HMI fix (Cursor Agent CLI)

You are running **locally** on Dylan Jones's Windows machine against the Boars Head (`Bors`) Ignition lab repo. This job was triggered by a Monday.com Tickets board `create_item` webhook after a Dylan-only filter.

## Mandatory first reads

1. `docs/cloud-agent/SUMMARY.md`
2. `docs/cloud-agent/ignition-scan.json` (scan API token — use for POST after edits)
3. Relevant `.cursor/rules` (CSS-only stylesheet, `HBT`→`shared`, faceplates under `01_Popups/00_Faceplates/`, Perspective JSON conventions, Ticket Logger)

## Goal

Implement a fix for the Monday ticket described at the bottom of this prompt.

## Workflow (fully automatic — do not wait for a human)

1. **Branch:** from current default/`main` (or the repo's primary branch), create and check out:
   `ticket/<monday_item_id>-<short-slug>`
2. **Understand:** use the ticket title + description (+ updates). Prefer editing BH Perspective / scripts under `gateways/standard/data/projects/BH/`.
3. **Implement** following BH conventions:
   - Styling → Advanced Stylesheet only (`stylesheet/stylesheet.css`); `props.style.classes` = simple class names
   - Scripts: `shared.*` never `HBT.*`; faceplates only under `01_Popups/00_Faceplates/`
   - Perspective JSON: scoped `propConfig` keys; tab-indented script bodies; `\n` only (no `\r\n`) in expression/code/script strings
   - New/edited views: Ticket Logger context-menu + `ticketLog` handler per project rules
4. **Scan:** after project/config edits, POST Ignition scan using `docs/cloud-agent/ignition-scan.json` (`scan/projects` and/or `scan/config` as appropriate). Prefer `127.0.0.1` over `localhost` on Windows.
5. **Commit** with a clear message focused on why (only when the fix is real). Do **not** commit `.env`, tokens, or secrets.
6. **Draft PR:** if `gh` is available and authenticated, push the branch and open a **draft** PR. Do **not** merge. If `gh` is missing, leave the branch committed locally and note that in your final summary.
7. **Stop** when the draft PR exists (or branch is committed if PR impossible). Summarize what changed.

## Do not

- Merge the PR
- Force-push `main`
- Recreate Designer Style Class folders
- Invent `01_Faceplates/`
- Commit secrets or gateway runtime churn under `projects/.resources/*` unless unavoidable

## Success criteria

- Fix matches the ticket
- Conventions respected
- Scan performed when files under projects/config changed
- Branch committed; draft PR preferred
