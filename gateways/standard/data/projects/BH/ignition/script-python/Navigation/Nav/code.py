#Navigation
# Nav items without a view (no page/viewPath, or a page missing from page-config) land here.
NO_VIEW_PAGE = "/no-view"
_routeCache = {"ts": 0.0, "routes": None}


def _pageRoutes():
	"""page-config URLs for this project, cached 60 s. Empty set when they can't be read."""
	import time
	now = time.time()
	if _routeCache["routes"] is not None and now - _routeCache["ts"] < 60:
		return _routeCache["routes"]
	routes = set()
	try:
		info = system.perspective.getProjectInfo()
		for pc in info.get("pageConfigs") or info.get("pages") or []:
			url = pc.get("url") or pc.get("path")
			if url:
				routes.add(str(url))
	except:  # bare: outside a session (WebDev, shared.Globe.relay) getProjectInfo raises a Java exception
		pass
	if not routes:
		try:
			import os
			from com.inductiveautomation.ignition.gateway import IgnitionGateway
			dataDir = IgnitionGateway.get().getSystemManager().getDataDir().getAbsolutePath()
			path = os.path.join(dataDir, "projects", system.util.getProjectName(),
				"com.inductiveautomation.perspective", "page-config", "config.json")
			f = open(path)
			try:
				cfg = system.util.jsonDecode(f.read())
			finally:
				f.close()
			routes = set(str(k) for k in (cfg.get("pages") or {}).keys())
		except Exception as e:
			system.util.getLogger("Navigation.Nav").warn("page-config routes unavailable: %s" % e)
	_routeCache["ts"] = now
	_routeCache["routes"] = routes
	return routes


def _hasRoute(page):
	routes = _pageRoutes()
	# Unknown route list -> trust the page (previous behavior) rather than blocking navigation.
	if (not routes) or page in routes:
		return True
	# plc-rack-io (2026-10-23): parameterised page-config routes - /operations/plcs/:plc matches /operations/plcs/RCP1
	# (the nav item for a PLC rack page; an exact match alone made the click go nowhere)
	segs = str(page or "").strip("/").split("/")
	for r in routes:
		if ":" not in r:
			continue
		rs = r.strip("/").split("/")
		if len(rs) == len(segs) and all(a.startswith(":") or a == b for a, b in zip(rs, segs)):
			return True
	return False


