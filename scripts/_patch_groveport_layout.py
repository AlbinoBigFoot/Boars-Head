#!/usr/bin/env python3
"""Tighten Groveport Site Overview flex layout (no stretch / nested scrollbars)."""
from __future__ import annotations

import re
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts/_build_groveport_site_dashboard.py"
src = path.read_text(encoding="utf-8")

new_meter = r'''def _meter_area_row(area: str, tag_root_expr: str) -> dict:
    """One metering placeholder row for a Groveport area."""
    safe = area.replace(" ", "")
    base = f"{tag_root_expr} + '/ComingOnline/Metering/{area}'"
    return {
        "type": "ia.container.flex",
        "meta": {"name": f"Meter{safe}"},
        "position": {"basis": "32px", "shrink": 0, "grow": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "flex-start",
            "style": {
                "classes": "kpi-coming-meter-row",
                "gap": "8px",
                "width": "100%",
                "maxWidth": "420px",
                "padding": "3px 0",
                "borderBottom": "1px solid rgba(0,0,0,0.06)",
                "overflow": "hidden",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Area"},
                "position": {"grow": 0, "basis": "110px", "shrink": 0},
                "props": {
                    "text": area,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "13px",
                        "width": "110px",
                        "minWidth": "110px",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "whiteSpace": "nowrap",
                    },
                },
            },
            _expr_label(
                "Status",
                f"coalesce(try(if(isBadOrError(tag({base} + '/Status')), null, tag({base} + '/Status')), null), 'Planned')",
                classes="font-label",
                fontSize="12px",
                opacity="0.8",
                width="70px",
                minWidth="70px",
                textAlign="left",
            ),
            _expr_label(
                "Kwh",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({base} + '/kWh')), null, tag({base} + '/kWh')), null), 0), '#,##0')",
                fontSize="13px",
                fontWeight="600",
                width="56px",
                minWidth="56px",
                textAlign="right",
            ),
            {
                "type": "ia.display.label",
                "meta": {"name": "KwhUnit"},
                "position": {"grow": 0, "shrink": 0},
                "props": {
                    "text": "kWh",
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "opacity": "0.65",
                        "width": "28px",
                    },
                },
            },
            _expr_label(
                "Therm",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({base} + '/Therm')), null, tag({base} + '/Therm')), null), 0), '#,##0')",
                fontSize="13px",
                fontWeight="600",
                width="40px",
                minWidth="40px",
                textAlign="right",
            ),
            {
                "type": "ia.display.label",
                "meta": {"name": "ThermUnit"},
                "position": {"grow": 0, "shrink": 0},
                "props": {
                    "text": "therm",
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "opacity": "0.65",
                        "width": "36px",
                    },
                },
            },
        ],
    }


'''

src2, n = re.subn(
    r"def _meter_area_row\(area: str, tag_root_expr: str\) -> dict:.*?\n\ndef _linebreak_block",
    new_meter + "def _linebreak_block",
    src,
    count=1,
    flags=re.S,
)
print("meter replace", n)
if n != 1:
    raise SystemExit("meter replace failed")

