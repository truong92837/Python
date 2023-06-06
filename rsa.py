#!/usr/bin/python3
c = 9327565722767258308650643213344542404592011161659991421
e = 1
n = 245841236512478852752909734912575581815967630033049838269083
# n = p*q
# c = pow(m,e,n)
# m = bytes_to_long(FLAG)
# Calculate the modular inverse of e modulo (p-1)*(q-1) using the extended Euclidean algorithm
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % m

# Extended Euclidean algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

# Calculate the modular inverse of e modulo (p-1)*(q-1)
phi_n = (p - 1) * (q - 1)
d = mod_inverse(e, phi_n)

# Calculate m = c^d mod n
m = pow(c, d, n)

# Convert m from integer to bytes
flag = m.to_bytes((m.bit_length() + 7) // 8, 'big')

print(flag)
