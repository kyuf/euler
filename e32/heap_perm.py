#Heap's algorithm
#work in progress...
import timeit

def perm(A, n):
    if n == 1:
        print A
    else:
        for i in range(n-1):
            perm(A, n - 1)
            if n % 2 == 0:
                A[i], A[n - 1] = A[n - 1], A[i]
            else:
                A[0], A[n - 1] = A[n - 1], A[0]
        perm(A, n - 1)

A = list("123456789")

start = timeit.default_timer()

perm(A, len(A))

stop = timeit.default_timer()

print stop - start
