#euler 57
"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""
from math import log10

#function that returns next iteration and previous iteration
def next(m, n):
    next_m = n
    next_n = 2 * n + m
    return (next_m, next_n)

count = 0
n_m = 3
n_n = 7
d_m = 2
d_n = 5

for i in range(2, 1001):
    n_m, n_n = next(n_m, n_n)
    d_m, d_n = next(d_m, d_n)
    #check if numerator has more digits than denominator
    if int(log10(n_n)) > int(log10(d_n)):
        count += 1

print(count)

