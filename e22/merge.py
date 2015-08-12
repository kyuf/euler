#basic merge sort
def merge_sort(A):
	if len(A) < 2:
		return A
	half = len(A) // 2
	left = merge_sort(A[:half])
	right = merge_sort(A[half:])
	i = 0
	j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			A[k] = left[i]
			i += 1
		else:
			A[k] = right[j]
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

A = [2, 5, 1, 8, 5, 2, 4, 9, 7, 8]
print(merge_sort(A))
