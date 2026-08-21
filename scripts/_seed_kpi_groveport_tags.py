# Generate Groveport KPI placeholder memory tags from Utility Tracker seeds.
# Stdlib only. Run: python scripts/_seed_kpi_groveport_tags.py
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG_ROOT = (
    ROOT
    / "gateways/standard/data/config/resources/core/ignition/tag-definition/default/KPI"
)

AREAS = [
    "Site",
    "Freezer",
    "SuperChill",
    "Club",
    "Palletizing",
    "East PH",
    "West PH",
    "Dock",
    "Machine Room",
]

# Other BH plants get Site-level placeholders so home SiteCards bind cleanly.
OTHER_PLANTS = {
    "NewCastle": "New Castle",
    "ForrestCity": "Forrest City",
    "Petersburg": "Petersburg",
    "Holland": "Holland",
}

EPMS = [
    ("BillDate", "DateTime", "2024-01-05T00:00:00.000Z"),
    ("MonthLabel", "String", "January 24'"),
    ("kWh", "Float8", 595200.0),
    ("kWhActual", "Float8", 595200.0),
    ("Kvar", "Float8", 444.48),
    ("Kmax", "Float8", 0.0),
    ("Days", "Int4", 31),
    ("OpDays", "Int4", 0),
    ("Avg3Yr", "Float8", 614400.0),
    ("Avg7Yr", "Float8", 624960.0),
    ("High7Yr", "Float8", 660480.0),
    ("Low7Yr", "Float8", 595200.0),
]

UTILITY = [
    ("Therm", "Float8", 28450.0),
    ("H2O", "Float8", 1260.0),
    ("CO2", "Float8", 41200.0),
    ("AmbientAvgF", "Float8", 41.97),
    ("AmbientMaxF", "Float8", 78.0),
    ("AmbientMinF", "Float8", 15.0),
]

# Demo metering-by-area (status, kWh MTD, therm MTD)
METERING_DEMO = {
    "Freezer": ("Online", 84210.0, 2140.0),
    "SuperChill": ("Online", 61180.0, 1825.0),
    "Club": ("Online", 22140.0, 910.0),
    "Palletizing": ("Online", 18450.0, 420.0),
    "East PH": ("Online", 33420.0, 1180.0),
    "West PH": ("Online", 29780.0, 1095.0),
    "Dock": ("Planned", 0.0, 0.0),
    "Machine Room": ("Installing", 15220.0, 780.0),
}

PRODUCTION = [
    ("ProdVol", "Float8", 130031.08),
    ("ProdVolDate", "DateTime", "2023-12-29T00:00:00.000Z"),
    ("ProdVolAvg7d", "Float8", 125071.0),
    ("kWhPerLb", "Float8", 4.76),
]

DOMAINS = {
    "EPMS": EPMS,
    "Utility": UTILITY,
    "Production": PRODUCTION,
}

EMPTY_UNARY = {
    "scope": "G",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": [],
    "attributes": {"config": {}},
}

TAGS_UNARY = {
    "scope": "G",
    "version": 1,
    "restricted": False,
    "overridable": True,
    "files": ["tags.json"],
    "attributes": {"config": {}},
}


def atomic(name: str, data_type: str, value):
    return {
        "valueSource": "memory",
        "dataType": data_type,
        "name": name,
        "value": value,
        "defaultValue": value,
        "tagType": "AtomicTag",
    }


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")


