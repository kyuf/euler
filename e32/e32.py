#euler 32
#defining recursive permutation function
def perm(A):
    if len(A) == 0:
        yield []
    elif len(A) == 1:
        yield A
    else:
        for i in range(len(A)):
            x = A[i]
            xs = A[:i] + A[i + 1:]
            for p in perm(xs):
                yield [x] + p

A = list("123456789")
pandigital = []
sum_n = 0

for a in perm(A):
    tmp = int(a[5] + a[6] + a[7] + a[8])
    if tmp not in pandigital:
        if int(a[0]) * int(a[1] + a[2] + a[3] + a[4]) == tmp or int(a[0] + a[1]) * int(a[2] + a[3] + a[4]) == tmp:
            pandigital.append(tmp)
            sum_n += tmp

print sum_n
