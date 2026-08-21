import re
from collections import Counter
from pathlib import Path

p = Path(
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/"
    "views/00_Pages/00_Docked/Navigation/view.json"
)
text = p.read_text(encoding="utf-8")
paths = re.findall(r'"path": "(material/[^"]+)"', text)
print("unique", len(set(paths)))
for x, c in Counter(paths).most_common(50):
    print(c, x)