def navigate(data=None):
	"""Navigate from the plant nav tree.

	BH tree item data shape:
	  action: 'page' | 'faceplate' | '' (no view -> stays on the current page)
	  page: page-config path e.g. '/evaporators'
	  viewPath: Perspective view path (faceplate or legacy SPA)
	  tagPath: device UDT path for faceplates / overview context

	Also maps AdhocTrend viewPaths to page-config URLs; other payloads keep
	the Lightspeed /data/<encoded> SPA style.
	Returns True when it navigated (or opened a faceplate), False when the item has nowhere to go.
	"""
	if data is None:
		data = {}
	try:
		action = data.get("action") or ""
	except Exception:
		action = ""
	try:
		page = data.get("page") or ""
	except Exception:
		page = ""
	try:
		viewPath = data.get("viewPath") or ""
	except Exception:
		viewPath = ""
	try:
		tagPath = data.get("tagPath") or ""
	except Exception:
		tagPath = ""
	# enterprise-demo-nav / local-groveport-mode: switch on -> data.demoPage (Boars Head opens the globe),
	# switch off -> data.localPage (Boars Head / Groveport open the Groveport Utility Overview)
	try:
		if data.get("demoPage") or data.get("localPage"):
			alt = data.get("demoPage") if demoEnabled() else data.get("localPage")
			if alt:
				page = alt
	except Exception:
		pass

	# Device instance → faceplate popup
	if action == "faceplate" or (viewPath and viewPath.startswith("01_Popups/00_Faceplates/")):
		title = tagPath.split("/")[-1] if tagPath else None
		popupId = "nav-fp-%s" % (tagPath or viewPath)
		# security-tiers: False when the session may not open faceplates
		return Navigation.Faceplate.openFaceplate(popupId, tagPath, viewPath, False, title) is not False

	# Explicit page-config route (device type / devices overview / ops).
	# A page with no page-config route, or a node with no page/view at all, goes nowhere (2026-09-24:
	# folders like Freezer / Groveport no longer open the NoViewPath placeholder).
	if action == "page" or page:
		if page and _hasRoute(page):
			system.perspective.navigate(page=page)
			return True
		return False

	# Device leaf (tagPath only, e.g. Machine Room > ... > Tanks > HTR): open its faceplate (user 2026-10-01)
	if tagPath and not viewPath and not page:
		return Navigation.Faceplate.openDevice(tagPath, data.get("label") if hasattr(data, "get") else None)

	if not viewPath and not page:
		return False

	bh_pages = {
		"98_Configuration/AdhocTrend/Trend": "/trending",
		"98_Configuration/AdhocTrend/UserSavedTrendConfig": "/trending/saved",
		"00_Pages/Boars Head/Evaporators/Overview": "/evaporators",
		"00_Pages/Boars Head/Evaporators/Graphic": "/evaporators/graphic",
		"00_Pages/Boars Head/Compressors/Overview": "/compressors",
		"00_Pages/Boars Head/Compressors/Graphic": "/compressors/graphic",
		"00_Pages/Boars Head/CoolingTowers/Overview": "/cooling-towers",
		"00_Pages/Boars Head/CoolingTowers/Graphic": "/cooling-towers/graphic",
		"00_Pages/Boars Head/Pumps/Overview": "/pumps",
		"00_Pages/Boars Head/Pumps/Graphic": "/pumps/graphic",
		"00_Pages/Boars Head/ExhaustFans/Overview": "/exhaust-fans",
		"00_Pages/Boars Head/ExhaustFans/Graphic": "/exhaust-fans/graphic",
		"00_Pages/Boars Head/Machine Room/Overview": "/machine-room",
		"00_Pages/Boars Head/Devices/Overview": "/devices",
		"00_Pages/Boars Head/Tanks/Overview": "/tanks",
		"00_Pages/Boars Head/Valves/Overview": "/valves",
		"00_Pages/Boars Head/Sensors/Overview": "/sensors",
		"00_Pages/Boars Head/Alarms/Summary": "/alarms",
		"00_Pages/Boars Head/Alarms/Journal": "/alarms/journal",
		"00_Pages/Boars Head/Operations/AuditLog": "/operations/audit",
	}
	if viewPath in bh_pages:
		system.perspective.navigate(page=bh_pages[viewPath])
		return True
	url = "/data/" + encodeUrlPayload(data)
	system.perspective.navigate(url)
	system.perspective.sendMessage(messageType="redirectUrl")
	return True

# URL PARAMETER ENCODING
# Needed something more readable than base64 for troubleshooting.
# May be best to revert to base64 or another encoding because a lot of cases need to be handled manually.
import urllib
import urlparse
import collections

def encodeUrlPayload(payload):
	# type: (Dict) -> str
	"""
	Encodes the payload with characters that are allowed in the url.
	"""
	cleanPayload = cleanObjForUrlEncoding(payload)
	return urllib.urlencode(cleanPayload)


def decodeUrlPayload(encodedPayload):
	# type: (str) -> Dict
	"""
	Inverse of encodeUrlPayload function.
	"""
	payload = {}
	for k, v in urlparse.parse_qsl(encodedPayload):
		# Nested objects get encoded as json.
		if v.startswith("[") and v.endswith("]") or v.startswith("{") and v.endswith("}"):
			payload[k] = system.util.jsonDecode(v)
		else:
			payload[k] = v
	return decodeSpecialCases(payload)