replacements = [
    (
        '''            "style": {
                "classes": "kpi-domain-panel",
                "gap": "14px",
                "padding": "16px 18px 20px",
                "width": "100%",
                "height": "100%",
                "overflow": "auto",
                "boxSizing": "border-box",
                "minHeight": "0",
            },''',
        '''            "style": {
                "classes": "kpi-domain-panel",
                "gap": "10px",
                "padding": "12px 14px 14px",
                "width": "100%",
                "height": "100%",
                "overflowX": "hidden",
                "overflowY": "auto",
                "boxSizing": "border-box",
                "minHeight": "0",
                "justifyContent": "flex-start",
                "alignContent": "flex-start",
            },''',
    ),
    (
        '''                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {
                        "gap": "10px",
                        "width": "100%",
                        "alignItems": "stretch",
                    },
                },
                "children": pens,''',
        '''                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {
                        "gap": "8px",
                        "width": "100%",
                        "alignItems": "flex-start",
                        "justifyContent": "flex-start",
                    },
                },
                "children": pens,''',
    ),
    (
        '''            "style": {
                "classes": "kpi-domain-subsection",
                "gap": "8px",
                "padding": "12px 12px 10px",
                "width": "100%",
                "boxSizing": "border-box",
            },''',
        '''            "style": {
                "classes": "kpi-domain-subsection",
                "gap": "6px",
                "padding": "10px 12px",
                "width": "100%",
                "maxWidth": "100%",
                "boxSizing": "border-box",
                "overflow": "hidden",
                "flexShrink": "0",
            },''',
    ),
    (
        '''                "meta": {"name": "ColA"},
                "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                "props": {"direction": "column", "style": {"gap": "0", "minWidth": "260px"}},
                "children": rows[:mid],
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "ColB"},
                "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                "props": {"direction": "column", "style": {"gap": "0", "minWidth": "260px"}},
                "children": rows[mid:],
            },''',
        '''                "meta": {"name": "ColA"},
                "position": {"grow": 0, "shrink": 1, "basis": "auto"},
                "props": {
                    "direction": "column",
                    "style": {"gap": "0", "minWidth": "280px", "maxWidth": "440px", "overflow": "hidden"},
                },
                "children": rows[:mid],
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "ColB"},
                "position": {"grow": 0, "shrink": 1, "basis": "auto"},
                "props": {
                    "direction": "column",
                    "style": {"gap": "0", "minWidth": "280px", "maxWidth": "440px", "overflow": "hidden"},
                },
                "children": rows[mid:],
            },''',
    ),
    (
        '''        "meta": {"name": f"Block{name}"},
        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
        "props": {
            "direction": "column",
            "style": {"gap": "6px", "minWidth": "0", "padding": "8px 10px", "classes": "kpi-coming-subcard"},
        },''',
        '''        "meta": {"name": f"Block{name}"},
        "position": {"grow": 0, "shrink": 0, "basis": "260px"},
        "props": {
            "direction": "column",
            "style": {
                "gap": "6px",
                "minWidth": "240px",
                "maxWidth": "320px",
                "width": "280px",
                "padding": "8px 10px",
                "classes": "kpi-coming-subcard",
                "overflow": "hidden",
            },
        },''',
    ),
    (
        '''        "meta": {"name": name},
        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border kpi-coming-chart",
                "gap": "6px",
                "padding": "12px 14px 8px",
                "minWidth": "min(100%, 280px)",
                "overflow": "hidden",
            },
        },''',
        '''        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0, "basis": "auto"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border kpi-coming-chart",
                "gap": "6px",
                "padding": "10px 12px 8px",
                "width": "100%",
                "maxWidth": "720px",
                "overflow": "hidden",
                "flexShrink": "0",
            },
        },''',
    ),
    (
        '''                "meta": {"name": "Chart"},
                "position": {"grow": 1, "basis": "160px", "shrink": 1},''',
        '''                "meta": {"name": "Chart"},
                "position": {"grow": 0, "basis": "160px", "shrink": 0},''',
    ),
    (
        '''                "classes": "kpi-dashboard-chart-card",
                "gap": "6px",
                "padding": "0",
                "minWidth": "0",
                "width": "100%",
                "overflow": "hidden",
            },''',
        '''                "classes": "kpi-dashboard-chart-card",
                "gap": "4px",
                "padding": "0",
                "minWidth": "0",
                "width": "100%",
                "maxWidth": "100%",
                "overflow": "hidden",
                "flexShrink": "0",
            },''',
    ),
]

for i, (a, b) in enumerate(replacements):
    if a not in src2:
        raise SystemExit(f"replacement {i} not found")
    src2 = src2.replace(a, b, 1)
    print("ok", i)

src2 = src2.replace("height=320,", "height=260,")

path.write_text(src2, encoding="utf-8")
compile(src2, str(path), "exec")
print("patched + syntax ok")
