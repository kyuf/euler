#permutation function
def perm(A):
	if len(A) < 2:
		yield A
	else:
		for i in range(len(A)):
			p = A[i]
			ps = A[:i] + A[i + 1:]
			for j in perm(ps):
				yield p + j

