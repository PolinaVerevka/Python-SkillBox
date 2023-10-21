def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclid_gcd(b, a % b)

print(euclid_gcd(24, 36)) # 12
print(euclid_gcd(13, 29)) # 1
