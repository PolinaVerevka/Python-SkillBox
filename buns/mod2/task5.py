i = input("Введите символ латинского алфавита: ")
n = int(input("Введите целое число: "))

i_index = ord(i) - 97
k_index = (i_index + n) % 26

if k_index < 0:
    k_index += 26
k = chr(k_index + 97)

print("Символ k: ", k)
