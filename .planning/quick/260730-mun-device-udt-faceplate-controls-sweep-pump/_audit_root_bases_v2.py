"""Deeper pass: instance conflicts + Interlock atomics + inventory gaps."""
from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
DEVICES = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json"
TAG_DEF = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-definition/default"
TARGET = {
    "Pump": "Pumps",
    "ExhaustFan": "ExhaustFans",
    "Valve": "Valves",
    "Tank": "Tanks",
    "Sensor": "Sensors",
    "Evaporator": "Evaporators",
    "CoolingTower": "CoolingTowers",
    "Compressor": "Compressors",
}

INTENTIONAL_BOOL_PREFIXES = ("Cmd_",)
INTENTIONAL_BOOL_EXACT = {
    "OPER", "MAINT", "PROG", "AutoEN", "HMIEnable", "Cleanup",
}

devices = json.loads(DEVICES.read_text(encoding="utf-8"))
by_name = {u["name"]: u for u in devices}


def collect_udt_shape(udt):
    out = {}

    def walk(tags, prefix=""):
        for n in tags or []:
            p = f"{prefix}/{n['name']}" if prefix else n["name"]
            out[p] = {
                "tagType": n.get("tagType"),
                "typeId": n.get("typeId"),
                "dataType": n.get("dataType"),
                "valueSource": n.get("valueSource"),
                "engUnit": n.get("engUnit"),
                "states": (n.get("metadata") or {}).get("states"),
            }
            if n.get("tagType") == "Folder":
                walk(n.get("tags"), p)

    walk(udt.get("tags"))
    return out


def list_interlock_atomics(udt):
    findings = []
    for n in udt.get("tags") or []:
        if n.get("name") not in ("Interlock", "Interlocks") or n.get("tagType") != "Folder":
            continue
        for c in n.get("tags") or []:
            if c.get("tagType") == "AtomicTag":
                findings.append({
                    "path": f"Interlock/{c.get('name')}",
                    "dataType": c.get("dataType"),
                    "valueSource": c.get("valueSource"),
                    "engUnit": c.get("engUnit"),
                })
            elif c.get("tagType") == "Folder":
                for cc in c.get("tags") or []:
                    if cc.get("tagType") == "AtomicTag":
                        findings.append({
                            "path": f"Interlock/{c.get('name')}/{cc.get('name')}",
                            "dataType": cc.get("dataType"),
                            "valueSource": cc.get("valueSource"),
                        })
    return findings


def scan_instances(folder_name, udt_shape):
    path = TAG_DEF / folder_name / "udts.json"
    if not path.exists():
        return [], [], [], 0
    data = json.loads(path.read_text(encoding="utf-8"))
    conflicts = []
    amplifies = []
    odd_overrides = []
    root_members = {p: s for p, s in udt_shape.items() if "/" not in p}

    for inst in data:
        iname = inst.get("name", "?")

        def walk(tags, prefix=""):
            for n in tags or []:
                p = f"{prefix}/{n['name']}" if prefix else n["name"]
                tt = n.get("tagType")
                if tt == "AtomicTag":
                    if p in udt_shape and udt_shape[p].get("tagType") == "UdtInstance":
                        conflicts.append({
                            "instance": iname,
                            "path": p,
                            "instance_shape": f"AtomicTag {n.get('dataType')} vs={n.get('valueSource')}",
                            "udt_expects": f"{udt_shape[p]['tagType']} {udt_shape[p].get('typeId')}",
                        })
                    elif p in udt_shape and udt_shape[p].get("tagType") == "AtomicTag":
                        amplifies.append({
                            "instance": iname,
                            "path": p,
                            "instance_shape": (
                                f"AtomicTag {n.get('dataType')} vs={n.get('valueSource')} "
                                f"eng={n.get('engUnit')}"
                            ),
                        })
                elif tt == "Folder":
                    if n.get("name") in ("Interlock", "Interlocks"):
                        continue
                    walk(n.get("tags"), p)
                elif tt == "UdtInstance":
                    if p in udt_shape:
                        expected = udt_shape[p].get("typeId")
                        got = n.get("typeId")
                        if expected and got and expected != got:
                            odd_overrides.append({
                                "instance": iname,
                                "path": p,
                                "instance_shape": f"UdtInstance {got}",
                                "udt_expects": f"UdtInstance {expected}",
                            })
                    continue

        walk(inst.get("tags"))
    return conflicts, amplifies, odd_overrides, len(data)


