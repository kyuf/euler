#euler 25
e = 10
n = 2
F_m = 1
F_n = 1
dig = 10 ** 10
while True:
    F_m, F_n = F_n, F_m + F_n
    n += 1
    if F_n // dig == 1:
        F_n /= 10
        F_m /= 10
        e += 1
    if e == 1000:
        break

print n
