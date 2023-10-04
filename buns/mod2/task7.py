s = input()
count_0 = 0
count_1 = 0

for c in s:
    if c == '0':
        count_0 += 1
    elif c == '1':
        count_1 += 1

if count_0 == count_1:
    print('yes')
else:
    print('no')
