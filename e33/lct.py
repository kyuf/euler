#lowest common terms
def lct(n, d):
    tmp = n if n < d else d
    for i in range(tmp, 1, -1):
        if n % i == 0 and d % i == 0:
            n /= i
            d /= i
            break
    print "%s / %s" % (n, d)

lct(25, 10)
