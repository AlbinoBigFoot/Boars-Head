# -*- coding: utf-8 -*-
"""Build Groveport KPI dashboard views, page-config routes, and nav EPMS/Utility/Production leaves."""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWS = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views"
)
PAGE_CONFIG = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/page-config/config.json"
)
NAV_VIEW = VIEWS / "00_Pages/00_Docked/Navigation/view.json"
TEMP_NAV = VIEWS / "00_Pages/00_Docked/TempNav/view.json"
TAGS = ROOT / (
    "gateways/standard/data/config/resources/core/"
    "ignition/tag-definition/default/_Config/tags.json"
)

AREAS = [
    ("Freezer", "freezer"),
    ("SuperChill", "superchill"),
    ("Club", "club"),
    ("Palletizing", "palletizing"),
    ("East PH", "east-ph"),
    ("West PH", "west-ph"),
    ("Dock", "dock"),
    ("Machine Room", "machine-room"),
]

# Use only material paths already proven elsewhere in the BH nav tree.
# bolt / water_drop / precision_manufacturing are absent from this gateway's
# material set — blank icons and Tree remount failures on collapse/expand.
DOMAINS = [
    ("EPMS", "epms", "material/show_chart"),
    ("Utility", "utility", "material/opacity"),
    ("Production", "production", "material/build"),
]

ZERO_SIG = "0" * 64


def resource_json() -> dict:
    return {
        "scope": "G",
        "version": 1,
        "restricted": False,
        "overridable": True,
        "files": ["view.json"],
        "attributes": {
            "lastModificationSignature": ZERO_SIG,
            "lastModification": {
                "actor": "external",
                "timestamp": "2026-08-20T18:00:00Z",
            },
        },
    }


def write_view(rel: str, view: dict) -> None:
    folder = VIEWS / rel
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "view.json").write_text(
        json.dumps(view, indent=2) + "\n", encoding="utf-8"
    )
    (folder / "resource.json").write_text(
        json.dumps(resource_json(), indent=2) + "\n", encoding="utf-8"
    )


def tag_value_expr(area_expr: str, domain: str, leaf: str, fmt: str = "#,##0.#") -> str:
    # area_expr is a Perspective expression fragment, e.g. {view.params.area}
    path = (
        f"'[default]KPI/Groveport/' + {area_expr} + '/{domain}/{leaf}'"
    )
    return (
        f"numberFormat(coalesce(try(if(isBadOrError(tag({path})), null, "
        f"tag({path})), null), 0), '{fmt}')"
    )


def metric_card_embed(name: str, category: str, title: str, unit: str, value_expr: str) -> dict:
    return {
        "type": "ia.display.view",
        "meta": {"name": name},
        "position": {"basis": "160px", "grow": 1, "shrink": 1},
        "props": {
            "path": "02_Components/02_Widgets/MetricCard",
            "params": {
                "category": category,
                "title": title,
                "unit": unit,
                "value": "—",
            },
            "style": {"minWidth": "220px", "maxWidth": "360px"},
        },
        "propConfig": {
            "props.params.value": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": value_expr},
                    "overlays": {
                        "bad": False,
                        "error": False,
                        "pending": False,
                        "stale": False,
                        "unknown": False,
                        "disabled": False,
                    },
                }
            }
        },
    }


def domain_view(domain: str, cards: list[tuple[str, str, str, str]]) -> dict:
    """cards: (name, title, unit, leaf) — leaf under domain folder."""
    children = [
        metric_card_embed(
            name=n,
            category=domain,
            title=t,
            unit=u,
            value_expr=tag_value_expr("{view.params.area}", domain, leaf),
        )
        for n, t, u, leaf in cards
    ]
    return {
        "custom": {},
        "params": {
            "area": {
                "paramType": "string",
                "dataType": "String",
                "defaultValue": "Freezer",
                "direction": "input",
            }
        },
        "propConfig": {
            "params.area": {"paramDirection": "input", "persistent": True}
        },
        "props": {"defaultSize": {"height": 480, "width": 1100}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "row",
                "wrap": "wrap",
                "style": {
                    "classes": "bg-page",
                    "gap": "12px",
                    "height": "100%",
                    "overflowY": "auto",
                    "padding": "4px",
                    "width": "100%",
                },
            },
            "children": children,
        },
    }


