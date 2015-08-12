#euler 37
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
#seed prime list and dictionary with single digit primes
prime_list = [2, 3, 5, 7]
prime_dic = {2: 1, 3: 1, 5: 1, 7: 1}

#function to check if n is prime
def is_prime(n, prime_list):
	tmp = n ** 0.5
	for i in prime_list:
		if i > tmp:
			break
		if n % i == 0:
			return False
	return True

#function to truncate n from left
def chop_left(n, prime_dic):
    tmp = 10
    while n % tmp != n:
    	if n % tmp in prime_dic:
    		tmp *= 10
    	else:
    		return False
    return True

#function to truncate n from right
def chop_right(n, prime_dic):
	n //= 10
	while n != 0:
		if n in prime_dic:
			n //= 10
		else:
			return False
	return True
	
count = 0
nsum = 0
n = 11

#finding the only 11
while count != 11:
	if is_prime(n, prime_list):
		prime_list.append(n)
		prime_dic[n] = 1
		if "0" in list(str(n)):
			n += 2
			continue
		if chop_left(n, prime_dic) and chop_right(n, prime_dic):
			nsum += n
			count += 1
			print(n)
	n += 2

print(nsum)
