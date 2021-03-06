#function to test if n is a triangle number
def is_triangle(Tn):
    if Tn < 0:
        return False
    sq = 1 + 8 * Tn
    root = int(sq ** 0.5 + 0.5)
    if root ** 2 == sq:
        num = root - 1
        n = num // 2
        if n * 2 == num:
            return True
    return False
