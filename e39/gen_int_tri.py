#function that returns number of right integer triangles with given perimeter
def triangles(p):
    count = 0
    #minimum a value is 3
    a = 3
    b = a + 1
    c = p - a - b
    while b < c:
        if c < a + b and a ** 2 + b ** 2 == c ** 2:
            count += 1
        if b + 1 >= c - 1:
            a += 1
            b = a + 1
            c = p - a - b
        else:
            b += 1
            c -= 1
    return count
