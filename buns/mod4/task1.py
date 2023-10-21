class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def check_numbers(self):
        if len(set(self.numbers)) == 1:
            print("Все числа равны")
        elif len(set(self.numbers)) == len(self.numbers):
            print("Все числа разные")
        else:
            print("Есть равные и неравные числа")

numbers1 = NumberList([1, 1, 1])
numbers1.check_numbers()

numbers2 = NumberList([1, 2, 3])
numbers2.check_numbers()

numbers3 = NumberList([1, 2, 2])
numbers3.check_numbers()
