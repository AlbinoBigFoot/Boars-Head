#!/usr/bin/env python3
"""Monday → local Cursor agent job helpers (filter, enrich, spawn, notify)."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = REPO_ROOT / "logs" / "monday-agent"
HANDOFF_DIR = REPO_ROOT / "docs" / "handoff"
PROMPT_FILE = REPO_ROOT / "scripts" / "prompts" / "monday-hmi-fix.md"
DEFAULT_AGENT = Path(
	os.environ.get(
		"CURSOR_AGENT_CMD",
		r"C:\Users\dylan.jones\AppData\Local\cursor-agent\agent.cmd",
	)
)
MONDAY_TAG_TOKEN_PATH = (
	REPO_ROOT
	/ "gateways"
	/ "standard"
	/ "data"
	/ "config"
	/ "resources"
	/ "core"
	/ "ignition"
	/ "tag-definition"
	/ "default"
	/ "_Config"
	/ "Monday"
	/ "tags.json"
)

# Tickets board (Service Agent Workspace)
DEFAULT_BOARD_ID = "18423731526"
PENDING_REVIEW_TITLE = "Pending Review"
# Created 2026-07-28 on board 18423731526 — override via MONDAY_PENDING_REVIEW_GROUP_ID
DEFAULT_PENDING_REVIEW_GROUP_ID = "group_mm5p3hpn"
# Files column on board 18423731526 ("Attached Files") — override via MONDAY_FILES_COLUMN_ID
DEFAULT_FILES_COLUMN_ID = "files"
# Monday /v2/file accepts .md (verified); keep original handoff name when attaching
MONDAY_FILE_ENDPOINT = "https://api.monday.com/v2/file"

# Dylan Jones — Monday account (Service Agent Workspace)
DEFAULT_USER_IDS = ("111292620",)
DEFAULT_MATCH_SUBSTRINGS = (
	"dylan.jones",
	"dylan jones",
	"djones@oneshotautomation",
	"death2bigfoot@proton.me",
	"dylan.jones@hbtech.com",
)


def load_dotenv(path: Path | None = None) -> None:
	"""Load KEY=VALUE from .env into os.environ if not already set."""
	env_path = path or (REPO_ROOT / ".env")
	if not env_path.is_file():
		return
	for raw in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
		line = raw.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		key, val = line.split("=", 1)
		key = key.strip()
		val = val.strip().strip("'").strip('"')
		if key and key not in os.environ:
			os.environ[key] = val


def env(name: str, default: str = "") -> str:
	return (os.environ.get(name) or default).strip()


def _csv_env(name: str, defaults: tuple[str, ...]) -> list[str]:
	raw = env(name)
	if not raw:
		return [d.lower() for d in defaults]
	return [p.strip().lower() for p in raw.split(",") if p.strip()]


def allowed_user_ids() -> set[str]:
	return set(_csv_env("MONDAY_AGENT_USER_IDS", DEFAULT_USER_IDS))


def match_substrings() -> list[str]:
	return _csv_env("MONDAY_AGENT_MATCH_SUBSTRINGS", DEFAULT_MATCH_SUBSTRINGS)


def monday_api_token() -> str:
	tok = env("MONDAY_API_TOKEN")
	if tok:
		return tok
	# Fallback: Ignition memory-tag defaultValue (gitignored runtime file)
	try:
		if MONDAY_TAG_TOKEN_PATH.is_file():
			tags = json.loads(MONDAY_TAG_TOKEN_PATH.read_text(encoding="utf-8"))
			for tag in tags:
				if tag.get("name") == "API Token":
					val = (tag.get("defaultValue") or "").strip()
					if val:
						return val
	except (OSError, json.JSONDecodeError, TypeError):
		pass
	return ""


def pushover(message: str, title: str = "BH Monday→Agent") -> bool:
	token = env("PUSHOVER_TOKEN")
	user = env("PUSHOVER_USER")
	if not token or not user:
		sys.stderr.write("pushover skipped: missing PUSHOVER_TOKEN/USER\n")
		return False
	data = urllib.parse.urlencode(
		{
			"token": token,
			"user": user,
			"title": title[:250],
			"message": message[:1024],
		}
	).encode("utf-8")
	req = urllib.request.Request(
		"https://api.pushover.net/1/messages.json",
		data=data,
		method="POST",
		headers={"Content-Type": "application/x-www-form-urlencoded"},
	)
	try:
		with urllib.request.urlopen(req, timeout=20) as resp:
			_ = resp.read()
		return True
	except Exception as exc:  # noqa: BLE001
		sys.stderr.write("pushover error: %s\n" % exc)
		return False


# late import for urllib.parse used above
import urllib.parse  # noqa: E402


def monday_graphql(query: str, variables: dict | None = None) -> dict:
	token = monday_api_token()
	if not token:
		raise RuntimeError("MONDAY_API_TOKEN not available")
	body = {"query": query}
	if variables is not None:
		body["variables"] = variables
	req = urllib.request.Request(
		"https://api.monday.com/v2",
		data=json.dumps(body).encode("utf-8"),
		headers={
			"Authorization": token,
			"Content-Type": "application/json",
			"API-Version": env("MONDAY_API_VERSION", "2026-07"),
		},
		method="POST",
	)
	with urllib.request.urlopen(req, timeout=30) as resp:
		payload = json.loads(resp.read().decode("utf-8"))
	if payload.get("errors"):
		raise RuntimeError("Monday GraphQL errors: %s" % payload["errors"])
	return payload.get("data") or {}


def fetch_item(item_id: str) -> dict:
	data = monday_graphql(
		"""
		query ($ids: [ID!]) {
			items(ids: $ids) {
				id
				name
				url
				creator { id name email }
				column_values { id text type value }
				updates(limit: 5) { body text_body creator { id name email } }
			}
		}
		""",
		{"ids": [str(item_id)]},
	)
	items = data.get("items") or []
	return items[0] if items else {}


def fetch_board_groups(board_id: str) -> list[dict]:
	data = monday_graphql(
		"""
		query ($ids: [ID!]) {
			boards(ids: $ids) {
				groups { id title }
			}
		}
		""",
		{"ids": [str(board_id)]},
	)
	boards = data.get("boards") or []
	if not boards:
		return []
	return list(boards[0].get("groups") or [])


def resolve_pending_review_group_id(board_id: str | None = None) -> str:
	"""Resolve Pending Review group id: env override → title match → default."""
	override = env("MONDAY_PENDING_REVIEW_GROUP_ID")
	if override:
		return override

	bid = (board_id or env("MONDAY_BOARD_ID") or DEFAULT_BOARD_ID).strip()
	try:
		groups = fetch_board_groups(bid)
		for g in groups:
			title = _norm(g.get("title")).lower()
			if title in ("pending review", "pending-review"):
				gid = _norm(g.get("id"))
				if gid:
					return gid
		# Fuzzy: title contains both words
		for g in groups:
			title = _norm(g.get("title")).lower()
			if "pending" in title and "review" in title:
				gid = _norm(g.get("id"))
				if gid:
					return gid
	except Exception as exc:  # noqa: BLE001
		sys.stderr.write(
			"pending-review group lookup failed board=%s err=%s; using default\n"
			% (bid, exc)
		)

	return DEFAULT_PENDING_REVIEW_GROUP_ID


def move_item_to_group(item_id: str, group_id: str) -> dict:
	data = monday_graphql(
		"""
		mutation ($itemId: ID!, $groupId: String!) {
			move_item_to_group(item_id: $itemId, group_id: $groupId) {
				id
			}
		}
		""",
		{"itemId": str(item_id), "groupId": str(group_id)},
	)
	return data.get("move_item_to_group") or {}


def create_monday_update(item_id: str, body: str) -> dict:
	data = monday_graphql(
		"""
		mutation ($itemId: ID!, $body: String!) {
			create_update(item_id: $itemId, body: $body) { id }
		}
		""",
		{"itemId": str(item_id), "body": body},
	)
	return data.get("create_update") or {}


def monday_multipart_file(
	query: str,
	file_path: Path,
	*,
	filename: str | None = None,
	content_type: str = "text/plain",
) -> dict:
	"""Upload a file via Monday's multipart /v2/file endpoint.

	Used by add_file_to_update / add_file_to_column (JSON /v2 cannot carry File!).
	"""
	token = monday_api_token()
	if not token:
		raise RuntimeError("MONDAY_API_TOKEN not available")
	path = Path(file_path)
	if not path.is_file():
		raise FileNotFoundError(str(path))
	name = filename or path.name
	data = path.read_bytes()
	boundary = "----MondayBoundary%s" % os.urandom(8).hex()
	parts: list[bytes] = []
	parts.append(
		(
			"--%s\r\n"
			'Content-Disposition: form-data; name="query"\r\n\r\n'
			"%s\r\n" % (boundary, query)
		).encode("utf-8")
	)
	parts.append(
		(
			"--%s\r\n"
			'Content-Disposition: form-data; name="variables[file]"; filename="%s"\r\n'
			"Content-Type: %s\r\n\r\n" % (boundary, name, content_type)
		).encode("utf-8")
		+ data
		+ b"\r\n"
	)
	parts.append(("--%s--\r\n" % boundary).encode("utf-8"))
	req = urllib.request.Request(
		MONDAY_FILE_ENDPOINT,
		data=b"".join(parts),
		method="POST",
		headers={
			"Authorization": token,
			"API-Version": env("MONDAY_API_VERSION", "2026-07"),
			"Content-Type": "multipart/form-data; boundary=%s" % boundary,
		},
	)
	with urllib.request.urlopen(req, timeout=60) as resp:
		payload = json.loads(resp.read().decode("utf-8"))
	if payload.get("errors"):
		raise RuntimeError("Monday file upload errors: %s" % payload["errors"])
	return payload.get("data") or {}


def add_file_to_update(update_id: str, file_path: Path, filename: str | None = None) -> dict:
	"""Attach a file to an existing Monday update (multipart /v2/file)."""
	name = filename or Path(file_path).name
	# Prefer text/plain for broad compatibility; .md extension still works on Monday.
	ctype = "text/markdown" if name.lower().endswith(".md") else "text/plain"
	query = (
		"mutation ($file: File!) {"
		" add_file_to_update(update_id: %s, file: $file) { id name url file_extension }"
		" }" % str(update_id)
	)
	data = monday_multipart_file(query, file_path, filename=name, content_type=ctype)
	return data.get("add_file_to_update") or {}


def add_file_to_column(
	item_id: str,
	file_path: Path,
	*,
	column_id: str | None = None,
	filename: str | None = None,
) -> dict:
	"""Attach a file to an item's Files column (multipart /v2/file)."""
	col = (column_id or env("MONDAY_FILES_COLUMN_ID") or DEFAULT_FILES_COLUMN_ID).strip()
	name = filename or Path(file_path).name
	ctype = "text/markdown" if name.lower().endswith(".md") else "text/plain"
	query = (
		"mutation ($file: File!) {"
		' add_file_to_column(item_id: %s, column_id: "%s", file: $file)'
		" { id name url file_extension }"
		" }" % (str(item_id), col)
	)
	data = monday_multipart_file(query, file_path, filename=name, content_type=ctype)
	return data.get("add_file_to_column") or {}


