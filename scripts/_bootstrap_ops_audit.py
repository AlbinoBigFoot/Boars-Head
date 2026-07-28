# -*- coding: utf-8 -*-
"""Bootstrap OPS Audit write path, Audit Log page, Control AnalogValue, Evap SP."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path("gateways/standard/data/projects/BH")
PERS = ROOT / "com.inductiveautomation.perspective"
IGN = ROOT / "ignition"

OPS_AUDIT_PROFILE = "OpsAudit"

TICKET_ITEMS_CODE = (
	"\ttagPath = ''\n"
	"\ttry:\n"
	"\t\ttagPath = self.view.params.tagPath\n"
	"\texcept:\n"
	"\t\tpass\n"
	"\tif tagPath is None or str(tagPath).strip() == '':\n"
	"\t\ttagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]\n"
	"\titems = [\n"
	"\t\t\t  {\n"
	"\t\t\t    \"text\": \"Ticket Logger\",\n"
	"\t\t\t    \"icon\": {\n"
	"\t\t\t      \"path\": \"material/info\",\n"
	"\t\t\t      \"color\": \"--neutral-80\",\n"
	"\t\t\t      \"style\": {}\n"
	"\t\t\t    },\n"
	"\t\t\t    \"style\": {\n"
	"\t\t\t      \"classes\": \"bg-component font-value\",\n"
	"\t\t\t      \"height\": 24,\n"
	"\t\t\t      \"width\": 120\n"
	"\t\t\t    },\n"
	"\t\t\t    \"type\": \"message\",\n"
	"\t\t\t    \"children\": [],\n"
	"\t\t\t    \"link\": {\n"
	"\t\t\t      \"url\": \"\",\n"
	"\t\t\t      \"target\": \"self\"\n"
	"\t\t\t    },\n"
	"\t\t\t    \"method\": {\n"
	"\t\t\t      \"name\": \"\",\n"
	"\t\t\t      \"params\": {}\n"
	"\t\t\t    },\n"
	"\t\t\t    \"message\": {\n"
	"\t\t\t      \"type\": \"ticketLog\",\n"
	"\t\t\t      \"payload\": {\n"
	"\t\t\t        \"tagPath\": tagPath,\n"
	"\t\t\t        \"viewName\": self.view.id.split('@')[0]\n"
	"\t\t\t      },\n"
	"\t\t\t      \"scope\": \"page\"\n"
	"\t\t\t    }\n"
	"\t\t\t  }\n"
	"\t\t\t]\n"
	"\treturn items"
)

TICKET_ENABLED_EXPR = "len({value}['items']) > 0 && {value}['permission']"

TICKET_HANDLER = {
	"messageType": "ticketLog",
	"pageScope": True,
	"script": "\t# Ticket Logger context-menu opener\n\tshared.Alerts.contextMenuTicketLog(payload['tagPath'], payload['viewName'])",
	"sessionScope": False,
	"viewScope": False,
}


def write_json(path: Path, data: dict) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(
		json.dumps(data, indent=2, ensure_ascii=False) + "\n",
		encoding="utf-8",
		newline="\n",
	)


def resource_json(files, *, scope="G", version=1, **attrs):
	attributes = {
		"lastModification": {
			"actor": "external",
			"timestamp": "2026-07-28T23:00:00Z",
		},
		**attrs,
	}
	# signature filled by repair script
	attributes.setdefault(
		"lastModificationSignature",
		"0" * 64,
	)
	return {
		"scope": scope,
		"version": version,
		"restricted": False,
		"overridable": True,
		"files": files,
		"attributes": attributes,
	}


def ticket_prop_config():
	return {
		"meta.contextMenu.items": {
			"binding": {
				"config": {
					"struct": {"tagPath": "\"No TagPath: \""},
					"waitOnAll": True,
				},
				"transforms": [{"code": TICKET_ITEMS_CODE, "type": "script"}],
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
					{"expression": TICKET_ENABLED_EXPR, "type": "expression"}
				],
				"type": "expr-struct",
			}
		},
	}


def write_audit_script_package():
	code = '''"""OPS Audit helpers for Perspective writable values.

