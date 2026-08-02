# Valve faceplate command helpers (SO/MO + SIM feedback).
# Plant Digitals are often valueSource=reference → RCP1 atomics; resolve before write.


def _resolve(path):
	"""Prefer OPC/Memory sourceTagPath when path is a reference leaf."""
	try:
		cfg = system.tag.getConfiguration(path, False)[0]
		src = cfg.get("sourceTagPath")
		if src:
			return str(src)
	except Exception:
		pass
	return path


def _write(paths, vals):
	resolved = [_resolve(p) for p in paths]
	try:
		return system.tag.writeBlocking(resolved, vals)
	except Exception:
		return system.tag.writeBlocking(paths, vals)


def _simFeedback(base, opened):
	"""Update limit switches + Val_Sts so SIM HMI reacts without a PLC."""
	# Val_Sts demo convention: 2=OPEN, 1=CLOSED (see Rcp1Simulate._demoValue)
	status = 2 if opened else 1
	paths = [
		base + "/OpenLS/Value",
		base + "/ClosedLS/Value",
		base + "/Status/Value",
	]
	vals = [bool(opened), not bool(opened), status]
	_write(paths, vals)


def openValve(tagPath, valveType="MO"):
	"""Open command. SO → Cmd/Value=True; MO → pulse Cmd_Open + SIM feedback."""
	base = str(tagPath or "").strip()
	if not base:
		return
	vt = str(valveType or "MO").strip().upper()
	if vt == "SO":
		_write([base + "/Cmd/Value"], [True])
	else:
		_write([base + "/Cmd_Open/Value", base + "/Cmd_Close/Value"], [True, False])
	_simFeedback(base, True)


def closeValve(tagPath, valveType="MO"):
	"""Close command. SO → Cmd/Value=False; MO → pulse Cmd_Close + SIM feedback."""
	base = str(tagPath or "").strip()
	if not base:
		return
	vt = str(valveType or "MO").strip().upper()
	if vt == "SO":
		_write([base + "/Cmd/Value"], [False])
	else:
		_write([base + "/Cmd_Open/Value", base + "/Cmd_Close/Value"], [False, True])
	_simFeedback(base, False)


def resetValve(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write([base + "/Cmd_Reset/Value"], [True])


def setMode(tagPath, mode):
	"""Set OPER/MAINT/PROG mutually exclusive (Valve / EF / CT style)."""
	base = str(tagPath or "").strip()
	if not base:
		return
	clicked = str(mode or "OPER").strip().upper()
	modes = ["OPER", "MAINT", "PROG"]
	if clicked not in modes:
		clicked = "OPER"
	paths = [base + "/" + m + "/Value" for m in modes]
	vals = [m == clicked for m in modes]
	_write(paths, vals)
