"""using recursion"""


def nth_fibonacci(n: int) -> int:
    """
    The Fibonacci sequence is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...]
    >>> nth_fibonacci(0)
    0
    >>> nth_fibonacci(1)
    1
    >>> nth_fibonacci(2)
    1
    >>> nth_fibonacci(3)
    2
    >>> nth_fibonacci(4)
    3
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
