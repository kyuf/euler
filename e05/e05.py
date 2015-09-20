#euler 5
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import log

#return prime factorization of n
def prime_fac(n, prime_list = [], factors = {}):
    for i in prime_list:
        if n % i == 0:
            pwr = int(log(n, i))
            if i not in factors or pwr > factors[i]:
                factors[i] = pwr
            n //= i ** pwr
        if n == 1:
            return factors
    factors[n] = 1
    prime_list.append(n)
    return factors

for i in range(2, 21):
    if i == 20:
        factors = prime_fac(i)
    else:
        prime_fac(i)

prod = 1
for k, v in factors.items():
    prod *= k ** v

print(prod)
