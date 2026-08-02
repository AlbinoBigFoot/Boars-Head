# RCP1 Simulate mode — flip AtomicTags between OPC UA and Memory.
# Watched by project tag-change script rcp1Simulate on [default]RCP1/Simulate.

logger = system.util.getLogger("shared.Rcp1Simulate")

RCP1_ROOT = "[default]RCP1"
SIMULATE_TAG = "[default]RCP1/Simulate"
OPC_SERVER = "Ignition OPC UA Server"
OPC_MARKER = "#OPC:"
EXCLUDE_NAMES = set(["Simulate"])

# Session cache: fullTagPath -> {"opcItemPath", "opcServer", "documentation"}
_opcCache = {}


def _browseName(br):
	try:
		return str(br.getName())
	except:
		pass
	try:
		return str(br["name"])
	except:
		pass
	try:
		if hasattr(br, "name"):
			return str(br.name)
	except:
		pass
	return None


def _browseFullPath(br):
	try:
		return str(br.getFullPath())
	except:
		pass
	try:
		return str(br["fullPath"])
	except:
		pass
	try:
		fp = getattr(br, "fullPath", None)
		if fp is not None:
			return str(fp)
	except:
		pass
	return None


def _browseTagType(br):
	try:
		return str(br.getTagType())
	except:
		pass
	try:
		return str(br["tagType"])
	except:
		pass
	return ""


def _normalizePath(full):
	fp = str(full).replace("\\", "/")
	if not fp.startswith("["):
		fp = "[default]" + (fp if fp.startswith("/") else "/" + fp)
	return fp


def _browseResults(folderPath, filt=None):
	"""Return iterable of browse results (Ignition 8.x shape varies)."""
	try:
		if filt is None:
			raw = system.tag.browse(folderPath)
		else:
			raw = system.tag.browse(folderPath, filt)
	except Exception as e:
		logger.warn("browse %s failed: %s" % (folderPath, str(e)))
		return []
	if raw is None:
		return []
	if hasattr(raw, "getResults"):
		try:
			return list(raw.getResults())
		except:
			pass
	try:
		return list(raw)
	except:
		return []


def _parentAndName(fullPath):
	s = str(fullPath).rstrip("/")
	if "/" not in s:
		return "", s
	idx = s.rfind("/")
	return s[:idx], s[idx + 1 :]


def _defaultForType(dataType):
	dt = str(dataType or "Float4").lower()
	if "bool" in dt:
		return False
	if "string" in dt or "datetime" in dt:
		return ""
	if "int" in dt or "long" in dt or "short" in dt or "byte" in dt:
		return 0
	return 0.0


def _parseOpcFromDocumentation(doc):
	"""Return (opcItemPath, cleanDocumentation) from a stashed doc string."""
	if doc is None:
		return None, ""
	text = str(doc)
	if not text.startswith(OPC_MARKER):
		return None, text
	rest = text[len(OPC_MARKER) :]
	nl = rest.find("\n")
	if nl < 0:
		return rest.strip() or None, ""
	return rest[:nl].strip() or None, rest[nl + 1 :]


def _stashDocumentation(opcItemPath, documentation):
	clean = documentation if documentation is not None else ""
	# Avoid double-stashing if already marked
	existing, clean = _parseOpcFromDocumentation(clean)
	path = opcItemPath or existing or ""
	return OPC_MARKER + str(path) + "\n" + str(clean)


def _readCurrentValue(tagPath, dataType, name=None):
	"""Read live value when quality is Good; otherwise demo-safe defaults.

	Comm Loss on device graphics is isBad(Rung/Value) — Memory tags must have
	Good quality. When OPC was Bad, seed Rung=True so the HMI is usable in SIM.
	"""
	fallback = _defaultForType(dataType)
	leaf = str(name or "")
	# Comm Loss = isBad(Rung/Value). Seed a Good numeric/bool when OPC was Bad.
	if leaf == "Rung":
		dt = str(dataType or "").lower()
		fallback = True if "bool" in dt else 1
	try:
		qv = system.tag.readBlocking([tagPath])[0]
		if qv is None:
			return fallback
		qual = getattr(qv, "quality", None)
		good = True
		try:
			if qual is not None and hasattr(qual, "isGood"):
				good = bool(qual.isGood())
			elif qual is not None:
				good = str(qual).upper().find("GOOD") >= 0
		except:
			good = True
		if not good:
			return fallback
		val = qv.value
		if val is None:
			return fallback
		return val
	except:
		return fallback


