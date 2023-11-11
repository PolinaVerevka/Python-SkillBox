def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def my_function(x):
    return x * 2

result = my_function(5)
print(result)  # Вывод: 10

result = my_function()
print(result)  # Вывод: "Not enough arguments"

result = my_function(1, 2, 3)
print(result)  # Вывод: "Too many arguments"

result = my_function("hello")
print(result)  # Вывод: "Wrong types"

result = my_function(-2)
print(result)  # Вывод: "Negative argument"
