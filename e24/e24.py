#euler 24
import math
n = 1000000
ans = []
A = [i for i in range(10)]
fac = [math.factorial(i) for i in range(1, 10)]
for i in range(len(A)):
    if n != 0:
        ind = -(i + 1)
        tmp = int(math.ceil(float(n) / fac[ind])) - 1
        ans.append(A[tmp])
        del A[tmp]
        n %= fac[ind]
    else:
        ans.append(A[-1])
        del A[-1]

print ans

