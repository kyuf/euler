#euler 3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
limit = int(600851475143 ** 0.5)

#prime function
def is_prime(n, prime_list = []):
    for i in prime_list:
        if i ** 2 > n:
            break
        elif n % i == 0:
            return False
    prime_list.append(n)
    return True

#factor function
def is_factor(n, m = 600851475143):
    if m % n == 0:
        return True
    else:
        return False

max_n = 0
for n in range(3, limit, 2):
    if is_prime(n):
        if is_factor(n):
            max_n = n

print(max_n)
