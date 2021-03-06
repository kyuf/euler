#euler 33
#remember to use float when dealing with decimals
def pdiv(q, n, d):
    return True if q == float(n) / d else False

def lct(n, d):
    tmp = n if n < d else d
    for i in range(tmp, 1, -1):
        if n % i == 0 and d % i == 0:
            n /= i
            d /= i
            break
    print "%s / %s" % (n, d)

nprod = 1
dprod = 1

for d in range(12, 100):
    if d % 10 == 0:
        continue
    for n in range(11, d):
        if n % 10 == 0:
            continue
        q = float(n) / d
        n1 = n % 10
        n2 = n // 10
        d1 = d % 10
        d2 = d // 10
        if n1 == d2 and pdiv(q, n2, d1) or n2 == d1 and pdiv(q, n1, d2):
            nprod *= n
            dprod *= d
            print "%s / %s" % (n, d)
lct(nprod, dprod)
