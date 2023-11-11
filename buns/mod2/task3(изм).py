line = input()
space1 = line.index(' ')
space2 = line.index(' ', space1 + 1)

a = int(line[:space1])
b = int(line[space1 + 1:space2])
c = int(line[space2 + 1:])

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)
