input_str = input()
comma_index = input_str.index(',')
s = input_str[:comma_index]
i = input_str[comma_index + 1:]
count = 0  
for char in s:
    if char == i:
        count += 1
    else:
        break  

print(count)
