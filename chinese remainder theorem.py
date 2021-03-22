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
        assert a % d == 0 and b % d == 0
        assert d == a * x + b * y
    return (d, x, y)

def ExtendedEuclid(a, b):
    # recall ax + by = 1
    (d, x, y) = extended_gcd(a, b)
    t = 1 // d
    x = t * x
    y = t * y
    return (x, y)

def ChineseRemainderTheorem(n1, r1, n2, r2):
    assert r1 >= 0 and r1 < n1 and r2 >= 0 and r2 < n2
    assert gcd(n1, n2) == 1 # assert that n1 and n2 are coprime
    (x, y) = ExtendedEuclid(n1, n2)
    n = ((r1 * n2 * y) + (r2 * n1 * x)) % (n1 * n2)
    print(x, y, n)
    assert n > 0 and n < (n1 * n2)
    return n

n1, r1, n2, r2 = 17, 8, 13, 2
ChineseRemainderTheorem(n1, r1, n2, r2)

n1, r1, n2, r2 = 686579304, 295310485, 26855093, 8217207
ChineseRemainderTheorem(n1, r1, n2, r2)
