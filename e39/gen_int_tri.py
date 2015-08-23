#function that returns number of right integer triangles with given perimeter
def triangles(p):
    count = 0
    #maximum a value is p // 3 - 1
    #minimum a is 2
    for a in range(2, p // 3):
        #using a + b + c = p and a^2 + b^2 = c^2 to solve for b
        #b must be integer so use //
        b = p * (p - 2 * a) // (2 * (p - a))
        c = p - a - b
        #if b should have been float it will fail this condition
        if a ** 2 + b ** 2 == c ** 2:
            count += 1
    return count
