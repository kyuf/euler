#euler problem 22
#opening given name txt file and spiltting accordingly
with open("e22.txt", "r") as f:
    A = f.readline().split('","')

for i in [0, -1]:
    A[i] = A[i].replace('"', "")

#defining sorting functions
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        #alpha will return whichever input comes first alphabetically
        tmp = alpha(left[0], right[0])
        result.append(tmp)
        if tmp == left[0]:
            del left[0]
        else:
            del right[0]
    while left:
        result.append(left[0])
        del left[0]
    while right:
        result.append(right[0])
        del right[0]
    return result

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

print total
    
