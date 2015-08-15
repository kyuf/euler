#euler 41
#preliminary
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

prime_list = [2, 3, 5, 7]
max_n = 0

#max pandigital number for 7-digit is 7654321
for n in range(11, 7654322, 2):
	if is_prime(n, prime_list):
		prime_list.append(n)
		if len(str(n)) == 4 or len(str(n)) == 7:
			if is_pandigital(n):
				max_n = n

print(max_n)
