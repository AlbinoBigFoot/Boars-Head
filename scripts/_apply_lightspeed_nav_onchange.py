# -*- coding: utf-8 -*-
"""Apply Lightspeed-faithful Tree props.items onChange + Tree onStartup."""
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


# Lightspeed-faithful props.items onChange (tab-indent Designer style).
# BH keeps is_admin for admin-only nodes; getChildrenAt already supports it.
onchange = """\t# THE SHIELD: Only run if a human clicked the expand arrow in the UI natively
\tif str(origin) == 'Browser':
\t\tis_admin = False
\t\ttry:
\t\t\tis_admin = bool(self.session.custom.Administrator)
\t\texcept:
\t\t\tpass
\t\t# Recursive visual scanner to update dummy nodes dynamically
\t\tdef upgrade_dummies(live_nodes, path_tracker):
\t\t\tif live_nodes is None:
\t\t\t\treturn
\t\t\tfor i in range(len(live_nodes)):
\t\t\t\tnode = live_nodes[i]
\t\t\t\tcurrent_path = path_tracker + [i]
\t\t\t\texpanded = False
\t\t\t\ttry:
\t\t\t\t\texpanded = bool(node[\"expanded\"])
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\titems_array = []
\t\t\t\ttry:
\t\t\t\t\titems_array = node[\"items\"]
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\t# Check for our Dummy Node in an expanded folder
\t\t\t\tif expanded and len(items_array) > 0:
\t\t\t\t\tlabel_text = \"\"
\t\t\t\t\ttry:
\t\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\t\texcept Exception:
\t\t\t\t\t\tpass
\t\t\t\t\t# Fetch from Cache and overwrite natively
\t\t\t\t\tif label_text == \"Loading...\":
\t\t\t\t\t\treal_children = Navigation.Nav.getChildrenAt(current_path, is_admin)
\t\t\t\t\t\tif real_children and len(real_children) > 0:
\t\t\t\t\t\t\tnode[\"items\"] = real_children
\t\t\t\t\t\t\treturn
\t\t\t\t# Recurse deeper into already-hydrated children (even if collapsed)
\t\t\t\tif len(items_array) > 0:
\t\t\t\t\tlabel_text = \"\"
\t\t\t\t\ttry:
\t\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\t\texcept Exception:
\t\t\t\t\t\tpass
\t\t\t\t\tif label_text != \"Loading...\":
\t\t\t\t\t\tupgrade_dummies(items_array, current_path)
\t\tupgrade_dummies(self.props.items, [])
"""

# Tree onStartup — Lightspeed root-layer only; keep BH is_admin + seedCache fallback
tree_startup = """\tis_admin = False
\ttry:
\t\tis_admin = bool(self.session.custom.Administrator)
\texcept:
\t\tpass
\t# Pass empty path to fetch only the Root layer (Loading... dummies)
\tinitial_tree = Navigation.Nav.getChildrenAt([], is_admin)
\tif not initial_tree:
\t\ttry:
\t\t\tseed = self.view.custom.items
\t\t\tNavigation.Nav.seedCacheFrom(seed)
\t\t\tinitial_tree = Navigation.Nav.getChildrenAt([], is_admin)
\t\texcept:
\t\t\tpass
\tif initial_tree:
\t\tself.props.items = initial_tree
"""

assert onchange.startswith("\t") and "\r" not in onchange
assert "str(origin) == 'Browser'" in onchange
assert "if not expanded" not in onchange
assert tree_startup.startswith("\t") and "\r" not in tree_startup
assert "self.props.items = initial_tree" in tree_startup
assert "self.props.items = []" not in tree_startup

tree = find(bh["root"], "Tree")
assert tree is not None
tree["propConfig"]["props.items"]["onChange"] = {"enabled": None, "script": onchange}
tree["events"]["system"]["onStartup"] = {
    "config": {"script": tree_startup},
    "scope": "G",
    "type": "script",
}

items = tree.get("props", {}).get("items", [])
assert len(items) >= 1
for it in items:
    kids = it.get("items") or []
    assert len(kids) == 1 and kids[0].get("label") == "Loading...", (
        "Tree props must be lazy stubs, got %r" % it.get("label")
    )

seed_s = json.dumps(bh.get("custom", {}).get("items", []))
assert "Machine Room" in seed_s

handlers = (bh["root"].get("scripts") or {}).get("messageHandlers") or []
assert any(h.get("messageType") == "ticketLog" for h in handlers)

text = json.dumps(bh, indent=2, ensure_ascii=False) + "\n"
text = text.replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
json.loads(p.read_text(encoding="utf-8"))

bh2 = json.loads(p.read_text(encoding="utf-8"))
tree2 = find(bh2["root"], "Tree")
oc = tree2["propConfig"]["props.items"]["onChange"]["script"]
st = tree2["events"]["system"]["onStartup"]["config"]["script"]
assert "\r" not in oc and "\r" not in st
assert oc.startswith("\t") and st.startswith("\t")
print("OK: Lightspeed-faithful onChange + Tree onStartup written")
print("onChange has Browser shield:", "str(origin) == 'Browser'" in oc)
print("onChange has skip-collapsed:", "if not expanded" in oc)
print("Tree startup assigns initial_tree:", "self.props.items = initial_tree" in st)