def decodeSpecialCases(obj):
	"""
	None is encoded as the string "None".
	CAUTION: This means any actual string "None" in the payload will be converted to None.
	Ampersands in strings were replaced during encoding.
	"""
	if obj == "None":
		return None
	if isinstance(obj, basestring):
		return obj.replace("qAMPq", "&") 
	if hasattr(obj, "items"):
		return dict(map(decodeSpecialCases, obj.iteritems()))
	if isinstance(obj, tuple):
		return tuple(map(decodeSpecialCases, obj))
	if isinstance(obj, collections.Iterable):  # Filter strings before this (they are iterable)
		return list(map(decodeSpecialCases, obj))
	return obj


def cleanObjForUrlEncoding(obj):
	"""
	urllib doesn't handle unicode, so convert before encoding.
	This also handles the conversion from perspective object to vanilla PyDictionary.
	"""
	if isinstance(obj, basestring):
		return str(obj.replace("&", "qAMPq"))  # Strings containing ampersands do not encode properly.
	if hasattr(obj, "items"):
		return dict(map(cleanObjForUrlEncoding, obj.iteritems()))
	if isinstance(obj, tuple):
		return tuple(map(cleanObjForUrlEncoding, obj))
	if isinstance(obj, collections.Iterable):
		return list(map(cleanObjForUrlEncoding, obj))
	if isinstance(obj, long):
		return int(obj)
	return obj
	
def findItemIndex(items, viewPath=None, tagPath=None, page=None, currentPath = []):
	"""Locate a tree index path by viewPath/tagPath and/or page-config route."""
	for index, item in enumerate(items):
		if 'data' in item:
			data = item['data']
			dataView = data.get('viewPath') or ''
			dataTag = data.get('tagPath') or ''
			dataPage = data.get('page') or ''
			viewOk = (viewPath is None or viewPath == '' or dataView == viewPath)
			tagOk = (tagPath is None or tagPath == '' or dataTag == tagPath)
			pageOk = (page is None or page == '' or dataPage == page)
			# Prefer an explicit match on at least one of viewPath or page
			if (viewPath or page) and viewOk and tagOk and pageOk:
				if (viewPath and dataView == viewPath) or (page and dataPage == page):
					if tagPath is None or tagPath == '' or dataTag == tagPath:
						return currentPath + [index]
		if 'items' in item:
			subPath = findItemIndex(item['items'], viewPath, tagPath, page, currentPath + [index])
			if subPath is not None:
				return subPath
	return None

# Libraries to identify Operating System
# Qualified Path to convert an alarm source path to a normal tagPath
import java.lang.System as System
import os
from com.inductiveautomation.ignition.common import QualifiedPath
# Double Clicking on Alarm Event on a Alarm Summary page will execute below alarmNavigation function and navigate to a respective alarm event device details view
def alarmNavigation(source = ''):
	tagPath = ''
	viewPath = ''
	osName = System.getProperty("os.name").lower()
	system.util.getLogger("Alarm Double Click Navigation").info(str(osName))
	projectName = system.util.getProjectName()
	filePath = ''
	if source != '':
		p = QualifiedPath.parse(source)
		provider = p.getPathComponent("prov")
		tagPath = p.getPathComponent("tag")
		unitPath = '/'.join(tagPath.split('/')[:5])
		tagPath = '[' + provider + ']' + unitPath
		data = findItemData(tagPath)
		if 'tagPath' in data.keys() and 'viewPath' in data.keys():
			Navigation.Nav.navigate(data)
		else:
			system.util.getLogger("Alarm Double Click Navigation").info("Data is empty, SourcePath doesn't match the tagPath in the Navigation Tree")
	else:
		system.util.getLogger("Alarm Double Click Navigation").info("Source is empty")
	
NAV_TAG_PATH = '[default]_Config/Navigation'

def _to_py(obj):
	"""Coerce Document / Java maps to plain Python via encode/decode."""
	if obj is None:
		return None
	if isinstance(obj, (dict, list)):
		return obj
	# Document text first: jsonEncode(Document) encodes only its keys ({"items": [...]} came back as ["items"],
	# so getNavItems() returned ['items'] - 2026-10-01)
	try:
		import json
		return json.loads(str(obj))
	except:
		pass
	try:
		return system.util.jsonDecode(system.util.jsonEncode(obj))
	except:
		pass
	try:
		return system.util.jsonDecode(str(obj))
	except:
		return None

