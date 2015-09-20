#euler 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
#brute force
sum_n = 0
for n in range(3, 1000):
    if n % 3 == 0 or n % 5 == 0:
        sum_n += n
print(sum_n)

#mathematical
def multi(n, i = 1000):
    #number of multiples under i
    terms = i // n
    
    #finding sum
    sum_n = int((terms / 2) * (n * (terms + 1)))
    
    return sum_n

print(multi(3) + multi(5) - multi(15))
