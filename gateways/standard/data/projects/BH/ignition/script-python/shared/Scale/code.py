# Coordinate-container view scaling (Scout-style).
# Bind root/Canvas props.style.transform via expr-struct + script:
#   return shared.Scale.cssTransform(value)
#
# value keys:
#   scale / Scale          — truthy enables; falsy returns "none"
#   primaryViewWidth/Height — page.props.dimensions.primaryView.*
#   defaultViewWidth/Height — view.props.defaultSize.*


def _truthy(v):
	if v in (True, 1, "1", "true", "True"):
		return True
	if v in (False, 0, "0", "false", "False", None, ""):
		return False
	try:
		return bool(v)
	except:
		return False


def _num(v):
	try:
		if v is None or v == "":
			return None
		return float(v)
	except:
		return None


def _get(value, *keys):
	for key in keys:
		try:
			if hasattr(value, "get"):
				if key in value:
					return value[key]
			else:
				return value[key]
		except:
			continue
	return None


def cssTransform(value):
	"""
	Return CSS transform string: scale(...) translate(...px, ...px).
	Fits defaultSize into primaryView (letterbox), origin top-left (Scout).
	"""
	enabled = _get(value, "scale", "Scale")
	if not _truthy(enabled):
		return "none"

	pw = _num(_get(value, "primaryViewWidth"))
	ph = _num(_get(value, "primaryViewHeight"))
	dw = _num(_get(value, "defaultViewWidth"))
	dh = _num(_get(value, "defaultViewHeight"))
	if pw is None or ph is None or dw is None or dh is None:
		return "none"
	if pw <= 0 or ph <= 0 or dw <= 0 or dh <= 0:
		return "none"

	s = min(pw / dw, ph / dh)
	if s <= 0:
		return "none"

	# Center within primary view; divide by s because translate is pre-scale
	# when written as "scale() translate()" (Scout order).
	tx = ((pw - dw * s) / 2.0) / s
	if pw > ph:
		ty = -((ph - dh * s) / 2.0) / s
	else:
		ty = 0.0

	return "scale(%s) translate(%spx, %spx)" % (s, tx, ty)
