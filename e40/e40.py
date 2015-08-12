#euler 40
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""
#array containing nth digits of interest
#array in reverse to optimize .pop()
digs = [1000000, 100000, 10000, 1000, 100, 10, 1]

#variable to track total number of digits
num_d = 0

#counters
n = 1
prod = 1

#iterate until all nth digits are found
while digs:
	#number of digits in n added to num_d
    num_d += len(str(n))
    if num_d >= digs[-1]:
        tmp = list(str(n))
        #take into account overcounting
        prod *= int(tmp[-1 - (num_d - digs[-1])])
        digs.pop()
    n += 1
print(prod)
