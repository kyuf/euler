#euler 36
"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
#function to determine if list is palindrome
def is_palindrome(lst):
    tmp = len(lst) - 1
    for i in range(len(lst) // 2):
        if lst[i] != lst[tmp - i]:
            return False
    return True

sum_n = 0

for n in range(1, 1000000):
    if is_palindrome(list(str(n))):
        tmp = list(bin(n))
        if is_palindrome(tmp[2:]):
            sum_n += n

print(sum_n)
