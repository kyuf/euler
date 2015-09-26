#euler 13
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (in num.txt).
"""
sum_n = 0
with open("num.txt", "r") as f:
    for line in f:
        sum_n += int(line.rstrip())

print(str(sum_n)[0:10])
