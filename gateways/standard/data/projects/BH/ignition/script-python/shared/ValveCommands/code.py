# Valve faceplate command helpers (SO/MO + SIM feedback).
# Plant Digitals are often valueSource=reference → RCP1 atomics; resolve before write.

logger = system.util.getLogger("shared.ValveCommands")


def _resolve(path):
	"""Prefer OPC/Memory sourceTagPath when path is a reference leaf."""
	try:
		cfg = system.tag.getConfiguration(path, False)[0]
		src = cfg.get("sourceTagPath") or cfg.get("sourceTagPath")
		if src:
			return str(src)
	except Exception:
		pass
	return path


def _qualityGood(q):
	try:
		if q is None:
			return False
		if hasattr(q, "isGood"):
			return bool(q.isGood())
		return str(q).upper().find("GOOD") >= 0
	except Exception:
		return False


def _writeRaw(paths, vals):
	"""Write resolved paths; if OPC rejects, ensure SIM memory and retry once."""
	resolved = [_resolve(p) for p in paths]
	try:
		shared.Rcp1Simulate.ensureApplied()
	except Exception as e:
		logger.warn("ensureApplied before write: %s" % str(e))

	try:
		qualities = system.tag.writeBlocking(resolved, vals)
	except Exception as e:
		logger.warn("writeBlocking resolved failed (%s); retry raw paths" % str(e))
		qualities = system.tag.writeBlocking(paths, vals)

	bad = []
	for i, q in enumerate(qualities or []):
		if not _qualityGood(q):
			bad.append((resolved[i] if i < len(resolved) else paths[i], str(q)))

	if bad:
		logger.warn("Bad write quality (will ensure SIM + retry): %s" % (bad,))
		try:
			shared.Rcp1Simulate.ensureApplied(force=True)
		except Exception as e:
			logger.warn("ensureApplied(force) failed: %s" % str(e))
		try:
			qualities = system.tag.writeBlocking(resolved, vals)
		except Exception:
			qualities = system.tag.writeBlocking(paths, vals)
		bad2 = []
		for i, q in enumerate(qualities or []):
			if not _qualityGood(q):
				bad2.append((resolved[i] if i < len(resolved) else paths[i], str(q)))
		if bad2:
			logger.error("Write still Bad after SIM ensure: %s" % (bad2,))

	return qualities


def _write(paths, vals, audit=True, label=None, viewName="Faceplate/Controls"):
	"""Operator writes go through OpsAudit; SIM feedback uses raw writes."""
	if not audit:
		return _writeRaw(paths, vals)
	results = []
	for p, v in zip(paths, vals):
		try:
			results.append(shared.Audit.writeTag(p, v, label=label, viewName=viewName))
		except Exception as e:
			logger.error("Audit.writeTag failed %s: %s" % (p, e))
			_writeRaw([p], [v])
	return results


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
	_write(paths, vals, audit=False)


def _simPumpRun(base, running):
	"""Drive P_Motor status so overview impeller + faceplate banner follow Start/Stop."""
	# Val_Sts: 1=STOPPED, 2=RUNNING (see Rcp1Simulate._demoValue / Devices/Pump)
	status = 2 if running else 1
	_write(
		[
			base + "/Val_Sts/Value",
			base + "/Sts_Running/Value",
			base + "/Sts_Stopped/Value",
		],
		[status, bool(running), not bool(running)],
		audit=False,
	)


