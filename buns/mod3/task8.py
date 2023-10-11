phone_number = input("Введите номер телефона: ")
print(phone_number.replace("+", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", ""))
