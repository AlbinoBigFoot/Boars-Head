"""Code -> text enums (evap-defrost-strings, 2026-10-22).

One source of truth per enum: a memory DataSet tag [default]_Config/Enums/<Group>/<Name> with the columns
value (Int4), label, short (String), selectable (Boolean), plus optional extras (PlcState: hmiStatus).
Expressions read the tag with lookup(), e.g.
	lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(x), toStr(x), 'value', 'label')
and scripts use the functions below. Every function is fail-safe: on any error it falls back to the raw value.
Tags + view patches: .cursor/tasks/evap-defrost-strings/build.py. Docs: docs/evaporator-hmi-components.md.
"""

ROOT = "[default]_Config/Enums/"

# Member name (the folder above /Value, or the last '.' part of a PLC path) -> enum under ROOT. Used by
# describe() for the confirm dialog (shared.Alerts.confirmApplyWrite) and the OpsAudit text (shared.Audit.writeTag).
MEMBERS = {
	"Cfg_DefrostStartMode": "Evaporator/DefrostStartMode",
	"Cfg_CycFans": "Evaporator/CycleFans",
}


def _int(value):
	"""Integral numbers (2, 2.0, '2') -> int; anything else (None, bool, 1.5, text) -> None."""
	if value is None or isinstance(value, bool):
		return None
	try:
		f = float(value)
		i = int(f)
	except Exception:
		return None
	return i if f == i else None


def _tagPath(enumPath):
	p = str(enumPath or "").strip().strip("/")
	if not p:
		return None
	return p if p.startswith("[") else ROOT + p


def rows(enumPath, dataset=None):
	"""Rows as dicts {value, label, short, selectable, <extra columns>} in tag order; [] if the tag is missing / bad.

	dataset: the DataSet when the caller already has it (a binding), so no tag read is needed."""
	try:
		ds = dataset
		if ds is None:
			path = _tagPath(enumPath)
			if not path:
				return []
			qv = system.tag.readBlocking([path])[0]
			if not qv.quality.isGood():
				return []
			ds = qv.value
		if ds is None:
			return []
		cols = [str(c) for c in ds.getColumnNames()]
		out = []
		for r in range(ds.getRowCount()):
			row = dict((cols[c], ds.getValueAt(r, c)) for c in range(len(cols)))
			v = _int(row.get("value"))
			if v is None:
				continue
			row["value"] = v
			if row.get("label") in (None, ""):
				row["label"] = str(v)
			if row.get("short") in (None, ""):
				row["short"] = row["label"]
			row["selectable"] = bool(row.get("selectable")) if "selectable" in row else True
			out.append(row)
		return out
	except Exception:
		return []


def _find(enumPath, value, dataset=None):
	v = _int(value)
	if v is None:
		return None
	for row in rows(enumPath, dataset):
		if row["value"] == v:
			return row
	return None


def label(enumPath, value, default=None):
	"""Long text for value ('Time Of Day'); default (None) when there is no match."""
	row = _find(enumPath, value)
	return row["label"] if row else default


def short(enumPath, value, default=None):
	"""Short text for value ('ToD'); default (None) when there is no match."""
	row = _find(enumPath, value)
	return row["short"] if row else default


def options(enumPath, current=None, dataset=None):
	"""Dropdown options [{value, label, isDisabled}]: every row; rows with selectable false stay listed but disabled
	(so the dropdown still shows a mode only the PLC can set). A current value missing from the enum is appended,
	disabled, so it shows as itself instead of a blank dropdown."""
	out = [{"value": r["value"], "label": r["label"], "isDisabled": not r["selectable"]}
		for r in rows(enumPath, dataset)]
	if out and current not in (None, ""):
		v = _int(current)
		if v is None or v not in [o["value"] for o in out]:
			out.append({"value": current, "label": str(current if v is None else v), "isDisabled": True})
	return out


def forTagPath(tagPath):
	"""Enum path for a member tag path ('.../CG-E2/Cfg_DefrostStartMode/Value', '[RCP1]CG[3].Cfg_CycFans'), or None."""
	try:
		p = str(tagPath or "").replace("\\", "/").strip()
		if p.startswith("[") and "]" in p:
			p = p[p.index("]") + 1:]
		parts = [x for x in p.split("/") if x]
		if not parts:
			return None
		leaf = parts[-1]
		if leaf == "Value" and len(parts) > 1:
			leaf = parts[-2]
		return MEMBERS.get(leaf.split(".")[-1])
	except Exception:
		return None


def describe(tagPath, value, enumPath=None):
	"""'Time Of Day (0)' when the member has an enum and the value a row; otherwise the raw value as text."""
	try:
		ep = enumPath or forTagPath(tagPath)
		if ep:
			row = _find(ep, value)
			if row:
				return "%s (%d)" % (row["label"], row["value"])
	except Exception:
		pass
	return "%s" % (value,)
