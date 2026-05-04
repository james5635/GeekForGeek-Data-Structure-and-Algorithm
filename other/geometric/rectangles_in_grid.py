"""Number of rectangles in N*M grid."""


def rectangles_in_grid(n: int, m: int) -> int:
    """Count the number of rectangles in an N x M grid.

    Args:
        n: Number of rows.
        m: Number of columns.

    Returns:
        Total number of rectangles.
    """
    return n * (n + 1) * m * (m + 1) // 4


if __name__ == "__main__":
    print(f"Rectangles in 2x2 grid: {rectangles_in_grid(2, 2)}")
    print(f"Rectangles in 3x3 grid: {rectangles_in_grid(3, 3)}")