def handoff_path_for_item(item_id: str) -> Path:
	return HANDOFF_DIR / ("ticket-%s.md" % item_id)


def resolve_handoff_file(item_id: str, artifacts: dict | None = None) -> Path | None:
	"""Return on-disk handoff Path if present (repo-relative artifacts.handoff or default)."""
	candidates: list[Path] = []
	rel = ""
	if artifacts:
		rel = str(artifacts.get("handoff") or "").replace("\\", "/").strip()
	if rel:
		candidates.append(REPO_ROOT / rel)
	candidates.append(handoff_path_for_item(item_id))
	candidates.append(REPO_ROOT / ("docs/handoff/tickets/%s.md" % item_id))
	seen: set[str] = set()
	for p in candidates:
		key = str(p.resolve()) if p.exists() else str(p)
		if key in seen:
			continue
		seen.add(key)
		if p.is_file():
			return p
	return None


def parse_agent_artifacts(log_text: str, item_id: str) -> dict:
	"""Best-effort extract branch / handoff / draft PR from agent log + disk."""
	branch = ""
	pr_url = ""
	handoff = ""

	# Branch: ticket/<id>-slug or any ticket/... mentioned
	m = re.search(
		r"(?im)\b(ticket/%s-[a-zA-Z0-9._/-]+)\b" % re.escape(str(item_id)),
		log_text or "",
	)
	if m:
		branch = m.group(1).rstrip("/.")
	if not branch:
		m = re.search(r"(?im)\b(ticket/[a-zA-Z0-9._/-]+)\b", log_text or "")
		if m:
			branch = m.group(1).rstrip("/.")

	# Draft PR URL (github.com/.../pull/N)
	m = re.search(
		r"https://github\.com/[^\s)\]\"']+/pull/\d+",
		log_text or "",
	)
	if m:
		pr_url = m.group(0).rstrip(".,;")

	# Handoff path in log or on disk
	expected = handoff_path_for_item(item_id)
	rel = "docs/handoff/ticket-%s.md" % item_id
	alt = "docs/handoff/tickets/%s.md" % item_id
	if expected.is_file():
		handoff = rel
	elif (REPO_ROOT / alt).is_file():
		handoff = alt
	else:
		m = re.search(
			r"(?im)\b(docs/handoff/(?:tickets/)?ticket-?%s\.md)\b" % re.escape(str(item_id)),
			log_text or "",
		)
		if m:
			handoff = m.group(1).replace("\\", "/")
		elif re.search(r"(?im)\bdocs/handoff/[^\s)\]\"']+\.md\b", log_text or ""):
			m2 = re.search(r"(?im)\b(docs/handoff/[^\s)\]\"']+\.md)\b", log_text or "")
			if m2:
				handoff = m2.group(1).replace("\\", "/")

	# Prefer live git branch if it looks like this ticket
	try:
		proc = subprocess.run(
			["git", "branch", "--show-current"],
			cwd=str(REPO_ROOT),
			capture_output=True,
			text=True,
			timeout=10,
		)
		cur = (proc.stdout or "").strip()
		if cur.startswith("ticket/") and str(item_id) in cur:
			branch = cur
	except Exception:  # noqa: BLE001
		pass

	return {
		"branch": branch,
		"handoff": handoff or (rel if expected.is_file() else ""),
		"pr_url": pr_url,
	}


