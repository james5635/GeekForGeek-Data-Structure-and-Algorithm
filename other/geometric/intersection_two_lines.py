"""Program for point of intersection of two lines."""


def intersection_two_lines(
    a1: float, b1: float, c1: float, a2: float, b2: float, c2: float
) -> tuple[float, float] | None:
    """Find the intersection point of two lines given in ax + by = c form.

    Args:
        a1, b1, c1: Coefficients of first line.
        a2, b2, c2: Coefficients of second line.

    Returns:
        Tuple of (x, y) intersection point or None if parallel.
    """
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)


if __name__ == "__main__":
    result = intersection_two_lines(1, 2, 5, 3, 4, 6)
    print(f"Intersection of lines: {result}")
