def is_armstrong_number(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    armstrong_sum = sum([d ** num_digits for d in digits])
    return armstrong_sum == n

def get_armstrong_numbers():
    n = 153
    count = 0
    while count < 8:
        if is_armstrong_number(n):
            yield n
            count += 1
        n += 1
        
for armstrong_num in get_armstrong_numbers():
    print(armstrong_num, end=' ')
