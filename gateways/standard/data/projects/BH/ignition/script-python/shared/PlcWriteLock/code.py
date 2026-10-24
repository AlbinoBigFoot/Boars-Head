# PLC write lock v2 (2026-10-23, .cursor/tasks/plc-write-lock - this file is the source of the BH project library
# shared.PlcWriteLock; the builder copies it to ignition/script-python/shared/PlcWriteLock/code.py). Docs:
# docs/plc-write-lock.md.
#
# User (2026-10-23): "I don't need that PLC Write Lock view. Remove it, delete the view. Just have a boolean under _Config
# that allows me to unlock and lock the read only param of each tag."
#
# ONE boolean, [default]_Config/PlcWriteLock/Locked (true = locked), drives readOnly on every tag that reads the RCP1
# controller (a LIVE PRODUCTION PLC):
#   - every AtomicTag under [default]_RCP1_ (the browsed controller tags);
#   - every OPC member of the UDT DEFINITIONS in TYPE_FOLDERS (PLC/** incl. Modules / Controllers / Sites, PLC_Ref,
#     Devices, Units) - set on the definition (_types_), so every instance inherits it; no per-instance overrides.
# Ignition 8.3 cannot bind a tag's readOnly property to another tag's value (an Expression / Tag binding on readOnly is
# dropped on import - checked 2026-10-23), so the gateway tag-change event 'plcWriteLock' on the boolean calls
# onLockChange(), which applies readOnly = Locked (only the tags whose readOnly differs; in chunks of CHUNK tags, in one
# background worker that re-reads the boolean until it settles) and logs each flip with counts.
# Fail-safe: a bad / null / unreadable boolean counts as LOCKED; on gateway startup (JVM uptime < STARTUP_S) the lock is
# forced: Locked is written true and readOnly re-asserted. HMI writes are refused while locked (writeAllowed: shared.Audit
# .writeTag / shared.Alerts.confirmApplyWrite / shared.ValveCommands). readOnly is the SOFT layer; the HARD layer is the
# OPC UA server device permission (Browse/Read only for RCP1, .cursor/tasks/rcp1-write-block) - a PLC write needs BOTH
# Locked=false AND the server block removed.
# Testing: the separate boolean TEST_LOCKED + tag-change event 'plcWriteLockTest' (onTestChange) drive only TEST_ROOT
# memory tags and the TEST_TYPES UDT folder - they never touch [RCP1] / _RCP1_.
# Configuration only: the configure payloads carry name + readOnly, never a value; nothing here writes a PLC value.

BASE = "[default]_Config/PlcWriteLock/"
T_LOCKED = BASE + "Locked"
RCP1_ROOT = "[default]_RCP1_"
TYPE_FOLDERS = ("PLC", "PLC_Ref", "Devices", "Units")
TEST_LOCKED = BASE + "_Test/Locked"
TEST_ROOT = BASE + "_Test/Tags"
TEST_TYPES = ("_PlcWriteLockTest",)
CHUNK = 5000
CHUNK_PAUSE_MS = 2000
STARTUP_S = 600
_log = system.util.getLogger("shared.PlcWriteLock")


def _text(v):
	if v is None:
		return u""
	try:
		return unicode(v).strip()
	except Exception:
		return u""


def _norm(path):
	"""[default]-qualified tag path with '/' separators and '..' segments resolved."""
	p = _text(path).replace("\\", "/")
	if not p:
		return p
	if not p.startswith("["):
		p = "[default]" + p.lstrip("/")
	prov, _, rest = p.partition("]")
	out = []
	for seg in rest.split("/"):
		if seg == "..":
			if out:
				out.pop()
		elif seg not in ("", "."):
			out.append(seg)
	return prov + "]" + "/".join(out)


def _under(path, scope):
	return bool(scope) and (path == scope or path.startswith(scope + "/"))


def _isRcp1(path):
	return _under(path, RCP1_ROOT)


# ------------------------------------------------------------------------------------------------ state
def _lockedFrom(qv):
	"""Fail-safe: anything but a good, non-null False counts as locked."""
	try:
		return (not qv.quality.isGood()) or qv.value is None or bool(qv.value)
	except Exception:
		return True


def status():
	"""{locked}. Fail-safe: unreadable = locked."""
	try:
		return {"locked": _lockedFrom(system.tag.readBlocking([T_LOCKED])[0])}
	except Exception:
		return {"locked": True}


def isLocked():
	return status()["locked"]


