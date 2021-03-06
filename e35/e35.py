#euler 35
#code is incorrect... refer to e35x.py
#rotating to larger number can give false positive if prime_list is not adequately developed...
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math

def is_prime(n, prime_list):
    tmp = math.ceil(math.sqrt(n))
    for p in prime_list:
        if p <= tmp:
            if n % p == 0:
                return False
    return True

def rotate(n):
    if n < 10:
        yield
    s = list(str(n))
    for i in range(len(s) - 1):
        s.append(s.pop(0))
        tmp = ""
        for j in s:
            tmp += j
        yield int(tmp)

#initialize prime list and circle with 2
prime_list = [2]
circle = [2]
limit = 10000

for n in range(3, limit, 2):
    if n in circle:
        continue
    elif is_prime(n, prime_list):
        tmp = []
        check = True
        for r in rotate(n):
            if r:
                if is_prime(r, prime_list):
                    if r != n and r not in circle:
                        tmp.append(r)
                else:
                    check = False
                    break
        if n < math.sqrt(limit):
            prime_list.append(n)
        if check:
            circle.append(n)
            if n > 10:
                circle.extend(tmp)

print len(circle)
print circle

