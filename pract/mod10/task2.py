import re
import doctest

def check_color(color):
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


def test_check_color():
    """
    >>> test_check_color()
    True
    """
    assert check_color("#21f48D") == True
    assert check_color("#888") == True
    assert check_color("rgb(255, 255,255)") == True
    assert check_color("rgb(10%, 20%, 0%)") == True
    assert check_color("hsl(200,100%,50%)") == True
    assert check_color("hsl(0, 0%, 0%)") == True
    assert check_color("#2345") == False
    assert check_color("ffffff") == False
    assert check_color("rgb(257, 50, 10)") == False
    assert check_color("hsl(20, 10, 0.5)") == False
    assert check_color("hsl(34%, 20%, 50%)") == False

doctest.testmod()

print(check_color("#21f48D"))
# Output: True

print(check_color("#888"))
# Output: True

print(check_color("rgb(255, 255,255)"))
# Output: True

print(check_color("rgb(10%, 20%, 0%)"))
# Output: True

print(check_color("hsl(200,100%,50%)"))
# Output: True

print(check_color("hsl(0, 0%, 0%)"))
# Output: True

print(check_color("#2345"))
# Output: False

print(check_color("ffffff"))
# Output: False

print(check_color("rgb(257, 50, 10)"))
# Output: False

print(check_color("hsl(20, 10, 0.5)"))
# Output: False

print(check_color("hsl(34%, 20%, 50%)"))
# Output: False
