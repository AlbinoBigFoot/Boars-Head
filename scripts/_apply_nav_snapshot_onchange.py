# -*- coding: utf-8 -*-
"""Apply snapshot-first hybrid onChange — never walk live Tree props on collapse."""
import json
from pathlib import Path

p = Path(
    r"gateways/standard/data/projects/BH/com.inductiveautomation.perspective/"
    r"views/00_Pages/00_Docked/Navigation/view.json"
)
bh = json.loads(p.read_text(encoding="utf-8"))


def find(n, name):
    if n.get("meta", {}).get("name") == name:
        return n
    for c in n.get("children") or []:
        r = find(c, name)
        if r:
            return r
    return None


# Snapshot-first: encode live items once, walk/mutate ONLY the copy.
# Collapse early-outs when no expanded+Loading exists on the snapshot.
onchange = """\t# 8.3 may report expand/collapse as Script; Lightspeed used Browser-only.
\tif str(origin) not in ('Browser', 'Script'):
\t\treturn
\tis_admin = False
\ttry:
\t\tis_admin = bool(self.session.custom.Administrator)
\texcept:
\t\tpass
\timport json
\t# Snapshot FIRST — never walk live Tree props during collapse (crashes 8.3)
\ttry:
\t\traw_json = system.util.jsonEncode(self.props.items)
\t\tworking_tree = json.loads(raw_json)
\texcept:
\t\treturn
\tdef needs_upgrade(nodes):
\t\tif nodes is None:
\t\t\treturn False
\t\ttry:
\t\t\tn = len(nodes)
\t\texcept Exception:
\t\t\treturn False
\t\tfor i in range(n):
\t\t\ttry:
\t\t\t\tnode = nodes[i]
\t\t\texcept Exception:
\t\t\t\tcontinue
\t\t\texpanded = False
\t\t\ttry:
\t\t\t\texpanded = bool(node.get(\"expanded\"))
\t\t\texcept Exception:
\t\t\t\tpass
\t\t\titems_array = node.get(\"items\") or []
\t\t\tif expanded and len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0].get(\"label\", \"\"))
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text == \"Loading...\":
\t\t\t\t\treturn True
\t\t\t# Recurse hydrated children (even if collapsed); never into Loading...
\t\t\tif len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0].get(\"label\", \"\"))
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text != \"Loading...\":
\t\t\t\t\tif needs_upgrade(items_array):
\t\t\t\t\t\treturn True
\t\treturn False
\tif not needs_upgrade(working_tree):
\t\treturn
\tdef upgrade_dummies(nodes, path_tracker):
\t\tif nodes is None:
\t\t\treturn False
\t\tfor i in range(len(nodes)):
\t\t\tnode = nodes[i]
\t\t\tcurrent_path = path_tracker + [i]
\t\t\texpanded = bool(node.get(\"expanded\", False))
\t\t\titems_array = node.get(\"items\") or []
\t\t\tif expanded and len(items_array) > 0:
\t\t\t\tlabel_text = str(items_array[0].get(\"label\", \"\"))
\t\t\t\tif label_text == \"Loading...\":
\t\t\t\t\treal_children = Navigation.Nav.getChildrenAt(current_path, is_admin)
\t\t\t\t\tif real_children and len(real_children) > 0:
\t\t\t\t\t\tnode[\"items\"] = real_children
\t\t\t\t\t\treturn True
\t\t\tif len(items_array) > 0:
\t\t\t\tlabel_text = str(items_array[0].get(\"label\", \"\"))
\t\t\t\tif label_text != \"Loading...\":
\t\t\t\t\tif upgrade_dummies(items_array, current_path):
\t\t\t\t\t\treturn True
\t\treturn False
\tif upgrade_dummies(working_tree, []):
\t\tself.props.items = working_tree
"""

assert onchange.startswith("\t") and "\r" not in onchange
assert "jsonEncode" in onchange
assert "needs_upgrade(working_tree)" in onchange
assert "not in ('Browser', 'Script')" in onchange

tree = find(bh["root"], "Tree")
tree["propConfig"]["props.items"]["onChange"] = {"enabled": None, "script": onchange}

text = json.dumps(bh, indent=2, ensure_ascii=False) + "\n"
text = text.replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
json.loads(p.read_text(encoding="utf-8"))
print("OK: snapshot-first onChange")