def _logSampleSources(label, samplePaths=None):
	"""Log valueSource for a few RCP1 leaves so gateway logs prove the flip."""
	if samplePaths is None:
		samplePaths = [
			"[default]RCP1/COMP 7/Alm",
			"[default]RCP1/COMP 7/Rung",
			"[default]RCP1/COMP 7/Amps",
			"[default]RCP1/Simulate",
			"[default]RCP1/MR EF/Started",
			"[default]RCP1/MR AD/Alm",
			"[default]RCP1/FIRE/Alm",
			"[default]Plant/Machine Room/Compressors/COMP 7/Rung/Value",
			"[default]Plant/Machine Room/ExhaustFans/MR EF/Status/Value",
			"[default]Plant/Machine Room/Digitals/MR AD/Value",
		]
	for tp in samplePaths:
		try:
			qv = system.tag.readBlocking([tp])[0]
			qual = str(getattr(qv, "quality", ""))
			val = getattr(qv, "value", None)
			vs = ""
			opc = ""
			stash = "n/a"
			try:
				cfg = system.tag.getConfiguration(tp, False)[0]
				vs = cfg.get("valueSource")
				opc = cfg.get("opcItemPath") or ""
				doc = str(cfg.get("documentation") or "")
				stash = "yes" if doc.startswith(OPC_MARKER) else "no"
				stp = cfg.get("sourceTagPath") or ""
				if stp:
					opc = "src=" + str(stp)
			except:
				pass
			logger.info(
				"%s sample %s valueSource=%s opc=%s stash=%s quality=%s value=%s"
				% (label, tp, vs, opc, stash, qual, val)
			)
		except Exception as e:
			logger.warn("%s sample %s failed: %s" % (label, tp, str(e)))


def _deviceKey(tagPath):
	"""RCP1 device folder name, e.g. COMP 7 / HTLR-Pump 1 / HTR."""
	parts = [p for p in str(tagPath).replace("\\", "/").split("/") if p]
	# [default]RCP1/<device>/...
	if len(parts) >= 3 and parts[1] == "RCP1":
		return parts[2]
	return parts[-2] if len(parts) >= 2 else ""


