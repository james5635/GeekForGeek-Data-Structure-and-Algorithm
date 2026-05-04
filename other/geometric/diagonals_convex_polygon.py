"""Find number of diagonals in n-sided convex polygon."""


def diagonals_convex_polygon(n: int) -> int:
    """Calculate the number of diagonals in an n-sided convex polygon.

    Args:
        n: Number of sides of the polygon.

    Returns:
        Number of diagonals.
    """
    return n * (n - 3) // 2


if __name__ == "__main__":
    print(f"Diagonals in quadrilateral: {diagonals_convex_polygon(4)}")
    print(f"Diagonals in pentagon: {diagonals_convex_polygon(5)}")
    print(f"Diagonals in hexagon: {diagonals_convex_polygon(6)}")
