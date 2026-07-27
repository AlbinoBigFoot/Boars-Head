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
	"""Return (matched, reason). Robust match for Dylan Jones / dylan.jones."""
	uid = _norm(user_id)
	if uid and uid in allowed_user_ids():
		return True, "user_id=%s" % uid

	blob = identity_blob(email, name, reporter, extra, uid)
	for needle in match_substrings():
		if needle and needle in blob:
			return True, "substring=%r in %r" % (needle, blob[:200])
	return False, "no match in %r" % (blob[:240] or "(empty)")


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


def evaluate_ticket(payload: dict, *, enrich: bool = True) -> dict:
	"""Parse webhook, optionally enrich via Monday API, apply Dylan filter.

	Returns dict with keys: ok, skip, reason, ticket, item.
	"""
	parsed = parse_create_item(payload)
	if not parsed:
		return {
			"ok": False,
			"skip": True,
			"reason": "not a create_item/create_pulse event (or missing item id)",
			"ticket": None,
			"item": None,
		}

	item: dict = {}
	if enrich and monday_api_token():
		try:
			item = fetch_item(parsed["item_id"])
		except Exception as exc:  # noqa: BLE001
			sys.stderr.write("monday enrich failed item=%s err=%s\n" % (parsed["item_id"], exc))

	creator = item.get("creator") if isinstance(item.get("creator"), dict) else {}
	reporter = column_text(item, "text")  # Employee Name
	email_col = column_text(item, "email")
	description = column_text(item, "long_text7")
	updates = item.get("updates") or []
	update_blob = " ".join(
		_norm(u.get("text_body") or u.get("body")) for u in updates if isinstance(u, dict)
	)

	user_id = parsed["user_id"] or _norm(creator.get("id"))
	email = _norm(creator.get("email")) or email_col
	name = parsed["user_name"] or _norm(creator.get("name"))

	matched, reason = is_dylan_match(
		user_id=user_id,
		email=email,
		name=name,
		reporter=reporter,
		extra=" ".join([description, update_blob, email_col, parsed["name"]]),
	)

	ticket = {
		**parsed,
		"creator_email": email,
		"creator_name": name,
		"reporter": reporter,
		"description": description,
		"url": _norm(item.get("url")),
		"title": _norm(item.get("name")) or parsed["name"],
	}

	if not matched:
		return {
			"ok": True,
			"skip": True,
			"reason": "skip non-dylan creator: %s" % reason,
			"ticket": ticket,
			"item": item,
		}

	return {
		"ok": True,
		"skip": False,
		"reason": "accept: %s" % reason,
		"ticket": ticket,
		"item": item,
	}


def build_agent_prompt(ticket: dict) -> str:
	template = ""
	if PROMPT_FILE.is_file():
		template = PROMPT_FILE.read_text(encoding="utf-8")
	else:
		template = (
			"Fix the Boars Head Ignition HMI issue described below. "
			"Read docs/cloud-agent/SUMMARY.md first. Create a branch, implement, "
			"scan, commit, open a draft PR (do not merge).\n\n"
		)
	body = {
		"monday_item_id": ticket.get("item_id"),
		"title": ticket.get("title"),
		"url": ticket.get("url"),
		"reporter": ticket.get("reporter"),
		"creator_name": ticket.get("creator_name"),
		"creator_email": ticket.get("creator_email"),
		"description": ticket.get("description"),
		"board_id": ticket.get("board_id"),
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
			status = "OK" if proc.returncode == 0 else "FAIL(%s)" % proc.returncode
			pushover(
				"Local agent %s for Monday ticket %s (%ss)\n%s"
				% (status, item_id, elapsed, ticket.get("title") or ""),
				title="Monday→Agent FINISH",
			)
		except Exception as exc:  # noqa: BLE001
			sys.stderr.write("agent job error item=%s err=%s\n" % (item_id, exc))
			try:
				with log_path.open("a", encoding="utf-8") as logf:
					logf.write("\nEXCEPTION: %s\n" % exc)
			except OSError:
				pass
			pushover(
				"Local agent ERROR for Monday ticket %s: %s" % (item_id, exc),
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


def self_test() -> int:
	"""Dry-run filter checks without spawning the agent."""
	load_dotenv()
	failures = 0

	# Accept Dylan by user id
	r1 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999001",
				"pulseName": "Test EV-01 fan",
				"userId": 111292620,
				"userName": "Dylan Jones",
				"boardId": 18423731526,
			}
		},
		enrich=False,
	)
	if r1["skip"]:
		sys.stderr.write("FAIL: expected accept for userId 111292620\n")
		failures += 1
	else:
		sys.stderr.write("PASS: accept userId — %s\n" % r1["reason"])

	# Accept by dylan.jones reporter-like name in pulse (no enrich)
	r2 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999002",
				"pulseName": "Created By: dylan.jones — CT water color",
				"userId": 1,
				"userName": "Someone Else",
				"boardId": 18423731526,
			}
		},
		enrich=False,
	)
	if r2["skip"]:
		sys.stderr.write("FAIL: expected accept for dylan.jones in pulseName\n")
		failures += 1
	else:
		sys.stderr.write("PASS: accept dylan.jones substring — %s\n" % r2["reason"])

	# Reject other user
	r3 = evaluate_ticket(
		{
			"event": {
				"type": "create_pulse",
				"pulseId": "999003",
				"pulseName": "Unrelated ticket",
				"userId": 42,
				"userName": "Alice Example",
				"boardId": 18423731526,
			}
		},
		enrich=False,
	)
	if not r3["skip"]:
		sys.stderr.write("FAIL: expected skip for Alice\n")
		failures += 1
	else:
		sys.stderr.write("PASS: skip other user — %s\n" % r3["reason"])

	# Challenge-shape should not parse as create
	r4 = parse_create_item({"challenge": "abc"})
	if r4 is not None:
		sys.stderr.write("FAIL: challenge should not parse as create\n")
		failures += 1
	else:
		sys.stderr.write("PASS: challenge not treated as create\n")

	sys.stderr.write("self_test failures=%s token_present=%s\n" % (failures, bool(monday_api_token())))
	return 1 if failures else 0


if __name__ == "__main__":
	load_dotenv()
	if "--self-test" in sys.argv:
		raise SystemExit(self_test())
	print("Use monday_webhook_proxy.py or: python scripts/monday_agent_job.py --self-test")
	raise SystemExit(0)
