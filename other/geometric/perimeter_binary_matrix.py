"""Find perimeter of shapes formed by 1s in binary matrix."""

from typing import Set


def perimeter_binary_matrix(matrix: list[list[int]]) -> int:
    """Calculate the perimeter of shapes formed by 1s in a binary matrix.

    Args:
        matrix: 2D binary matrix.

    Returns:
        Total perimeter of all shapes.
    """
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                perimeter += 4
                if i > 0 and matrix[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and matrix[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    print(f"Perimeter: {perimeter_binary_matrix(matrix)}")
