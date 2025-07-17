""" Using Conditional Loop """
def lcm(a: int, b:int) -> int:
    """
    >>> lcm(10,5)
    10
    """
    g = max(a,b)
    s = min(a,b)
    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)