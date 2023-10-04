numbers = input()
result = False
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            result = True
            break
print(result)
