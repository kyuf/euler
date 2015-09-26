#euler 6
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sum_squares = 0
sum_n = 0
for i in range(1, 101):
    sum_squares += i **2
    sum_n += i
print(sum_n ** 2 - sum_squares)
    
