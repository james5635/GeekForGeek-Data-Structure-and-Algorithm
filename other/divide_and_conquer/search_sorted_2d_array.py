def search_sorted_2d(matrix: list[list[int]], target: int) -> tuple[int, int]:
    """
    Search for a target in a row-wise and column-wise sorted 2D array.

    Uses divide and conquer approach.

    Args:
        matrix: 2D array sorted row-wise and column-wise
        target: Value to search for

    Returns:
        Tuple of (row, col) if found, (-1, -1) otherwise
    """
    if not matrix or not matrix[0]:
        return (-1, -1)

    return _search(matrix, target, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)


def _search(
    matrix: list[list[int]],
    target: int,
    top: int,
    left: int,
    bottom: int,
    right: int,
) -> tuple[int, int]:
    if top > bottom or left > right:
        return (-1, -1)

    mid_row = (top + bottom) // 2
    mid_col = (left + right) // 2

    if matrix[mid_row][mid_col] == target:
        return (mid_row, mid_col)

    if matrix[mid_row][mid_col] < target:
        result = _search(matrix, target, mid_row + 1, left, bottom, right)
        if result != (-1, -1):
            return result
        return _search(matrix, target, top, mid_col + 1, mid_row, right)
    else:
        result = _search(matrix, target, top, left, mid_row - 1, right)
        if result != (-1, -1):
            return result
        return _search(matrix, target, mid_row, left, mid_row, mid_col - 1)


if __name__ == "__main__":
    matrix = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    print(search_sorted_2d(matrix, 29))
    print(search_sorted_2d(matrix, 100))
