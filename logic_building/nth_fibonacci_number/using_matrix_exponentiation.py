def nth_fibonacci(n: int) -> int:
    """
    >>> nth_fibonacci(5)
    5
    >>> nth_fibonacci(2)
    1
    """

    def multiply(mat1, mat2):
        x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
        y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
        z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
        w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

        mat1[0][0], mat1[0][1] = x, y
        mat1[1][0], mat1[1][1] = z, w

    def matrix_power(mat1, n):
        if n == 0 or n == 1:
            return
        mat2 = [[1, 1], [1, 0]]
        matrix_power(mat1, n // 2)
        multiply(mat1, mat1)
        if n % 2 != 0:
            multiply(mat1, mat2)

    if n < 0:
        raise ValueError("n must not be non-negative")
    if n <= 1:
        return n
    mat1 = [[1, 1], [1, 0]]
    matrix_power(mat1, n - 1)
    return mat1[0][0]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
