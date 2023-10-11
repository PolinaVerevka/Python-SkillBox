words = input("Введите список слов через  пробел: ").split(" ")
print(''.join([word[-1] for word in words]))
