#euler 10
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
#function to check if n is prime
#do not need to check for 2 since all numbers checked will be odd
def is_prime(n, prime_list = []):
	tmp = n ** 0.5
	for i in prime_list:
		if i > tmp:
			break
		if n % i == 0:
			return False
	if n < 2000000 ** 0.5:
		prime_list.append(n)
	return True

#seed with 2
sum_n = 2

for n in range(3, 2000000, 2):
	if is_prime(n):
		sum_n += n
print(sum_n)