def _demoValue(name, dataType, tagPath=None):
	"""Demo values so Machine Room looks alive in SIM (varied, not all alarming)."""
	n = str(name or "")
	dt = str(dataType or "").lower()
	dev = _deviceKey(tagPath) if tagPath else ""

	# Pump Val_Sts: 0=UNK, 1=STOPPED, 2=RUNNING
	if n == "Val_Sts":
		if "Pump 2" in dev:
			return 1  # STOPPED
		return 2  # RUNNING

	# Tank Status: 0=OK, 1=LOW, … — never seed 1 (looks like LOW fault)
	# Sensor Status (Val_Fault): 0=OK. Do not match "Pump" inside "*-Pumps Pressure".
	if n == "Status":
		if "Pumps Pressure" in dev or "Pressure" in dev:
			return 0  # Sensor OK
		# ExhaustFan Status = P_Motor Val_Sts: 0=UNK, 1=STOPPED, 2=RUNNING
		if "EF" in dev and "Pressure" not in dev:
			return 2  # RUNNING
		if "Pump" in dev and "Pressure" not in dev:
			return 1
		if any(x in dev for x in ("HTR", "LTR", "HPR")):
			return 0  # OK
		if "SV" in dev or "Valve" in dev or "Liq" in dev:
			return 2  # OPEN
		return 0

	# Valve travel / transit stall timer (Cfg_TransitStallT) — never leave null/0 in SIM.
	if n == "TravelTime":
		return 5

	# Valve ownership modes (P_ValveSO Sts_Oper/Prog/Maint) — default Operator so
	# Open/Close are usable; mutual exclusive with PROG/MAINT.
	if n == "OPER":
		return True
	if n in ("PROG", "MAINT"):
		return False

	# Limit switches follow Status for valve demo (OPEN → OpenLS).
	if n == "OpenLS":
		if "SV" in dev or "Valve" in dev or "Liq" in dev:
			return True
		return False
	if n == "ClosedLS":
		return False

	# Compressor Rung: 0=Off, 1=Running — vary the bank
	if n == "Rung":
		if dev in ("COMP 6",):
			return 0  # STOP
		return 1  # RUN

	if n in ("Color", "CP_Mode", "SV_Mode"):
		return 1
	if n == "Started":
		# Exhaust fans (MR EF / BR EF) run in demo; Pump 2 / COMP 6 stay off.
		return False if dev in ("COMP 6",) or "Pump 2" in dev else True
	if n in ("AutoEN", "Rdy", "Enable"):
		return True
	# Safety lamps (MR AD / VL AD / RDISKS / FIRE) — False = normal (okValue false).
	if n == "Alm" and any(x in dev for x in ("MR AD", "VL AD", "RDISKS", "FIRE")):
		return False

	# Comm/Value has Equality@1 alarm on Devices UDTs. Seeding Comm=True lights
	# every compressor/valve alarm chrome (metrics High maps to CSS "medium").
	# Perspective Comm Loss uses isBad(Rung/Value), not this bit — keep False.
	if n == "Comm":
		return False

	# Discrete alarm bits — all clear for a clean SIM demo.
	if n in (
		"Alm", "Failed", "Cutout", "Fault",
		"Alm_FailToStart", "Alm_IOFault", "Sts_FailToStart",
		"HH", "LL", "H", "L", "LSH", "LSL",
		"Hi", "Lo", "HiHi", "LoLo", "Fail",
	):
		return False

	# Sensor PV leaf is named Value (…/HSS-Pumps Pressure/Value on RCP1).
	if n == "Value":
		if "HSS" in dev:
			return 145.0
		if "HSL" in dev:
			return 42.0
		if "LSL" in dev:
			return 28.0
		if "LSS" in dev:
			return 18.0
		# Non-sensor leaves named Value are rare under RCP1 — leave numeric 0.
		return 0.0

	if n in ("Amps", "FLA"):
		if dev == "COMP 6":
			return 0.0
		if dev == "COMP 1":
			return 48.0
		if dev == "COMP 4":
			return 36.0
		if dev == "COMP 5":
			return 41.0
		if dev == "COMP 7":
			return 52.0
		return 40.0
	if n == "SVP":
		if dev == "COMP 6":
			return 0.0
		if dev == "COMP 7":
			return 72.0
		return 55.0
	if n in ("Level", "Pressure"):
		if "HTR" in dev:
			return 62.0
		if "LTR" in dev:
			return 48.0
		if "HPR" in dev:
			return 55.0
		return 50.0
	if n.endswith("_SP") or n.endswith("SP"):
		return 25.0
	if "bool" in dt:
		return False
	if "int" in dt or "long" in dt or "short" in dt or "byte" in dt:
		return 0
	if "string" in dt:
		return ""
	return 0.0


