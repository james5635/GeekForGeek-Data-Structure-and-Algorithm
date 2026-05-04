"""Section formula: point dividing line in given ratio."""


def section_formula(
    x1: float, y1: float, x2: float, y2: float, m: float, n: float
) -> tuple[float, float]:
    """Find the point dividing a line segment in a given ratio.

    Args:
        x1: X-coordinate of first point.
        y1: Y-coordinate of first point.
        x2: X-coordinate of second point.
        y2: Y-coordinate of second point.
        m: First part of ratio.
        n: Second part of ratio.

    Returns:
        Tuple of (x, y) coordinates of the dividing point.
    """
    x = (m * x2 + n * x1) / (m + n)
    y = (m * y2 + n * y1) / (m + n)
    return (x, y)


if __name__ == "__main__":
    x1, y1 = 1, 2
    x2, y2 = 5, 6
    m, n = 3, 2
    point = section_formula(x1, y1, x2, y2, m, n)
    print(f"Point dividing ({x1},{y1}) and ({x2},{y2}) in ratio {m}:{n} is {point}")
