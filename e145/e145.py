#euler 145
#severly suboptimal
"""
Some positive integers n have the property that the sum [n + reverse(n)] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion?
"""
def is_reversible(n):    
    #reverse number
    rev_n = int(str(n)[::-1])
          
    #checking sum for all odd digits
    sum_n = n + rev_n
    for i in str(sum_n):
        if int(i) % 2 == 0:
            return False
    return True
    
count = 0

#first and last digits cannot both be odd or even
#only need to consider odd and increment by 2
#due to carry overs, no solutions exist for 5-digit and 9-digit
for n in range(11, 10000, 2):
    if is_reversible(n):
        count += 2

for n in range(100001, 100000000, 2):
    if is_reversible(n):
        count += 2
        
print(count)
            
