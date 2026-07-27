"""Deprecated alias — use scripts/repair-resource-signatures.py."""
from __future__ import annotations

import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(
        str(Path(__file__).resolve().parent / "repair-resource-signatures.py"),
        run_name="__main__",
    )
