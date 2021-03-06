#euler problem 22
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
#opening given name txt file and spiltting accordingly
with open("e22.txt", "r") as f:
    A = f.readline().split('","')

#removing quotations
for i in [0, -1]:
    A[i] = A[i].replace('"', "")

#defining sorting functions
def merge_sort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    i = 0
    j = 0
    k = 0
    
    while i < len(left) and j < len(right):
        #alpha will return whichever input comes first alphabetically
        tmp = alpha(left[i], right[j])
        A[k] = tmp
        if tmp == left[i]:
            i += 1
        else:
            j += 1
        k += 1
        
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    return A

def alpha(left, right):
    len_left = len(left)
    len_right = len(right)
    for i in range(0, min(len_left, len_right)):
        if ord(left[i]) < ord(right[i]):
            return left
        elif ord(left[i]) > ord(right[i]):
            return right
    return left if len_left < len_right else right

#solving problem
A = merge_sort(A)

total = 0

for i in range(0, len(A)):
    tmp = 0
    for j in A[i]:
        tmp += (ord(j) - 64)
    total += ((i + 1) * tmp)

print(total)
    
