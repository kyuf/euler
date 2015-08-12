#test palindrome checker
def is_palindrome(lst):
    tmp = len(lst) - 1
    for i in range(len(lst) // 2):
        if lst[i] != lst[tmp - i]:
            return False
    return True

print is_palindrome(list(str(123)))
tmp = list(bin(2))
print tmp[2:]