def startPump(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write(
		[base + "/OCmd_Start/Value", base + "/OCmd_Stop/Value"],
		[True, False],
		label="Start pump",
		viewName="Faceplate/Controls",
	)
	_simPumpRun(base, True)


def stopPump(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write(
		[base + "/OCmd_Stop/Value", base + "/OCmd_Start/Value"],
		[True, False],
		label="Stop pump",
		viewName="Faceplate/Controls",
	)
	_simPumpRun(base, False)


def resetPump(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write([base + "/OCmd_Reset/Value"], [True], label="Reset pump", viewName="Faceplate/Controls")
	_write(
		[
			base + "/Sts_FailToStart/Value",
			base + "/Sts_FailToStop/Value",
			base + "/Alm_FailToStart/Value",
			base + "/Alm_FailToStop/Value",
		],
		[False, False, False, False],
		audit=False,
	)


def openValve(tagPath, valveType="MO"):
	"""Open command. SO → Cmd + Cmd_Open; MO → pulse Cmd_Open + SIM feedback."""
	base = str(tagPath or "").strip()
	if not base:
		return
	vt = str(valveType or "MO").strip().upper()
	if vt == "SO":
		# Plant Cmd aliases Cmd_Open; write both for SO faceplate parity
		_write(
			[base + "/Cmd/Value", base + "/Cmd_Open/Value"],
			[True, True],
		)
	else:
		_write([base + "/Cmd_Open/Value", base + "/Cmd_Close/Value"], [True, False])
	_simFeedback(base, True)


def closeValve(tagPath, valveType="MO"):
	"""Close command. SO → clear Cmd/Cmd_Open + pulse Cmd_Close; MO → Cmd_Close."""
	base = str(tagPath or "").strip()
	if not base:
		return
	vt = str(valveType or "MO").strip().upper()
	if vt == "SO":
		_write(
			[base + "/Cmd/Value", base + "/Cmd_Close/Value", base + "/Cmd_Open/Value"],
			[False, True, False],
		)
	else:
		_write([base + "/Cmd_Open/Value", base + "/Cmd_Close/Value"], [False, True])
	_simFeedback(base, False)


def resetValve(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write([base + "/Cmd_Reset/Value"], [True])


def writeTag(tagPath, value):
	"""Write one tag path, resolving Digitals reference → source when needed."""
	path = str(tagPath or "").strip()
	if not path:
		return
	_write([path], [value])


def _applyDisabled(base, disabled, sts_leaf="Disabled"):
	"""SIM has no PLC enable/disable logic — drive Disabled / Nrdy_Disabled locally."""
	flag = bool(disabled)
	leaf = str(sts_leaf or "Disabled").strip() or "Disabled"
	_write(
		[base + "/" + leaf + "/Value"],
		[flag],
		label="Disable device" if flag else "Enable device",
		viewName="Faceplate/Interlocks",
	)
	_write([base + "/Nrdy_Disabled/Value"], [flag], audit=False)


def _readBool(path, default=False):
	try:
		return bool(system.tag.readBlocking([_resolve(path)])[0].value)
	except Exception:
		return default


def enableDevice(tagPath, cmd_leaf="Cmd_Enable", sts_leaf="Disabled"):
	base = str(tagPath or "").strip()
	if not base:
		return
	cmd = str(cmd_leaf or "Cmd_Enable").strip() or "Cmd_Enable"
	_write([base + "/" + cmd + "/Value"], [True], audit=False)
	_applyDisabled(base, False, sts_leaf=sts_leaf)


def disableDevice(tagPath, cmd_leaf="Cmd_Disable", sts_leaf="Disabled"):
	base = str(tagPath or "").strip()
	if not base:
		return
	cmd = str(cmd_leaf or "Cmd_Disable").strip() or "Cmd_Disable"
	_write([base + "/" + cmd + "/Value"], [True], audit=False)
	_applyDisabled(base, True, sts_leaf=sts_leaf)


def bypassActive(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return False
	return _readBool(base + "/Interlock/Sts_BypActive/Value")


def bypassDevice(tagPath, active=None, cmd_leaf="Cmd_Bypass"):
	"""Pulse Cmd_Bypass (or OCmd_Bypass) and set Interlock/Sts_BypActive. active=None toggles."""
	base = str(tagPath or "").strip()
	if not base:
		return
	if active is None:
		active = not bypassActive(base)
	else:
		active = bool(active)
	cmd = str(cmd_leaf or "Cmd_Bypass").strip() or "Cmd_Bypass"
	_write([base + "/" + cmd + "/Value"], [True], audit=False)
	_write(
		[base + "/Interlock/Sts_BypActive/Value"],
		[active],
		label="Bypass interlocks" if active else "Clear interlock bypass",
		viewName="Faceplate/Interlocks",
	)


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


def setPumpMode(tagPath, mode):
	"""Set Sts_Oper/Sts_Maint/Sts_Prog mutually exclusive (Pump style)."""
	base = str(tagPath or "").strip()
	if not base:
		return
	clicked = str(mode or "Sts_Oper").strip()
	modes = ["Sts_Oper", "Sts_Maint", "Sts_Prog"]
	if clicked not in modes:
		clicked = "Sts_Oper"
	paths = [base + "/" + m + "/Value" for m in modes]
	vals = [m == clicked for m in modes]
	_write(paths, vals)