def build_review_update_body(
	ticket: dict,
	artifacts: dict,
	*,
	handoff_markdown: str | None = None,
	file_attached: bool = False,
) -> str:
	item_id = ticket.get("item_id") or ""
	title = ticket.get("title") or ticket.get("name") or ""
	branch = artifacts.get("branch") or "(see handoff / local git)"
	handoff = artifacts.get("handoff") or ("docs/handoff/ticket-%s.md" % item_id)
	pr_url = artifacts.get("pr_url") or ""
	parts = [
		"Local agent finished — ready for Dylan review (NOT on main).",
		"",
		"Ticket: %s" % title,
		"Branch: %s" % branch,
		"Handoff: %s" % handoff,
	]
	if pr_url:
		parts.append("Draft PR: %s" % pr_url)
	else:
		parts.append("Draft PR: (none — checkout branch locally)")
	if file_attached:
		parts.append("Handoff file: attached once to Attached Files (files column).")
	parts.extend(
		[
			"",
			"Next: open Cursor Desktop → checkout the branch → read the handoff → continue or merge when ready.",
			"Do not merge to main until Dylan confirms.",
		]
	)
	# Fallback: embed full handoff markdown when file attach is unavailable/failed
	if handoff_markdown and not file_attached:
		parts.extend(
			[
				"",
				"---",
				"Handoff (inline — file attach failed or unavailable):",
				"",
				handoff_markdown.strip(),
			]
		)
	return "\n".join(parts)