def main():
    write_json(TAG_ROOT / "unary-resource.json", EMPTY_UNARY)
    grove = TAG_ROOT / "Groveport"
    write_json(grove / "unary-resource.json", EMPTY_UNARY)

    for area in AREAS:
        area_dir = grove / area
        write_json(area_dir / "unary-resource.json", EMPTY_UNARY)
        for domain, leaves in DOMAINS.items():
            ddir = area_dir / domain
            tags = [atomic(n, t, v) for n, t, v in leaves]
            if area == "Site" and domain == "EPMS":
                tags.append(atomic("ChartLengthMonths", "Int4", 36))
            write_json(ddir / "tags.json", tags)
            write_json(ddir / "unary-resource.json", TAGS_UNARY)

    # Coming-online demo values (metering, line-break restarts, YoY, Innovative)
    coming = grove / "Site" / "ComingOnline"
    write_json(
        coming / "tags.json",
        [
            atomic("MeteringCoveragePct", "Float8", 75.0),
            atomic("MeteringInstalledCount", "Int4", 6),
            atomic("MeteringPlannedCount", "Int4", 8),
            atomic("InnovativeStatus", "String", "Demo"),
            atomic("InnovativeInitiatives", "Int4", 3),
            atomic("InnovativeEstSavingsKwh", "Float8", 128400.0),
            atomic("InnovativePilotAreas", "String", "Freezer · Dock · Machine Room"),
        ],
    )
    write_json(coming / "unary-resource.json", TAGS_UNARY)

    metering = coming / "Metering"
    write_json(metering / "unary-resource.json", EMPTY_UNARY)
    for area in AREAS:
        if area == "Site":
            continue
        status, kwh, therm = METERING_DEMO.get(area, ("Planned", 0.0, 0.0))
        installed = status in ("Online", "Installing")
        meter_id = f"GP-{area.replace(' ', '').upper()[:6]}-01" if installed else ""
        adir = metering / area
        write_json(
            adir / "tags.json",
            [
                atomic("Installed", "Boolean", installed),
                atomic("Status", "String", status),
                atomic("MeterId", "String", meter_id),
                atomic("kWh", "Float8", kwh),
                atomic("Therm", "Float8", therm),
                atomic("H2O", "Float8", round(kwh * 0.004, 1) if kwh else 0.0),
            ],
        )
        write_json(adir / "unary-resource.json", TAGS_UNARY)

    linebreak = coming / "LineBreak"
    write_json(linebreak / "unary-resource.json", EMPTY_UNARY)
    # Excel Dashboard: Cascade Groveport baseline = October; Eneroi sites are enterprise
    for name, baseline, note, avg_min in (
        ("Cascade", "October", "Groveport", 18.4),
        ("Eneroi", "—", "Petersburg / Jarratt / Holland", 24.1),
    ):
        ldir = linebreak / name
        write_json(
            ldir / "tags.json",
            [
                atomic("RestartAvgMin", "Float8", avg_min),
                atomic("BaselineMonth", "String", baseline),
                atomic("SiteScope", "String", note),
                atomic("Status", "String", "Demo"),
            ],
        )
        write_json(ldir / "unary-resource.json", TAGS_UNARY)

    yoy = coming / "YoY"
    write_json(
        yoy / "tags.json",
        [
            atomic("kWhThisYear", "Float8", 6821400.0),
            atomic("kWhLastYear", "Float8", 7148200.0),
            atomic("ThermThisYear", "Float8", 318400.0),
            atomic("ThermLastYear", "Float8", 341200.0),
            atomic("ProdThisYear", "Float8", 1482100.0),
            atomic("ProdLastYear", "Float8", 1418800.0),
            atomic("Status", "String", "Demo"),
        ],
    )
    write_json(yoy / "unary-resource.json", TAGS_UNARY)

    # Site rollups for other plants (zeros / light placeholders for home cards)
    for folder, _label in OTHER_PLANTS.items():
        plant = TAG_ROOT / folder
        write_json(plant / "unary-resource.json", EMPTY_UNARY)
        site = plant / "Site"
        write_json(site / "unary-resource.json", EMPTY_UNARY)
        for domain, leaves in DOMAINS.items():
            ddir = site / domain
            # Placeholder zeros so gauges/pens don't error; Groveport keeps real seeds.
            tags = [atomic(n, t, 0 if t != "String" else "") for n, t, v in leaves if t != "DateTime"]
            tags.extend(
                [
                    atomic(n, t, v)
                    for n, t, v in leaves
                    if t == "DateTime"
                ]
            )
            write_json(ddir / "tags.json", tags)
            write_json(ddir / "unary-resource.json", TAGS_UNARY)

    print(f"seeded KPI tags under {TAG_ROOT}")


if __name__ == "__main__":
    main()
