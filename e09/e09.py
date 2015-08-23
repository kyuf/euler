#euler 9
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#function returns sides of triangle given a perimeter
def triangles(p):
    tri = None
    for a in range(2, p // 3):
        #assuming b must be an integer
        b = p * (p - 2 * a) // (2 * (p - a))
        c = p - a - b
        if a ** 2 + b ** 2 == c ** 2:
            tri = a * b * c
    return tri

print(triangles(1000))