def post_success_review(ticket: dict, log_path: Path) -> dict:
	"""Move Monday item to Pending Review + post update (+ handoff file attach).

	File attach uses multipart /v2/file once only:
	  - add_file_to_column on Files / Attached Files (board default: files)
	Do not also add_file_to_update — that duplicates entries in Attached Files.
	If column attach fails, the update body includes the full handoff markdown.
	"""
	item_id = str(ticket.get("item_id") or "")
	board_id = str(ticket.get("board_id") or env("MONDAY_BOARD_ID") or DEFAULT_BOARD_ID)
	log_text = ""
	try:
		if log_path.is_file():
			log_text = log_path.read_text(encoding="utf-8", errors="replace")
	except OSError:
		pass

	artifacts = parse_agent_artifacts(log_text, item_id)
	handoff_file = resolve_handoff_file(item_id, artifacts)
	handoff_md = ""
	if handoff_file is not None:
		try:
			handoff_md = handoff_file.read_text(encoding="utf-8", errors="replace")
			rel = str(handoff_file.relative_to(REPO_ROOT)).replace("\\", "/")
			artifacts["handoff"] = rel
		except OSError as exc:
			sys.stderr.write("handoff read failed item=%s err=%s\n" % (item_id, exc))

	result: dict[str, Any] = {
		"item_id": item_id,
		"artifacts": artifacts,
		"group_id": "",
		"moved": False,
		"update_id": "",
		"file_update_asset_id": "",
		"file_column_asset_id": "",
		"errors": [],
	}

	if not monday_api_token():
		result["errors"].append("no MONDAY_API_TOKEN — skip move/update")
		return result

	try:
		group_id = resolve_pending_review_group_id(board_id)
		result["group_id"] = group_id
		move_item_to_group(item_id, group_id)
		result["moved"] = True
		sys.stderr.write(
			"monday moved item=%s → group=%s (Pending Review)\n" % (item_id, group_id)
		)
	except Exception as exc:  # noqa: BLE001
		result["errors"].append("move failed: %s" % exc)
		sys.stderr.write("monday move failed item=%s err=%s\n" % (item_id, exc))

	# Attach handoff once to Files column (Attached Files), then post short text update
	file_attached = False
	if handoff_file is not None:
		try:
			asset = add_file_to_column(item_id, handoff_file)
			result["file_column_asset_id"] = _norm(asset.get("id"))
			if result["file_column_asset_id"]:
				file_attached = True
			sys.stderr.write(
				"monday handoff attached to Files column item=%s asset=%s name=%s\n"
				% (
					item_id,
					result["file_column_asset_id"],
					asset.get("name") or handoff_file.name,
				)
			)
		except Exception as exc:  # noqa: BLE001
			result["errors"].append("file→column failed: %s" % exc)
			sys.stderr.write(
				"monday handoff→column failed item=%s err=%s\n" % (item_id, exc)
			)

	try:
		body = build_review_update_body(
			ticket, artifacts, file_attached=file_attached
		)
		upd = create_monday_update(item_id, body)
		result["update_id"] = _norm(upd.get("id"))
		sys.stderr.write(
			"monday update posted item=%s update_id=%s file_attached=%s\n"
			% (item_id, result["update_id"], file_attached)
		)
	except Exception as exc:  # noqa: BLE001
		result["errors"].append("update failed: %s" % exc)
		sys.stderr.write("monday update failed item=%s err=%s\n" % (item_id, exc))

	# Reliable fallback: full handoff markdown in a second update when attach failed
	if handoff_md and not file_attached:
		try:
			fallback = build_review_update_body(
				ticket,
				artifacts,
				handoff_markdown=handoff_md,
				file_attached=False,
			)
			upd2 = create_monday_update(item_id, fallback)
			fallback_id = _norm(upd2.get("id"))
			if fallback_id:
				result["update_id"] = result["update_id"] or fallback_id
			sys.stderr.write(
				"monday handoff inline fallback posted item=%s update_id=%s\n"
				% (item_id, fallback_id)
			)
		except Exception as exc:  # noqa: BLE001
			result["errors"].append("inline handoff fallback failed: %s" % exc)
			sys.stderr.write(
				"monday handoff inline fallback failed item=%s err=%s\n"
				% (item_id, exc)
			)

	return result


def format_finish_pushover(
	*,
	status: str,
	ticket: dict,
	elapsed: int,
	artifacts: dict | None = None,
	review: dict | None = None,
) -> str:
	item_id = ticket.get("item_id") or ""
	title = ticket.get("title") or ""
	arts = artifacts or {}
	branch = arts.get("branch") or "(unknown branch)"
	handoff = arts.get("handoff") or ("docs/handoff/ticket-%s.md" % item_id)
	pr_url = arts.get("pr_url") or ""
	lines = [
		"Local agent %s for Monday ticket %s (%ss)" % (status, item_id, elapsed),
		title,
		"branch: %s" % branch,
		"handoff: %s" % handoff,
		"NOT on main — review locally before merge",
	]
	if pr_url:
		lines.append("draft PR: %s" % pr_url)
	if review and review.get("moved"):
		lines.append("Monday → Pending Review (%s)" % (review.get("group_id") or ""))
	elif review and review.get("errors"):
		lines.append("Monday review hooks: %s" % "; ".join(review["errors"][:2]))
	return "\n".join(lines)


def _norm(value: Any) -> str:
	if value is None:
		return ""
	return str(value).strip()


def identity_blob(*parts: Any) -> str:
	return " | ".join(_norm(p) for p in parts if _norm(p)).lower()


def is_dylan_match(
	*,
	user_id: Any = None,
	email: Any = None,
	name: Any = None,
	reporter: Any = None,
	extra: Any = None,
) -> tuple[bool, str]:
	"""Return (matched, reason). Match Dylan on identity fields only (not ticket body)."""
	uid = _norm(user_id)
	if uid and uid in allowed_user_ids():
		return True, "user_id=%s" % uid

	blob = identity_blob(email, name, reporter, extra, uid)
	for needle in match_substrings():
		if needle and needle in blob:
			return True, "substring=%r in %r" % (needle, blob[:200])
	return False, "no match in %r" % (blob[:240] or "(empty)")


def parse_created_by(description: str) -> str:
	"""Extract Ticket Logger 'Created By: …' line from Description column.

	Only the remainder of the same line counts — do not let whitespace span
	newlines (that would steal 'Expected Result:' as the filer name).
	"""
	if not description:
		return ""
	m = re.search(r"(?im)^Created By:[ \t]*(.*)$", description)
	return (m.group(1) or "").strip() if m else ""


def extract_event(payload: dict) -> dict:
	"""Normalize Monday webhook shapes to a flat event dict."""
	if not isinstance(payload, dict):
		return {}
	event = payload.get("event")
	if isinstance(event, dict):
		return event
	# Some payloads nest under "payload"
	inner = payload.get("payload")
	if isinstance(inner, dict) and isinstance(inner.get("event"), dict):
		return inner["event"]
	return payload


