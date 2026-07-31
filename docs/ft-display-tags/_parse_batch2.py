#!/usr/bin/env python3
"""Parse FactoryTalk display XMLs (batch 2) into JSONL — aligned with batch1 schema."""
from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

DISPLAYS_DIR = Path(r"C:\Users\dylan.jones\Documents\Bors\Displays")
OUT_PATH = Path(r"C:\Users\dylan.jones\Documents\Bors\docs\ft-display-tags\batch2.jsonl")

FILES = [
    "(RA-BAS) P_DIn-Help.xml",
    "(RA-BAS) P_DIn-Quick.xml",
    "(RA-BAS) P_DOut-Faceplate.xml",
    "(RA-BAS) P_DOut-Help.xml",
    "(RA-BAS) P_DOut-Quick.xml",
    "(RA-BAS) P_Intlk-Faceplate.xml",
    "(RA-BAS) P_IntlkPerm-Help.xml",
    "(RA-BAS) P_Mode-Config.xml",
    "(RA-BAS) P_Mode-Help.xml",
    "(RA-BAS) P_Motor-Help.xml",
    "(RA-BAS) P_Motor-Quick.xml",
    "(RA-BAS) P_Mruntime.xml",
    "(RA-BAS) P_Perm-Faceplate.xml",
    "(RA-BAS) P_PF753-Faceplate.xml",
    "(RA-BAS) P_PF753-Quick.xml",
    "(RA-BAS) P_PF755-Faceplate.xml",
    "(RA-BAS) P_PF755-Quick.xml",
]

# Absolute PLC tags {[RCP1]...}
ABS_TAG_RE = re.compile(r"\{(?:::+)?(?:/\*[^*]*\*/\s*)?\[([^\]]+)\]([^}]*)\}")
# Any brace expression
BRACE_RE = re.compile(r"\{[^{}]+\}")
# Parameter refs in expressions: #1, #102, {#1.Foo}, #1.Rdy_X
PARAM_IN_EXPR_RE = re.compile(r"#(\d+)")
PARAM_NAME_RE = re.compile(r"^#\d+$")
PLC_IN_DESC_RE = re.compile(r"\b(P_[A-Za-z0-9]+)\b")

# Expressions / attrs worth recording when they reference tags
TAGGISH_RE = re.compile(
    r"(?:\{[#\[]|#\d+\.|\{\[[^\]]+\])"
)


def unescape(s: str) -> str:
    if not s:
        return ""
    return html.unescape(s.replace("&#xA;", "\n"))


def resolved_from(expr: str) -> str:
    m = ABS_TAG_RE.search(expr or "")
    if not m:
        return ""
    return "{[%s]%s}" % (m.group(1), m.group(2).strip())


def primary_param(expr: str) -> str:
    """Pick primary #N from braced refs; prefer #1xx over bare digits when braced."""
    if not expr:
        return ""
    braced = BRACE_RE.findall(expr)
    for b in braced:
        nums = PARAM_IN_EXPR_RE.findall(b)
        if nums:
            # Prefer first number in brace (typically #1 for AOI instance)
            return "#" + nums[0]
    return ""


def plc_hint(display: str, desc: str = "", expr: str = "") -> str:
    m = PLC_IN_DESC_RE.search(desc or "")
    if m:
        return m.group(1)
    if "Screw_Compressor" in (desc or ""):
        return "Screw_Compressor"
    dm = re.search(r"\(RA-BAS\)\s+(P_[A-Za-z0-9]+)", display)
    if dm:
        return dm.group(1)
    return ""


def bh_component(display: str, hint: str, tag: str, desc: str) -> str:
    t = (tag or "").upper()
    hint_u = (hint or "").upper()
    desc_u = (desc or "").upper()
    blob = " ".join([hint_u, t, desc_u])

    # Absolute plant tags first (rare in this RA-BAS batch)
    if "SCREW_COMPRESSOR" in hint_u or re.search(r"COMP\[\d+\]", t):
        return "Compressor"
    if re.search(r"\{\[", tag or "") and ("PF753" in t or "PF755" in t or re.search(r"\bVSD\b", t)):
        return "VFD"
    if re.search(r"\{\[", tag or "") and ("VALVE" in t or "_CV" in t):
        return "Valve"
    if re.search(r"\{\[", tag or "") and ("PUMP" in t):
        return "ExhaustFan" if any(x in blob for x in ("FAN", "EEF", "EXHAUST")) else "Pump"
    if re.search(r"\{\[", tag or "") and re.search(r"\b(HTR|HPR|LTR|VESSEL|ACCUM)\b", t):
        return "Tank"
    if re.search(r"\{\[", tag or "") and ("EVAP" in t or "CG_" in t):
        return "Evaporator"

    # Library Faceplate / Quick / Help / Config → Faceplate (batch1 rule)
    if re.search(r"(Faceplate|Quick|Help|Config|Mruntime)", display, re.I):
        return "Faceplate"

    if "P_VALVE" in hint_u:
        return "Valve"
    if "P_MOTOR" in hint_u:
        return "ExhaustFan" if any(x in blob for x in ("FAN", "EEF", "EXHAUST")) else "Pump"
    if "P_AIN" in hint_u or "P_AOUT" in hint_u:
        return "Sensor"
    if "P_DIN" in hint_u or "P_DOUT" in hint_u:
        return "Tank" if any(x in blob for x in ("LEVEL", "HLCO", "LOLO", "HIHI")) else "Sensor"
    if "PF75" in hint_u or "P_VSD" in hint_u:
        return "VFD"
    return "Unknown"


