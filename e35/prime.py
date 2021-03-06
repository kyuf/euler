#testing prime function
import math

def is_prime(n, prime_list):
    tmp = math.ceil(math.sqrt(n))
    for p in prime_list:
        if p <= tmp:
            if n % p == 0:
                return False
    return True

#initialize prime list with 2 to allow odd counting
prime_list = [2]

#begin count at 3
for n in range(3, 10):
    if is_prime(n, prime_list):
        prime_list.append(n)

print prime_list
