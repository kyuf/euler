#test n-roots
import math


for a in range(2, 101):
    for n in range(2, 7):
        tmp = a ** (1.0 / n)
        if int(math.ceil(tmp)) ** n == a or int(math.floor(tmp)) == a:
            print [a, n]

