# one-shot: inspect Utility Tracker xlsx (stdlib only)
import zipfile, re, xml.etree.ElementTree as ET
from collections import defaultdict

path = r"docs/kpi/Utility Tracker_template.xlsx"
z = zipfile.ZipFile(path)
ss = []
if "xl/sharedStrings.xml" in z.namelist():
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    for si in root.findall("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si"):
        texts = [t.text or "" for t in si.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]
        ss.append("".join(texts))

wb = ET.fromstring(z.read("xl/workbook.xml"))
rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
rid_to_target = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
sheets = []
for s in wb.findall("m:sheets/m:sheet", NS):
    rid = s.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
    sheets.append((s.attrib["name"], "xl/" + rid_to_target[rid].lstrip("/")))


def colrow(cell_ref):
    m = re.match(r"([A-Z]+)(\d+)", cell_ref)
    return m.group(1), int(m.group(2))


def cell_value(c):
    t = c.attrib.get("t")
    v = c.find("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v")
    if v is None or v.text is None:
        return None
    if t == "s":
        return ss[int(v.text)]
    return v.text


for name, target in sheets:
    print("\n====", name, "====")
    root = ET.fromstring(z.read(target))
    rows = defaultdict(dict)
    for c in root.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c"):
        ref = c.attrib.get("r")
        if not ref:
            continue
        col, row = colrow(ref)
        rows[row][col] = cell_value(c)
    shown = 0
    for r in sorted(rows)[:100]:
        vals = [(c, rows[r][c]) for c in sorted(rows[r], key=lambda x: (len(x), x)) if rows[r][c] not in (None, "")]
        vals = [(c, v) for c, v in vals if len(c) == 1 or c.startswith("A") or c[0] <= "P"]
        if not vals:
            continue
        print(f"R{r}:", "; ".join(f"{c}={v}" for c, v in vals[:14]))
        shown += 1
        if shown >= 20:
            break
