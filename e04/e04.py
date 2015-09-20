#euler 4
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palin(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    return True

ans = 0
for m in range(100, 1000):
    for n in range(100, 1000):
        prod = m * n
        if is_palin(prod) and prod > ans:
            ans = prod
            
print(ans)