def _as_items(obj):
	"""Document may be {items:[...]} or a bare list of tree nodes."""
	decoded = _to_py(obj)
	if decoded is None:
		return []
	if isinstance(decoded, list):
		return decoded
	if isinstance(decoded, dict):
		inner = decoded.get('items')
		if isinstance(inner, list):
			return inner
		if 'label' in decoded or 'data' in decoded:
			return [decoded]
	return []

def _deep_decode(node):
	"""Unwrap nested JSON strings that Document tags sometimes embed."""
	import json
	if isinstance(node, list):
		return [_deep_decode(n) for n in node]
	if isinstance(node, dict):
		out = {}
		for k in node.keys():
			out[k] = _deep_decode(node[k])
		return out
	if isinstance(node, basestring):
		s = node.strip()
		if s.startswith('{') or s.startswith('['):
			try:
				return _deep_decode(json.loads(s))
			except:
				pass
	return node

def _read_nav_items_from_tag():
	"""Read live Navigation Document; fall back to tag defaultValue if empty."""
	logger = system.util.getLogger("TreeDebug")
	tagPath = NAV_TAG_PATH
	try:
		qv = system.tag.readBlocking([tagPath])[0]
	except Exception, e:
		logger.error("Failed to read navigation tag: " + str(e))
		return []
	items = []
	if qv is not None and qv.quality.isGood() and qv.value is not None:
		items = _as_items(qv.value)
		items = _deep_decode(items) if items else []
	if items:
		return items
	try:
		cfg = system.tag.getConfiguration(tagPath, False)
		if cfg and len(cfg) > 0:
			dv = cfg[0].get('defaultValue')
			items = _as_items(dv)
			if items:
				items = _deep_decode(items)
				try:
					system.tag.writeBlocking([tagPath], [{'items': items}])
					logger.info("Restored Navigation tag from defaultValue")
				except:
					pass
				return items
	except Exception, e:
		logger.warn("Navigation defaultValue fallback failed: " + str(e))
	return []

NAV_CACHE_S = 60


def getNavItems():
	"""Full nav tree from the Document tag, cached gateway-wide for NAV_CACHE_S (nav edits show within a minute)."""
	import time
	globals_dict = system.util.getGlobals()
	cached = globals_dict.get("NavMasterTreeCache")
	# old cache shape was a bare list (and could hold ['items']); only trust {ts, items} with dict nodes
	if hasattr(cached, "get") and time.time() - cached.get("ts", 0) < NAV_CACHE_S:
		items = cached.get("items") or []
		if items and all(hasattr(i, "get") for i in items):
			return items
	items = _read_nav_items_from_tag()
	if items:
		globals_dict["NavMasterTreeCache"] = {"ts": time.time(), "items": items}
	return items

# enterprise-demo-nav: nodes with data.hidden stay out of the tree/titles unless they carry data.demo and the switch
# [default]_Config/DemoEnterpriseNav is on (Navigation Tree props.items transform does the same).
DEMO_TAG = "[default]_Config/DemoEnterpriseNav"


def demoEnabled():
	try:
		qv = system.tag.readBlocking([DEMO_TAG])[0]
		return bool(qv.value) if qv.quality.isGood() and qv.value is not None else False
	except Exception:
		return False


def _shown(data, demo):
	return not data.get("hidden") or bool(demo and data.get("demo"))

# Grouping folders left out of the page title (user 2026-10-01: "Groveport Machine Room Tanks").
TITLE_SKIP = set(["Boars Head", "Utility", "Devices", "Operations", "Admin", "Enterprise Operations"])
TITLE_HOME = "Boars Head International"
TITLE_LOCAL_HOME = "Groveport Utility Overview"


