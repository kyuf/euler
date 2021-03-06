#testing permutation algorithm
import timeit

def perm(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm(xs):
                yield [x] + p

data = list("123456789")

start = timeit.default_timer()

for i in perm(data):
    print i

stop = timeit.default_timer()

print stop - start

