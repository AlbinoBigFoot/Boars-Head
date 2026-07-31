# -*- coding: utf-8 -*-
"""Apply 8.3 hybrid Lightspeed-faithful Tree onChange (Browser|Script + snapshot)."""
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


# Hybrid: Browser|Script (8.3), Lightspeed fetch rules, snapshot assign only on upgrade.
onchange = """\t# 8.3 may report expand/collapse as Script; Lightspeed used Browser-only.
\tif str(origin) not in ('Browser', 'Script'):
\t\treturn
\tis_admin = False
\ttry:
\t\tis_admin = bool(self.session.custom.Administrator)
\texcept:
\t\tpass
\timport json
\t# Collapse safety: no-op unless some expanded folder still has Loading...
\tdef needs_upgrade(live_nodes):
\t\tif live_nodes is None:
\t\t\treturn False
\t\ttry:
\t\t\tn = len(live_nodes)
\t\texcept Exception:
\t\t\treturn False
\t\tfor i in range(n):
\t\t\ttry:
\t\t\t\tnode = live_nodes[i]
\t\t\texcept Exception:
\t\t\t\tcontinue
\t\t\texpanded = False
\t\t\ttry:
\t\t\t\texpanded = bool(node[\"expanded\"])
\t\t\texcept Exception:
\t\t\t\tpass
\t\t\titems_array = []
\t\t\ttry:
\t\t\t\titems_array = node[\"items\"]
\t\t\texcept Exception:
\t\t\t\tpass
\t\t\tif expanded and len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text == \"Loading...\":
\t\t\t\t\treturn True
\t\t\t# Recurse hydrated children (even if collapsed) looking for expanded+Loading
\t\t\tif len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text != \"Loading...\":
\t\t\t\t\tif needs_upgrade(items_array):
\t\t\t\t\t\treturn True
\t\treturn False
\tif not needs_upgrade(self.props.items):
\t\treturn
\t# Snapshot: mutate a clean copy, single push (avoids in-place Tree crash)
\traw_json = system.util.jsonEncode(self.props.items)
\tworking_tree = json.loads(raw_json)
\tdef upgrade_dummies(live_nodes, path_tracker):
\t\tif live_nodes is None:
\t\t\treturn False
\t\tfor i in range(len(live_nodes)):
\t\t\tnode = live_nodes[i]
\t\t\tcurrent_path = path_tracker + [i]
\t\t\texpanded = False
\t\t\ttry:
\t\t\t\texpanded = bool(node[\"expanded\"])
\t\t\texcept Exception:
\t\t\t\tpass
\t\t\titems_array = []
\t\t\ttry:
\t\t\t\titems_array = node[\"items\"]
\t\t\texcept Exception:
\t\t\t\tpass
\t\t\tif items_array is None:
\t\t\t\titems_array = []
\t\t\t# Fetch only when expanded folder still has Loading... dummy
\t\t\tif expanded and len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text == \"Loading...\":
\t\t\t\t\treal_children = Navigation.Nav.getChildrenAt(current_path, is_admin)
\t\t\t\t\tif real_children and len(real_children) > 0:
\t\t\t\t\t\tnode[\"items\"] = real_children
\t\t\t\t\t\treturn True
\t\t\t# Recurse hydrated children even if collapsed (never into Loading...)
\t\t\tif len(items_array) > 0:
\t\t\t\tlabel_text = \"\"
\t\t\t\ttry:
\t\t\t\t\tlabel_text = str(items_array[0][\"label\"])
\t\t\t\texcept Exception:
\t\t\t\t\tpass
\t\t\t\tif label_text != \"Loading...\":
\t\t\t\t\tif upgrade_dummies(items_array, current_path):
\t\t\t\t\t\treturn True
\t\treturn False
\tif upgrade_dummies(working_tree, []):
\t\tself.props.items = working_tree
"""

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
assert "Browser', 'Script'" in onchange or "('Browser', 'Script')" in onchange
assert "needs_upgrade" in onchange
assert "jsonEncode" in onchange
assert "self.props.items = working_tree" in onchange
assert tree_startup.startswith("\t") and "\r" not in tree_startup
assert "self.props.items = []" not in tree_startup

tree = find(bh["root"], "Tree")
assert tree is not None
tree["propConfig"]["props.items"]["onChange"] = {"enabled": None, "script": onchange}
tree["events"]["system"]["onStartup"] = {
    "config": {"script": tree_startup},
    "scope": "G",
    "type": "script",
}

seed_s = json.dumps(bh.get("custom", {}).get("items", []))
assert "Machine Room" in seed_s
handlers = (bh["root"].get("scripts") or {}).get("messageHandlers") or []
assert any(h.get("messageType") == "ticketLog" for h in handlers)

text = json.dumps(bh, indent=2, ensure_ascii=False) + "\n"
text = text.replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
json.loads(p.read_text(encoding="utf-8"))
print("OK: hybrid onChange written")
