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
	if leaf == "Rung":
		fallback = True
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
		]
	for tp in samplePaths:
		try:
			cfg = system.tag.getConfiguration(tp, False)[0]
			vs = cfg.get("valueSource")
			opc = cfg.get("opcItemPath") or ""
			doc = str(cfg.get("documentation") or "")
			stash = "yes" if doc.startswith(OPC_MARKER) else "no"
			qv = system.tag.readBlocking([tp])[0]
			qual = str(getattr(qv, "quality", ""))
			logger.info(
				"%s sample %s valueSource=%s opc=%s stash=%s quality=%s value=%s"
				% (label, tp, vs, opc, stash, qual, getattr(qv, "value", None))
			)
		except Exception as e:
			logger.warn("%s sample %s failed: %s" % (label, tp, str(e)))


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

		value = _readCurrentValue(tagPath, dataType, name)
		newCfg = {
			"name": name,
			"tagType": "AtomicTag",
			"valueSource": "memory",
			"dataType": dataType,
			"opcItemPath": "",
			"opcServer": "",
			"documentation": stashDoc,
			"value": value,
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

	logger.info("RCP1 Simulate ON — memory=%d fail=%d" % (ok, fail))
	_logSampleSources("after-toMemory")
	return ok, fail


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
