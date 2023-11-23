import re

def check_password(password):
    # Проверка наличия только латинских символов, цифр и специальных символов
    if not re.match(r'^[a-zA-Z0-9^$%@#&*!?]+$', password):
        return False
    
    # Проверка длины пароля
    if len(password) < 6:
        return False
    
    # Проверка наличия по крайней мере двух латинских символов в верхнем регистре
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False
    
    # Проверка наличия по крайней мере одной цифры
    if len(re.findall(r'\d', password)) < 1:
        return False
    
    # Проверка наличия по крайней мере двух различных специальных символов
    if len(set(re.findall(r'[^\w\s]', password))) < 2:
        return False
    
    # Проверка отсутствия трех одинаковых символов подряд
    if re.search(r'([a-zA-Z0-9^$%@#&*!?])\1\1', password):
        return False
    
    return True

print(check_password("rtG3FG!Tr^e"))
# Output: True

print(check_password("aA1!*!1Aa"))
# Output: True

print(check_password("oF^a1D@y5e6"))
# Output: True

print(check_password("enroi#$rkdeR#$092uWedchf34tguv394h"))
# Output: True

print(check_password("пароль"))
# Output: False

print(check_password("password"))
# Output: False

print(check_password("qwerty"))
# Output: False

print(check_password("lOngPa$$$W0Rd"))
# Output: False

def test_check_password():
    """
    >>> test_check_password()
    True
    """
    assert check_password("rtG3FG!Tr^e") == True
    assert check_password("aA1!*!1Aa") == True
    assert check_password("oF^a1D@y5e6") == True
    assert check_password("enroi#$rkdeR#$092uWedchf34tguv394h") == True
    assert check_password("пароль") == False
    assert check_password("password") == False
    assert check_password("qwerty") == False
    assert check_password("lOngPa$$$W0Rd") == False

import doctest

doctest.testmod()