def pageTitle(path):
	"""Header title for a page from its nav tree position, grouping folders skipped:
	/machine-room -> 'Groveport Machine Room', /tanks -> 'Groveport Machine Room Tanks'. A device-type page is
	named after its tag folder (nav 'Comps' -> 'Compressors'). A node's data.title overrides the whole title."""
	import re
	path = str(path or "")
	if path in ("", "/"):
		# local-groveport-mode: '/' is the Utility Overview (the Header route guard moves it there)
		return TITLE_HOME if demoEnabled() else TITLE_LOCAL_HOME

	def search(items, chain):
		if hasattr(items, "get") and not isinstance(items, list):
			items = items.get("items")
		for item in items or []:
			if not hasattr(item, "get"):
				continue
			data = item.get("data") or {}
			if not hasattr(data, "get"):
				data = {}
			if not _shown(data, demo):
				continue
			here = chain + [(str(item.get("label") or ""), data)]
			if data.get("page") == path or (demo and data.get("demoPage") == path):
				return here
			found = search(item.get("items"), here)
			if found:
				return found
		return None

	demo = demoEnabled()
	chain = search(getNavItems(), []) or []
	if len(chain) == 1 and demo and chain[0][1].get("demoPage") == path:
		return TITLE_HOME
	if chain and str(chain[-1][1].get("title") or "").strip():
		return str(chain[-1][1].get("title")).strip()
	parts = []
	for i, (label, data) in enumerate(chain):
		if label in TITLE_SKIP:
			continue
		folder = re.sub(r"^\[[^\]]*\]", "", str(data.get("tagPath") or "")).rstrip("/").split("/")[-1]
		if i == len(chain) - 1 and folder and data.get("action") == "page":
			label = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", folder)
		parts.append(label)
	return " ".join(parts) or "Groveport"

def findItemData(tagPath):
	stack = list(Navigation.Nav.getNavItems())
	matchedItemData = {}
	matchedPathLength = -1

	while stack:
		item = stack.pop()

		# Use .get(key, default) to avoid TypeError from Java Maps
		children = item.get('items', None)
		if children:
			stack.extend(children)

		data = item.get('data', None)
		if not data:
			continue

		path = data.get('tagPath', None)
		if not path:
			continue

		# Exact match: return immediately
		if tagPath == path:
			return data

		# Longest matching prefix logic
		if tagPath.startswith(path + "/") and len(path) > matchedPathLength:
			matchedItemData = data
			matchedPathLength = len(path)

	return matchedItemData

def _resolve_is_admin(is_admin):
	if is_admin is not None:
		return bool(is_admin)
	return False

def _node_allowed(node, is_admin, perms=None):
	if not isinstance(node, dict):
		node = _to_py(node)
	if not isinstance(node, dict):
		return False
	data = node.get('data') or {}
	if not isinstance(data, dict):
		data = _to_py(data) if data is not None else {}
	if not isinstance(data, dict):
		data = {}
	# security-tiers: data.permission 'Device/Action' (Roles & Permissions row) wins over adminOnly;
	# without perms (server callers) it falls back to the admin flag
	perm = data.get('permission')
	if perm:
		if perms is None:
			if not is_admin:
				return False
		else:
			dev, _, act = str(perm).partition('/')
			if not bool((perms.get(dev) or {}).get(act)):
				return False
	elif data.get('adminOnly') and not is_admin:
		return False
	# hidden = kept in the tree config but not shown (demo sections parked 2026-09-22)
	if data.get('hidden') and not (data.get('demo') and demoEnabled()):
		return False
	return True

def seedCacheFrom(items):
	"""Prime NavMasterTreeCache from a Python list (view.custom.items seed)."""
	globals_dict = system.util.getGlobals()
	py = _as_items(items)
	if not py:
		py = _to_py(items)
		if isinstance(py, dict):
			py = py.get("items") if isinstance(py.get("items"), list) else []
		if not isinstance(py, list):
			py = []
	py = _deep_decode(py) if py else []
	if isinstance(py, dict):
		py = py.get("items") if isinstance(py.get("items"), list) else []
	import time
	py = py if isinstance(py, list) else []
	globals_dict["NavMasterTreeCache"] = {"ts": time.time(), "items": py}
	return py

