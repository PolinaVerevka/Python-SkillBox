numbers = input("Введите последовательность чисел через пробел: ").split(' ')
print(len(set(numbers)) != len(numbers))
