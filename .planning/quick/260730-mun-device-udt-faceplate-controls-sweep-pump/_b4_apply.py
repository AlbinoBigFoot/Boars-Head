# -*- coding: utf-8 -*-
"""B4: Faceplate deviceType routing + device openers + thin wrappers + stub Controls."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BH = ROOT / "gateways/standard/data/projects/BH"
FP_DIR = BH / "com.inductiveautomation.perspective/views/01_Popups/00_Faceplates"
DEVICES = BH / "com.inductiveautomation.perspective/views/02_Components/01_Devices"
ASSETS = FP_DIR / "_Assets"

DEVICE_TYPES = [
    "Compressor",
    "Pump",
    "ExhaustFan",
    "Valve",
    "Tank",
    "Sensor",
    "Evaporator",
    "CoolingTower",
]

# graphic view name -> deviceType for unified Faceplate
OPENERS = {
    "Pump": "Pump",
    "ExhaustFan": "ExhaustFan",
    "CoolingTower": "CoolingTower",
    "Evaporator": "Evaporator",
    "EvaporatorDual": "Evaporator",
    "EvaporatorTriple": "Evaporator",
    "Tank": "Tank",
    "Sensor": "Sensor",
    "SolenoidValve": "Valve",
    "SolenoidValve3Way": "Valve",
}

# legacy faceplate wrappers to thin-embed Faceplate (nav stable paths)
WRAPPERS = {
    "Pump": "Pump",
    "ExhaustFan": "ExhaustFan",
    "CoolingTower": "CoolingTower",
    "Evaporator": "Evaporator",
    "Tank": "Tank",
    "Sensor": "Sensor",
    "SolenoidValve": "Valve",
    "SolenoidValve3Way": "Valve",
}


def opener_script(device_type: str, popup_prefix: str, allow_empty_faceplate: bool = False) -> str:
    """Tab-indented Perspective event script opening unified Faceplate."""
    # Mirror Compressor gate: None or blank => no open (except Pump/ExhaustFan which treat '' as self.name historically).
    # After migration we always open Faceplate when faceplate is set; empty string also opens (Overview always sets name).
    lines = [
        "faceplate = self.view.params.faceplate",
        "if faceplate is None or str(faceplate).strip() == '':",
        "\treturn",
        "tagPath = str(self.view.params.tagPath or '')",
        "title = str(self.view.custom.label or '')",
        "if title in (None, '', 'nn'):",
        "\ttitle = tagPath.split('/')[-1] if tagPath else self.view.name",
        "# Unified tabbed Faceplate. show* are hints; tagFlags hide empty tabs.",
        "params = {",
        "\t'tagPath': tagPath,",
        f"\t'deviceType': '{device_type}',",
        "\t'webGuiUrl': '',",
        "\t'showControls': True,",
        "\t'showConfiguration': True,",
        "\t'showInterlocks': True,",
        "\t'showTrend': True,",
        "\t'showAlarmConfiguration': True,",
        "\t'showAlarms': True",
        "}",
        "Navigation.Faceplate.openFaceplate(",
        f"\t'{popup_prefix}-fp-%s' % (tagPath or title),",
        "\ttagPath,",
        "\t'01_Popups/00_Faceplates/Faceplate',",
        "\tFalse,",
        "\ttitle,",
        "\t560,",
        "\t640,",
        "\tparams",
        ")",
    ]
    # Sensor historically also rejected 'SNS' titles — keep title fallback only
    return "\t" + "\n\t".join(lines) + "\n"


def thin_wrapper_view(device_type: str, include_web_gui: bool = False) -> dict:
    """Compressor-style thin wrapper embedding Faceplate with hardcoded deviceType."""
    params = {"tagPath": ""}
    prop_config = {
        "params.tagPath": {"paramDirection": "input", "persistent": True},
    }
    embed_params = {
        "tagPath": "",
        "deviceType": device_type,
        "webGuiUrl": "",
        "showControls": True,
        "showConfiguration": True,
        "showTrend": True,
        "showAlarmConfiguration": True,
        "showAlarms": True,
        "showInterlocks": True,
    }
    embed_prop_config = {
        "props.params.tagPath": {
            "binding": {"config": {"path": "view.params.tagPath"}, "type": "property"}
        },
        "props.params.showInterlocks": {
            "binding": {
                "config": {"path": "view.params.showInterlocks"},
                "type": "property",
            }
        },
    }
    params["showInterlocks"] = True
    prop_config["params.showInterlocks"] = {
        "paramDirection": "input",
        "persistent": True,
    }
    if include_web_gui:
        params["webGuiUrl"] = "https://127.0.0.1/"
        prop_config["params.webGuiUrl"] = {
            "paramDirection": "input",
            "persistent": True,
        }
        embed_prop_config["props.params.webGuiUrl"] = {
            "binding": {
                "config": {"path": "view.params.webGuiUrl"},
                "type": "property",
            }
        }

    ticket_code = (
        "\ttagPath = ''\n"
        "\ttry:\n"
        "\t\ttagPath = self.view.params.tagPath\n"
        "\texcept:\n"
        "\t\tpass\n"
        "\tif tagPath is None or str(tagPath).strip() == '':\n"
        "\t\ttagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]\n"
        "\titems = [\n"
        "\t\t\t  {\n"
        '\t\t\t    "text": "Ticket Logger",\n'
        '\t\t\t    "icon": {\n'
        '\t\t\t      "path": "material/info",\n'
        '\t\t\t      "color": "--neutral-80",\n'
        '\t\t\t      "style": {}\n'
        "\t\t\t    },\n"
        '\t\t\t    "style": {\n'
        '\t\t\t      "classes": "bg-component font-value",\n'
        '\t\t\t      "height": 24,\n'
        '\t\t\t      "width": 120\n'
        "\t\t\t    },\n"
        '\t\t\t    "type": "message",\n'
        '\t\t\t    "children": [],\n'
        '\t\t\t    "link": {\n'
        '\t\t\t      "url": "",\n'
        '\t\t\t      "target": "self"\n'
        "\t\t\t    },\n"
        '\t\t\t    "method": {\n'
        '\t\t\t      "name": "",\n'
        '\t\t\t      "params": {}\n'
        "\t\t\t    },\n"
        '\t\t\t    "message": {\n'
        '\t\t\t      "type": "ticketLog",\n'
        '\t\t\t      "payload": {\n'
        '\t\t\t        "tagPath": tagPath,\n'
        '\t\t\t        "viewName": self.view.id.split(\'@\')[0]\n'
        "\t\t\t      },\n"
        '\t\t\t      "scope": "page"\n'
        "\t\t\t    }\n"
        "\t\t\t  }\n"
        "\t\t\t]\n"
        "\treturn items"
    )

    return {
        "custom": {},
        "params": params,
        "propConfig": prop_config,
        "props": {"defaultSize": {"height": 640, "width": 560}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root", "contextMenu": {}},
            "props": {
                "direction": "column",
                "style": {
                    "height": "100%",
                    "width": "100%",
                    "minHeight": 0,
                    "overflow": "hidden",
                    "padding": "0px",
                },
            },
            "children": [
                {
                    "type": "ia.display.view",
                    "meta": {"name": "FaceplateShell"},
                    "position": {"grow": 1, "shrink": 1, "basis": "0px"},
                    "propConfig": embed_prop_config,
                    "props": {
                        "params": embed_params,
                        "path": "01_Popups/00_Faceplates/Faceplate",
                        "style": {
                            "height": "100%",
                            "width": "100%",
                            "minHeight": 0,
                        },
                        "useDefaultViewHeight": False,
                        "useDefaultViewWidth": False,
                    },
                }
            ],
            "propConfig": {
                "meta.contextMenu.items": {
                    "binding": {
                        "config": {
                            "struct": {"tagPath": '"No TagPath: "'},
                            "waitOnAll": True,
                        },
                        "transforms": [{"code": ticket_code, "type": "script"}],
                        "type": "expr-struct",
                    }
                },
                "meta.contextMenu.enabled": {
                    "binding": {
                        "config": {
                            "struct": {
                                "items": "{this.meta.contextMenu.items}",
                                "permission": "{session.custom.TicketLogAccess}",
                            },
                            "waitOnAll": True,
                        },
                        "transforms": [
                            {
                                "expression": "len({value}['items']) > 0 && {value}['permission']",
                                "type": "expression",
                            }
                        ],
                        "type": "expr-struct",
                    }
                },
            },
            "scripts": {
                "customMethods": [],
                "extensionFunctions": None,
                "messageHandlers": [
                    {
                        "messageType": "ticketLog",
                        "pageScope": True,
                        "script": "\t# Ticket Logger context-menu opener\n\tshared.Alerts.contextMenuTicketLog(payload['tagPath'], payload['viewName'])",
                        "sessionScope": False,
                        "viewScope": False,
                    }
                ],
            },
        },
    }


def stub_controls_view() -> dict:
    """Minimal Status Controls so Faceplate does not View-Not-Found."""
    ticket_code = (
        "\ttagPath = ''\n"
        "\ttry:\n"
        "\t\ttagPath = self.view.params.tagPath\n"
        "\texcept:\n"
        "\t\tpass\n"
        "\tif tagPath is None or str(tagPath).strip() == '':\n"
        "\t\ttagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]\n"
        "\titems = [\n"
        "\t\t\t  {\n"
        '\t\t\t    "text": "Ticket Logger",\n'
        '\t\t\t    "icon": {\n'
        '\t\t\t      "path": "material/info",\n'
        '\t\t\t      "color": "--neutral-80",\n'
        '\t\t\t      "style": {}\n'
        "\t\t\t    },\n"
        '\t\t\t    "style": {\n'
        '\t\t\t      "classes": "bg-component font-value",\n'
        '\t\t\t      "height": 24,\n'
        '\t\t\t      "width": 120\n'
        "\t\t\t    },\n"
        '\t\t\t    "type": "message",\n'
        '\t\t\t    "children": [],\n'
        '\t\t\t    "link": {"url": "", "target": "self"},\n'
        '\t\t\t    "method": {"name": "", "params": {}},\n'
        '\t\t\t    "message": {\n'
        '\t\t\t      "type": "ticketLog",\n'
        '\t\t\t      "payload": {\n'
        '\t\t\t        "tagPath": tagPath,\n'
        '\t\t\t        "viewName": self.view.id.split(\'@\')[0]\n'
        "\t\t\t      },\n"
        '\t\t\t      "scope": "page"\n'
        "\t\t\t    }\n"
        "\t\t\t  }\n"
        "\t\t\t]\n"
        "\treturn items"
    )
    return {
        "custom": {},
        "params": {"tagPath": ""},
        "propConfig": {
            "params.tagPath": {"paramDirection": "input", "persistent": True}
        },
        "props": {"defaultSize": {"height": 400, "width": 520}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root", "contextMenu": {}},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "faceplate-section",
                    "gap": "12px",
                    "padding": "12px",
                    "overflowY": "auto",
                    "height": "100%",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "StatusSection"},
                    "props": {
                        "direction": "column",
                        "style": {
                            "classes": "faceplate-section-card",
                            "gap": "8px",
                            "padding": "12px",
                        },
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "StatusTitle"},
                            "props": {
                                "text": "Status",
                                "style": {"classes": "faceplate-section-title"},
                            },
                        },
                        {
                            "type": "ia.display.view",
                            "meta": {"name": "Status"},
                            "propConfig": {
                                "props.params.tagPath": {
                                    "binding": {
                                        "config": {
                                            "expression": "if({view.params.tagPath}='','',{view.params.tagPath}+'/Status')"
                                        },
                                        "type": "expr",
                                    }
                                }
                            },
                            "props": {
                                "path": "02_Components/00_General/StatusIndicator",
                                "params": {"tagPath": ""},
                                "useDefaultViewHeight": False,
                                "useDefaultViewWidth": False,
                                "style": {"width": "100%"},
                            },
                        },
                    ],
                }
            ],
            "propConfig": {
                "meta.contextMenu.items": {
                    "binding": {
                        "config": {
                            "struct": {"tagPath": '"No TagPath: "'},
                            "waitOnAll": True,
                        },
                        "transforms": [{"code": ticket_code, "type": "script"}],
                        "type": "expr-struct",
                    }
                },
                "meta.contextMenu.enabled": {
                    "binding": {
                        "config": {
                            "struct": {
                                "items": "{this.meta.contextMenu.items}",
                                "permission": "{session.custom.TicketLogAccess}",
                            },
                            "waitOnAll": True,
                        },
                        "transforms": [
                            {
                                "expression": "len({value}['items']) > 0 && {value}['permission']",
                                "type": "expression",
                            }
                        ],
                        "type": "expr-struct",
                    }
                },
            },
            "scripts": {
                "customMethods": [],
                "extensionFunctions": None,
                "messageHandlers": [
                    {
                        "messageType": "ticketLog",
                        "pageScope": True,
                        "script": "\t# Ticket Logger context-menu opener\n\tshared.Alerts.contextMenuTicketLog(payload['tagPath'], payload['viewName'])",
                        "sessionScope": False,
                        "viewScope": False,
                    }
                ],
            },
        },
    }


def stub_resource() -> dict:
    return {
        "scope": "G",
        "version": 1,
        "restricted": False,
        "overridable": True,
        "files": ["view.json"],
        "attributes": {
            "lastModificationSignature": "0" * 64,
            "lastModification": {
                "actor": "external",
                "timestamp": "2026-07-30T21:00:00Z",
            },
        },
    }


def patch_faceplate() -> None:
    path = FP_DIR / "Faceplate" / "view.json"
    text = path.read_text(encoding="utf-8")

    old_has = "hasControlsAsset = str(deviceType or '') in ('Compressor', '')"
    new_has = (
        "hasControlsAsset = str(deviceType or '') in ("
        "'Compressor', 'Pump', 'ExhaustFan', 'Valve', 'Tank', 'Sensor', "
        "'Evaporator', 'CoolingTower', '')"
    )
    if old_has not in text:
        raise SystemExit(f"hasControlsAsset pattern not found in {path}")
    text = text.replace(old_has, new_has, 1)

    # Faceplate stores expression strings with escaped \n and \"
    old_case = (
        'case({view.params.deviceType},\\n'
        '      \\"Compressor\\", \\"01_Popups/00_Faceplates/_Assets/Compressor/Controls\\",\\n'
        '      \\"01_Popups/00_Faceplates/_Assets/Compressor/Controls\\"),'
    )
    new_case = (
        'case({view.params.deviceType},\\n'
        '      \\"Compressor\\", \\"01_Popups/00_Faceplates/_Assets/Compressor/Controls\\",\\n'
        '      \\"Pump\\", \\"01_Popups/00_Faceplates/_Assets/Pump/Controls\\",\\n'
        '      \\"ExhaustFan\\", \\"01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls\\",\\n'
        '      \\"Valve\\", \\"01_Popups/00_Faceplates/_Assets/Valve/Controls\\",\\n'
        '      \\"Tank\\", \\"01_Popups/00_Faceplates/_Assets/Tank/Controls\\",\\n'
        '      \\"Sensor\\", \\"01_Popups/00_Faceplates/_Assets/Sensor/Controls\\",\\n'
        '      \\"Evaporator\\", \\"01_Popups/00_Faceplates/_Assets/Evaporator/Controls\\",\\n'
        '      \\"CoolingTower\\", \\"01_Popups/00_Faceplates/_Assets/CoolingTower/Controls\\",\\n'
        '      \\"01_Popups/00_Faceplates/_Assets/Compressor/Controls\\"),'
    )
    if old_case not in text:
        raise SystemExit(f"Controls case() pattern not found in {path}")
    text = text.replace(old_case, new_case, 1)

    # Web GUI verify (must remain compressor-only)
    web = "{view.params.deviceType} = 'Compressor' && len(coalesce({view.params.webGuiUrl}, '')) > 0"
    if web not in text:
        raise SystemExit("Web GUI visibility expression missing or changed — abort")

    path.write_text(text, encoding="utf-8", newline="\n")
    print("Faceplate shell updated")


def _replace_onclick_script(view_path: Path, new_script: str) -> None:
    """Replace root onClick script via JSON round-trip of that key only when possible.

    Prefer surgical replace of the existing script string value to avoid reformatting
    the whole device graphic JSON.
    """
    data = json.loads(view_path.read_text(encoding="utf-8"))
    events = data.get("root", {}).get("events", {}).get("dom", {}).get("onClick")
    if not events or events.get("type") != "script":
        raise SystemExit(f"No onClick script on {view_path}")
    old_script = events["config"]["script"]
    raw = view_path.read_text(encoding="utf-8")
    # Encode like json.dumps string content (escape control + quotes)
    old_json = json.dumps(old_script)
    new_json = json.dumps(new_script)
    # old_json includes surrounding quotes
    if old_json not in raw:
        # Fallback: full rewrite of view (Tank may use unicode escapes)
        events["config"]["script"] = new_script
        view_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return
    view_path.write_text(raw.replace(old_json, new_json, 1), encoding="utf-8", newline="\n")


def patch_openers() -> None:
    prefixes = {
        "Pump": "pump",
        "ExhaustFan": "efan",
        "CoolingTower": "ct",
        "Evaporator": "ev",
        "EvaporatorDual": "ev",
        "EvaporatorTriple": "ev",
        "Tank": "tank",
        "Sensor": "sensor",
        "SolenoidValve": "sv",
        "SolenoidValve3Way": "sv",
    }
    for name, dtype in OPENERS.items():
        view_path = DEVICES / name / "view.json"
        if not view_path.is_file():
            print(f"SKIP missing device view: {name}")
            continue
        script = opener_script(dtype, prefixes[name])
        if name == "Sensor":
            script = script.replace(
                "if title in (None, '', 'nn'):",
                "if title in (None, '', 'nn', 'SNS'):",
            )
        _replace_onclick_script(view_path, script)
        print(f"Opener updated: {name} -> deviceType={dtype}")


def write_wrappers() -> None:
    for name, dtype in WRAPPERS.items():
        view_path = FP_DIR / name / "view.json"
        res_path = FP_DIR / name / "resource.json"
        view_path.parent.mkdir(parents=True, exist_ok=True)
        data = thin_wrapper_view(dtype, include_web_gui=False)
        view_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        if not res_path.is_file():
            res_path.write_text(
                json.dumps(stub_resource(), indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
        print(f"Thin wrapper: {name} -> deviceType={dtype}")


def ensure_stub_controls() -> None:
    stub = stub_controls_view()
    for dtype in DEVICE_TYPES:
        if dtype == "Compressor":
            continue
        cdir = ASSETS / dtype / "Controls"
        vpath = cdir / "view.json"
        rpath = cdir / "resource.json"
        if vpath.is_file():
            print(f"Controls exists (keep): {dtype}")
            continue
        cdir.mkdir(parents=True, exist_ok=True)
        vpath.write_text(
            json.dumps(stub, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        rpath.write_text(
            json.dumps(stub_resource(), indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(f"Stub Controls created: {dtype}")


def main() -> None:
    patch_faceplate()
    patch_openers()
    write_wrappers()
    ensure_stub_controls()
    print("B4 apply done")


if __name__ == "__main__":
    main()
