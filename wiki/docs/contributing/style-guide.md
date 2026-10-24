---
title: Style Guide
sidebar_position: 2
description: How to write wiki pages - audience, voice, Title Case, terminology, structure, and what must never appear.
sources:
  - README.md
last_verified: 2026-10-23
---

# Style Guide

## Audience

Write for a **novice Ignition developer who joins cold**: they know what a PLC and a database are, but not this
project. Every page should answer **what it is, where it lives, how it works, and how to change it safely**.

- Give the **location** of everything three ways when they exist: the file path in the repo, the Designer location
  (Project Browser > Perspective > Views > ...) and the Gateway web UI location (Connections > Devices > ...).
- Define jargon the first time on a page, or link the [Glossary](../getting-started/glossary.md).
- Explain the **why** behind non-obvious settings (the tag group rates, the write lock): the next person will want to
  change them.
- Prefer a numbered how-to over a paragraph when there are steps.

## Voice

- Plain, direct sentences in the present tense. "The Header holds the logo", not "will hold".
- Second person for instructions: "Open the view in the Designer."
- No marketing words, no filler.
- Dates as `2026-10-23`. Say when something is temporary: "Recently Redesigned (2026-10-23)", "planned, not started".

## Title Case

All user-facing text in the HMI is Title Case, and the wiki mirrors it:

- Page titles and headings: `Tag Providers And Tag Groups`, `Your First Change`.
- HMI labels exactly as shown on screen: **Out Of Service**, **Roles & Permissions**, **Start Defrost**.
- Tag paths, member names, file names and code keep their own casing: `Sts_Running`, `_Config/PlcWriteLock/Locked`.

## Terms

| Use | Not |
|---|---|
| gateway, Gateway web UI | server, config page |
| Designer | IDE |
| view, page (= a route), faceplate, dock | screen (except when quoting FT) |
| tag provider `[default]` | default provider |
| UDT definition / UDT instance | template / object |
| RCP1, the PLC | the controller (when ambiguous) |
| Local Groveport mode / enterprise mode | demo mode |

## Structure

- Start with one or two sentences saying what the page covers.
- Tables for settings (Setting / Value / Meaning) and inventories.
- `<details>` for long lists that most readers skip.
- Admonitions: `:::danger` for things that can hurt the plant or lose data, `:::warning` for traps, `:::note` /
  `:::tip` / `:::info` for the rest. Don't overuse them.
- End with "How To Change It" when the page documents a feature or a setting: Designer or Gateway web UI steps only (Project Browser path, which view or component, which property or binding, which script module or named query, then save and test in a Perspective session).

## Audience Rule

The wiki is for engineers who maintain the project **only through the Ignition Designer and the Gateway web UI**, plus git for version control. Never describe scripts that generate or edit project files, or the tooling around them. Where a setting can only be changed outside those two tools, say what it is and what it does, and write "changed by the system integrator".

## Never In The Wiki

- Passwords, API tokens, `.env` values, the contents of the lab scan settings file, encrypted blobs from
  config files.
- SecureLink tunnel addresses, plant IP addresses, VPN details.
- Test user names and their passwords.
- Personal data (names in screenshots: mask them).
- The contents of third-party reference files the project only borrows from (e.g. `lightspeeddefaulttags.json`).
