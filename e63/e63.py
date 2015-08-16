#euler 63
"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
#calcs
"""
n digit numbers that also have nth power are:

10^(n - 1) <= x^n < 10^n

so x must be between 1 and 9

upper limit for x is reached when:

x^n < 10^(n - 1)

x^n will produce an n digit number for each n until above limit is reached

simplifying above, upper limit becomes:

n >= 1 / (1 - log(x))

"""
from math import log10

count = 0
for x in range(1, 10):
	#summing all n digit nth power numbers produced by x
	count += int(1 / (1 - log10(x)))
print(count)