def getChildrenAt(item_path, is_admin=None):
	"""Return children at item_path from the full master tree (no Loading stubs).

	Kept for optional callers; the Navigation Tree UI binds the full tree
	from view.custom.items and does not use this for expand/collapse.
	"""
	is_admin = _resolve_is_admin(is_admin)
	cached_tree = getNavItems()
	if not cached_tree:
		return []
	if isinstance(cached_tree, dict):
		cached_tree = cached_tree.get("items") or []
	if not isinstance(cached_tree, list):
		return []

	if not item_path:
		items_to_process = cached_tree
	else:
		current = cached_tree
		target = None
		try:
			for index in item_path:
				idx = int(index)
				if idx < 0 or idx >= len(current):
					return []
				target = current[idx]
				if not isinstance(target, dict):
					target = _to_py(target)
				current = (target.get("items") or []) if isinstance(target, dict) else []
		except:
			return []
		items_to_process = (target.get("items") or []) if isinstance(target, dict) else []

	out = []
	for child in items_to_process or []:
		if not isinstance(child, dict):
			child = _to_py(child)
		if not isinstance(child, dict) or not _node_allowed(child, is_admin):
			continue
		try:
			copy = system.util.jsonDecode(system.util.jsonEncode(child))
		except:
			copy = dict(child)
		kids = copy.get("items") or []
		# Recurse full subtree (admin-filtered); no Loading... dummies
		if kids:
			# Build filtered recursive copy via getMasterTree-style walk on this node
			pass
		out.append(copy)
	# Admin-filter nested items in place
	def filter_nodes(nodes):
		filtered = []
		for n in nodes or []:
			if not isinstance(n, dict):
				continue
			if not _node_allowed(n, is_admin):
				continue
			kids = n.get("items") or []
			if kids:
				n["items"] = filter_nodes(kids)
			else:
				n["items"] = []
			filtered.append(n)
		return filtered
	return filter_nodes(out)

def getMasterTree(is_admin=None):
	"""Full decoded nav tree (admin-filtered). Used by search helpers if needed."""
	is_admin = _resolve_is_admin(is_admin)
	cached = getNavItems()
	if not cached:
		return []

	def filter_nodes(nodes):
		out = []
		for n in nodes or []:
			if not isinstance(n, dict):
				n = _to_py(n)
			if not isinstance(n, dict):
				continue
			if not _node_allowed(n, is_admin):
				continue
			try:
				copy = system.util.jsonDecode(system.util.jsonEncode(n))
			except:
				copy = dict(n)
			kids = n.get("items") or []
			if isinstance(kids, list) and kids:
				copy["items"] = filter_nodes(kids)
			else:
				copy["items"] = []
			out.append(copy)
		return out

	return filter_nodes(cached)

def findItemPath(viewPath=None, tagPath=None, page=None):
	"""Locate index path in master cache by viewPath / tagPath / page."""
	cached_tree = getNavItems()
	if not cached_tree:
		return None

	def search_tree(nodes, current_path):
		for i, node in enumerate(nodes or []):
			if not isinstance(node, dict):
				node = _to_py(node) or {}
			data = node.get("data") or {}
			if not isinstance(data, dict):
				data = {}
			node_view = data.get("viewPath") or ""
			node_tag = data.get("tagPath") or ""
			node_page = data.get("page") or ""
			viewOk = (viewPath is None or viewPath == "" or node_view == viewPath)
			tagOk = (tagPath is None or tagPath == "" or node_tag == tagPath)
			pageOk = (page is None or page == "" or node_page == page)
			if (viewPath or page) and viewOk and tagOk and pageOk:
				if (viewPath and node_view == viewPath) or (page and node_page == page):
					if tagPath is None or tagPath == "" or node_tag == tagPath:
						return current_path + [i]
			kids = node.get("items") or []
			if kids:
				result = search_tree(kids, current_path + [i])
				if result:
					return result
		return None

	return search_tree(cached_tree, [])

def flushCache():
	system.util.getGlobals().pop("NavMasterTreeCache", None)
