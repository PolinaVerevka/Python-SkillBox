s = input()
i = input()
count = 0
for j in range(len(s)):
    if s[j] == i:
        count += 1
    else:
        break
print(count)
