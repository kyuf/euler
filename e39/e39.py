#euler 39
#brute
"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from gen_int_tri import triangles

max_p = None
max_n = 0

for p in range(12, 1001):
    n = triangles(p)
    if n > max_n:
        max_n = n
        max_p = p
print(max_p)
