#euler 3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
#prime function
def is_prime(n, prime_list = []):
    for i in prime_list:
        if i ** 2 > n:
            break
        elif n % i == 0:
            return False
    prime_list.append(n)
    return True

#finding largest prime factor of 600851475143
m = 600851475143
limit = int(m ** 0.5)
max_n = 0
for n in range(3, limit, 2):
    if is_prime(n):
        if m % n == 0:
            max_n = n

print(max_n)
