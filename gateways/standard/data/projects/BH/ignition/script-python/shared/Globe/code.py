# Globe landing page (WebDev iframe <-> Perspective page), scoped to ONE session + page.
#
# The iframe at /system/webdev/BH/globe/map cannot talk to Perspective directly, so it POSTs
# to /system/webdev/BH/globe/mapMarkers. The iframe src carries the owning session id, page id
# and an HMAC token (iframeSrc); doPost hands the body to relay(), which verifies the token and
# that the session/page is live, then system.perspective.sendMessage(..., scope='page') to that
# page only. The Globe view's page-scoped handlers (globeHover / globeNavigate) do the rest.
# See docs/globe-hover.md.

import hashlib
import hmac

LOGGER = "BH.Globe"
INDEX_URL = "/system/webdev/BH/globe/map"
THEME_ALIASES = {"light": "light-cool", "dark": "dark-cool"}
HOVER_MESSAGE = "globeHover"
NAV_MESSAGE = "globeNavigate"
_SECRET_KEY = "bh.globe.hmacSecret"
_fallback = {}


def _secret():
	"""Random per-gateway-run secret, shared by Perspective bindings and WebDev (getGlobals)."""
	try:
		store = system.util.getGlobals()
	except Exception:
		store = _fallback
	s = store.get(_SECRET_KEY)
	if not s:
		from java.util import UUID
		s = (str(UUID.randomUUID()) + str(UUID.randomUUID())).replace("-", "")
		store[_SECRET_KEY] = s
	return str(s)


def token(sessionId, pageId):
	msg = "%s|%s" % (sessionId or "", pageId or "")
	return hmac.new(_secret(), msg, hashlib.sha256).hexdigest()


def _same(a, b):
	a, b = str(a or ""), str(b or "")
	if len(a) != len(b):
		return False
	diff = 0
	for x, y in zip(a, b):
		diff |= ord(x) ^ ord(y)
	return diff == 0


def iframeSrc(theme, sessionId, pageId):
	"""Globe iframe src for this session/page (bound on the Globe view's IFrame props.src)."""
	t = str(theme or "light-cool").lower()
	t = THEME_ALIASES.get(t, t)
	sid, pid = str(sessionId or ""), str(pageId or "")
	return "%s?theme=%s&sessionId=%s&pageId=%s&token=%s#NoAlarms" % (INDEX_URL, t, sid, pid, token(sid, pid))


def _sessionHasPage(sessionId, pageId):
	"""True when sessionId is a live BH session and pageId is one of its open pages."""
	try:
		infos = system.perspective.getSessionInfo(projectFilter=system.util.getProjectName())
	except:
		infos = system.perspective.getSessionInfo()
	for info in infos or []:
		try:
			if str(info.get("id")) != sessionId:
				continue
			pages = info.get("pageIds")
			return pageId in [str(p) for p in (pages or [])]
		except Exception:
			continue
	return False


def _routeOk(page):
	try:
		return Navigation.Nav._hasRoute(page)
	except:  # bare: Java exceptions are not Exception subclasses in Jython
		return False


def relay(data):
	"""Handle a globe marker POST body. Returns (httpStatus, reason).

	Body: {"__globe": "hover"|"navigate", "sessionId", "pageId", "token", "page", "seq"?}
	"""
	try:
		kind = str(data.get("__globe") or "")
		sid = str(data.get("sessionId") or "")
		pid = str(data.get("pageId") or "")
		page = str(data.get("page") or "")
	except Exception:
		return 400, "bad body"
	log = system.util.getLogger(LOGGER)
	if kind not in ("hover", "navigate"):
		return 400, "unknown message"
	if not sid or not pid or not _same(data.get("token"), token(sid, pid)):
		log.debug("globe %s rejected: bad token" % kind)
		return 403, "bad token"
	if page and not page.startswith("/"):
		return 400, "bad page"
	if kind == "navigate" and not (page and _routeOk(page)):
		return 400, "unknown route"
	if not _sessionHasPage(sid, pid):
		log.debug("globe %s rejected: session/page not live" % kind)
		return 404, "session/page not live"
	if kind == "hover":
		try:
			seq = float(data.get("seq") or 0)
		except Exception:
			seq = 0.0
		payload = {"page": page, "seq": seq}
		mtype = HOVER_MESSAGE
	else:
		payload = {"page": page}
		mtype = NAV_MESSAGE
	system.perspective.sendMessage(mtype, payload=payload, scope="page", sessionId=sid, pageId=pid)
	return 200, "ok"


ADMIN_ROLES_TAG = "[default]_Config/Security/AdminRoles"
USER_SOURCE = "default"


def adminWriter(request):
	"""(httpStatus, user) for a config write on globe/mapMarkers (GeoJSON markers, Navigation document).

	The iframe's hover/navigate relay needs a logged-in BH session (shared.WebAuth); config writes check HTTP Basic
	credentials here, BEFORE the body is looked at: a user of the 'default' user source holding a role listed
	in _Config/Security/AdminRoles (shared.Security, no hard-coded role names). 401 = missing/invalid
	credentials (sets WWW-Authenticate), 403 = valid user without an admin role, 200 = allowed."""
	import base64
	log = system.util.getLogger(LOGGER)
	resp = request.get("servletResponse")
	try:
		hdr = str(request["servletRequest"].getHeader("Authorization") or "")
	except Exception:
		hdr = ""
	user, pw = "", ""
	if hdr[:6].lower() == "basic ":
		try:
			user, _, pw = base64.b64decode(hdr[6:].strip()).partition(":")
		except Exception:
			user, pw = "", ""
	ok = False
	if user and pw:
		try:
			ok = bool(system.security.validateUser(user, pw, USER_SOURCE))
		except Exception as e:
			log.warn("globe config write: validateUser failed: %s" % e)
	if not ok:
		try:
			resp.setHeader("WWW-Authenticate", 'Basic realm="BH globe config"')
		except Exception:
			pass
		log.info("globe config write refused (401) user='%s'" % user)
		return 401, user
	try:
		u = system.user.getUser(USER_SOURCE, user)
		held = [str(r) for r in (u.getRoles() if u is not None else [])]
	except Exception:
		held = []
	csv = system.tag.readBlocking([ADMIN_ROLES_TAG])[0].value
	if not shared.Security.hasAnyRole(held, csv):
		log.info("globe config write refused (403) user='%s'" % user)
		return 403, user
	return 200, user
