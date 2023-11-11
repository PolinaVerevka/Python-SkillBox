input_str = input()
comma_index = input_str.index(',')
a = int(input_str[:comma_index])
b = int(input_str[comma_index + 1:])
remainder = a % b
print(remainder)
