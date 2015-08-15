#euler 10
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
#function to check if n is prime
def is_prime(n):
	global prime_list
	tmp = n ** 0.5
	for i in prime_list:
		if i > tmp:
			break
		if n % i == 0:
			return False
	return True

#seed with 2
sum_n = 2

#do not need to check for 2 since all numbers checked will be odd
prime_list = []

for n in range(3, 2000000, 2):
	if is_prime(n):
		if n < 2000000 ** 0.5:
			prime_list.append(n)
		sum_n += n
print(sum_n)
