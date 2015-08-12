#euler 11

#importing file with grid numbers
A = []
with open("e11.txt", "r") as f:
    for i in range(0, 20):
        tmp = f.readline().split()
        for i in range(0, len(tmp)):
            tmp[i] = int(tmp[i])
        A.append(tmp)

product = 0

#horizontal products
for i in range(0, len(A)):
    for j in range(0, len(A[i]) - 3):
        tmp = A[i][j] * A[i][j + 1] * A[i][j + 2]* A[i][j + 3]
        if tmp > product:
            product = tmp

#vertical products
for i in range(0, len(A) - 3):
    for j in range(0, len(A[i])):
        tmp = A[i][j] * A[i + 1][j] * A[i + 2][j] * A[i + 3][j]
        if tmp > product:
            product = tmp

#diagonal 1 products
for i in range(0, len(A) - 3):
    for j in range(0, len(A[i]) - 3):
        tmp = A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3]
        if tmp > product:
            product = tmp

#diagonal 2 products
for i in range(3, len(A)):
    for j in range(0, len(A[i]) - 3):
        tmp = A[i][j] * A[i - 1][j + 1] * A[i - 2][j + 2] * A[i - 3][j + 3]
        if tmp > product:
            product = tmp

print product
