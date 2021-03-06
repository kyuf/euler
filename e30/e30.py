#euler 30

#function to find upper limit
def max_n(pwr):
    max_digit = 9 ** pwr
    n = 0
    while ((n + 1) * max_digit) // (10 ** n):
        n += 1
    return (n * max_digit)

#set pwr
pwr = 5

#create dictionary storing digits raised to pwr
#start wit base cases 0 and 1
pwr_dict = {"0": 0, "1": 1}
for i in range(2, 10):
    pwr_dict[str(i)] = i ** pwr

#set sum
sum_n = 0

#run main algorithm
for i in range(10, max_n(pwr)):
    tmp = 0
    for j in str(i):
        tmp += pwr_dict[j]
    if tmp == i:
        sum_n += i

print sum_n