def parse_create_item(payload: dict) -> dict | None:
	event = extract_event(payload)
	etype = _norm(event.get("type") or event.get("event") or "").lower()
	# Accept create_pulse / create_item / empty type with pulseId
	item_id = (
		event.get("pulseId")
		or event.get("itemId")
		or event.get("pulse_id")
		or event.get("item_id")
	)
	if not item_id:
		return None
	if etype and etype not in ("create_pulse", "create_item", "create"):
		# Still allow if clearly an item create with pulseName
		if not (event.get("pulseName") or event.get("itemName")):
			return None
	return {
		"item_id": str(item_id),
		"board_id": str(event.get("boardId") or event.get("board_id") or ""),
		"name": _norm(event.get("pulseName") or event.get("itemName") or event.get("name")),
		"user_id": _norm(event.get("userId") or event.get("user_id")),
		"user_name": _norm(event.get("userName") or event.get("user_name")),
		"group_id": _norm(event.get("groupId") or event.get("group_id")),
		"raw_event": event,
	}


def column_text(item: dict, *column_ids: str) -> str:
	cols = item.get("column_values") or []
	by_id = {c.get("id"): c for c in cols if isinstance(c, dict)}
	parts = []
	for cid in column_ids:
		c = by_id.get(cid)
		if c:
			parts.append(_norm(c.get("text")))
	return "\n".join(p for p in parts if p)


def evaluate_ticket(
	payload: dict,
	*,
	enrich: bool = True,
	item_override: dict | None = None,
) -> dict:
	"""Parse webhook, optionally enrich via Monday API, apply Dylan filter.

	Ticket Logger creates items with Dylan's Monday API token, so webhook userId
	and items.creator are always Dylan. Prefer Employee Name / Email / Created By
	as the real filer; only fall back to Monday creator/userId when those are empty
	(manual Monday UI creates).

	Returns dict with keys: ok, skip, reason, ticket, item, notify.
	"""
	parsed = parse_create_item(payload)
	if not parsed:
		return {
			"ok": False,
			"skip": True,
			"reason": "not a create_item/create_pulse event (or missing item id)",
			"ticket": None,
			"item": None,
			"notify": False,
		}

	item: dict = {}
	enrich_failed = False
	if item_override is not None:
		item = item_override
	elif enrich and monday_api_token():
		try:
			item = fetch_item(parsed["item_id"])
			if not item:
				enrich_failed = True
				sys.stderr.write("monday enrich empty item=%s\n" % parsed["item_id"])
		except Exception as exc:  # noqa: BLE001
			enrich_failed = True
			sys.stderr.write("monday enrich failed item=%s err=%s\n" % (parsed["item_id"], exc))
	elif enrich and not monday_api_token():
		enrich_failed = True
		sys.stderr.write("monday enrich skipped: no API token item=%s\n" % parsed["item_id"])

	creator = item.get("creator") if isinstance(item.get("creator"), dict) else {}
	reporter = column_text(item, "text")  # Employee Name (Ticket Logger filer)
	email_col = column_text(item, "email")
	description = column_text(item, "long_text7")
	created_by = parse_created_by(description)

	# Optional: first update creator (identity only — never body text)
	update_creator: dict = {}
	updates = item.get("updates") or []
	for u in updates:
		if isinstance(u, dict) and isinstance(u.get("creator"), dict):
			update_creator = u["creator"]
			break

	api_creator_id = _norm(creator.get("id")) or parsed["user_id"]
	api_creator_email = _norm(creator.get("email"))
	api_creator_name = _norm(creator.get("name")) or parsed["user_name"]

	# Real filer signals (Ticket Logger). When any is set, ignore API creator id —
	# that id is the token owner (Dylan), not the HMI reporter.
	filer_name = reporter or created_by
	filer_email = email_col
	has_filer_signal = bool(filer_name or filer_email)

	ticket = {
		**parsed,
		"creator_email": filer_email or api_creator_email,
		"creator_name": filer_name or api_creator_name,
		"api_creator_id": api_creator_id,
		"api_creator_name": api_creator_name,
		"api_creator_email": api_creator_email,
		"reporter": reporter,
		"created_by": created_by,
		"description": description,
		"url": _norm(item.get("url")),
		"title": _norm(item.get("name")) or parsed["name"],
		"filter_source": "",
	}

	# Cannot verify Ticket Logger filer without enrich — refuse agent (avoid false accept)
	if enrich_failed and not has_filer_signal and item_override is None:
		ticket["filter_source"] = "enrich_failed"
		return {
			"ok": True,
			"skip": True,
			"reason": "skip: enrich failed; cannot verify filer (API creator may be token owner)",
			"ticket": ticket,
			"item": item,
			"notify": True,
		}

	if has_filer_signal:
		ticket["filter_source"] = "filer_columns"
		matched, reason = is_dylan_match(
			user_id=None,  # never trust token-owner userId when filer columns exist
			email=filer_email,
			name=filer_name,
			reporter=filer_name,
			extra=None,
		)
	else:
		# Manual Monday UI create (no Employee Name / Created By / Email)
		ticket["filter_source"] = "monday_creator"
		uc_id = _norm(update_creator.get("id"))
		uc_email = _norm(update_creator.get("email"))
		uc_name = _norm(update_creator.get("name"))
		matched, reason = is_dylan_match(
			user_id=api_creator_id or uc_id,
			email=api_creator_email or uc_email,
			name=api_creator_name or uc_name,
			reporter=None,
			extra=None,
		)

	sys.stderr.write(
		"monday filter decision item=%s source=%s filer=%r email=%r api_creator=%s matched=%s detail=%s\n"
		% (
			parsed["item_id"],
			ticket["filter_source"],
			filer_name or "",
			filer_email or "",
			api_creator_id or "",
			matched,
			reason,
		)
	)

	if not matched:
		return {
			"ok": True,
			"skip": True,
			"reason": "skip non-dylan filer: %s" % reason,
			"ticket": ticket,
			"item": item,
			"notify": True,
		}

	return {
		"ok": True,
		"skip": False,
		"reason": "accept: %s (via %s)" % (reason, ticket["filter_source"]),
		"ticket": ticket,
		"item": item,
		"notify": False,
	}


