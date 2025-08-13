"""Bottom-Up Approach"""


def nth_fibonacci(n: int) -> int:
    """
    >>> nth_fibonacci(5)
    5
    >>> nth_fibonacci(2)
    1
    """
    if n < 0:
        raise ValueError("n muse be non-negative")
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
