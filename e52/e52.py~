#euler 52
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
#function that returns perm dictionary for comparison
def perm_set(n):
    perms = {}
    for i in str(n):
        if i in perms:
            perms[i] += 1
        else:
            perms[i] = 1
    return perms

#function to check if multiples are permutations
def multicheck(n, perm_base):
	for i in range(2, 7):
		if perm_set(i * n) != perm_base:
			return False
	return True

#pick start point..
n = 10
found = False

while True:
	#must have same number of digits
	if len(str(n)) != len(str(6 * n)):
		n += 1
		continue
	
	#check 2x to 6x
	if multicheck(n, perm_set(n)):
		break
	else:
		n += 1

print(n)