def build_parents(root: ET.Element) -> dict:
    parents = {root: None}
    for p in root.iter():
        for c in list(p):
            parents[c] = p
    return parents


def nearest_meta(elem: ET.Element, parents: dict) -> tuple[str, str]:
    object_name = ""
    link_base = ""
    cur = parents.get(elem)
    while cur is not None:
        name = cur.attrib.get("name") or ""
        lb = cur.attrib.get("linkBaseObject") or ""
        if not object_name and name and cur.tag not in (
            "parameters", "animations", "connections", "animations", "ability", "confirm"
        ):
            object_name = name
        if not link_base and lb:
            link_base = unescape(lb)
        if object_name and link_base:
            break
        cur = parents.get(cur)
    return object_name, link_base


def element_path_tag(elem: ET.Element) -> str:
    return elem.tag


def parse_file(path: Path) -> list[dict]:
    display = path.stem
    text = path.read_text(encoding="utf-8", errors="replace")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        return [{
            "display": display,
            "object_name": "",
            "link_base": "",
            "parameter": "",
            "parameter_description": "",
            "tag_expression": "",
            "resolved_tag": "",
            "plc_type_hint": "",
            "bh_component": "Unknown",
            "notes": f"XML parse error: {e}",
        }]

    parents = build_parents(root)
    rows: list[dict] = []
    seen: set[tuple] = set()

    def add_row(
        object_name="",
        link_base="",
        parameter="",
        parameter_description="",
        tag_expression="",
        resolved_tag="",
        notes="",
        hint_override="",
    ):
        hint = hint_override or plc_hint(display, parameter_description, tag_expression)
        rtag = resolved_tag or resolved_from(tag_expression)
        bh = bh_component(display, hint, rtag or tag_expression, parameter_description)
        key = (
            display,
            object_name,
            link_base,
            parameter,
            rtag or tag_expression,
            notes,
        )
        if key in seen:
            return
        seen.add(key)
        rows.append({
            "display": display,
            "object_name": object_name,
            "link_base": link_base,
            "parameter": parameter,
            "parameter_description": parameter_description,
            "tag_expression": tag_expression,
            "resolved_tag": rtag,
            "plc_type_hint": hint,
            "bh_component": bh,
            "notes": notes,
        })

    def walk(elem: ET.Element):
        tag = elem.tag

        # --- parameters #N ---
        if tag == "parameter":
            pname = elem.attrib.get("name", "")
            if PARAM_NAME_RE.match(pname):
                # Focus #1xx per prompt; also keep #1 instance when value is taggish
                num = int(pname[1:])
                pdesc = unescape(elem.attrib.get("description", ""))
                pval = unescape(elem.attrib.get("value", ""))
                keep = False
                if 100 <= num <= 199:
                    keep = True
                elif num == 1 and (ABS_TAG_RE.search(pval) or BRACE_RE.search(pval) or re.search(r"#1[._]", pval)):
                    keep = True
                if keep:
                    obj, link = nearest_meta(elem, parents)
                    add_row(
                        object_name=obj,
                        link_base=link,
                        parameter=pname,
                        parameter_description=pdesc,
                        tag_expression=pval,
                        notes="parameter value",
                    )

        # --- connections ---
        if tag == "connection":
            expr = unescape(elem.attrib.get("expression", ""))
            cname = elem.attrib.get("name", "") or "connection"
            if expr and (ABS_TAG_RE.search(expr) or BRACE_RE.search(expr) or TAGGISH_RE.search(expr)):
                obj, link = nearest_meta(elem, parents)
                add_row(
                    object_name=obj,
                    link_base=link,
                    parameter=primary_param(expr),
                    tag_expression=expr,
                    notes=f"connection:{cname}",
                )

        # --- action tag= ---
        if tag == "action":
            atag = unescape(elem.attrib.get("tag", ""))
            if atag and (ABS_TAG_RE.search(atag) or BRACE_RE.search(atag)):
                obj, link = nearest_meta(elem, parents)
                add_row(
                    object_name=obj,
                    link_base=link,
                    parameter=primary_param(atag),
                    tag_expression=atag,
                    notes="attr:action.tag",
                )

        # --- animations ---
        if tag.startswith("animate"):
            expr = unescape(elem.attrib.get("expression", ""))
            if expr and (
                ABS_TAG_RE.search(expr)
                or BRACE_RE.search(expr)
                or re.search(r"#\d+\.", expr)
                or TAGGISH_RE.search(expr)
            ):
                obj, link = nearest_meta(elem, parents)
                # Match batch1: braced → fill parameter; bare #1.x visibility often blank param
                param = primary_param(expr) if BRACE_RE.search(expr) else ""
                add_row(
                    object_name=obj,
                    link_base=link,
                    parameter=param,
                    tag_expression=expr,
                    notes=f"attr:{tag}.expression",
                )
            # touch actions
            for act_attr in ("pressAction", "releaseAction", "repeatAction"):
                aval = unescape(elem.attrib.get(act_attr, ""))
                if aval and (ABS_TAG_RE.search(aval) or BRACE_RE.search(aval)):
                    obj, link = nearest_meta(elem, parents)
                    add_row(
                        object_name=obj,
                        link_base=link,
                        parameter=primary_param(aval),
                        tag_expression=aval,
                        notes=f"attr:{tag}.{act_attr}",
                    )

        # --- button command actions ---
        if tag == "command":
            for act_attr in ("pressAction", "releaseAction", "repeatAction"):
                aval = unescape(elem.attrib.get(act_attr, ""))
                if aval and (ABS_TAG_RE.search(aval) or BRACE_RE.search(aval) or re.search(r"#1\.", aval)):
                    obj, link = nearest_meta(elem, parents)
                    add_row(
                        object_name=obj,
                        link_base=link,
                        parameter=primary_param(aval),
                        tag_expression=aval,
                        notes=f"attr:command.{act_attr}",
                    )

        # --- captions / tooltips with tag refs ---
        if tag in (
            "text", "button", "image", "multistateIndicator", "numericDisplay",
            "numericInput", "stringDisplay", "stringInput", "group", "rectangle",
            "panel", "polygon", "activeX",
        ):
            caption = unescape(elem.attrib.get("caption", ""))
            if caption and (ABS_TAG_RE.search(caption) or BRACE_RE.search(caption)):
                obj, link = nearest_meta(elem, parents)
                # object itself may have the name
                oname = elem.attrib.get("name") or obj
                lbase = unescape(elem.attrib.get("linkBaseObject", "")) or link
                add_row(
                    object_name=oname,
                    link_base=lbase,
                    parameter=primary_param(caption),
                    tag_expression=caption,
                    notes=f"attr:{tag}.caption",
                )
            tip = unescape(elem.attrib.get("toolTipText", ""))
            if tip and (ABS_TAG_RE.search(tip) or BRACE_RE.search(tip)):
                obj, link = nearest_meta(elem, parents)
                oname = elem.attrib.get("name") or obj
                lbase = unescape(elem.attrib.get("linkBaseObject", "")) or link
                add_row(
                    object_name=oname,
                    link_base=lbase,
                    parameter=primary_param(tip),
                    tag_expression=tip,
                    notes=f"attr:{tag}.toolTipText",
                )

        # --- readFromTagExpressionRange ---
        if tag == "readFromTagExpressionRange":
            for attr in ("minTag", "maxTag"):
                aval = unescape(elem.attrib.get(attr, ""))
                if aval and (ABS_TAG_RE.search(aval) or BRACE_RE.search(aval) or TAGGISH_RE.search(aval)):
                    obj, link = nearest_meta(elem, parents)
                    add_row(
                        object_name=obj,
                        link_base=link,
                        parameter=primary_param(aval),
                        tag_expression=aval,
                        notes=f"attr:readFromTagExpressionRange.{attr}",
                    )

        for child in list(elem):
            walk(child)

    walk(root)
    return rows


def main() -> None:
    all_rows: list[dict] = []
    per_file: list[tuple[str, int]] = []
    for fname in FILES:
        path = DISPLAYS_DIR / fname
        if not path.exists():
            print("MISSING:", fname)
            continue
        rows = parse_file(path)
        per_file.append((fname, len(rows)))
        all_rows.extend(rows)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="\n") as f:
        for row in all_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print("Wrote", len(all_rows), "rows ->", OUT_PATH)
    for name, n in per_file:
        print(f"  {n:5d}  {name}")
    abs_n = sum(1 for r in all_rows if r["resolved_tag"])
    print("absolute resolved_tag rows:", abs_n)


if __name__ == "__main__":
    main()
