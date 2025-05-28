""" Loop Based Summation """

def find_sum(n: int) -> int:
    """
    >>> find_sum(10)
    55
    >>> find_sum(100)
    5050
    >>> find_sum(1000)
    500500
    """
    sum = 0
    x = 1
    while x <= n:
        sum += x
        x += 1
    return sum
if __name__ == "__main__":  
    from doctest import testmod
    testmod(verbose=True)

