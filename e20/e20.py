#euler 20
"""
n! means n × (n − 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
n = 1

for i in range(2, 101):
    n *= i
    
    #code below trims end zeros
    """
    while (n % 10) == 0:
        n //= 10
    """

print(n)

sum_n = 0

for i in str(n):
    sum_n += int(i)

print(sum_n)


