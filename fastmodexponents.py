#!/usr/bin/env python3

import random

def bigrandom(): #generates an integer of one thousand digits
    return random.randint(1*10**100,1*10**1000)

def FastModularExponentiation(b, e, m):
    ebin = bin(e)[2:]
    ebinrev = ebin[::-1]
    c = b % m
    k = 0
    n = 1
    while k < len(ebinrev):
        if ebinrev[k] == '1':
            n = (n * c) % m
        c = (c * c) % m
        #e = e // 2
        k += 1
    print('n =',n)
    return n

FastModularExponentiation(7, 13, 11)
FastModularExponentiation(bigrandom(),bigrandom(),2392487098)
