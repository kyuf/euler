#brute force
#always start with solutions that do not require fancy math tricks
#remember that you are a computer scientist and not a mathematician
lim = 100

distinct = []

for a in range(2, lim + 1):
    for b in range(2, lim + 1):
        tmp = a ** b
        if tmp not in distinct:
            distinct.append(tmp)

print len(distinct)