def listRcp1AtomicTags():
	"""Return list of full paths for AtomicTags under RCP1 (excludes Simulate)."""
	paths = []
	seen = set()
	candidates = []

	# Prefer one recursive browse (no tagType filter — that often returns empty).
	candidates = _browseResults(RCP1_ROOT, {"recursive": True})
	if not candidates:
		# Fallback: walk folders one level at a time
		stack = [RCP1_ROOT]
		while stack:
			folder = stack.pop()
			for br in _browseResults(folder):
				name = _browseName(br)
				full = _browseFullPath(br)
				if not name or not full:
					continue
				fp = _normalizePath(full)
				tt = _browseTagType(br)
				isFolder = tt == "Folder"
				if not tt:
					try:
						cfg = system.tag.getConfiguration(fp, False)[0]
						isFolder = str(cfg.get("tagType", "")) == "Folder"
						tt = str(cfg.get("tagType", ""))
					except:
						isFolder = False
				if isFolder:
					stack.append(fp)
				else:
					candidates.append(br)

	for br in candidates:
		name = _browseName(br)
		full = _browseFullPath(br)
		if not name or not full:
			continue
		if name in EXCLUDE_NAMES:
			continue
		fp = _normalizePath(full)
		if fp in seen:
			continue
		tt = _browseTagType(br)
		if tt and tt not in ("AtomicTag", "atomic", "Atomic"):
			# Still confirm via config — browse type strings can vary
			pass
		try:
			cfg = system.tag.getConfiguration(fp, False)[0]
			if str(cfg.get("tagType", "")) != "AtomicTag":
				continue
			if str(cfg.get("name", name)) in EXCLUDE_NAMES:
				continue
		except Exception as e:
			logger.warn("skip %s: %s" % (fp, str(e)))
			continue
		seen.add(fp)
		paths.append(fp)

	paths.sort()
	logger.info("listRcp1AtomicTags found %d" % len(paths))
	return paths


def _cachePut(tagPath, opcItemPath, opcServer, documentation):
	_opcCache[str(tagPath)] = {
		"opcItemPath": opcItemPath,
		"opcServer": opcServer or OPC_SERVER,
		"documentation": documentation if documentation is not None else "",
	}


def _resolveOpc(tagPath, cfg):
	"""Resolve opcItemPath/opcServer/cleanDoc from cache, cfg, or documentation stash."""
	cached = _opcCache.get(str(tagPath))
	opcItemPath = None
	opcServer = OPC_SERVER
	documentation = ""

	if cached:
		opcItemPath = cached.get("opcItemPath")
		opcServer = cached.get("opcServer") or OPC_SERVER
		documentation = cached.get("documentation") or ""

	if not opcItemPath:
		opcItemPath = cfg.get("opcItemPath")
		opcServer = cfg.get("opcServer") or OPC_SERVER
		documentation = cfg.get("documentation") or ""

	stashed, cleanDoc = _parseOpcFromDocumentation(cfg.get("documentation"))
	if stashed:
		opcItemPath = opcItemPath or stashed
		documentation = cleanDoc
	elif not cached:
		documentation = cfg.get("documentation") or ""

	return opcItemPath, opcServer, documentation


def _configureOne(parent, cfg):
	try:
		system.tag.configure(parent, [cfg], "o")
		return True
	except Exception as e:
		logger.error("configure %s/%s failed: %s" % (parent, cfg.get("name"), str(e)))
		return False