def area_dashboard() -> dict:
    return {
        "custom": {},
        "params": {
            "site": {
                "paramType": "string",
                "dataType": "String",
                "defaultValue": "Groveport",
                "direction": "input",
            },
            "area": {
                "paramType": "string",
                "dataType": "String",
                "defaultValue": "Freezer",
                "direction": "input",
            },
            "domain": {
                "paramType": "string",
                "dataType": "String",
                "defaultValue": "Utility",
                "direction": "input",
            },
        },
        "propConfig": {
            "params.site": {"paramDirection": "input", "persistent": True},
            "params.area": {"paramDirection": "input", "persistent": True},
            "params.domain": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 800, "width": 1400}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page",
                    "gap": "16px",
                    "height": "100%",
                    "overflow": "hidden",
                    "padding": "20px 24px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Title"},
                    "position": {"shrink": 0},
                    "props": {
                        "text": "Groveport KPI",
                        "style": {
                            "classes": "font-title",
                            "fontSize": "22px",
                            "fontWeight": "700",
                        },
                    },
                    "propConfig": {
                        "props.text": {
                            "binding": {
                                "type": "expr",
                                "config": {
                                    "expression": (
                                        "coalesce({view.params.site}, 'Groveport') + ' — ' + "
                                        "coalesce({view.params.area}, '') + ' — ' + "
                                        "coalesce({view.params.domain}, '')"
                                    )
                                },
                            }
                        }
                    },
                },
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Subtitle"},
                    "position": {"shrink": 0},
                    "props": {
                        "text": "Placeholder KPIs from Utility Tracker sample (memory tags).",
                        "style": {"classes": "font-label"},
                    },
                },
                {
                    "type": "ia.display.view",
                    "meta": {"name": "DomainBody"},
                    "position": {"grow": 1},
                    "props": {
                        "path": "00_Pages/Groveport/Domains/Utility",
                        "params": {"area": "Freezer"},
                        "style": {"height": "100%", "width": "100%"},
                    },
                    "propConfig": {
                        "props.path": {
                            "binding": {
                                "type": "expr",
                                "config": {
                                    "expression": (
                                        "case(lower(coalesce({view.params.domain}, 'utility')), "
                                        "'epms', '00_Pages/Groveport/Domains/EPMS', "
                                        "'utility', '00_Pages/Groveport/Domains/Utility', "
                                        "'production', '00_Pages/Groveport/Domains/Production', "
                                        "'00_Pages/Groveport/Domains/Utility')"
                                    )
                                },
                            }
                        },
                        "props.params.area": {
                            "binding": {
                                "type": "property",
                                "config": {"path": "view.params.area"},
                            }
                        },
                    },
                },
            ],
        },
    }


def site_overview() -> dict:
    # Site-level cards bound to KPI/Groveport/Site/...
    cards = [
        ("kWh", "EPMS", "Site kWh (MTD)", "kWh", "EPMS", "kWh"),
        ("Kvar", "EPMS", "Reactive", "kvar", "EPMS", "Kvar"),
        ("Therm", "Utility", "Natural Gas", "therm", "Utility", "Therm"),
        ("H2O", "Utility", "Water", "H2O", "Utility", "H2O"),
        ("Prod", "Production", "Production Volume", "lb", "Production", "ProdVol"),
        ("Temp", "Utility", "Outdoor Temp (avg)", "°F", "Utility", "AmbientAvgF"),
    ]
    children = []
    for name, cat, title, unit, domain, leaf in cards:
        expr = tag_value_expr("'Site'", domain, leaf)
        children.append(metric_card_embed(name, cat, title, unit, expr))
    return {
        "custom": {},
        "params": {
            "plantName": {
                "paramType": "string",
                "dataType": "String",
                "defaultValue": "Groveport",
                "direction": "input",
            }
        },
        "propConfig": {
            "params.plantName": {"paramDirection": "input", "persistent": True}
        },
        "props": {"defaultSize": {"height": 800, "width": 1400}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page",
                    "gap": "16px",
                    "height": "100%",
                    "overflowY": "auto",
                    "padding": "20px 24px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Title"},
                    "props": {
                        "text": "Groveport — Site KPI",
                        "style": {
                            "classes": "font-title",
                            "fontSize": "22px",
                            "fontWeight": "700",
                        },
                    },
                },
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Subtitle"},
                    "props": {
                        "text": "Site rollup placeholders (EPMS / Utility / Production).",
                        "style": {"classes": "font-label"},
                    },
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Cards"},
                    "props": {
                        "direction": "row",
                        "wrap": "wrap",
                        "style": {"gap": "12px", "width": "100%"},
                    },
                    "children": children,
                },
            ],
        },
    }


