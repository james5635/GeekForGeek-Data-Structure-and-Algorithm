""" Using Nested Loops """
def count_pair_cube(n : int) -> int:
    """
    >>> count_pair_cube(9)
    2
    """
    count = 0
    for a in range(n+1):
        for b in range(n+1):
            if a ** 3 + b ** 3 == n:
                count += 1
    return count
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)