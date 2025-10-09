"""Using Dynamic Programming"""


def print_pascal_triangle(n: int) -> None:
    """
    >>> print_pascal_triangle(5)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    """
    matrix: list[list[int]] = []
    for row in range(n):
        arr: list[int] = []
        for i in range(row + 1):
            if i == 0 or i == row:
                arr.append(1)
            else:
                arr.append(matrix[row - 1][i - 1] + matrix[row - 1][i])
        matrix.append(arr)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
