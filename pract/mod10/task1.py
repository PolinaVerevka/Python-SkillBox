import re
import doctest


def check_password(password):
	# Проверка длины пароля
	if len(password) < 6:
		return False

	# Проверка наличия латинских символов в верхнем регистре
	if not re.search(r'[A-Z].*[A-Z]', password):
		return False

	# Проверка наличия цифры
	if not re.search(r'\d', password):
		return False

	# Проверка наличия двух различных специальных символов
	special_chars = r'^$%@#&*!?'
	count = 0
	for char in special_chars:
		if re.search(re.escape(char), password):
			count += 1
	if count < 2:
		return False

	# Проверка отсутствия трех одинаковых символов подряд
	if re.search(r'(.)\1\1', password):
		return False

	return True


def test_check_password():
	"""
    >>> check_password('rtG3FG!Tr^e')
    True
    >>> check_password('aA1!*!1Aa')
    True
    >>> check_password('oF^a1D@y5e6')
    True
    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$$W0Rd.')
    False
    """
	pass

if __name__ == "__main__":
    doctest.testmod(verbose=True)
