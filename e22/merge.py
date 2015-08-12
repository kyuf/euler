#basic merge sort
A = [2, 5, 1, 8, 5, 2, 4, 9, 7, 8]

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
        if left[0] < right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    while left:
        result.append(left[0])
        del left[0]
    while right:
        result.append(right[0])
        del right[0]
    return result

print merge_sort(A)
