input_str = input().strip()
comma_index = input_str.index(',')
i = input_str[:comma_index]
n = int(input_str[comma_index+1:])
alphabet_len = 26
i_num = ord(i) - ord('a')
k_num = (i_num + n) % alphabet_len
k = chr(ord('a') + k_num)
print(k)
