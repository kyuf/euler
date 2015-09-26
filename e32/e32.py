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
    a = "".join(a)
    tmp = int(a[5:])
    if tmp not in pandigital:
        if int(a[0]) * int(a[1:5]) == tmp or int(a[:2]) * int(a[2:5]) == tmp:
            pandigital.append(tmp)
            sum_n += tmp

print(sum_n)
