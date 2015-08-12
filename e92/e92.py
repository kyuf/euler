#euler 92
#need to make more efficient
"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
#function to find next number in chain
def next_chain(n):
	nsum = 0
	for i in str(n):
		nsum += int(i) ** 2
	return nsum

count89 = 0
set89 = {89}
set_bad = {1}

for n in range(10000000):
	#initialize seen set with starting number
	seen = {n}
	
	#chain until a repeat number appears
	hold_next = next_chain(n)
	next_n = hold_next
	while next_n not in seen:
		#increment count89 when upon arrival at 89 or in set89
		if next_n == 89 or next_n in set89:
			set89.add(hold_next)
			count89 += 1
			break
		#terminate if in bad set
		if next_n in set_bad:
			set_bad.add(hold_next)
			break
		seen.add(next_n)
		next_n = next_chain(next_n)

print(count89)
	
