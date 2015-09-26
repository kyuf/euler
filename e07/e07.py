#euler 7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def is_prime(n, prime_list = []):
    for i in prime_list:
        if n % i == 0:
            return False
    prime_list.append(n)
    return True

count = 1
n = 3
while True:
    if is_prime(n):
        count += 1
    if count == 10001:
        print(n)
        break
    else:
        n += 2
