#!/usr/bin/env python3

def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def extended_gcd(a, b):
    # return (gcd(a, b), x, y) : gcd(a, b) = ax + by
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
        assert a % d ==0 and b % d ==0
        assert d == a * x + b * y
    return (d, x, y)

def diophantine(a, b, c):
    # recall ax + by = c
    assert c % gcd(a, b) == 0
    (d, x, y) = extended_gcd(a, b)
    t = c // d
    x = t * x
    y = t * y
    return (x, y)

def divide(a, b, n):
    # return the number x such that
    # 0 <= x <= n-1
    # b/a = x (mod n) (that is, b = ax (mod n))

    assert n > 1 and a > 0 and gcd(a, n) == 1
    # nt + as = 1 where x is s
    (t, s) = diophantine(n, a, 1)
    s2 = s % n
    x = (b * s2) % n
    assert (x * a) % n == b % n
    return x

print('find the modular inverse for b/a mod n = x')
print('example 7/2 mod 9')
print (divide(2, 7, 9))
print(divide(3, 1, 4))
