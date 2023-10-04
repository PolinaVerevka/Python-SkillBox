def decimal_to_binary(decimal):
    if decimal <= 0:
        return ''
    quotient = decimal // 2
    remainder = decimal % 2
    return decimal_to_binary(quotient) + str(remainder)

def decimal_to_octal(decimal):
    if decimal <= 0:
        return ''
    quotient = decimal // 8
    remainder = decimal % 8
    return decimal_to_octal(quotient) + str(remainder)

def decimal_to_hexadecimal(decimal):
    if decimal <= 0:
        return ''
    quotient = decimal // 16
    remainder = decimal % 16
    if remainder < 10:
        return decimal_to_hexadecimal(quotient) + str(remainder)
    else:
        return decimal_to_hexadecimal(quotient) + chr(remainder + 55)

try:
    decimal = int(input("Введите натуральное число в десятичной системе: "))
    if decimal <= 0:
        print("Неверный ввод")
    else:
        binary = decimal_to_binary(decimal)
        octal = decimal_to_octal(decimal)
        hexadecimal = decimal_to_hexadecimal(decimal)
        print("Двоичное представление:", binary)
        print("Восьмеричное представление:", octal)
        print("Шестнадцатеричное представление:", hexadecimal)
except ValueError:
    print("Неверный ввод")
