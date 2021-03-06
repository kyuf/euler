#euler 92
"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
import math

#function to find next number in chain
def next_chain(n):
	nsum = 0
	for i in str(n):
		nsum += int(i) ** 2
	return nsum

#function to determine next permutation set to be evaluated	
def next(n):
	inc_list = [1000000, 100000, 10000, 1000, 100, 10, 1]
	if str(n)[0] == str(n)[-1]:
		n = (n // inc_list[0] + 1) * inc_list[0]
	else:
		for j in range(len(str(n)) - 1, 0, -1):
			if str(n)[j] != str(n)[j - 1]:
				n = (n // inc_list[j] + 1) * inc_list[j]
				break
	return n

#function to check number of unique permutations
def multi(n):
	multi_dic = {"0": 7 - len(str(n))}
	for i in str(n):
		if i in multi_dic:
			multi_dic[i] += 1
		else:
			multi_dic[i] = 1
	com = math.factorial(7)
	for i in multi_dic:
		com //= math.factorial(multi_dic[i])
	return com

count89 = 0
set89 = {89}
set_bad = {1}

n = 1

while n != 10000000:
	
	#chain until a repeat number appears
	hold_next = next_chain(n)
	next_n = hold_next
	while True:
		#increment count89 when upon arrival at 89 or in set89
		if next_n == 89 or next_n in set89:
			set89.add(hold_next)
			count89 += multi(n)
			break
			
		#terminate if in bad set
		if next_n in set_bad:
			set_bad.add(hold_next)
			break

		#terminate if arrive at 1
		if next_n == 1:
			break
		next_n = next_chain(next_n)
	n = next(n)

print(count89)
	
