s = input()

vowels = 0  
consonants = 0  

for i in range(len(s)):
    if s[i] == ' ':  
        continue
    elif s[i] in 'аеёиоуыэюя':  
        vowels += 1
    else:
        consonants += 1

print(vowels, consonants)
