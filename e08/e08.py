#euler 8
"""
The four adjacent digits in the 1000-digit number (in num.txt) that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""
num = ""
prod = 1
max_prod = 0
consecutive = 1
with open("num.txt", "r") as f:
    for line in f:
        num += line.rstrip()

for i in range(len(num)):
    n = int(num[i])
    if n == 0:
        consecutive = 1
        prod = 1
    else:
        if consecutive > 13:
            prod //= int(num[i - 13])
        prod *= n
        consecutive += 1
        if prod > max_prod:
            max_prod = prod

print(max_prod)