Central write path for AnalogValue / Control Numeric (and later any
writable view field). Records into the OpsAudit profile table
ops_audit_events with every configured column populated.
"""

OPS_AUDIT_PROFILE = "OpsAudit"


def _status_code(quality):
	try:
		return int(quality.getCode())
	except Exception:
		try:
			return int(quality)
		except Exception:
			return 0


def writeTag(tagPath, value, label=None, viewName=None):
	"""Write a tag and log the change to OpsAudit.

	Parameters
	----------
	tagPath : str
		Full tag path to write.
	value : any
		New value.
	label : str, optional
		Human label for the audit action_target (defaults to tag leaf).
	viewName : str, optional
		Perspective view path for originating_system context.

	Returns
	-------
	dict
		{ok, oldValue, newValue, quality, statusCode}
	"""
	tagPath = str(tagPath or "").strip()
	if not tagPath:
		raise ValueError("tagPath is required")

	old_qv = system.tag.readBlocking([tagPath])[0]
	old_value = old_qv.value
	qualities = system.tag.writeBlocking([tagPath], [value])
	quality = qualities[0] if qualities else None
	ok = False
	try:
		ok = bool(quality.isGood())
	except Exception:
		ok = str(quality) in ("Good", "192")

	status = _status_code(quality) if quality is not None else 0
	leaf = tagPath.split("/")[-1]
	target = label if label not in (None, "") else tagPath
	action_value = "%s -> %s" % (old_value, value)

	origin = ["tagPath", tagPath, "tagName", leaf]
	if viewName:
		origin.extend(["view", str(viewName)])

	try:
		system.util.audit(
			action="tag write",
			actionTarget=str(target),
			actionValue=str(action_value),
			auditProfile=OPS_AUDIT_PROFILE,
			originatingSystem=origin,
			originatingContext=4,
			statusCode=status,
		)
	except Exception as ex:
		system.util.getLogger("shared.Audit").warn(
			"OpsAudit write failed for %s: %s" % (tagPath, ex)
		)

	return {
		"ok": ok,
		"oldValue": old_value,
		"newValue": value,
		"quality": quality,
		"statusCode": status,
	}
'''
	# Convert to tab-indented Ignition style for body of functions
	# (module-level docstring/imports stay; function bodies use tabs)
	pkg = IGN / "script-python/shared/Audit"
	pkg.mkdir(parents=True, exist_ok=True)
	(pkg / "code.py").write_text(code.replace("    ", "\t"), encoding="utf-8", newline="\n")
	write_json(
		pkg / "resource.json",
		resource_json(["code.py"], scope="A", hintScope=2),
	)
	print("wrote shared.Audit")


def write_named_query():
	sql = """SELECT
    event_timestamp,
    actor,
    actor_host,
    action,
    action_target,
    action_value,
    status_code,
    originating_system,
    originating_context,
    audit_events_id
FROM dbo.ops_audit_events
WHERE event_timestamp BETWEEN :startDate AND :endDate
  AND (
        COALESCE(:search, '') = ''
        OR actor LIKE :search
        OR action_target LIKE :search
        OR action_value LIKE :search
        OR action LIKE :search
      )
