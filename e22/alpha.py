#alphabetical sorter test. based off merge sort
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
        tmp = alpha(left[0], right[0])
        result.append(tmp)
        if left[0] == tmp:
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

A = ["all", "a", "c", "q", "d", "v", "b"]

print merge_sort(A)


