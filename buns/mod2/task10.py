string = input()

result = ''

while string != '':
    word = '' 
    i = 0  

    while i < len(string) and string[i] != ' ':
        word += string[i]
        i += 1

    result += word[-1]

    while i < len(string) and string[i] == ' ':
        i += 1

    string = string[i:]

print(result)