# ------------------------------------------------------------------------------------------------ write guard
def resolve(tagPath, hops=6):
	"""(final tag path, kind) for a write target, following reference tags to their source. kind: rcp1-tag (under
	[default]_RCP1_), rcp1-opc ([RCP1] OPC item elsewhere), opc, memory, expr, reference, reference-param, unknown, ..."""
	p = _norm(tagPath)
	leaf = p.rsplit("/", 1)[-1]
	if "." in leaf:
		p = p.rsplit(".", 1)[0]          # a property write (Tag.Enabled ...) concerns the tag itself
	cur = p
	for _ in range(hops):
		if _isRcp1(cur):
			return cur, "rcp1-tag"
		try:
			cfg = system.tag.getConfiguration(cur, False)[0]
		except Exception:
			return cur, "unknown"
		vs = _text(cfg.get("valueSource"))
		if vs == "opc":
			ip = _text(cfg.get("opcItemPath"))
			if "[RCP1]" not in ip and ("{" in ip or "bindType" in ip):
				# parameterised OPC item (UDT member, e.g. [{PlcDevice}]HMI_Ltu_Clear): the raw config shows the binding,
				# the resolved item path is on the OPCItemPath property (2026-10-24, LTU Reset Count)
				try:
					ip = _text(system.tag.readBlocking([cur + ".OPCItemPath"])[0].value) or ip
				except Exception:
					pass
			return cur, ("rcp1-opc" if "[RCP1]" in ip else "opc")
		if vs == "reference":
			src = _text(cfg.get("sourceTagPath"))
			if not src:
				return cur, "reference"
			if "{" in src:
				return cur, "reference-param"
			if src.startswith("[.]"):
				src = cur.rsplit("/", 1)[0] + "/" + src[3:]
			elif src.startswith("[~]"):
				src = cur.split("]", 1)[0] + "]" + src[3:]
			cur = _norm(src)
			continue
		return cur, (vs or "other")
	return cur, "too-deep"


def writeAllowed(tagPath, who=""):
	"""False when a write to tagPath would reach the RCP1 controller while Locked (or the lock is unreadable).
	Unresolvable targets that name RCP1 count as RCP1."""
	try:
		final, kind = resolve(tagPath)
	except Exception:
		final, kind = _norm(tagPath), "unknown"
	rcp1 = kind in ("rcp1-tag", "rcp1-opc")
	if not rcp1 and kind in ("unknown", "reference-param", "too-deep"):
		rcp1 = "RCP1_" in _norm(tagPath) or "[RCP1]" in final or "RCP1_" in final
	if not rcp1:
		return True
	if not isLocked():
		return True
	_log.info("Refused write %s -> %s (%s): PLC writes locked%s" % (tagPath, final, kind, (" - " + who) if who else ""))
	return False


# ------------------------------------------------------------------------------------------------ tag store (files)
def _dataDir():
	try:
		from com.inductiveautomation.ignition.gateway import IgnitionGateway
		return unicode(IgnitionGateway.get().getSystemManager().getDataDir().getAbsolutePath())
	except Exception:
		return u"/usr/local/bin/ignition/data"


def _resDir(kind):
	import os
	return os.path.join(_dataDir(), "config", "resources", "core", "ignition", kind, "default")


def _readJson(path):
	try:
		with open(path) as fh:
			return system.util.jsonDecode(fh.read())     # Java parser (Jython's json module is slow)
	except Exception:
		return None


def _unesc(rel):
	return rel.replace("%3a", ":").replace("%3A", ":").replace("%20", " ")


def storeTags(root):
	"""{tag path: readOnly} for every AtomicTag under a [default] folder, from the file-based tag store
	(tag-definition/default/<root>/**/tags.json + udts.json) - far faster than browsing 35K tags."""
	import os
	segs = root.split("]", 1)[1].split("/")
	out = {}

	def walk(base, lst):
		for t in lst or []:
			name = t.get("name")
			if not name:
				continue
			if t.get("tagType") == "AtomicTag":
				out[base + "/" + name] = bool(t.get("readOnly"))
			elif t.get("tagType") == "Folder" and t.get("tags"):
				walk(base + "/" + name, t.get("tags"))
	# deepest existing directory on the path; the rest of the path may be Folder entries inside its tags.json
	top, depth = _resDir("tag-definition"), 0
	for k in range(len(segs), 0, -1):
		cand = os.path.join(_resDir("tag-definition"), *segs[:k])
		if os.path.isdir(cand):
			top, depth = cand, k
			break
	if depth < len(segs):
		lst = _readJson(os.path.join(top, "tags.json")) or []
		for seg in segs[depth:]:
			node = next((t for t in lst if t.get("name") == seg), None)
			if node is None:
				return out
			lst = node.get("tags") or []
		walk(root, lst)
		return out
	for dp, dn, fn in os.walk(top):
		rel = os.path.relpath(dp, top).replace(os.sep, "/")
		base = root if rel in (".", "") else root + "/" + _unesc(rel)
		if "tags.json" in fn:
			walk(base, _readJson(os.path.join(dp, "tags.json")))
	return out


