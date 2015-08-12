#euler 27
"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import math

def prime_check(n):
    if n <= 0:
        return False
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True

prime_list = [2]

for n in range(3, 1000, 2):
    if prime_check(n):
        prime_list.append(n)

prod = 0
con_p = 0

for a in range(-999, 1000, 2):
    for b in prime_list:
        n = 0
        con = 0
        while prime_check((n ** 2) + (a * n) + b):
            n += 1
            con += 1
        if con > con_p:
            prod = a * b
            con_p = con

print prod
