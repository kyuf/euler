#pndigital checker for 1-9
def pan_check(n):
    tmp = str(n)
    distinct = []
    for i in range(9):
        if tmp[i] == "0" or tmp[i] in distinct:
            return False
        else:
            distinct.append(tmp[i])
    return True

print pan_check(123456789)
print pan_check(192384576)
print pan_check(120498294)

a = 123
tmp = list(str(a))
n = ""
for i in tmp:
    n += i

print int(n)