def notify_non_dylan_ticket(ticket: dict, reason: str = "") -> bool:
	"""Pushover when a non-Dylan ticket is added (no agent spawn)."""
	creator = (
		ticket.get("reporter")
		or ticket.get("created_by")
		or ticket.get("creator_name")
		or ticket.get("user_name")
		or "unknown"
	)
	title = ticket.get("title") or ticket.get("name") or "(untitled)"
	item_id = ticket.get("item_id") or ""
	url = ticket.get("url") or ""
	parts = [
		"Monday ticket added by %s: %s" % (creator, title),
		"id=%s" % item_id if item_id else "",
		url,
	]
	if reason:
		parts.append("(%s)" % reason)
	msg = "\n".join(p for p in parts if p)
	return pushover(msg, title="Monday ticket (no agent)")


def build_agent_prompt(ticket: dict) -> str:
	template = ""
	if PROMPT_FILE.is_file():
		template = PROMPT_FILE.read_text(encoding="utf-8")
	else:
		template = (
			"Fix the Boars Head Ignition HMI issue described below. "
			"Read docs/cloud-agent/SUMMARY.md first. Create branch ticket/<id>-slug, "
			"implement, scan, commit on that branch only, push origin ticket/…, "
			"write docs/handoff/ticket-<id>.md, open a draft PR (do not merge to main).\n\n"
		)
	body = {
		"monday_item_id": ticket.get("item_id"),
		"title": ticket.get("title"),
		"url": ticket.get("url"),
		"reporter": ticket.get("reporter"),
		"creator_name": ticket.get("creator_name"),
		"creator_email": ticket.get("creator_email"),
		"description": ticket.get("description"),
		"board_id": ticket.get("board_id") or DEFAULT_BOARD_ID,
		"handoff_path": "docs/handoff/ticket-%s.md" % (ticket.get("item_id") or "ID"),
		"review_note": (
			"After exit 0 the job moves this item to Monday group Pending Review "
			"and posts a handoff update. Never merge to main."
		),
	}
	return (
		template.strip()
		+ "\n\n---\n## Monday ticket\n\n```json\n"
		+ json.dumps(body, indent=2)
		+ "\n```\n"
	)


def agent_cmd() -> Path:
	candidates = [
		Path(env("CURSOR_AGENT_CMD")) if env("CURSOR_AGENT_CMD") else None,
		DEFAULT_AGENT,
		Path(r"C:\Users\dylan.jones\AppData\Local\cursor-agent\cursor-agent.cmd"),
	]
	for c in candidates:
		if c and c.is_file():
			return c
	return DEFAULT_AGENT


def spawn_agent_job(ticket: dict, *, dry_run: bool = False) -> dict:
	"""Spawn local Cursor agent in a background thread/process. Returns job meta."""
	LOG_DIR.mkdir(parents=True, exist_ok=True)
	ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
	item_id = ticket.get("item_id") or "unknown"
	safe_title = re.sub(r"[^a-zA-Z0-9._-]+", "-", (ticket.get("title") or "ticket"))[:40]
	log_path = LOG_DIR / ("%s-%s-%s.log" % (ts, item_id, safe_title))
	prompt_path = LOG_DIR / ("%s-%s.prompt.md" % (ts, item_id))
	prompt = build_agent_prompt(ticket)
	prompt_path.write_text(prompt, encoding="utf-8")

	meta = {
		"item_id": item_id,
		"log_path": str(log_path),
		"prompt_path": str(prompt_path),
		"dry_run": dry_run,
		"started_at": ts,
	}

	if dry_run:
		log_path.write_text(
			"DRY RUN — would spawn agent for item %s\nPrompt written to %s\n"
			% (item_id, prompt_path),
			encoding="utf-8",
		)
		sys.stderr.write("dry-run job queued item=%s log=%s\n" % (item_id, log_path))
		return meta

	cmd_path = agent_cmd()
	# Headless local agent: print + force + trust workspace
	cmd = [
		str(cmd_path),
		"-p",
		"--force",
		"--trust",
		"--sandbox",
		"disabled",
		"--workspace",
		str(REPO_ROOT),
		"--approve-mcps",
		prompt,
	]
	# Prefer cmd.exe for .cmd wrappers on Windows
	if cmd_path.suffix.lower() == ".cmd":
		cmd = ["cmd.exe", "/c"] + cmd

	# Ensure GitHub CLI is visible to the agent even if not on user PATH
	job_env = {**os.environ, "CURSOR_AGENT_NONINTERACTIVE": "1"}
	gh_dirs = [
		r"C:\Program Files\GitHub CLI",
		os.path.expandvars(r"%LOCALAPPDATA%\Programs\GitHub CLI"),
	]
	path_parts = [job_env.get("PATH", "")]
	for d in gh_dirs:
		if d and os.path.isdir(d) and d not in path_parts[0]:
			path_parts.insert(0, d)
	job_env["PATH"] = os.pathsep.join(p for p in path_parts if p)

	pushover(
		"Local agent START for Monday ticket %s: %s\nLog: %s"
		% (item_id, ticket.get("title") or "", log_path.name),
		title="Monday→Agent START",
	)

	def _run() -> None:
		t0 = time.time()
		sys.stderr.write("agent spawn item=%s cmd=%s\n" % (item_id, cmd_path))
		try:
			with log_path.open("w", encoding="utf-8", errors="replace") as logf:
				logf.write("CMD: %s\n\n" % " ".join(cmd[:8] + ["<prompt>"]))
				logf.flush()
				proc = subprocess.run(
					cmd,
					cwd=str(REPO_ROOT),
					stdout=logf,
					stderr=subprocess.STDOUT,
					text=True,
					encoding="utf-8",
					errors="replace",
					env=job_env,
				)
				elapsed = int(time.time() - t0)
				logf.write("\n\nEXIT=%s ELAPSED_SEC=%s\n" % (proc.returncode, elapsed))

			ok = proc.returncode == 0
			status = "OK" if ok else "FAIL(%s)" % proc.returncode
			log_text = ""
			try:
				log_text = log_path.read_text(encoding="utf-8", errors="replace")
			except OSError:
				pass
			artifacts = parse_agent_artifacts(log_text, str(item_id))
			review: dict | None = None

			if ok:
				# Move to Pending Review + Monday update (leave item on failure)
				try:
					review = post_success_review(ticket, log_path)
					# Refresh artifacts from review (disk may have handoff after agent)
					if review.get("artifacts"):
						artifacts = {**artifacts, **review["artifacts"]}
					with log_path.open("a", encoding="utf-8") as logf:
						logf.write(
							"\nREVIEW_HOOKS: moved=%s group=%s update_id=%s "
							"file_update=%s file_column=%s errors=%s\n"
							% (
								review.get("moved"),
								review.get("group_id"),
								review.get("update_id"),
								review.get("file_update_asset_id"),
								review.get("file_column_asset_id"),
								review.get("errors"),
							)
						)
				except Exception as rev_exc:  # noqa: BLE001
					sys.stderr.write(
						"post_success_review error item=%s err=%s\n" % (item_id, rev_exc)
					)
					review = {"errors": [str(rev_exc)], "moved": False}

			pushover(
				format_finish_pushover(
					status=status,
					ticket=ticket,
					elapsed=elapsed,
					artifacts=artifacts,
					review=review if ok else None,
				),
				title="Monday→Agent FINISH",
			)
		except Exception as exc:  # noqa: BLE001
			sys.stderr.write("agent job error item=%s err=%s\n" % (item_id, exc))
			try:
				with log_path.open("a", encoding="utf-8") as logf:
					logf.write("\nEXCEPTION: %s\n" % exc)
			except OSError:
				pass
			# Failure: leave Monday item where it is; Pushover only
			pushover(
				"Local agent ERROR for Monday ticket %s: %s\n(left on current Monday group; not on main)"
				% (item_id, exc),
				title="Monday→Agent ERROR",
			)

	thread = threading.Thread(target=_run, name="monday-agent-%s" % item_id, daemon=True)
	thread.start()
	meta["thread"] = thread.name
	return meta