def typeMembers(folders, opcOnly=True):
	"""{'[default]_types_/<folder>/<udt>/<member path>': readOnly} for the OPC members (opcOnly) - or every memory /
	OPC member (test types) - defined in the UDT definitions under the given type folders (sub folders included).
	Members of nested UDT instances are skipped: they come from their own type (no per-instance overrides)."""
	import os
	top = _resDir("tag-type-definition")
	out = {}

	def walk(base, lst, inType):
		for t in lst or []:
			name = t.get("name")
			tt = t.get("tagType")
			if not name:
				continue
			p = base + "/" + name
			if tt == "UdtType":
				walk(p, t.get("tags"), True)
			elif tt == "UdtInstance":
				continue
			elif tt == "Folder":
				walk(p, t.get("tags"), inType)
			elif tt == "AtomicTag" and inType:
				vs = _text(t.get("valueSource"))
				if vs == "opc" or (not opcOnly and vs in ("memory", "opc")):
					out[p] = bool(t.get("readOnly"))
	for folder in folders:
		fdir = os.path.join(top, *folder.split("/"))
		for dp, dn, fn in os.walk(fdir):
			if "udts.json" not in fn:
				continue
			rel = os.path.relpath(dp, top).replace(os.sep, "/")
			walk("[default]_types_/" + _unesc(rel), _readJson(os.path.join(dp, "udts.json")), False)
	return out


# ------------------------------------------------------------------------------------------------ apply
def _chunks(paths):
	"""[{parent: [names]}, ...] - whole parent folders per chunk, about CHUNK tags each."""
	byParent = {}
	for p in paths:
		parent, name = p.rsplit("/", 1)
		byParent.setdefault(parent, []).append(name)
	out, cur, n = [], {}, 0
	for parent in sorted(byParent):
		cur[parent] = byParent[parent]
		n += len(byParent[parent])
		if n >= CHUNK:
			out.append(cur)
			cur, n = {}, 0
	if cur:
		out.append(cur)
	return out


def _setReadOnly(paths, readOnly):
	"""Merge {name, readOnly} per parent (configuration only), CHUNK tags at a time with a pause between chunks.
	Returns the paths whose configure call did not report Good."""
	from java.lang import Thread
	bad = []
	chunks = _chunks(paths)
	for k, chunk in enumerate(chunks):
		if k:
			Thread.sleep(CHUNK_PAUSE_MS)
		for parent in sorted(chunk):
			tags = [{"name": n, "readOnly": bool(readOnly)} for n in chunk[parent]]
			res = system.tag.configure(parent, tags, "m")
			for t, q in zip(tags, res):
				try:
					good = q.isGood()
				except Exception:
					good = "Good" in str(q)
				if not good:
					bad.append(parent + "/" + t["name"])
		if len(chunks) > 1:
			_log.info("readOnly=%s chunk %d/%d done (%d bad so far)" % (bool(readOnly), k + 1, len(chunks), len(bad)))
	return bad


class _Target(object):
	"""What one boolean drives: the real RCP1 set, or the memory test set (never both)."""
	def __init__(self, name, flag, roots, typeFolders, opcOnly, skip=()):
		self.name, self.flag, self.roots, self.typeFolders, self.opcOnly, self.skip = \
			name, flag, roots, typeFolders, opcOnly, skip

	def items(self, readOnly):
		"""{path: readOnly} of every driven tag / member (skip: never unlocked, e.g. driver diagnostics)."""
		out = {}
		for root in self.roots:
			for p, ro in storeTags(root).items():
				if not readOnly and any(_under(p, s) for s in self.skip):
					continue
				out[p] = ro
		out.update(typeMembers(self.typeFolders, self.opcOnly))
		return out


REAL = _Target("PLC", T_LOCKED, (RCP1_ROOT,), TYPE_FOLDERS, True, (RCP1_ROOT + "/_Diagnostics_",))
TEST = _Target("TEST", TEST_LOCKED, (TEST_ROOT,), TEST_TYPES, False)



