def strassen_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """
    Multiply two square matrices using Strassen's algorithm.

    Args:
        a: First square matrix (n x n, where n is power of 2)
        b: Second square matrix (n x n, where n is power of 2)

    Returns:
        Product matrix (n x n)
    """
    n = len(a)

    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    a11 = _submatrix(a, 0, 0, mid)
    a12 = _submatrix(a, 0, mid, mid)
    a21 = _submatrix(a, mid, 0, mid)
    a22 = _submatrix(a, mid, mid, mid)

    b11 = _submatrix(b, 0, 0, mid)
    b12 = _submatrix(b, 0, mid, mid)
    b21 = _submatrix(b, mid, 0, mid)
    b22 = _submatrix(b, mid, mid, mid)

    m1 = strassen_multiply(_add(a11, a22), _add(b11, b22))
    m2 = strassen_multiply(_add(a21, a22), b11)
    m3 = strassen_multiply(a11, _sub(b12, b22))
    m4 = strassen_multiply(a22, _sub(b21, b11))
    m5 = strassen_multiply(_add(a11, a12), b22)
    m6 = strassen_multiply(_sub(a21, a11), _add(b11, b12))
    m7 = strassen_multiply(_sub(a12, a22), _add(b21, b22))

    c11 = _add(_sub(_add(m1, m4), m5), m7)
    c12 = _add(m3, m5)
    c21 = _add(m2, m4)
    c22 = _add(_sub(_add(m1, m3), m2), m6)

    result = [[0] * n for _ in range(n)]
    _combine(result, c11, c12, c21, c22, mid)
    return result


def _submatrix(m: list[list[int]], row: int, col: int, size: int) -> list[list[int]]:
    return [[m[row + i][col + j] for j in range(size)] for i in range(size)]


def _add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def _sub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]


def _combine(result: list[list[int]], c11, c12, c21, c22, mid: int) -> None:
    for i in range(mid):
        for j in range(mid):
            result[i][j] = c11[i][j]
            result[i][j + mid] = c12[i][j]
            result[i + mid][j] = c21[i][j]
            result[i + mid][j + mid] = c22[i][j]


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = strassen_multiply(a, b)
    for row in result:
        print(row)