def handle_webhook_payload(payload: dict, *, dry_run: bool = False) -> dict:
	"""Full pipeline step for one webhook body (after challenge handled)."""
	result = evaluate_ticket(payload, enrich=True)
	sys.stderr.write(
		"monday filter skip=%s reason=%s item=%s\n"
		% (
			result.get("skip"),
			result.get("reason"),
			(result.get("ticket") or {}).get("item_id"),
		)
	)
	if result.get("skip") or not result.get("ticket"):
		if result.get("notify") and result.get("ticket"):
			notify_non_dylan_ticket(result["ticket"], reason=str(result.get("reason") or ""))
		return {
			"ok": True,
			"skipped": True,
			"reason": result.get("reason"),
			"ticket": result.get("ticket"),
		}

	job = spawn_agent_job(result["ticket"], dry_run=dry_run)
	return {
		"ok": True,
		"skipped": False,
		"reason": result.get("reason"),
		"ticket": result["ticket"],
		"job": {k: v for k, v in job.items() if k != "thread"},
	}


def _synthetic_item(
	*,
	name: str,
	reporter: str = "",
	email: str = "",
	description: str = "",
	creator_id: str = "111292620",
	creator_name: str = "Dylan Jones",
	creator_email: str = "djones@oneshotautomation.net",
	url: str = "",
) -> dict:
	cols = [
		{"id": "text", "text": reporter, "type": "text"},
	]
	if email:
		cols.append({"id": "email", "text": email, "type": "email"})
	if description:
		cols.append({"id": "long_text7", "text": description, "type": "long_text"})
	return {
		"id": "synthetic",
		"name": name,
		"url": url or "https://monday.com/boards/1/pulses/1",
		"creator": {"id": creator_id, "name": creator_name, "email": creator_email},
		"column_values": cols,
		"updates": [],
	}


