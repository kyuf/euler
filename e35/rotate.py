#testing rotate function
def rotate(n):
    if n < 10:
        yield
    s = list(str(n))
    for i in range(len(s) - 1):
        s.append(s.pop(0))
        tmp = ""
        for j in s:
            tmp += j
        yield int(tmp)

for i in rotate(100):
    print i
