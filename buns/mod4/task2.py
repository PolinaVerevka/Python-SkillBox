def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power(a**2, n/2)
    else:
        return a * fast_power(a, n-1)

print(fast_power(2, 10)) # 1024
print(fast_power(3, 5)) # 243
