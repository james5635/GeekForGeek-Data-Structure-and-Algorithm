"""Program to find mid-point of a line."""


def midpoint(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    """Find the midpoint of a line segment given two endpoints.

    Args:
        x1: X-coordinate of first point.
        y1: Y-coordinate of first point.
        x2: X-coordinate of second point.
        y2: Y-coordinate of second point.

    Returns:
        Tuple of (x, y) coordinates of the midpoint.
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)


if __name__ == "__main__":
    x1, y1 = 1, 2
    x2, y2 = 5, 6
    mid = midpoint(x1, y1, x2, y2)
    print(f"Midpoint of ({x1},{y1}) and ({x2},{y2}) is {mid}")