result = {}
for tname, folder in TARGET.items():
    udt = by_name.get(tname)
    if not udt:
        result[tname] = {"error": "missing"}
        continue
    shape = collect_udt_shape(udt)
    interlock = list_interlock_atomics(udt)
    conflicts, amplifies, odd, ninst = scan_instances(folder, shape)

    intentional = []
    convert_candidates = []
    for p, s in sorted(shape.items()):
        if s["tagType"] != "AtomicTag":
            continue
        if p.startswith("Interlock/") or p.startswith("Interlocks/"):
            continue
        if "_Alarms" in p:
            continue
        leaf = p.split("/")[-1]
        if leaf.startswith(INTENTIONAL_BOOL_PREFIXES) or leaf in INTENTIONAL_BOOL_EXACT:
            intentional.append({
                "path": p,
                "dataType": s.get("dataType"),
                "valueSource": s.get("valueSource"),
                "engUnit": s.get("engUnit"),
                "reason": "Compressor golden: raw bool cmd/mode",
            })
            continue
        convert_candidates.append({
            "path": p,
            "dataType": s.get("dataType"),
            "valueSource": s.get("valueSource"),
            "engUnit": s.get("engUnit"),
            "states": s.get("states"),
        })

    root_ok = [
        {"path": p, **s}
        for p, s in sorted(shape.items())
        if s["tagType"] == "UdtInstance" and (s.get("typeId") or "").startswith("_Root/")
    ]
    non_root_inst = [
        {"path": p, **s}
        for p, s in sorted(shape.items())
        if s["tagType"] == "UdtInstance" and not (s.get("typeId") or "").startswith("_Root/")
    ]
    folders = [p for p, s in sorted(shape.items()) if s["tagType"] == "Folder"]

    amp_by_path = defaultdict(list)
    for a in amplifies:
        amp_by_path[a["path"]].append(a)
    conf_by_path = defaultdict(list)
    for c in conflicts:
        conf_by_path[c["path"]].append(c)

    # Only amplify paths that are convert candidates (or all atomics for report)
    convert_paths = {c["path"] for c in convert_candidates}
    intentional_paths = {c["path"] for c in intentional}

    result[tname] = {
        "root_ok": root_ok,
        "non_root_instances": non_root_inst,
        "folders": folders,
        "intentional_atomics": intentional,
        "convert_candidates": convert_candidates,
        "interlock_atomic_count": len(interlock),
        "interlock_sample": interlock[:12],
        "instance_conflicts_by_path": {
            path: {
                "count": len(items),
                "udt_expects": items[0]["udt_expects"],
                "sample": [
                    {"instance": i["instance"], "shape": i["instance_shape"]}
                    for i in items[:5]
                ],
            }
            for path, items in sorted(conf_by_path.items())
        },
        "instance_amplify_convert_paths": {
            path: {
                "count": len(items),
                "sample": [
                    {"instance": i["instance"], "shape": i["instance_shape"]}
                    for i in items[:5]
                ],
            }
            for path, items in sorted(amp_by_path.items())
            if path in convert_paths
        },
        "instance_amplify_intentional_paths": {
            path: {"count": len(items)}
            for path, items in sorted(amp_by_path.items())
            if path in intentional_paths
        },
        "odd_typeId_overrides": odd[:20],
        "instance_count_checked": ninst,
    }

out = ROOT / ".planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/_audit_root_bases_v2.json"
out.write_text(json.dumps(result, indent=2), encoding="utf-8")
print("Wrote", out)
for t, d in result.items():
    if "error" in d:
        print(t, d)
        continue
    print(
        f"{t}: root_ok={len(d['root_ok'])} convert={len(d['convert_candidates'])} "
        f"intentional={len(d['intentional_atomics'])} conflicts={len(d['instance_conflicts_by_path'])} "
        f"interlock_atomics={d['interlock_atomic_count']} non_root_udt={len(d['non_root_instances'])} "
        f"instances={d['instance_count_checked']}"
    )
    for c in d["convert_candidates"]:
        print(f"  CONVERT {c['path']}: {c['dataType']} eng={c.get('engUnit')}")
    for path, info in d["instance_conflicts_by_path"].items():
        print(f"  CONFLICT {path}: n={info['count']} expects={info['udt_expects']}")
    for path, info in d["instance_amplify_convert_paths"].items():
        print(f"  AMPLIFY {path}: n={info['count']} sample={info['sample'][:2]}")