def self_test() -> int:
	"""Dry-run filter checks without spawning the agent."""
	load_dotenv()
	failures = 0

	def _check( Cond: bool, label: str, detail: str = "") -> None:
		nonlocal failures
		if Cond:
			sys.stderr.write("PASS: %s — %s\n" % (label, detail))
		else:
			sys.stderr.write("FAIL: %s — %s\n" % (label, detail))
			failures += 1

	# 1) Manual Monday create by Dylan (no Employee Name) → accept via userId
	r1 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999001",
				"pulseName": "Manual Dylan ticket",
				"userId": 111292620,
				"userName": "Dylan Jones",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(name="Manual Dylan ticket", reporter=""),
	)
	_check(not r1["skip"], "accept manual Dylan userId", r1["reason"])

	# 2) Ticket Logger: Tylor Slack but API creator = Dylan token → REJECT
	tylor_desc = (
		"Tag Path: Evaporators/EV-01\n"
		"Created By: Tylor Slack\n\n"
		"Expected Result:\nmodes"
	)
	r2 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "12652699666",
				"pulseName": "Evaporators/EV-01/Status/Value",
				"userId": 111292620,
				"userName": "Dylan Jones",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(
			name="Evaporators/EV-01/Status/Value",
			reporter="Tylor Slack",
			description=tylor_desc,
			creator_id="111292620",
			creator_name="Dylan Jones",
			creator_email="djones@oneshotautomation.net",
		),
	)
	_check(
		r2["skip"] and r2.get("notify"),
		"reject Tylor despite Dylan API creator",
		r2["reason"],
	)

	# 3) Ticket Logger: Dylan Jones reporter → accept (ignore that userId also Dylan)
	r3 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999003",
				"pulseName": "Dylan HMI ticket",
				"userId": 111292620,
				"userName": "Dylan Jones",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(
			name="Dylan HMI ticket",
			reporter="Dylan Jones",
			email="djones@oneshotautomation.net",
			description="Created By: Dylan Jones\nExpected Result:\nok",
		),
	)
	_check(not r3["skip"], "accept Dylan Employee Name", r3["reason"])

	# 4) Ticket Logger: dylan.jones email only → accept
	r4 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999004",
				"pulseName": "Email-only Dylan",
				"userId": 111292620,
				"userName": "Dylan Jones",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(
			name="Email-only Dylan",
			reporter="",
			email="dylan.jones@hbtech.com",
			description="Created By: \nExpected Result:\nok",
		),
	)
	_check(not r4["skip"], "accept Dylan email column", r4["reason"])

	# 5) Title containing dylan.jones must NOT accept when filer is someone else
	r5 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999005",
				"pulseName": "Created By: dylan.jones — fake",
				"userId": 42,
				"userName": "Alice Example",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(
			name="Created By: dylan.jones — fake",
			reporter="Alice Example",
			creator_id="42",
			creator_name="Alice Example",
			creator_email="alice@example.com",
		),
	)
	_check(r5["skip"], "reject title substring trap", r5["reason"])

	# 6) Plain other user manual create → reject
	r6 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999006",
				"pulseName": "Unrelated ticket",
				"userId": 42,
				"userName": "Alice Example",
				"boardId": 18423731526,
			}
		},
		enrich=False,
		item_override=_synthetic_item(
			name="Unrelated ticket",
			reporter="",
			creator_id="42",
			creator_name="Alice Example",
			creator_email="alice@example.com",
		),
	)
	_check(r6["skip"], "reject other manual user", r6["reason"])

	# 7) Challenge-shape should not parse as create
	r7 = parse_create_item({"challenge": "abc"})
	_check(r7 is None, "challenge not treated as create", "")

	# 8) parse_created_by — same-line only (not next heading)
	_check(
		parse_created_by(tylor_desc) == "Tylor Slack",
		"parse_created_by Tylor",
		parse_created_by(tylor_desc),
	)
	_check(
		parse_created_by("Created By: \nExpected Result:\nok") == "",
		"parse_created_by empty same-line",
		repr(parse_created_by("Created By: \nExpected Result:\nok")),
	)

	# 9) parse_agent_artifacts extracts branch + PR + handoff path
	sample_log = (
		"Created branch ticket/999777-demo-fix\n"
		"Wrote docs/handoff/ticket-999777.md\n"
		"Draft PR: https://github.com/example/Bors/pull/42\n"
	)
	arts = parse_agent_artifacts(sample_log, "999777")
	_check(
		arts.get("branch") == "ticket/999777-demo-fix",
		"parse branch from log",
		str(arts.get("branch")),
	)
	_check(
		"pull/42" in (arts.get("pr_url") or ""),
		"parse draft PR from log",
		str(arts.get("pr_url")),
	)
	_check(
		arts.get("handoff") == "docs/handoff/ticket-999777.md",
		"parse handoff path from log",
		str(arts.get("handoff")),
	)

	# 10) FINISH message mentions not on main
	finish = format_finish_pushover(
		status="OK",
		ticket={"item_id": "999777", "title": "Demo"},
		elapsed=12,
		artifacts=arts,
		review={"moved": True, "group_id": DEFAULT_PENDING_REVIEW_GROUP_ID},
	)
	_check("NOT on main" in finish, "finish pushover says not on main", finish[:200])
	_check("ticket/999777-demo-fix" in finish, "finish pushover has branch", finish[:200])

	# 11) Pending Review group id: env override wins
	os.environ["MONDAY_PENDING_REVIEW_GROUP_ID"] = "group_from_env"
	_check(
		resolve_pending_review_group_id(DEFAULT_BOARD_ID) == "group_from_env",
		"env overrides pending review group",
		resolve_pending_review_group_id(DEFAULT_BOARD_ID),
	)
	del os.environ["MONDAY_PENDING_REVIEW_GROUP_ID"]

	# 12) Default fallback when API unavailable / no match
	# (resolve without override should return default or live title match)
	gid = resolve_pending_review_group_id(DEFAULT_BOARD_ID)
	_check(
		bool(gid),
		"resolve pending review group id",
		"group_id=%s" % gid,
	)

	# 13) Review update body embeds handoff when file not attached
	inline_body = build_review_update_body(
		{"item_id": "999777", "title": "Demo"},
		arts,
		handoff_markdown="# Hello handoff\n\nDetails here.",
		file_attached=False,
	)
	_check(
		"Hello handoff" in inline_body and "file attach failed" in inline_body.lower(),
		"inline handoff fallback in update body",
		inline_body[-120:],
	)
	attached_body = build_review_update_body(
		{"item_id": "999777", "title": "Demo"},
		arts,
		handoff_markdown="# Hello handoff\n\nDetails here.",
		file_attached=True,
	)
	_check(
		"Hello handoff" not in attached_body
		and "Attached Files" in attached_body,
		"attached flag skips inline handoff",
		attached_body[:240],
	)

	sys.stderr.write("self_test failures=%s token_present=%s\n" % (failures, bool(monday_api_token())))
	return 1 if failures else 0


if __name__ == "__main__":
	load_dotenv()
	if "--self-test" in sys.argv:
		raise SystemExit(self_test())
	print("Use monday_webhook_proxy.py or: python scripts/monday_agent_job.py --self-test")
	raise SystemExit(0)
