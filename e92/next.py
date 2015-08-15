#function that returns unique permutation sets
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

n = 0
while n != 4000000:
	print(n)
	n = next(n)
	
