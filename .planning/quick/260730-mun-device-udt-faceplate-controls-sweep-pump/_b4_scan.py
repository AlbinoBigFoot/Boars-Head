# -*- coding: utf-8 -*-
import json
import urllib.request
from pathlib import Path

cfg = json.loads(Path("docs/cloud-agent/ignition-scan.json").read_text(encoding="utf-8"))
url = cfg["scanProjectsUrl"]
token = cfg["apiToken"]
req = urllib.request.Request(
    url,
    data=b"{}",
    method="POST",
    headers={
        "Content-Type": "application/json",
        "X-Ignition-API-Token": token,
    },
)
with urllib.request.urlopen(req, timeout=60) as r:
    body = r.read().decode("utf-8", errors="replace")
    print("status", r.status)
    print(body[:800])