ORDER BY audit_events_id DESC
"""
	nq = IGN / "named-query/OpsAudit/AuditLog"
	nq.mkdir(parents=True, exist_ok=True)
	(nq / "query.sql").write_text(sql.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
	write_json(
		nq / "resource.json",
		resource_json(
			["query.sql"],
			scope="DG",
			version=2,
			useMaxReturnSize=False,
			autoBatchEnabled=False,
			fallbackValue="",
			maxReturnSize=5000,
			cacheUnit="SEC",
			type="Query",
			enabled=True,
			cacheAmount=1,
			cacheEnabled=False,
			database="ignition",
			fallbackEnabled=False,
			permissions=[{"zone": "", "role": ""}],
			parameters=[
				{"type": "Parameter", "identifier": "startDate", "sqlType": 8},
				{"type": "Parameter", "identifier": "endDate", "sqlType": 8},
				{"type": "Parameter", "identifier": "search", "sqlType": 7},
			],
		),
	)
	print("wrote named-query OpsAudit/AuditLog")


def control_numeric_view():
	on_change = (
		"\ttry:\n"
		"\t\tif origin == 'Browser':\n"
		"\t\t\tself.refreshBinding('props.value')\n"
		"\t\t\tself.view.custom.timeOut.startTime = system.date.now()\n"
		"\t\t\toldValue = previousValue.value\n"
		"\t\t\tnewValue = currentValue.value\n"
		"\t\t\tlabel = self.view.custom.tagName\n"
		"\t\t\ttry:\n"
		"\t\t\t\tmd = self.view.custom.metadata\n"
		"\t\t\t\tif md and 'shortDescription' in md and md['shortDescription']:\n"
		"\t\t\t\t\tlabel = md['shortDescription']\n"
		"\t\t\texcept:\n"
		"\t\t\t\tpass\n"
		"\t\t\tpayload = {\n"
		"\t\t\t\t'tagPath': self.view.params.tagPath,\n"
		"\t\t\t\t'value': currentValue.value,\n"
		"\t\t\t\t'label': label,\n"
		"\t\t\t\t'viewName': self.view.id.split('@')[0],\n"
		"\t\t\t}\n"
		"\t\t\tshared.Alerts.showAlert(\n"
		"\t\t\t\ttitle='Update setpoint',\n"
		"\t\t\t\tmessage='Tag: %s<br><br>Old: %s<br>New: %s' % (label, oldValue, newValue),\n"
		"\t\t\t\tshowCloseBtn=False,\n"
		"\t\t\t\tbtnTextPrimary='Cancel',\n"
		"\t\t\t\tbtnTextSecondary='Accept',\n"
		"\t\t\t\tbtnActionPrimary='cancel',\n"
		"\t\t\t\tbtnActionSecondary='writeValue',\n"
		"\t\t\t\tpayload=payload,\n"
		"\t\t\t)\n"
		"\texcept:\n"
		"\t\tsystem.util.getLogger('ControlNumeric').info('Error prompting write')\n"
	)
	write_handler = (
		"\tif payload.get('tagPath') == self.view.params.tagPath:\n"
		"\t\tshared.Audit.writeTag(\n"
		"\t\t\tpayload['tagPath'],\n"
		"\t\t\tpayload['value'],\n"
		"\t\t\tlabel=payload.get('label'),\n"
		"\t\t\tviewName=payload.get('viewName'),\n"
		"\t\t)\n"
		"\t\tself.view.custom.timeOut.actionComplete = True\n"
	)
	cancel_handler = (
		"\tif payload.get('tagPath') == self.view.params.tagPath:\n"
		"\t\tself.getChild('NumericEntryField').refreshBinding('props.value')\n"
		"\t\tself.view.custom.timeOut.actionComplete = True\n"
	)
	click_script = (
		"\tif self.view.params.permissions and self.view.params.setpoint and not self.session.custom.ReadOnly:\n"
		"\t\tself.position.display = False\n"
		"\t\tself.view.custom.timeOut.startTime = system.date.now()\n"
		"\t\tself.view.custom.timeOut.actionComplete = False\n"
	)

	return {
		"custom": {
			"engUnit": "",
			"format": "#0.0",
			"metadata": None,
			"quality": "",
			"tagName": "",
			"timeOut": {"actionComplete": True, "startTime": None},
			"value": "",
		},
		"params": {
			"permissions": True,
			"setpoint": True,
			"spacing": {"center": False, "data": 0, "engUnit": 30},
			"tagPath": "",
		},
		"propConfig": {
			"custom.engUnit": {
				"binding": {
					"config": {
						"expression": "if(qualityOf(tag({view.params.tagPath})) != 'Good',\n\t'',\n\ttag({view.params.tagPath} + '.EngUnit'))"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"custom.format": {
				"binding": {
					"config": {
						"expression": "if(qualityOf(tag({view.params.tagPath})) != 'Good',\n\t'#0.0',\n\tif(isNull(tag({view.params.tagPath} + '.FormatString')) || tag({view.params.tagPath} + '.FormatString') = '',\n\t\t'#0.0',\n\t\ttag({view.params.tagPath} + '.FormatString')))"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"custom.metadata": {
				"binding": {
					"config": {
						"expression": "if({view.params.tagPath} != '' && isGood(tag({view.params.tagPath} + '.Metadata')),\n\ttag({view.params.tagPath} + '.Metadata'),\n\t'')"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"custom.quality": {
				"binding": {
					"config": {
						"expression": "qualityOf(tag({view.params.tagPath}))"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"custom.tagName": {
				"binding": {
					"config": {
						"expression": "subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"custom.timeOut": {"persistent": True},
			"custom.timeOut.endTime": {
				"binding": {
					"config": {
						"expression": "dateArithmetic({view.custom.timeOut.startTime}, 60, 'sec')"
					},
					"type": "expr",
				}
			},
			"custom.timeOut.status": {
				"binding": {
					"config": {
						"expression": "(now() > {view.custom.timeOut.endTime}) || {view.custom.timeOut.actionComplete}"
					},
					"type": "expr",
				},
				"onChange": {
					"enabled": None,
					"script": "\tsystem.perspective.closePopup(id = 'alertDialog')",
				},
			},
			"custom.value": {
				"binding": {
					"config": {
						"expression": "if({view.custom.quality} != 'Good',\n\t'',\n\tnumberFormat(tag({view.params.tagPath}), {view.custom.format}))"
					},
					"type": "expr",
				},
				"persistent": True,
			},
			"params.permissions": {"paramDirection": "input", "persistent": True},
			"params.setpoint": {"paramDirection": "input", "persistent": True},
			"params.spacing": {"paramDirection": "inout", "persistent": True},
			"params.tagPath": {"paramDirection": "input", "persistent": True},
		},
		"props": {"defaultSize": {"height": 20, "width": 100}},
		"root": {
			"children": [
				{
					"meta": {"name": "NumericEntryField"},
					"position": {"grow": 1},
					"propConfig": {
						"position.display": {
							"binding": {
								"config": {
									"expression": "!{../Value.position.display}"
								},
								"type": "expr",
							}
						},
						"props.enabled": {
							"binding": {
								"config": {
									"expression": "{view.params.permissions} && !{session.custom.ReadOnly}"
								},
								"type": "expr",
							}
						},
						"props.format": {
							"binding": {
								"config": {"path": "view.custom.format"},
								"type": "property",
							}
						},
						"props.style.classes": {
							"binding": {
								"config": {
									"expression": "if({view.custom.quality} = 'Good',\n\t'font-value',\n\t'font-label')"
								},
								"type": "expr",
							}
						},
						"props.value": {
							"binding": {
								"config": {
									"expression": "toFloat({view.custom.value})"
								},
								"type": "expr",
							},
							"onChange": {"enabled": None, "script": on_change},
						},
					},
					"props": {
						"spinner": {"enabled": False},
						"style": {"classes": "font-value", "marginRight": "2px"},
					},
					"type": "ia.input.numeric-entry-field",
				},
				{
					"events": {
						"dom": {
							"onClick": {
								"config": {"script": click_script},
								"scope": "G",
								"type": "script",
							}
						}
					},
					"meta": {"name": "Value"},
					"position": {"grow": 1},
					"propConfig": {
						"position.display": {
							"binding": {
								"config": {"path": "view.custom.timeOut.status"},
								"type": "property",
							}
						},
						"props.style.classes": {
							"binding": {
								"config": {
									"expression": "if({view.custom.quality} = 'Good',\n\t'font-value',\n\t'font-label')"
								},
								"type": "expr",
							}
						},
						"props.style.cursor": {
							"binding": {
								"config": {
									"expression": "if({view.params.setpoint} && {view.params.permissions} && !{session.custom.ReadOnly},\n\t'pointer',\n\tif({view.params.setpoint},\n\t\t'not-allowed',\n\t\t''))"
								},
								"type": "expr",
							}
						},
						"props.text": {
							"binding": {
								"config": {"path": "view.custom.value"},
								"type": "property",
							}
						},
					},
					"props": {
						"style": {
							"overflow": "hidden",
							"textAlign": "right",
							"textDecoration": "underline",
						}
					},
					"type": "ia.display.label",
				},
				{
					"meta": {"name": "EngineeringUnit"},
					"position": {"shrink": 0},
					"propConfig": {
						"props.text": {
							"binding": {
								"config": {"path": "view.custom.engUnit"},
								"type": "property",
							}
						}
					},
					"props": {
						"style": {
							"classes": "font-label",
							"marginLeft": "4px",
							"marginTop": "1%",
						}
					},
					"type": "ia.display.label",
				},
			],
			"events": {
				"system": {
					"onStartup": {
						"config": {
							"script": "\tself.getChild('Value').position.display = True"
						},
						"scope": "G",
						"type": "script",
					}
				}
			},
			"meta": {"name": "root", "contextMenu": {}},
			"props": {
				"alignContent": "flex-start",
				"alignItems": "center",
				"style": {"minHeight": 20, "overflow": "visible"},
			},
			"propConfig": ticket_prop_config(),
			"scripts": {
				"customMethods": [],
				"extensionFunctions": None,
				"messageHandlers": [
					{
						"messageType": "cancel",
						"pageScope": True,
						"script": cancel_handler,
						"sessionScope": False,
						"viewScope": False,
					},
					{
						"messageType": "writeValue",
						"pageScope": True,
						"script": write_handler,
						"sessionScope": False,
						"viewScope": False,
					},
					TICKET_HANDLER,
				],
			},
			"type": "ia.container.flex",
		},
	}


def control_analog_value_view():
	return {
		"custom": {},
		"params": {
			"permissions": True,
			"setpoint": True,
			"spacing": {"center": True, "data": 0, "engUnit": 30},
			"tagPath": "",
		},
		"propConfig": {
			"params.permissions": {"paramDirection": "input", "persistent": True},
			"params.setpoint": {"paramDirection": "input", "persistent": True},
			"params.spacing": {"paramDirection": "input", "persistent": True},
			"params.tagPath": {"paramDirection": "input", "persistent": True},
		},
		"props": {"defaultSize": {"height": 20, "width": 100}},
		"root": {
			"type": "ia.container.flex",
			"meta": {"name": "root", "contextMenu": {}},
			"props": {
				"alignItems": "center",
				"justify": "center",
				"style": {"overflow": "visible", "minHeight": "20px", "height": "20px"},
			},
			"children": [
				{
					"type": "ia.display.view",
					"meta": {"name": "Numeric"},
					"position": {"grow": 1},
					"propConfig": {
						"props.params.tagPath": {
							"binding": {
								"config": {"path": "view.params.tagPath"},
								"type": "property",
							}
						},
						"props.params.permissions": {
							"binding": {
								"config": {"path": "view.params.permissions"},
								"type": "property",
							}
						},
						"props.params.setpoint": {
							"binding": {
								"config": {"path": "view.params.setpoint"},
								"type": "property",
							}
						},
						"props.params.spacing.center": {
							"binding": {
								"config": {"path": "view.params.spacing.center"},
								"type": "property",
							}
						},
					},
					"props": {
						"params": {
							"permissions": True,
							"setpoint": True,
							"spacing": {"center": True, "data": 0, "engUnit": 30},
							"tagPath": "",
						},
						"path": "03_Elements/00_Control/_Assets/Numeric",
						"style": {"overflow": "visible"},
					},
				}
			],
			"propConfig": ticket_prop_config(),
			"scripts": {
				"customMethods": [],
				"extensionFunctions": None,
				"messageHandlers": [TICKET_HANDLER],
			},
		},
	}


def audit_log_view():
	"""Simple Operations Audit Log page (Admin-only content)."""
	return {
		"custom": {},
		"params": {},
		"props": {"defaultSize": {"height": 900, "width": 1200}},
		"root": {
			"type": "ia.container.flex",
			"meta": {"name": "root", "contextMenu": {}},
			"props": {
				"direction": "column",
				"style": {
					"classes": "bg-page",
					"gap": "8px",
					"padding": "16px",
					"height": "100%",
				},
			},
			"children": [
				{
					"type": "ia.display.label",
					"meta": {"name": "Title"},
					"position": {"shrink": 0},
					"props": {
						"style": {
							"classes": "font-title",
							"fontSize": "20px",
							"fontWeight": "700",
						},
						"text": "OPS Audit Log",
					},
				},
				{
					"type": "ia.display.label",
					"meta": {"name": "Subtitle"},
					"position": {"shrink": 0},
					"props": {
						"style": {
							"classes": "font-label",
							"fontSize": "13px",
							"marginBottom": "8px",
						},
						"text": "Operator writes recorded in the OpsAudit profile (ops_audit_events). Administrators only.",
					},
				},
				{
					"type": "ia.container.flex",
					"meta": {
						"name": "Denied",
					},
					"propConfig": {
						"meta.visible": {
							"binding": {
								"config": {
									"expression": "!{session.custom.Administrator}"
								},
								"type": "expr",
							}
						}
					},
					"position": {"grow": 1},
					"props": {
						"alignItems": "center",
						"justify": "center",
						"style": {
							"classes": "bg-component container-card",
							"padding": "24px",
						},
					},
					"children": [
						{
							"type": "ia.display.label",
							"meta": {"name": "DeniedMsg"},
							"props": {
								"style": {
									"classes": "font-value",
									"fontSize": "16px",
									"fontWeight": "600",
								},
								"text": "Access denied — Administrator role required.",
							},
						}
					],
				},
				{
					"type": "ia.container.flex",
					"meta": {"name": "Content"},
					"propConfig": {
						"meta.visible": {
							"binding": {
								"config": {
									"expression": "{session.custom.Administrator}"
								},
								"type": "expr",
							}
						}
					},
					"position": {"grow": 1},
					"props": {
						"direction": "column",
						"style": {"gap": "8px", "height": "100%", "overflow": "visible"},
					},
					"children": [
						{
							"type": "ia.container.flex",
							"meta": {"name": "Filters"},
							"position": {"shrink": 0},
							"props": {
								"alignItems": "flex-end",
								"style": {"gap": "12px", "flexWrap": "wrap"},
							},
							"children": [
								{
									"type": "ia.container.flex",
									"meta": {"name": "Start"},
									"position": {"basis": "220px", "shrink": 0},
									"props": {"direction": "column"},
									"children": [
										{
											"type": "ia.display.label",
											"meta": {"name": "Lbl"},
											"props": {
												"style": {"classes": "font-label"},
												"text": "Start",
											},
										},
										{
											"type": "ia.input.date-time-input",
											"meta": {"name": "Date"},
											"propConfig": {
												"props.value": {
													"binding": {
														"config": {
															"expression": "dateArithmetic(now(0), -1, 'day')"
														},
														"type": "expr",
													}
												}
											},
											"props": {
												"format": "YYYY-MM-DD HH:mm:ss",
												"style": {"height": "32px"},
											},
										},
									],
								},
								{
									"type": "ia.container.flex",
									"meta": {"name": "End"},
									"position": {"basis": "220px", "shrink": 0},
									"props": {"direction": "column"},
									"children": [
										{
											"type": "ia.display.label",
											"meta": {"name": "Lbl"},
											"props": {
												"style": {"classes": "font-label"},
												"text": "End",
											},
										},
										{
											"type": "ia.input.date-time-input",
											"meta": {"name": "Date"},
											"propConfig": {
												"props.value": {
													"binding": {
														"config": {
															"expression": "dateArithmetic(now(0), 1, 'day')"
														},
														"type": "expr",
													}
												}
											},
											"props": {
												"format": "YYYY-MM-DD HH:mm:ss",
												"style": {"height": "32px"},
											},
										},
									],
								},
								{
									"type": "ia.container.flex",
									"meta": {"name": "Search"},
									"position": {"basis": "240px", "grow": 1},
									"props": {"direction": "column"},
									"children": [
										{
											"type": "ia.display.label",
											"meta": {"name": "Lbl"},
											"props": {
												"style": {"classes": "font-label"},
												"text": "Search",
											},
										},
										{
											"type": "ia.input.text-field",
											"meta": {"name": "Text"},
											"propConfig": {
												"custom.searchStr": {
													"binding": {
														"config": {
															"expression": "if(coalesce({this.props.text}, '') = '', '', '%' + {this.props.text} + '%')"
														},
														"type": "expr",
													}
												}
											},
											"props": {
												"placeholder": "actor, tag, value…",
												"style": {
													"classes": "bg-component font-value",
													"height": "32px",
												},
												"text": "",
											},
										},
									],
								},
							],
						},
						{
							"type": "ia.display.table",
							"meta": {"name": "Table"},
							"position": {"grow": 1},
							"propConfig": {
								"props.data": {
									"binding": {
										"config": {
											"parameters": {
												"endDate": "{../Filters/End/Date.props.value}",
												"search": "{../Filters/Search/Text.custom.searchStr}",
												"startDate": "{../Filters/Start/Date.props.value}",
											},
											"queryPath": "OpsAudit/AuditLog",
											"returnFormat": "dataset",
										},
										"type": "query",
									}
								}
							},
							"props": {
								"columns": [
									{
										"field": "event_timestamp",
										"header": {"title": "Timestamp"},
										"render": "date",
										"dateFormat": "YYYY-MM-DD HH:mm:ss",
										"sortable": True,
										"resizable": True,
										"width": "170px",
									},
									{
										"field": "actor",
										"header": {"title": "Actor"},
										"sortable": True,
										"resizable": True,
										"width": "110px",
									},
									{
										"field": "actor_host",
										"header": {"title": "Host"},
										"sortable": True,
										"resizable": True,
										"width": "120px",
									},
									{
										"field": "action",
										"header": {"title": "Action"},
										"sortable": True,
										"resizable": True,
										"width": "100px",
									},
									{
										"field": "action_target",
										"header": {"title": "Target"},
										"sortable": True,
										"resizable": True,
										"width": "220px",
									},
									{
										"field": "action_value",
										"header": {"title": "Value"},
										"sortable": True,
										"resizable": True,
										"width": "140px",
									},
									{
										"field": "status_code",
										"header": {"title": "Status"},
										"sortable": True,
										"resizable": True,
										"width": "80px",
									},
									{
										"field": "originating_system",
										"header": {"title": "Origin"},
										"sortable": True,
										"resizable": True,
										"width": "220px",
									},
									{
										"field": "originating_context",
										"header": {"title": "Ctx"},
										"sortable": True,
										"resizable": True,
										"width": "60px",
									},
									{
										"field": "audit_events_id",
										"header": {"title": "ID"},
										"sortable": True,
										"resizable": True,
										"width": "70px",
									},
								],
								"header": {
									"style": {
										"classes": "bg-header font-label",
										"fontWeight": "600",
									}
								},
								"rows": {"style": {"classes": "font-value"}},
								"style": {
									"classes": "bg-component container-card",
									"height": "100%",
									"overflow": "auto",
								},
							},
						},
					],
				},
			],
			"propConfig": ticket_prop_config(),
			"scripts": {
				"customMethods": [],
				"extensionFunctions": None,
				"messageHandlers": [TICKET_HANDLER],
			},
		},
	}


def write_views():
	pairs = [
		(
			PERS / "views/03_Elements/00_Control/_Assets/Numeric",
			control_numeric_view(),
		),
		(
			PERS / "views/03_Elements/00_Control/AnalogValue",
			control_analog_value_view(),
		),
		(
			PERS / "views/00_Pages/Operations/AuditLog",
			audit_log_view(),
		),
	]
	for folder, view in pairs:
		write_json(folder / "view.json", view)
		write_json(folder / "resource.json", resource_json(["view.json"]))
		print("wrote", folder.relative_to(ROOT))


def patch_session_props():
	path = PERS / "session-props/props.json"
	data = json.loads(path.read_text(encoding="utf-8"))
	data.setdefault("custom", {})["Administrator"] = False
	data.setdefault("propConfig", {})["custom.Administrator"] = {
		"binding": {
			"config": {
				"expression": (
					"try(\n"
					"\thasRole('Administrator',{session.props.auth.user.userName},{session.props.auth.idp})\n"
					"\t|| hasRole('Admin',{session.props.auth.user.userName},{session.props.auth.idp})\n"
					"\t|| hasRole('Admins',{session.props.auth.user.userName},{session.props.auth.idp}),\n"
					"\tfalse)"
				)
			},
			"type": "expr",
		}
	}
	write_json(path, data)
	# resource.json may exist
	print("patched session-props Administrator")


def patch_page_config():
	path = PERS / "page-config/config.json"
	data = json.loads(path.read_text(encoding="utf-8"))
	data["pages"]["/operations/audit"] = {
		"title": "OPS Audit Log",
		"viewPath": "00_Pages/Operations/AuditLog",
	}
	write_json(path, data)
	print("patched page-config")


def patch_navigation():
	path = PERS / "views/00_Pages/00_Docked/Navigation/view.json"
	data = json.loads(path.read_text(encoding="utf-8"))
	items = data["custom"]["items"]
	ops = next(i for i in items if i.get("label") == "Operations")
	children = ops.setdefault("items", [])
	if not any(c.get("label") == "Audit Log" for c in children):
		children.append(
			{
				"data": {
					"tagPath": "",
					"viewPath": "00_Pages/Operations/AuditLog",
					"page": "/operations/audit",
					"action": "page",
					"adminOnly": True,
				},
				"expanded": False,
				"icon": {
					"color": "",
					"path": "material/history",
					"style": {"classes": "", "height": "18px", "width": "18px"},
				},
				"items": [],
				"label": "Audit Log",
			}
		)

	# Filter admin-only nodes unless Administrator
	tree = None
	for c in data["root"]["children"]:
		if c.get("meta", {}).get("name") == "Tree":
			tree = c
			break
	if tree is None:
		raise SystemExit("Navigation Tree missing")

	pc = tree.setdefault("propConfig", {})
	pc["props.items"] = {
		"binding": {
			"config": {
				"struct": {
					"items": "{view.custom.items}",
					"isAdmin": "{session.custom.Administrator}",
				},
				"waitOnAll": True,
			},
			"transforms": [
				{
					"code": (
						"\timport copy\n"
						"\titems = copy.deepcopy(value['items'])\n"
						"\tis_admin = bool(value['isAdmin'])\n"
						"\tdef filter_nodes(nodes):\n"
						"\t\tout = []\n"
						"\t\tfor n in nodes:\n"
						"\t\t\tdata = n.get('data') or {}\n"
						"\t\t\tif data.get('adminOnly') and not is_admin:\n"
						"\t\t\t\tcontinue\n"
						"\t\t\tkids = n.get('items') or []\n"
						"\t\t\tif kids:\n"
						"\t\t\t\tn['items'] = filter_nodes(kids)\n"
						"\t\t\tout.append(n)\n"
						"\t\treturn out\n"
						"\treturn filter_nodes(items)\n"
					),
					"type": "script",
				}
			],
			"type": "expr-struct",
		}
	}
	write_json(path, data)
	print("patched Navigation")


def patch_nav_code():
	path = IGN / "script-python/Navigation/Nav/code.py"
	text = path.read_text(encoding="utf-8")
	needle = '\t\t"00_Pages/Alarms/Journal": "/alarms/journal",\n'
	insert = '\t\t"00_Pages/Alarms/Journal": "/alarms/journal",\n\t\t"00_Pages/Operations/AuditLog": "/operations/audit",\n'
	if "Operations/AuditLog" not in text:
		if needle not in text:
			raise SystemExit("Nav bh_pages needle missing")
		text = text.replace(needle, insert)
		path.write_text(text, encoding="utf-8", newline="\n")
		print("patched Navigation.Nav bh_pages")
	else:
		print("Navigation.Nav already has AuditLog")


def patch_evaporator_faceplate():
	path = PERS / "views/01_Popups/00_Faceplates/Evaporator/view.json"
	data = json.loads(path.read_text(encoding="utf-8"))
	# add custom.values.sp
	data["propConfig"]["custom.values.sp"] = {
		"binding": {
			"config": {
				"expression": "if({view.params.tagPath} = '',\n\t'',\n\t{view.params.tagPath} + '/Temp/SP')"
			},
			"type": "expr",
		}
	}

	children = data["root"]["children"]
	# Insert SP block after AnalogValue (PV)
	sp_block = [
		{
			"type": "ia.display.label",
			"meta": {"name": "SpLabel"},
			"position": {"shrink": 0},
			"props": {
				"style": {
					"classes": "font-label",
					"fontSize": "12px",
					"fontWeight": "600",
					"marginBottom": "2px",
				},
				"text": "Setpoint (SP) — click value to edit",
			},
		},
		{
			"type": "ia.display.view",
			"meta": {"name": "SpAnalogValue"},
			"position": {"shrink": 0},
			"propConfig": {
				"props.params.tagPath": {
					"binding": {
						"config": {"expression": "{view.custom.values.sp}"},
						"type": "expr",
					}
				},
				"props.params.permissions": {
					"binding": {
						"config": {
							"expression": "!{session.custom.ReadOnly}"
						},
						"type": "expr",
					}
				},
			},
			"props": {
				"params": {
					"permissions": True,
					"setpoint": True,
					"spacing": {"center": True, "data": 0, "engUnit": 30},
					"tagPath": "",
				},
				"path": "03_Elements/00_Control/AnalogValue",
				"style": {"marginBottom": "16px"},
			},
		},
	]

	# Find AnalogValue index
	idx = next(
		i
		for i, c in enumerate(children)
		if c.get("meta", {}).get("name") == "AnalogValue"
	)
	# Avoid duplicate insert
	if not any(c.get("meta", {}).get("name") == "SpAnalogValue" for c in children):
		children[idx + 1 : idx + 1] = sp_block

	# Fix Close button script newlines if double-escaped
	for c in children:
		if c.get("meta", {}).get("name") == "CloseButton":
			script = (
				c.get("events", {})
				.get("component", {})
				.get("onActionPerformed", {})
				.get("config", {})
				.get("script", "")
			)
			if "\\n" in script:
				c["events"]["component"]["onActionPerformed"]["config"]["script"] = (
					"\ttagPath = str(self.view.params.tagPath)\n"
					"\tlabel = str(self.view.custom.label)\n"
					"\tsystem.perspective.closePopup('ev-fp-%s' % (tagPath or label))\n"
				)

	write_json(path, data)
	print("patched Evaporator faceplate SP editor")


def main():
	write_audit_script_package()
	write_named_query()
	write_views()
	patch_session_props()
	patch_page_config()
	patch_navigation()
	patch_nav_code()
	patch_evaporator_faceplate()
	print("done")


if __name__ == "__main__":
	main()