def toMemory(tagPaths=None):
	"""Convert RCP1 AtomicTags (except Simulate) to Memory; stash OPC paths."""
	if tagPaths is None:
		tagPaths = listRcp1AtomicTags()
	ok = 0
	fail = 0
	for tagPath in tagPaths:
		parent, name = _parentAndName(tagPath)
		try:
			cfg = system.tag.getConfiguration(tagPath, False)[0]
		except Exception as e:
			logger.warn("getConfiguration %s: %s" % (tagPath, str(e)))
			fail += 1
			continue

		dataType = cfg.get("dataType") or "Float4"
		opcItemPath = cfg.get("opcItemPath")
		opcServer = cfg.get("opcServer") or OPC_SERVER
		documentation = cfg.get("documentation") or ""

		# Prefer live OPC path; fall back to prior stash/cache
		resolvedPath, resolvedServer, cleanDoc = _resolveOpc(tagPath, cfg)
		if opcItemPath:
			_cachePut(tagPath, opcItemPath, opcServer, documentation)
			stashDoc = _stashDocumentation(opcItemPath, documentation)
			server = opcServer
			path = opcItemPath
		elif resolvedPath:
			_cachePut(tagPath, resolvedPath, resolvedServer, cleanDoc)
			stashDoc = _stashDocumentation(resolvedPath, cleanDoc)
			server = resolvedServer
			path = resolvedPath
		else:
			logger.warn("no opcItemPath for %s — skipping stash" % tagPath)
			stashDoc = documentation
			path = ""
			server = OPC_SERVER

		# Prefer live Good OPC value; otherwise seed a readable demo value.
		live = _readCurrentValue(tagPath, dataType, name)
		try:
			qv = system.tag.readBlocking([tagPath])[0]
			qual = getattr(qv, "quality", None)
			good = False
			if qual is not None and hasattr(qual, "isGood"):
				good = bool(qual.isGood())
			elif qual is not None:
				good = str(qual).upper().find("GOOD") >= 0
		except:
			good = False
		# Prefer live Good OPC; still replace null / empty travel timer so SIM HMI is usable.
		demo = _demoValue(name, dataType, tagPath)
		if not good or live is None:
			value = demo
		elif name == "TravelTime" and (live == 0 or live == 0.0):
			value = demo
		else:
			value = live
		newCfg = {
			"name": name,
			"tagType": "AtomicTag",
			"valueSource": "memory",
			"dataType": dataType,
			"opcItemPath": "",
			"opcServer": "",
			"documentation": stashDoc,
			"value": value,
			"defaultValue": value,
		}
		# Preserve metadata when present
		if cfg.get("metadata") is not None:
			newCfg["metadata"] = cfg.get("metadata")
		if cfg.get("formatString") is not None:
			newCfg["formatString"] = cfg.get("formatString")
		if cfg.get("engUnit") is not None:
			newCfg["engUnit"] = cfg.get("engUnit")

		if _configureOne(parent, newCfg):
			ok += 1
			if path:
				_cachePut(tagPath, path, server, cleanDoc if opcItemPath else (cleanDoc or documentation))
		else:
			fail += 1

	# Second pass: force demo values on key leaves (configure defaultValue can lag).
	seedPaths = []
	seedVals = []
	seedNames = set([
		"Rung", "Status", "Val_Sts", "Comm", "Started", "AutoEN",
		"Alm", "Failed", "Cutout", "Alm_FailToStart", "Alm_IOFault", "Sts_FailToStart",
		"Amps", "FLA", "SVP", "Level", "Pressure", "Value",
		"Color", "CP_Mode", "SV_Mode",
		"Hi", "Lo", "HiHi", "LoLo", "Fail", "LSH", "LSL", "H", "L", "HH", "LL",
		# Valve faceplate Controls: modes, LS, travel timer
		"OPER", "PROG", "MAINT", "TravelTime", "OpenLS", "ClosedLS",
	])
	for tagPath in tagPaths:
		_parent, name = _parentAndName(tagPath)
		if name not in seedNames:
			continue
		try:
			cfg = system.tag.getConfiguration(tagPath, False)[0]
			dt = cfg.get("dataType") or "Float4"
			seedPaths.append(tagPath)
			seedVals.append(_demoValue(name, dt, tagPath))
		except:
			pass
	if seedPaths:
		try:
			system.tag.writeBlocking(seedPaths, seedVals)
			logger.info("seeded %d demo values for running HMI" % len(seedPaths))
		except Exception as e:
			logger.warn("seed write failed: %s" % str(e))

	_seedInterlockDemo()

	logger.info("RCP1 Simulate ON — memory=%d fail=%d" % (ok, fail))
	_logSampleSources("after-toMemory")
	return ok, fail


