#euler 34
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
fac = [1]
for i in range(1, 10):
    fac.append(fac[-1] * i)

nsum = 0

for n in range(10, 2540160):
    tmp = 0
    tmp_n = n
    while tmp_n >= 10:
        tmp += fac[tmp_n % 10]
        tmp_n //= 10
    tmp += fac[tmp_n]
    if tmp == n:
        nsum += n
print nsum
