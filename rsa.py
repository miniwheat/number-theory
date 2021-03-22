#!/usr/bin/env python3

import math, random

def encodemsg(m):
    mhex = m.encode('ascii').hex()
    mint = int(mhex, 16)
    mlength = int(math.log10(mint))
    return (mint, mlength)

def decodemsg(c):
    m = ''
    chex = str(hex(c))
    for i in range(2,len(chex),2):
        m += chr(int('0x' + chex[i:i+2],16))
    return m

def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def extended_gcd(a, b):
    # return (gcd(a, b), x, y) : gcd(a, b) = ax + by
    #assert a >= b and b >= 0 and a + b > 0
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
    # ax + by = 1
    assert c % gcd(a, b) == 0
    (d, x, y) = extended_gcd(a, b)
    t = c // d
    x = t * x
    y = t * y
    return (x, y)

def genprimes():
    p, q = 2, 4
    while gcd(p, q) != 1:
        p = random.randint(10**1000, 10**1001)
        q = random.randint(10**1000, 10**1001)

    p1q1 = (p - 1) * (q - 1)
    e = random.randint(10**1000, 10**1001)
    while gcd(e, p1q1) != 1:
        e = random.randint(10**1000, 10**1001)

    return (p, q, e)

def getd(a, b):
    assert gcd(a, b) == 1
    (d, x, y) = extended_gcd(a, b)
    t = 1 // d
    x = t * x
    y = t * y
    return x

m = 'hello'
mint, mlength = encodemsg('hello')
print(m, mint, mlength)

p, q, e = genprimes()

assert p * q > mlength
