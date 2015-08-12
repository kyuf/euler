#improved version of euler 11
A = []
with open("e11.txt", "r") as f:
    for i in range(0, 20):
        tmp = f.readline().split()
        for i in range(0, len(tmp)):
            tmp[i] = int(tmp[i])
        A.append(tmp)

product = 0

for i in range (0, 20):
    for j in range(0, 20):
        if j < 17:
            tmp = A[i][j] * A[i][j + 1] * A[i][j + 2]* A[i][j + 3]
            if tmp > product:
                product = tmp
        if i < 17:
            tmp = A[i][j] * A[i + 1][j] * A[i + 2][j] * A[i + 3][j]
            if tmp > product:
                product = tmp
        if j < 17 and i < 17:
            tmp = A[i][j] * A[i + 1][j + 1] * A[i + 2][j + 2] * A[i + 3][j + 3]
            if tmp > product:
                product = tmp
        if i > 2 and j < 17:
            tmp = A[i][j] * A[i - 1][j + 1] * A[i - 2][j + 2] * A[i - 3][j + 3]
            if tmp > product:
                product = tmp

print product
