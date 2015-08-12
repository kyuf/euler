#euler 49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


#function to check if number is prime
def is_prime(n, prime_list):
    tmp = n ** 0.5
    for i in prime_list:
        if i > tmp:
            break
        if n % i == 0:
            return False
    return True

#function that returns dictionary for permutation comparison
def perm_set(n):
    n_set = {}
    for i in str(n):
        if i in n_set:
            n_set[i] += 1
        else:
            n_set[i] = 1
    return n_set

#seed prime_list with 2 to allow for odd iteration
prime_list = [2]
prime_dic = {}

#seed prime list
for n in range(3, 1000, 2):
    if is_prime(n, prime_list):
        prime_list.append(n)

#update prime list and prime dictionary for permutation comparison
for n in range(1001, 10000, 2):
    if is_prime(n, prime_list):
        prime_list.append(n)
        prime_dic[n] = 1

l = len(prime_list)

for n in range(l):
    for m in range(n + 1, l):
        ntmp = perm_set(prime_list[n])
        if ntmp != perm_set(prime_list[m]):
            continue
        #find next number in arithmetic sequence
        tmp = (2 * prime_list[m] - prime_list[n])
        if tmp >= 10000:
            break
        if tmp in prime_dic and ntmp == perm_set(tmp):
            print("%s%s%s" % (prime_list[n], prime_list[m], tmp))
