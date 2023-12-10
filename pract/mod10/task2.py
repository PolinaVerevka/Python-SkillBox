import re
import doctest


def check_web_color(color):
	# Проверка формата rgb
	if re.match(r'^rgb\(\s*((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])%|\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*,\s*((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])%|\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*,\s*((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])%|\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\s*\)$', color):
		return True

	# Проверка формата hex
	if re.match(r'^#([0-9a-fA-F]{3}){1,2}$', color):
		return True

	# Проверка формата hsl
	if re.match(r'^hsl\s*\(\s*(?:\d{1,3}\s*,\s*(?:100|\d{1,2})%\s*,\s*(?:100|\d{1,2})%|100%\s*,\s*(?:100|\d{1,2})%\s*,\s*(?:100|\d{1,2})%\s*)\)$', color):
		return True

	return False


def test_check_web_color():
	"""
	>>> check_web_color('#21f48D')
	True
	>>> check_web_color('#888')
	True
	>>> check_web_color('rgb(255, 255,255)')
	True
	>>> check_web_color('rgb(10%, 20%, 0%)')
	True
	>>> check_web_color('hsl(200,100%,50%)')
	True
	>>> check_web_color('hsl(0, 0%, 0%)')
	True
	>>> check_web_color('#2345')
	False
	>>> check_web_color('ffffff')
	False
	>>> check_web_color('rgb(257, 50, 10)')
	False
	>>> check_web_color('hsl(20, 10, 0.5)')
	False
	>>> check_web_color('hsl(34%, 20%, 50%)')
	False
	"""

if __name__ == "__main__":
    doctest.testmod(verbose=True)
