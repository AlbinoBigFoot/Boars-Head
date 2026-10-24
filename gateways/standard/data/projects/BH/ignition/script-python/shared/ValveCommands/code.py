# Valve / pump faceplate command helpers (SO/MO).
# Plant Digitals are often valueSource=reference → RCP1 atomics; resolve before write.

logger = system.util.getLogger("shared.ValveCommands")


def _resolve(path):
	"""Prefer OPC/Memory sourceTagPath when path is a reference leaf."""
	path = shared.Pax.livePath(path)   # a PLC device's field -> its PLC member (flat-member cleanup 2026-10-23)
	try:
		cfg = system.tag.getConfiguration(path, False)[0]
		src = cfg.get("sourceTagPath") or cfg.get("sourceTagPath")
		if src:
			return str(src)
	except Exception:
		pass
	return path


def _plcAllowed(path):
	"""plc-write-lock: shared.PlcWriteLock.writeAllowed (an error blocks only paths naming RCP1)."""
	try:
		return shared.PlcWriteLock.writeAllowed(path)
	except Exception as e:
		logger.warn("PlcWriteLock check failed for %s: %s" % (path, e))
		p = str(path or "")
		return not ('_RCP1_' in p or '[RCP1]' in p)


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
	"""Write resolved paths (raw, no audit); Bad qualities are logged."""
	resolved = [_resolve(p) for p in paths]
	# plc-write-lock (.cursor/tasks/plc-write-lock): raw writes skip anything that would reach the RCP1 controller
	# while PLC writes are locked (shared.PlcWriteLock.writeAllowed)
	keep = [i for i, p in enumerate(resolved) if _plcAllowed(p)]
	if len(keep) != len(resolved):
		paths = [paths[i] for i in keep]
		vals = [vals[i] for i in keep]
		resolved = [resolved[i] for i in keep]
		if not resolved:
			return []
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
		logger.warn("Bad write quality: %s" % (bad,))

	return qualities


def _write(paths, vals, audit=True, label=None, viewName="Faceplate/Controls"):
	"""Operator writes go through OpsAudit; audit=False writes raw."""
	# security-tiers + device-perms: Faceplates/Operate AND the device-type row of each path (Pump/Command,
	# Valve/Mode, ...; a refusal shows 'Not Permitted'). Gateway scripts pass.
	for p in paths:
		if not shared.Security.requireWrite(p, label or str(p)):
			return []
	# pax-bindings: a PLC device (shared.Pax.part) is read only - its commands, mode and bypass bits belong to
	# the PLC; never write its old members or its nested PlantPAx members from the HMI
	for p in paths:
		dev = shared.Pax.device(str(p).rsplit('/', 2)[0])
		if shared.Pax.part(dev):
			logger.info('Refused write %s: %s is mapped to the PLC (read only)' % (p, dev))
			return []
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


def resetPump(tagPath):
	base = str(tagPath or "").strip()
	if not base:
		return
	_write([base + "/OCmd_Reset/Value"], [True], label="Reset pump", viewName="Faceplate/Controls")


def openValve(tagPath, valveType="MO"):
	"""Open command. SO → Cmd + Cmd_Open; MO → pulse Cmd_Open."""
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
	_write([base + "/" + cmd + "/Value"], [True], label="Enable device", viewName="Faceplate/Interlocks")


def disableDevice(tagPath, cmd_leaf="Cmd_Disable", sts_leaf="Disabled"):
	base = str(tagPath or "").strip()
	if not base:
		return
	cmd = str(cmd_leaf or "Cmd_Disable").strip() or "Cmd_Disable"
	_write([base + "/" + cmd + "/Value"], [True], label="Disable device", viewName="Faceplate/Interlocks")


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
