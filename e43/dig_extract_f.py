#function to extract digits of interest for euler 43
#takes in string and returns an array of ints
def dig_extract(A):
	digs = []
	for i in range(1, 8):
		if A[i] == 0:
			digs.append(int(A[i + 1:i + 3]))
		else:
			digs.append(int(A[i:i + 3]))
	return digs
