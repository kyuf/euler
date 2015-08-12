#permutation checker
def perm_set(n):
    n_set = {}
    for i in str(n):
        if i in n_set:
            n_set[i] += 1
        else:
            n_set[i] = 1
    return n_set

print perm_set(123) == perm_set(431)
