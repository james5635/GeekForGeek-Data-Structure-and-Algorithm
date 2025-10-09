"""Using Binomial Coefficient"""


def binomial_coefficient(n: int, k: int) -> int:
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res


def pascal_triangle(n: int) -> list[list[int]]:
    matrix = []
    for row in range(n):
        arr = []
        for i in range(row + 1):
            arr.append(binomial_coefficient(row, i))
        matrix.append(arr)
    return matrix


def print_pascal_triangle(triangle: list[list[int]]) -> None:
    """
    >>> t = pascal_triangle(5)
    >>> print_pascal_triangle(t)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    for row in triangle:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
