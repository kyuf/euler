#euler 48
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

#create function to truncate to wanted digits
def limit_check(n, limit):
    if n >= limit:
        return (n % limit)
    return n

#set limit to 10^10 for 10 desired digits
limit = 10 ** 10
sum_n = 0
n = 1000
for i in range(1, (n + 1)):
    tmp = i
    #iterate to (i - 1) since first run will give tmp ^ 2. can also use range(2, (i + 1))
    for j in range(i - 1):
        tmp = limit_check((tmp * i), limit)
    sum_n = limit_check((sum_n + tmp), limit)

#add in any missing 0's at higher digits
if sum_n < (10 ** 9):
    sum_n = list(str(sum_n))
    while len(sum_n) != 10:
        sum_n.insert(0, "0")
    tmp = ""
    for i in range(10):
        tmp += sum_n[i]
    sum_n = tmp

print sum_n