def domain_leaf(label: str, slug: str, area_label: str, icon_path: str) -> dict:
    domain_slug = next(dslug for dname, dslug, _ in DOMAINS if dname == label)
    page = f"/plants/groveport/{slug}/{domain_slug}"
    return {
        "label": label,
        "expanded": False,
        "icon": {
            "color": "",
            "path": icon_path,
            "style": {"classes": "", "height": "18px", "width": "18px"},
        },
        "data": {
            "action": "page",
            "page": page,
            "viewPath": "00_Pages/Groveport/Area/Dashboard",
            "tagPath": "",
        },
        "items": [],
    }


def inject_domains(items: list) -> int:
    """Prepend EPMS/Utility/Production under Groveport area nodes. Returns count of areas updated."""
    updated = 0
    area_names = {a[0] for a in AREAS}

    def walk(nodes, under_groveport=False):
        nonlocal updated
        for it in nodes or []:
            label = it.get("label")
            if label == "Groveport":
                walk(it.get("items") or [], under_groveport=True)
                continue
            if under_groveport and label in area_names:
                kids = it.setdefault("items", [])
                # remove existing domain leaves then prepend
                kids[:] = [
                    k
                    for k in kids
                    if k.get("label") not in ("EPMS", "Utility", "Production")
                ]
                slug = next(s for n, s in AREAS if n == label)
                prepend = [
                    domain_leaf(dname, slug, label, icon)
                    for dname, _dslug, icon in DOMAINS
                ]
                it["items"] = prepend + kids
                updated += 1
                # still walk children (CG rooms etc.) but not as groveport areas
                walk(kids, under_groveport=False)
            else:
                walk(it.get("items") or [], under_groveport=under_groveport)

    walk(items, False)
    return updated


def update_nav_file(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("custom", {}).get("items")
    if not items:
        raise SystemExit(f"No custom.items in {path}")
    n = inject_domains(items)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return n


def update_config_nav_tags() -> int:
    tags = json.loads(TAGS.read_text(encoding="utf-8"))
    nav = next(t for t in tags if t.get("name") == "Navigation")
    items = nav["defaultValue"]["items"]
    n = inject_domains(items)
    TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8")
    return n


def update_page_config() -> None:
    cfg = json.loads(PAGE_CONFIG.read_text(encoding="utf-8"))
    pages = cfg.setdefault("pages", {})
    pages["/plants/groveport"] = {
        "title": "Groveport",
        "viewPath": "00_Pages/Groveport/Site/Overview",
        "viewParams": {"plantName": "Groveport"},
    }
    for area_label, slug in AREAS:
        for dname, dslug, _icon in DOMAINS:
            route = f"/plants/groveport/{slug}/{dslug}"
            pages[route] = {
                "title": f"Groveport {area_label} {dname}",
                "viewPath": "00_Pages/Groveport/Area/Dashboard",
                "viewParams": {
                    "site": "Groveport",
                    "area": area_label,
                    "domain": dname,
                },
            }
    PAGE_CONFIG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    write_view(
        "00_Pages/Groveport/Domains/EPMS",
        domain_view(
            "EPMS",
            [
                ("kWh", "kWh (MTD)", "kWh", "kWh"),
                ("Kvar", "Reactive", "kvar", "Kvar"),
                ("Avg3", "3yr Month Avg", "kWh", "Avg3Yr"),
                ("Avg7", "7yr Month Avg", "kWh", "Avg7Yr"),
            ],
        ),
    )
    write_view(
        "00_Pages/Groveport/Domains/Utility",
        domain_view(
            "Utility",
            [
                ("Therm", "Natural Gas", "therm", "Therm"),
                ("H2O", "Water", "H2O", "H2O"),
                ("CO2", "CO₂", "tons", "CO2"),
                ("AmbAvg", "Outdoor Temp (avg)", "°F", "AmbientAvgF"),
                ("AmbMax", "Outdoor Temp (max)", "°F", "AmbientMaxF"),
            ],
        ),
    )
    write_view(
        "00_Pages/Groveport/Domains/Production",
        domain_view(
            "Production",
            [
                ("ProdVol", "Production Volume", "lb", "ProdVol"),
                ("ProdAvg", "7-day Avg Volume", "lb", "ProdVolAvg7d"),
                ("Intensity", "kWh / lb", "kWh/lb", "kWhPerLb"),
            ],
        ),
    )
    write_view("00_Pages/Groveport/Area/Dashboard", area_dashboard())
    write_view("00_Pages/Groveport/Site/Overview", site_overview())

    update_page_config()
    n1 = update_nav_file(NAV_VIEW)
    n2 = update_nav_file(TEMP_NAV) if TEMP_NAV.exists() else 0
    n3 = update_config_nav_tags()
    print(f"views written; page-config updated; nav areas: Navigation={n1} TempNav={n2} tags={n3}")


if __name__ == "__main__":
    main()