def _seedInterlockDemo():
	"""Named CondTxt + status bits + Alm_* for Main Liq SV faceplate demos."""
	# Prefer Valves/ folder layout; fall back to flat Machine Room (main).
	plantBase = "[default]Plant/Machine Room/Valves/Main Liq SV"
	try:
		qv = system.tag.readBlocking([plantBase + "/Failed/Value"])
		if str(qv[0].quality) != "Good":
			plantBase = "[default]Plant/Machine Room/Main Liq SV"
	except Exception:
		plantBase = "[default]Plant/Machine Room/Main Liq SV"
	plantIlk = plantBase + "/Interlock"
	rcpIlk = "[default]RCP1/Main Liq SV/Interlock"
	rcpBase = "[default]RCP1/Main Liq SV"
	conds = {
		"00": "Open Travel Timeout",
		"01": "Close Travel Timeout",
		"02": "Not in Auto",
		"03": "Permissive Lost",
	}
	paths = []
	vals = []
	for nn, text in conds.items():
		paths.append("%s/Cfg_CondTxt%s/Value" % (plantIlk, nn))
		vals.append(text)
	paths.extend([
		rcpIlk + "/Sts_Intlk",
		rcpIlk + "/Sts_IntlkOK",
		rcpIlk + "/Sts_NBIntlkOK",
		rcpIlk + "/Sts_FirstOut",
		rcpIlk + "/Cfg_Bypassable",
		rcpIlk + "/Rdy_Reset",
	])
	vals.extend([5, False, True, 1, 15, True])
	for alm in ("Alm_IOFault", "Alm_FullStall", "Alm_TransitStall", "Alm_IntlkTrip"):
		paths.append("%s/%s" % (rcpBase, alm))
		vals.append(False)
	try:
		system.tag.writeBlocking(paths, vals)
		logger.info("seeded Main Liq SV interlock/alarm demo (%d tags)" % len(paths))
	except Exception as e:
		logger.warn("interlock demo seed failed: %s" % str(e))


def toOpc(tagPaths=None):
	"""Restore RCP1 AtomicTags to OPC UA using cached / stashed paths."""
	if tagPaths is None:
		tagPaths = listRcp1AtomicTags()
	ok = 0
	fail = 0
	for tagPath in tagPaths:
		parent, name = _parentAndName(tagPath)
		try:
			cfg = system.tag.getConfiguration(tagPath, False)[0]
		except Exception as e:
			logger.warn("getConfiguration %s: %s" % (tagPath, str(e)))
			fail += 1
			continue

		opcItemPath, opcServer, documentation = _resolveOpc(tagPath, cfg)
		if not opcItemPath:
			logger.warn("cannot restore OPC for %s — no stashed path" % tagPath)
			fail += 1
			continue

		dataType = cfg.get("dataType") or "Float4"
		newCfg = {
			"name": name,
			"tagType": "AtomicTag",
			"valueSource": "opc",
			"dataType": dataType,
			"opcItemPath": opcItemPath,
			"opcServer": opcServer or OPC_SERVER,
			"documentation": documentation,
		}
		if cfg.get("metadata") is not None:
			newCfg["metadata"] = cfg.get("metadata")
		if cfg.get("formatString") is not None:
			newCfg["formatString"] = cfg.get("formatString")
		if cfg.get("engUnit") is not None:
			newCfg["engUnit"] = cfg.get("engUnit")

		if _configureOne(parent, newCfg):
			ok += 1
			_cachePut(tagPath, opcItemPath, opcServer or OPC_SERVER, documentation)
		else:
			fail += 1

	logger.info("RCP1 Simulate OFF — opc=%d fail=%d" % (ok, fail))
	_logSampleSources("after-toOpc")
	return ok, fail


def applySimulate(simulate):
	"""
	Apply Simulate mode.
	True  → Memory tags (demo / faceplate writes)
	False → OPC UA tags (Ignition OPC UA Server, device RCP1)
	"""
	wantSim = bool(simulate)
	logger.info("applySimulate(%s)" % wantSim)
	_logSampleSources("before-apply")
	if wantSim:
		return toMemory()
	return toOpc()
