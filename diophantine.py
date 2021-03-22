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
    assert c % gcd(a, b) == 0
    (d, x, y) = extended_gcd(a, b)
    t = c // d
    x = t * x
    y = t * y
    return (x, y)

print('test 10x + 6y = 14')
print(diophantine(10, 6, 14))
print('test 391x + 299y = -69')
print(diophantine(391, 299, -69))
print('test ax + by = 1')
print('test 9x + 2y = 1')
print(diophantine(9, 2, 1))
print('looking for x such that b/a (mod n) = x')
print('where 7/2 (mod 9) = x')
print(diophantine(9, 2, 1))
