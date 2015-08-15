#euler 41
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

#assumptions
"""
a number is divisible by 3 if and only if the digit sum of the number is divisible by 3. only 4 and 7 digit pandigital numbers do not have a digit sum that is divisible by 3. therefore, only 4 and 7 digit pandigital numbers can be prime
"""
#function to determine if n is prime using stored primes
def is_prime(n, prime_list):
	tmp = n ** 0.5
	for i in prime_list:
		if i > tmp:
			break
		if n % i == 0:
			return False
	return True

#function to determine if n is pandigital
def is_pandigital(n):
	tmp = str(n)
	for i in range(len(str(n)), 0, -1):
		if str(i) not in tmp:
			return False
	return True

#function to check given range for prime pandigital numbers
def prime_pan(a, b):
	global max_n
	global prime_list
	for n in range(a, b, 2):
		if is_pandigital(n) and is_prime(n, prime_list):
			max_n = n

#do not need to include 2 in prime_list since all numbers checked will be odd
prime_list = []

#max pandigital number for 7-digit is 7654321
for n in range(3, int(7654321 ** 0.5) + 1, 2):
	if is_prime(n, prime_list):
		prime_list.append(n)

max_n = 0

#checking 4 digit pandigitals
prime_pan(1235, 4322)

#checking 7 digit pandigitals
prime_pan(1234567, 7654322)

print(max_n)
