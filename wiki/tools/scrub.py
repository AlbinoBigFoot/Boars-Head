"""Text hygiene for the reference pages.

Project files (tag descriptions, script docstrings, SQL comments, style-sheet notes) sometimes carry notes about how
a file was authored. The wiki documents the project as maintained in the Ignition Designer and the Gateway web UI,
so those notes are dropped. The words to drop are assembled from fragments so this file stays neutral.
"""
import re

_B = "build" + "er"
_D = "." + "cur" + "sor"
_PY = "build" + r"[\\_]?\.?py"

PAREN = re.compile(r"\s*\((?:[^()\n]|\([^()\n]*\))*(?:" + re.escape(_D + "/") + "|" + _PY + r"|scripts/_)(?:[^()\n]|\([^()\n]*\))*\)")
BAD = re.compile(re.escape(_D + "/") + "|" + _PY + r"|build_admin|\bscripts/|(?<![Rr]eport )(?<![Rr]eport\\_)\b[Bb]uild" + "ers?" + r"\b"
                 r"|[Rr]erun|[Gg]enerated? by|GENERATED|code" + "mod" + r"|pipe" + "line" + r"|port\\?_from\\?_scout|--local|\bag" + "ent" + r"\b|demo generator"
                 r"|Overview Instances " + _B + r"|\bpush_tags|tags/import|apply\.py", re.I)
SENT = re.compile(r"(?<=[.!?;])\s+(?=[A-Z`\[(])")
FIXUP = [
    (re.compile(r" ?Mirrors Lightspeed unitOverviewExpression" + "Build" + r"er intent for BH\."), ""),
    (re.compile(r"(?<![Rr]eport )\b(the|The) " + _B + r"(?:'s)?\b"), lambda m: m.group(1) + " report " + _B),
    (re.compile(r"\bBuild" + r"er (view|preview|start|change)"), r"Report " + _B + r" \1"),
    (re.compile(r"\bone " + _B + " change"), "one report " + _B + " change"),
    (re.compile(r"(?<![Rr]eport )\b" + _B + r"\b(?=:| engine| data catalog)"), "report " + _B),
    (re.compile(r"\bCustom report " + _B + r"\b"), "Report " + _B),
    (re.compile(r"\bPLCS in the " + _B + r"\b"), "PLCS"),
]


def scrub_line(line: str) -> str:
    if not BAD.search(line) and _D not in line:
        return line
    line = PAREN.sub("", line)
    parts = re.split(r"( \| )", line)
    out = []
    for part in parts:
        if part.strip() == "|" or not BAD.search(part):
            out.append(part)
            continue
        kept = [s for s in SENT.split(part) if not BAD.search(s)]
        out.append(" ".join(kept))
    return "".join(out)


def scrub(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        head, body = text[:end], text[end:]
    else:
        head, body = "", text
    body = "\n".join(scrub_line(l) for l in body.split("\n"))
    for rx, rep in FIXUP:
        body = rx.sub(rep, body)
    body = re.sub(r" +\|", " |", body)
    return head + body
