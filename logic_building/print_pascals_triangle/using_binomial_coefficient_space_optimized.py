"""using_binomial_coefficient_space_optimized"""


def print_pascal_triangle(n: int) -> None:
    """
    >>> n = 5
    >>> print_pascal_triangle(n)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    for row in range(n):
        c = 1  # nC0 = 1
        print(c, end=" ")
        for i in range(1, row + 1):
            c = c * (row - i + 1) // i
            print(c, end=" ")
        print()


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