def apply(target, readOnly, why):
	"""readOnly on every driven tag of target whose readOnly differs; returns {total, changed, bad, mismatch}."""
	import time
	t0 = time.time()
	items = target.items(readOnly)
	todo = sorted(p for p, ro in items.items() if ro != bool(readOnly))
	bad = _setReadOnly(todo, readOnly) if todo else []
	res = {"total": len(items), "changed": len(todo) - len(bad), "bad": len(bad), "seconds": round(time.time() - t0, 1)}
	_log.info("%s write lock (%s): Locked=%s -> readOnly=%s on %d tags / UDT members: %d changed, %d already, %d bad, "
		"%.1f s%s" % (target.name, why, bool(readOnly), bool(readOnly), res["total"], res["changed"],
			res["total"] - len(todo), res["bad"], res["seconds"], (" - bad: %s" % bad[:5]) if bad else ""))
	return res


def _shared(name):
	"""(Java lock, Java pending flag) per target, kept in the gateway globals so they survive project script reloads
	(each project save restarts the tag-change script; a module-level lock would let two workers run at once)."""
	g = system.util.getGlobals()
	key = "shared.PlcWriteLock." + name
	st = g.get(key)
	if st is None:
		from java.util.concurrent.locks import ReentrantLock
		from java.util.concurrent.atomic import AtomicBoolean
		st = g.setdefault(key, (ReentrantLock(), AtomicBoolean(False)))
	return st


def _worker(target, why):
	"""Applies until the boolean stops moving (one worker per target, gateway-wide; a flip during a run is picked up
	after it - the final state always follows the latest boolean value)."""
	lock, pending = _shared(target.name)
	pending.set(True)
	while True:
		if not lock.tryLock():
			return                  # the running worker re-reads the boolean when it finishes
		try:
			while pending.getAndSet(False):
				want = _lockedFrom(system.tag.readBlocking([target.flag])[0])
				try:
					apply(target, want, why)
				except Exception as e:
					_log.error("%s write lock apply (readOnly=%s) failed: %s" % (target.name, want, e))
				why = "re-check"
		finally:
			lock.unlock()
		if not pending.get():       # a change that arrived between the last check and unlock() is not lost
			return


def _uptimeS():
	try:
		from java.lang.management import ManagementFactory
		return ManagementFactory.getRuntimeMXBean().getUptime() / 1000.0
	except Exception:
		return 0.0


def _onChange(target, initialChange, newValue, startupForce):
	locked = _lockedFrom(newValue)
	why = "flip"
	if initialChange:
		why = "script start"
		if startupForce and _uptimeS() < STARTUP_S:
			why = "gateway startup (fail-safe lock)"
			if not locked:
				system.tag.writeBlocking([target.flag], [True])
	elif locked:
		try:
			bad = not newValue.quality.isGood() or newValue.value is None
		except Exception:
			bad = True
		if bad:
			why = "bad / null lock value (fail-safe lock)"
	_log.info("%s write lock %s: Locked=%s" % (target.name, why, locked))
	system.util.invokeAsynchronous(lambda: _worker(target, why))


def onLockChange(initialChange, newValue, event=None):
	"""Gateway tag-change event 'plcWriteLock' on [default]_Config/PlcWriteLock/Locked (value + quality changes)."""
	_onChange(REAL, initialChange, newValue, True)


def onTestChange(initialChange, newValue, event=None):
	"""Gateway tag-change event 'plcWriteLockTest' on the TEST boolean: drives only the memory test tags / test types."""
	_onChange(TEST, initialChange, newValue, False)


def counts(which="PLC"):
	"""Read-only summary {total, readOnly, writable} of a target from the tag store files (verification)."""
	target = REAL if which == "PLC" else TEST
	items = target.items(True)
	ro = sum(1 for v in items.values() if v)
	return {"total": len(items), "readOnly": ro, "writable": len(items) - ro}


def selfTest():
	"""Read-only check of the guards: nothing is written."""
	out = {"status": status()}
	samples = [
		"[default]_RCP1_/Controller:Global/HTPS_SET",
		"[default]_RCP1_/Controller:Global/AD/AD_1_/Cfg_0StText",
		"[default]Boars_Head/GrovePort/Machine Room/Valves/Main Liq SV/Cmd_Open/Value",
		TEST_ROOT + "/TEST_PUMP/OCmd_Start",
	]
	out["writeAllowed"] = dict((p, {"allowed": writeAllowed(p, "selfTest"), "resolve": list(resolve(p))}) for p in samples)
	return out
