# Login check for WebDev resources that a logged-in Perspective session loads (iframe src, fetch from the iframe).
#
# The browser sends the same HTTP session cookie to /system/webdev/... as to the Perspective client, and the gateway
# keeps that browser's Perspective project sessions on the HTTP session (attribute "perspective-session",
# a PerspectiveSessionCollection). perspectiveUser() returns the user of THIS project's session when its web auth
# status is authenticated + authorized, else None. No HTTP Basic prompt, so it works inside an iframe.
# WebDev's own require-auth is HTTP Basic only (and text resources have no auth at all). docs/security-access.md

LOGGER = "BH.WebAuth"
PROJECT = "BH"
_ATTR = "perspective-session"


def _unwrap(v):
	if v is not None and hasattr(v, "orElse"):
		return v.orElse(None)
	return v


def perspectiveUser(request, project=None):
	"""Username of the authenticated BH Perspective session of the browser that sent this request, else None."""
	project = project or PROJECT
	try:
		hs = request["servletRequest"].getSession(False)
	except:  # bare: Java exceptions are not Exception subclasses in Jython
		return None
	if hs is None:
		return None
	try:
		col = hs.getAttribute(_ATTR)
		if col is None:
			return None
		s = _unwrap(col.findProjectSession(project))
		if s is None:
			return None
		# Jython hands back the session's scripting wrapper (what a view sees as self.session), so read props.auth
		auth = s.props.auth
		if not auth.authenticated:
			return None
		name = None
		try:
			name = auth.user.userName
		except:
			name = None
		return str(name) if name else "authenticated"
	except:
		system.util.getLogger(LOGGER).debug("perspectiveUser check failed")
		return None


def hasBasicHeader(request):
	try:
		return str(request["servletRequest"].getHeader("Authorization") or "")[:6].lower() == "basic "
	except:
		return False


def deny(request, status=401, reason=None):
	"""Plain JSON refusal, no WWW-Authenticate header (an iframe must never get a Basic login prompt)."""
	try:
		resp = request["servletResponse"]
		resp.setStatus(status)
		resp.setHeader("Cache-Control", "no-store")
	except:
		pass
	return {"json": {"ok": False, "reason": reason or ("login required" if status == 401 else "forbidden")}}


def noStore(request):
	try:
		request["servletResponse"].setHeader("Cache-Control", "no-store")
	except:
		pass
